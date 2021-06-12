from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.


# Create your models here.
# 1、创建学生公寓信息表
class TbApartment(models.Model):
    room_no = models.CharField(primary_key=True, max_length=10, verbose_name='房间号')
    bed_no = models.CharField(unique=True, max_length=10, verbose_name='床号')
    kz_number = models.IntegerField(verbose_name='可住人数')
    xz_number = models.IntegerField(verbose_name='现住人数')
    state = models.CharField(max_length=50, blank=True, null=True, verbose_name='状态')
    s_no = models.ForeignKey('TbStudent', on_delete=models.DO_NOTHING, db_column='s_no', verbose_name='学号')
    m_no = models.ForeignKey('TbManage', on_delete=models.DO_NOTHING, db_column='m_no', verbose_name='管理员编号')
    lou_no = models.ForeignKey('TbFloor', on_delete=models.CASCADE, db_column='lou_no', verbose_name='楼号')

    class Meta():
        db_table = '公寓号信息管理'
        verbose_name_plural = '公寓号信息管理'


# 2、创建公寓楼表
class TbFloor(models.Model):
    lou_no = models.CharField(primary_key=True, max_length=10, verbose_name='楼号')
    rooms = models.IntegerField(verbose_name='房间数')
    m_no = models.ForeignKey('TbManage', on_delete=models.DO_NOTHING, db_column='m_no', verbose_name='管理员编号')

    class Meta():
        db_table = '公寓楼管理'
        verbose_name_plural = db_table


# 3、创建违规记录表
class TbIllegal(models.Model):
    id = models.AutoField(primary_key=True)
    s_no = models.ForeignKey('TbStudent', on_delete=models.CASCADE, db_column='s_no', blank=True, null=True,
                             verbose_name='学号')
    lou_no = models.ForeignKey('TbFloor', on_delete=models.DO_NOTHING, db_column='lou_no', blank=True, null=True,
                               verbose_name='楼号')
    room_no = models.ForeignKey('TbApartment', on_delete=models.DO_NOTHING, db_column='room_no', blank=True, null=True,
                                verbose_name='房间号')
    stamp_time = models.CharField(max_length=20, verbose_name='违规时间')
    wreason = models.TextField(max_length=500, verbose_name='违规事件')

    class Meta():
        db_table = '违规记录管理'
        verbose_name_plural = db_table


# 4、创建离校表
class TbLx(models.Model):
    s_no = models.ForeignKey('TbStudent', on_delete=models.CASCADE, db_column='s_no', blank=True, null=True,
                             verbose_name='学号')
    room_no = models.ForeignKey('TbApartment', on_delete=models.DO_NOTHING, db_column='room_no', blank=True, null=True,
                                verbose_name='房间号')
    bed_no = models.CharField(max_length=10, blank=True, null=True, verbose_name='床位号')
    l_time = models.CharField(max_length=10, blank=True, null=True, verbose_name='离开时间')
    l_reason = models.TextField(max_length=20, blank=True, null=True, verbose_name='离开原因')

    class Meta():
        db_table = '离校信息管理'
        verbose_name_plural = db_table


# 5、创建管理员信息表
class TbManage(models.Model):
    gender = (
        ("male", "男"),
        ("female", "女"),
    )
    m_no = models.CharField(primary_key=True, max_length=20, verbose_name='管理员编号')
    m_name = models.CharField(max_length=20, verbose_name='管理员姓名')
    m_sex = models.CharField(max_length=10, choices=gender, default='男', verbose_name='性别')
    m_tele = models.CharField(unique=True, max_length=20, blank=True, null=True, verbose_name='电话')
    image = models.ImageField(max_length=256, upload_to='user/%Y%d', default='user/default1.jpg')

    class Meta():
        db_table = '管理员信息管理'
        verbose_name_plural = db_table


# 6、水电费表
class TbSdb(models.Model):
    lou_no = models.ForeignKey(TbFloor, on_delete=models.CASCADE, db_column='lou_no', blank=True, null=True,
                               verbose_name='楼号')
    room_no = models.ForeignKey(TbApartment, on_delete=models.CASCADE, db_column='room_no', blank=True, null=True,
                                verbose_name='房间号')
    month_field = models.CharField(db_column='month_', max_length=4, blank=True, null=True,
                                   verbose_name='月份')  # Field renamed because it ended with '_'.
    elect = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='用电量')
    electric = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='电费')
    water = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='水量')
    waterc = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='水费')

    class Meta():
        db_table = '水电管理'
        verbose_name_plural = db_table


# 7、创建宿管员信息表
class TbSgy(models.Model):
    gender = (
        ("male", "男"),
        ("female", "女"),
    )
    sgy_no = models.CharField(primary_key=True, max_length=10, verbose_name='宿管员号')
    password = models.CharField(max_length=256, verbose_name='密码')
    sgy_name = models.CharField(max_length=10, verbose_name='宿管员姓名')
    sgy_sex = models.CharField(max_length=10, choices=gender, default='男', blank=True, null=True, verbose_name='性别')
    sgy_age = models.SmallIntegerField(blank=True, null=True, verbose_name='年龄')
    sgy_tele = models.CharField(unique=True, max_length=11, blank=True, null=True, verbose_name='电话')
    sgy_rz = models.CharField(max_length=10, blank=True, null=True, verbose_name='职位')
    lou_no = models.ForeignKey(TbFloor, on_delete=models.CASCADE, db_column='lou_no', blank=True, null=True,
                               verbose_name='楼号')
    image = models.ImageField(max_length=256, upload_to='user/%Y%m', default='user/default1.jpg', null=True)

    class Meta():
        db_table = '宿管员信息管理'
        verbose_name_plural = db_table


# 8、创建宿舍卫生信息表
class TbSsws(models.Model):
    lou_no = models.ForeignKey(TbFloor, on_delete=models.CASCADE, db_column='lou_no', blank=True, null=True,
                               verbose_name='楼号')
    room_no = models.ForeignKey(TbApartment, on_delete=models.CASCADE, db_column='room_no', blank=True, null=True,
                                verbose_name='房间号')
    scores = models.IntegerField(blank=True, null=True, verbose_name='得分')
    descores = models.CharField(max_length=50, blank=True, null=True, verbose_name='扣分原因')
    comment_time = models.CharField(max_length=10, blank=True, null=True, verbose_name='检查时间')
    comment_name = models.CharField(max_length=10, blank=True, null=True, verbose_name='评测人')
    image = models.ImageField(max_length=256, null=True, upload_to='image/content/%Y/%m/%d')

    class Meta():
        db_table = '宿舍卫生信息管理'
        verbose_name_plural = db_table


# 9、创建报修管理信息表
class TbSthFix(models.Model):
    content = models.TextField(max_length=200, verbose_name='报修内容')
    lou_no = models.ForeignKey('TbFloor', on_delete=models.CASCADE, db_column='lou_no', verbose_name='楼号')
    room_no = models.ForeignKey('TbApartment', on_delete=models.CASCADE, db_column='room_no', verbose_name='房间号')
    report_time = models.CharField(max_length=20, verbose_name='报修时间')
    reporter = models.CharField(max_length=20, blank=True, null=True, verbose_name='报修人')
    fix_time = models.CharField(max_length=20, blank=True, null=True, verbose_name='维修时间')
    fixer = models.CharField(max_length=20, blank=True, null=True, verbose_name='维修人')
    state = models.TextField(max_length=256, blank=True, null=True, verbose_name='维修状态')
    image = models.ImageField(max_length=256, upload_to='image/content/%Y/%m%d', default='image/default.jpg', null=True)

    class Meta():
        db_table = '报修管理信息管理'
        verbose_name_plural = db_table


# 10、创建学生信息表
class TbStudent(models.Model):
    gender = (
        ("male", "男"),
        ("female", "女"),
    )
    s_no = models.CharField(primary_key=True, max_length=20, verbose_name='学号')
    s_name = models.CharField(max_length=10, verbose_name='姓名')
    s_sex = models.CharField(max_length=10, choices=gender, default='男', verbose_name='性别')
    s_age = models.IntegerField(verbose_name='年龄')
    s_tele = models.CharField(unique=True, max_length=15, blank=True, null=True, verbose_name='电话')
    s_college = models.CharField(max_length=20, verbose_name='所属学院')
    m_no = models.ForeignKey('TbManage', on_delete=models.DO_NOTHING, db_column='m_no', verbose_name='管理员编号')
    image = models.ImageField(max_length=256, upload_to='user/%Y/%m', default='user/default1.jpg')

    class Meta():
        db_table = '学生信息管理'
        verbose_name_plural = db_table


# 11、创建来访者记录表
class TbVisit(models.Model):
    visitor_name = models.CharField(primary_key=True, max_length=20, verbose_name='来访者姓名')
    visitor_tele = models.CharField(unique=True, max_length=20, verbose_name='来访者电话')
    visit_time = models.CharField(max_length=20, verbose_name='来访时间')
    end_time = models.CharField(max_length=20, verbose_name='结束时间')
    visit_sy = models.CharField(max_length=30, blank=True, null=True, verbose_name='事由')
    zbr = models.ForeignKey(TbSgy, on_delete=models.CASCADE, db_column='zbr', blank=True, null=True,
                            verbose_name='值班人')
    hoster_name = models.CharField(max_length=20, verbose_name='被访者')
    hoster_no = models.ForeignKey(TbStudent, on_delete=models.CASCADE, db_column='hoster_no', verbose_name='被访者学号')

    class Meta():
        db_table = '来访者登记管理'
        verbose_name_plural = db_table


# 12、创建学生用户密码表
class StudentModel(models.Model):
    GENDER_CHOICES = (("0", '女'), ('1', '男'))
    stuname = models.CharField(max_length=64, verbose_name='昵称', null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name='性别', null=True)
    stuid = models.CharField(max_length=128, verbose_name='登录账号')
    password = models.CharField(max_length=256, verbose_name='密码')
    email = models.EmailField(max_length=128, blank=True, verbose_name='邮箱地址')
    phone = models.CharField(unique=True, max_length=11, verbose_name='电话', null=True)
    image = models.ImageField(max_length=256, upload_to='user/%Y/%m', default='user/default1.jpg')

    class Meta():
        db_table = '学生用户密码管理'
        verbose_name_plural = db_table

    def __str__(self):
        return "{stuid}".format(stuid=self.stuid)


# 13、创建管理员用户密码表
class ManageModel(models.Model):
    GENDER_CHOICES = (("0", '女'), ('1', '男'))
    mname = models.CharField(max_length=64, verbose_name='昵称', null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, verbose_name='性别')
    mid = models.CharField(max_length=128, verbose_name='账号')
    password = models.CharField(max_length=256, verbose_name='密码')
    email = models.EmailField(max_length=128, blank=True, verbose_name='邮箱地址')
    phone = models.CharField(unique=True, max_length=11, null=True, verbose_name='电话')
    image = models.ImageField(max_length=256, upload_to='user/%Y/%m', default='user/default1.jpg')

    class Meta():
        db_table = '管理员用户密码管理'
        verbose_name_plural = db_table


# 14、公寓评论文章内容
class Content(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(TbStudent, to_field='s_no', on_delete=models.CASCADE, related_name='context',
                                verbose_name='用户')
    type_id = models.ForeignKey(TbIllegal, to_field='id', on_delete=models.CASCADE, related_name='context',
                                verbose_name='类型')
    title = models.CharField(max_length=128, verbose_name='标题')
    picture = models.CharField(max_length=50, verbose_name='标签')
    content = RichTextUploadingField(verbose_name='内容', null=True, blank=True)
    image = models.ImageField(upload_to='user/%Y/%m', default='user/default1.jpg', max_length=256, verbose_name='文章图片')
    publish_time = models.DateTimeField(default=datetime.now, verbose_name='发布时间')
    clicked = models.IntegerField(verbose_name='点击量', default=0)

    def __str__(self):
        return '%s' % self.title

    class Meta:
        verbose_name = '文章内容'
        verbose_name_plural = verbose_name
        db_table = 'content'


# 15、公寓信息表评论
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(TbStudent, to_field='s_no', on_delete=models.CASCADE, verbose_name='用户')
    news_id = models.ForeignKey(Content, to_field='id', on_delete=models.CASCADE, verbose_name='新闻')
    content = RichTextUploadingField(verbose_name='评论内容')
    publish_time = models.DateTimeField(default=datetime.now, verbose_name='评论时间')
    state = models.BooleanField(default=True, verbose_name='审核状态')
    restore = models.ForeignKey(to='self', to_field='id', on_delete=models.CASCADE, verbose_name='回复对象', null=True,
                                blank=True)
    restore_user = models.ForeignKey(TbStudent, to_field='s_no', on_delete=models.CASCADE, related_name='restore',
                                     verbose_name='回复的用户', null=True, blank=True)

    def __str__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = '评论表'
        verbose_name_plural = verbose_name
        db_table = 'comment'

