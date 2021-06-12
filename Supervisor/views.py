from django.shortcuts import render

# Create your views here.
from django.db import transaction
from django.shortcuts import render, redirect
from ApartmentSystem import models
from Supervisor import forms
from django.contrib.auth.hashers import make_password


# Create your views here.
def index(request):
    if not request.session.get('is_login', None):
        return redirect('supervisor:login')
    return render(request, 'supervisor_login/index.html')


def login(request):
    if request.method == "POST":
        login_form = forms.SupervisorForm(request.POST)
        message = '请检查填写的内容'
        if login_form.is_valid():
            sgy_no = login_form.cleaned_data.get('sgy_no')
            password = login_form.cleaned_data.get('password')  # 确保用户名和密码都不为空
            try:
                supervisorResult = models.TbSgy.objects.get(sgy_no=sgy_no, password=password)
            except:
                message = "账号或密码不存在！"
                return render(request, 'supervisor_login/login.html', locals())
            if supervisorResult.password == password:
                request.session['is_login'] = True
                request.session['supervisor_id'] = supervisorResult.password
                request.session['supervisor_sgy_no'] = supervisorResult.sgy_no
                return redirect('supervisor:index')
            else:
                message = "密码不正确！"
                return render(request, 'supervisor_login/login.html', locals())
        else:
            return render(request, 'supervisor_login/login.html', locals())
    login_form = forms.SupervisorForm()
    return render(request, 'supervisor_login/login.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return redirect('supervisor:login')
    request.session.flush()
    return redirect('supervisor:login')


def addIllegal(request):
    if request.method == 'POST':
        s_no = request.POST.get('s_no')
        lou_no = request.POST.get('lou_no')
        room_no = request.POST.get('room_no')
        stamp_time = request.POST.get('stamp_time')
        wreason = request.POST.get('wreason')
        s_no = models.TbStudent.objects.get(s_no=s_no)
        lou_no = models.TbFloor.objects.get(lou_no=lou_no)
        room_no = models.TbApartment.objects.get(room_no=room_no)
        illegal_data = models.TbIllegal()
        illegal_data.s_no = s_no
        illegal_data.lou_no = lou_no
        illegal_data.room_no = room_no
        illegal_data.stamp_time = stamp_time
        illegal_data.wreason = wreason
        illegal_data.save()
        message = '添加违规记录成功'
        return render(request, 'manager_login/addIllegal.html', locals())
    else:
        message = '添加失败'
        return render(request, 'manager_login/addIllegal.html', locals())


def addLx(request):
    if request.method == 'POST':
        s_no = request.POST.get('s_no')
        room_no = request.POST.get('room_no')
        bed_no = request.POST.get('bed_no')
        l_time = request.POST.get('l_time')
        l_reason = request.POST.get('l_reason')
        s_no = models.TbStudent.objects.get(s_no=s_no)
        room_no = models.TbApartment.objects.get(room_no=room_no)
        lx_data = models.TbLx()
        lx_data.s_no = s_no
        lx_data.room_no = room_no
        lx_data.bed_no = bed_no
        lx_data.l_time = l_time
        lx_data.l_reason = l_reason
        lx_data.save()
        message = '添加离校学生成功'
        return render(request, 'manager_login/addLx.html', locals())
    else:
        message = '添加失败'
        return render(request, 'manager_login/addLx.html', locals())

def addSdb(request):
    if request.method == 'POST':
        lou_no = request.POST.get('lou_no')
        room_no = request.POST.get('room_no')
        month_field = request.POST.get('month_field')
        elect = request.POST.get('elect')
        electric = request.POST.get('electric')
        water = request.POST.get('water')
        waterc = request.POST.get('waterc')
        lou_no = models.TbFloor.objects.get(lou_no=lou_no)
        room_no = models.TbApartment.objects.get(room_no=room_no)
        sdb_data = models.TbSdb()
        sdb_data.lou_no = lou_no
        sdb_data.room_no = room_no
        sdb_data.month_field = month_field
        sdb_data.elect = elect
        sdb_data.electric = electric
        sdb_data.water = water
        sdb_data.waterc = waterc
        sdb_data.save()
        message = '添加水电表信息成'
        return render(request, 'manager_login/addSdb.html', locals())
    else:
        message = '添加失败'
        return render(request, 'manager_login/addSdb.html', locals())

def addSsws(request):
    if request.method == 'POST':
        lou_no = request.POST.get('lou_no')
        room_no = request.POST.get('room_no')
        scores = request.POST.get('scores')
        descores = request.POST.get('desocres')
        comment_time = request.POST.get('comment_time')
        comment_name = request.POST.get('comment_name')
        image = request.POST.get('image')
        lou_no = models.TbFloor.objects.get(lou_no=lou_no)
        room_no = models.TbApartment.objects.get(room_no=room_no)
        ssws_data = models.TbSsws()
        ssws_data.lou_no = lou_no
        ssws_data.room_no = room_no
        ssws_data.scores = scores
        ssws_data.descores = descores
        ssws_data.comment_time = comment_time
        ssws_data.comment_name = comment_name
        ssws_data.image = image
        ssws_data.save()
        message = '添加宿舍卫生成功'
        return render(request, 'manager_login/addSsws.html', locals())
    else:
        message = '添加失败'
        return render(request, 'manager_login/addSsws.html', locals())


def addSthfix(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        lou_no = request.POST.get('lou_no')
        room_no = request.POST.get('room_no')
        report_time = request.POST.get('report_time')
        reporter = request.POST.get('reporter')
        fix_time = request.POST.get('fix_time')
        fixer = request.POST.get('fixer')
        state = request.POST.get('state')
        image = request.POST.get('image')
        lou_no = models.TbFloor.objects.get(lou_no=lou_no)
        room_no = models.TbApartment.objects.get(room_no=lou_no)
        sthfix_data = models.TbSthFix()
        sthfix_data.content = content
        sthfix_data.lou_no = lou_no
        sthfix_data.room_no = room_no
        sthfix_data.report_time = report_time
        sthfix_data.reporter = reporter
        sthfix_data.fix_time = fix_time
        sthfix_data.fixer = fixer
        sthfix_data.state = state
        sthfix_data.image = image
        sthfix_data.save()
        message = '报修信息添加成功'
        return render(request, 'manager_login/addSthfix.html', locals())
    else:
        message = '添加失败'
        return render(request, 'manager_login/addSthfix.html', locals())

# 查询功能
def select(request):
    if request.method == 'POST':
        s_no = request.POST.get('s_no')
        stu_data = models.TbStudent.objects.get(s_no=s_no)
        s_no = stu_data.s_no
        s_name = stu_data.s_name
        s_sex = stu_data.s_sex
        s_age = stu_data.s_age
        s_tele = stu_data.s_tele
        s_college = stu_data.s_college
        m_no = stu_data.m_no
        stu_reason = models.TbIllegal.objects.filter(s_no=s_no)
        dct = {}
        for stu in stu_reason:
            dct[stu.s_no] = stu.wreason
        context = {
            's_no': s_no,
            's_name': s_name,
            's_sex': s_sex,
            's_age': s_age,
            's_tele': s_tele,
            's_college': s_college,
            'm_no': m_no,
            'wreason_data': dct,
            'msg': True
        }
        return render(request, 'manager_login/select.html', context)
    else:
        message = '没有这个学生'
        return render(request, 'manager_login/select.html', locals())


# 删除功能
def delete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        models.TbStudent.objects.filter(s_no=id).delete()
        context = {
            'msg': '删除成功'
        }
        return render(request, 'manager_login/delete.html', context)
    else:
        message = '没有这个学生'
        return render(request, 'manager_login/delete.html', locals())


# 修改
def update(request):
    stu_data = models.TbStudent()
    s_no = stu_data.s_no
    s_name = stu_data.s_name
    s_sex = stu_data.s_sex
    s_age = stu_data.s_age
    s_tele = stu_data.s_tele
    s_college = stu_data.s_college
    context = {
        's_no': s_no,
        's_name': s_name,
        's_sex': s_sex,
        's_age': s_age,
        's_tele': s_tele,
        's_college': s_college,
    }
    if request.method == 'POST':
        s_no = request.POST.get('s_no')
        s_name = request.POST.get('s_name')
        s_sex = request.POST.get('s_sex')
        s_age = request.POST.get('s_age')
        s_tele = request.POST.get('s_tele')
        s_college = request.POST.get('s_college')
        m_no = request.POST.get('m_no')
        m_no = models.TbManage.objects.get(m_no=m_no)
        s_data = models.TbStudent()
        s_data.s_no = s_no
        s_data.s_name = s_name
        s_data.s_sex = s_sex
        s_data.s_age = s_age
        s_data.s_tele = s_tele
        s_data.s_college = s_college
        s_data.m_no = m_no
        s_data.save()
        context = {
            's_no': s_no,
            's_name': s_name,
            's_sex': s_sex,
            's_age': s_age,
            's_tele': s_tele,
            's_college': s_college,
            'm_no': m_no,
            'msg': True
        }
        return render(request, 'manager_login/update.html', context)
    else:
        return render(request, 'manager_login/update.html', context)
