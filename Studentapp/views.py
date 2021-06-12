from Studentapp import forms
from django.views import View
from ApartmentSystem import models
from django.http import HttpResponse
from Studentapp.forms import CommentForm, UserForm
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    if not request.session.get('is_login', None):
        return redirect('student:index')
    return render(request, 'student_login/index.html')


def login(request):
    if request.method == "POST":
        login_form = forms.StudentForm(request.POST)
        message = '请检查填写的内容'
        if login_form.is_valid():
            stuid = login_form.cleaned_data.get('stuid')
            password = login_form.cleaned_data.get('password')  # 确保用户名和密码都不为空
            try:
                managerResult = models.StudentModel.objects.get(stuid=stuid, password=password)
            except:
                message = "账号或密码不存在！"
                return render(request, 'student_login/login.html', locals())
            if managerResult.password == password:
                request.session['is_login'] = True
                request.session['student_id'] = managerResult.id
                request.session['student_stuid'] = managerResult.stuid
                return redirect('student:index')
            else:
                message = "密码不正确！"
                return render(request, 'student_login/login.html', locals())
        else:
            return render(request, 'student_login/login.html', locals())
    login_form = forms.StudentForm()
    return render(request, 'student_login/login.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return redirect('student:login')
    request.session.flush()
    return redirect('student:login')


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
        return render(request, 'student_login/select.html', context)
    else:
        message = '没有这个学生'
        return render(request, 'student_login/select.html', locals())


# 修改
def update(request):
    stu_data = models.StudentModel()
    stuname = stu_data.stuname
    stuid = stu_data.stuid
    password = stu_data.password
    gender = stu_data.gender
    phone = stu_data.phone
    email = stu_data.email
    context = {
        'stuname': stuname,
        'stuid': stuid,
        'gender': gender,
        'password': password,
        'email': email,
        'phone': phone,
    }
    if request.method == 'POST':
        stuname = request.POST.get('stuname')
        stuid = request.POST.get('stuid')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        s_data = models.StudentModel()
        s_data.stuname = stuname
        s_data.stuid = stuid
        s_data.gender = gender
        s_data.password = password
        s_data.email = email
        s_data.phone = phone
        s_data.save()
        context = {
            'stuname': stuname,
            'stuid': stuid,
            'gender': gender,
            'password': password,
            'email': email,
            'phone': phone,
            'msg': True
        }
        return render(request, 'student_login/update.html', context)
    else:
        return render(request, 'student_login/update.html', context)


class News(View):
    def get(self, request, content_id):
        illegal = models.TbIllegal.objects.all()
        data = models.Content.objects.get(id=content_id)
        data.clicked = int(data.clicked) + 1
        data.save()
        form = CommentForm()
        comment_list = models.Comment.objects.filter(news_id=data, restore=None)
        hot_news = models.Content.objects.all().order_by('-clicked')[:10]
        return render(request, 'news.html', locals())

    def post(self, request, content_id):
        form = CommentForm(request.POST)
        if form.is_valid():
            if request.POST.get('s_no'):  # 可能会错误
                restore = request.POST.get('restore', None)
                if restore:
                    models.Comment.objects.create(
                        user_id=models.TbStudent.objects.get(id=request.POST.get('user_id')),
                        news_id=models.Content.objects.get(id=content_id),
                        content=request.POST.get('content'),
                        restore=models.Comment.objects.get(id=request.POST.get('restore')),
                        restore_user=models.TbStudent.objects.get(id=request.POST.get('restore_user')),
                    )
                else:
                    models.Comment.objects.create(
                        user_id=request.s_no,
                        news_id=models.Content.objects.get(id=content_id),
                        content=request.POST.get('content'),
                    )
            else:
                return render(request, 'student_login/login.html', locals())
        return redirect('/news/%s' % content_id)
