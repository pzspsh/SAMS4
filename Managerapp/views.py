from django.db import transaction
from django.shortcuts import render, redirect
from ApartmentSystem import models
from Managerapp import forms
import hashlib
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse


# Create your views here.
def index(request):
    # if not request.session.get('is_login', None):
    #     return redirect('manager:login')
    q = request.GET.get('q')
    error_msg = ''
    if not q:
        error_msg = '请输入关键词'
        return render(request, 'manager_login/index.html', {'error_msg': error_msg})
    post_list = models.Content.objects.filter(title=q)
    return render(request, 'manager_login/index.html', {'error_msg': error_msg,
                                                        'post_list': post_list})


def login(request):
    if request.method == "POST":
        login_form = forms.ManageForm(request.POST)
        message = '请检查填写的内容'
        if login_form.is_valid():
            mid = login_form.cleaned_data.get('mid')
            password = login_form.cleaned_data.get('password')  # 确保用户名和密码都不为空
            md5 = hashlib.md5()
            md5.update(password.encode('utf-8'))
            password = md5.hexdigest()
            try:
                managerResult = models.ManageModel.objects.get(mid=mid, password=password)
            except:
                message = "账号或密码不存在！"
                return render(request, 'manager_login/login.html', locals())
            if managerResult.password == password:
                request.session['is_login'] = True
                request.session['manager_id'] = managerResult.id
                request.session['manager_mid'] = managerResult.mid
                return redirect('manager:index')
            else:
                message = "密码不正确！"
                return render(request, 'manager_login/login.html', locals())
        else:
            return render(request, 'manager_login/login.html', locals())
    login_form = forms.ManageForm()
    return render(request, 'manager_login/login.html', locals())


def register(request):
    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = '请检查填写的内容！'
        if register_form.is_valid():
            mname = register_form.cleaned_data.get('mname')
            mid = register_form.cleaned_data.get('mid')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            md5 = hashlib.md5()
            md5.update(password1.encode('utf-8'))
            password = md5.hexdigest()
            email = register_form.cleaned_data.get('email')
            phone = register_form.cleaned_data.get('phone')
            sex = register_form.cleaned_data.get('sex')

            if password1 != password2:
                message = '两次输入的密码不正确！'
                return render(request, 'manager_login/register.html', locals())
            else:
                same_mid_user = models.ManageModel.objects.filter(mid=mid)
                if same_mid_user:
                    message = '账号已存在！'
                    return render(request, 'manager_login/register.html', locals())
                same_tele_user = models.ManageModel.objects.filter(phone=phone)
                if same_tele_user:
                    message = '该电话已注册！'
                    return render(request, 'manager_login/register.html', locals())
                same_email_user = models.ManageModel.objects.filter(email=email)
                if same_email_user:
                    message = '该邮箱已经被注册了！'
                    return render(request, 'manager_login/register.html', locals())
                new_manage = models.ManageModel()
                new_manage.mname = mname
                new_manage.mid = mid
                new_manage.password = password
                new_manage.email = email
                new_manage.phone = phone
                new_manage.gender = sex
                new_manage.save()

                return redirect('manager:login')
        else:
            return render(request, 'manager_login/register.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'manager_login/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return redirect('manager:login')
    request.session.flush()
    return redirect('manager:login')


# 添加数据 只能admin或者管理员才能操作
# 添加学生信息
def addStudent(request):
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
        message = '添加成功'
        return render(request, 'manager_login/addStudent.html', locals())
    else:
        message = '添加失败'
        return render(request, 'manager_login/addStudent.html', locals())


# 添加公寓好
def addApartment(request):
    if request.method == 'POST':
        room_no = request.POST.get('room_no')
        bed_no = request.POST.get('bed_no')
        kz_number = request.POST.get('kz_number')
        xz_number = request.POST.get('xz_number')
        state = request.POST.get('state')
        s_no = request.POST.get('s_no')
        m_no = request.POST.get('m_no')
        lou_no = request.POST.get('lou_no')
        s_no = models.TbStudent.objects.get(s_no=s_no)
        m_no = models.TbManage.objects.get(m_no=m_no)
        lou_no = models.TbFloor.objects.get(lou_no=lou_no)
        apartment_data = models.TbApartment()
        apartment_data.room_no = room_no
        apartment_data.bed_no = bed_no
        apartment_data.kz_number = kz_number
        apartment_data.xz_number = xz_number
        apartment_data.state = state
        apartment_data.s_no = s_no
        apartment_data.m_no = m_no
        apartment_data.lou_no = lou_no
        apartment_data.save()
        message = '添加成功'
        return render(request, 'manager_login/addApartment.html', locals())
    else:
        message = '添加失败'
        return render(request, 'manager_login/addApartment.html', locals())


# 添加公寓楼
def addFloor(request):
    if request.method == 'POST':
        lou_no = request.POST.get('lou_no')
        rooms = request.POST.get('rooms')
        m_no = request.POST.get('m_no')
        m_no = models.TbManage.objects.get(m_no=m_no)
        floor_data = models.TbFloor()
        floor_data.lou_no = lou_no
        floor_data.rooms = rooms
        floor_data.m_no = m_no
        floor_data.save()
        message = '添加成功'
        return render(request, 'manager_login/addFloor.html', locals())
    else:
        message = '添加失败'
        return render(request, 'manager_login/addFloor.html', locals())


# 记录学生的信息
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


# 记录学生离校记录
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


def addManager(request):
    if request.method == 'POST':
        m_no = request.POST.get('m_no')
        m_name = request.POST.get('m_name')
        m_sex = request.POST.get('m_sex')
        m_tele = request.POST.get('m_tele')
        image = request.POST.get('image')
        manager_data = models.TbManage()
        manager_data.m_no = m_no
        manager_data.m_name = m_name
        manager_data.m_sex = m_sex
        manager_data.m_tele = m_tele
        manager_data.image = image
        manager_data.save()
        message = '管理员信息添加成功'
        return render(request, 'manager_login/addManager.html', locals())
    else:
        message = '添加失败'
        return render(request, 'manager_login/addManager.html', locals())


# 记录水电信息
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


# 宿管员信息
def addSgy(request):
    if request.method == 'POST':
        sgy_no = request.POST.get('sgy_no')
        sgy_name = request.POST.get('sgy_name')
        sgy_sex = request.POST.get('sgy_sex')
        sgy_age = request.POST.get('sgy_age')
        sgy_tele = request.POST.get('sgy_tele')
        sgy_rz = request.POST.get('sgy_rz')
        lou_no = request.POST.get('lou_no')
        lou_no = models.TbFloor.objects.get(lou_no=lou_no)
        image = request.POST.get('image')
        sgy_data = models.TbSgy()
        sgy_data.sgy_no = sgy_no
        sgy_data.sgy_name = sgy_name
        sgy_data.sgy_sex = sgy_sex
        sgy_data.sgy_age = sgy_age
        sgy_data.sgy_tele = sgy_tele
        sgy_data.sgy_rz = sgy_rz
        sgy_data.lou_no = lou_no
        sgy_data.image = image
        sgy_data.save()
        message = '添加宿管员信息成功'
        return render(request, 'manager_login/addSgy.html', locals())
    else:
        message = '添加失败'
        return render(request, 'manager_login/addSgy.html', locals())


# 记录宿舍卫生情况
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


# 报修管理记录
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


# 注册学生登录密码
def addStudentModel(request):
    if request.method == 'POST':
        stuname = request.POST.get('stuname')
        gender = request.POST.get('gender')
        stuid = request.POST.get('stuid')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        studentmodel_data = models.StudentModel()
        studentmodel_data.stuname = stuname
        studentmodel_data.gender = gender
        studentmodel_data.stuid = stuid
        studentmodel_data.password = password
        studentmodel_data.email = email
        studentmodel_data.phone = phone
        studentmodel_data.save()
        message = '添加学生用户密码成功'
        return render(request, 'manager_login/addStudentModel.html', locals())
    else:
        message = '添加失败'
        return render(request, 'manager_login/addStudentModel.html')


# 查询学生信息功能
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
        stu_room = models.TbApartment.objects.filter(s_no=s_no)
        dct = {}
        dct1 = {}
        for stu in stu_reason:
            dct['违规记录'] = stu.wreason
            for stu2 in stu_reason:
                dct['违规时间'] = stu.stamp_time
        for stu1 in stu_room:
            dct1['所住床号'] = stu1.bed_no
            for stu3 in stu_room:
                dct1['所在楼号'] = stu1.lou_no
        context = {
            's_no': s_no,
            's_name': s_name,
            's_sex': s_sex,
            's_age': s_age,
            's_tele': s_tele,
            's_college': s_college,
            'm_no': m_no,
            'wreason_data': dct,
            'bed_no': dct1,
            'msg': True
        }
        return render(request, 'manager_login/select.html', context)
    else:
        message = '没有这个学生'
        return render(request, 'manager_login/select.html', locals())


# 删除学生信息功能
def delete(request):
    if request.method == 'POST':
        s_no = request.POST.get('s_no')
        models.TbStudent.objects.filter(s_no=s_no).delete()
        context = {
            'msg': '删除成功'
        }
        return render(request, 'manager_login/delete.html', context)
    else:
        message = '没有这个学生'
        return render(request, 'manager_login/delete.html', locals())


# 修改学生信息功能
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


def content_list(request):
    content = models.Content.objects.all()
    return render(request, 'manager_login/home.html', {'content': content})


from dwebsocket.decorators import accept_websocket,require_websocket
from collections import defaultdict

allconn = defaultdict(list)
@accept_websocket
def echo(request,userid):
    allresult = {}
    userinfo = request.user
    allresult['userinfo'] = userinfo
    global allconn
    if not request.is_websocket():
        try:
            message = request.GET['message']
            return HttpResponse(message)
        except:
            return render(request,'chat.html')
    else:
        allconn[str(userid)] = request.websocket
        for message in request.websocket:
            request.websocket.send(message)
            for i in allconn:
                if i != str(userid):
                    allconn[i].send(message)