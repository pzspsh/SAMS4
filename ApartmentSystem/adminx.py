# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Pan
# @Time:2020/5/10 18:39
# Project_name: SAMS4
# Name: adminx
import xadmin
from xadmin import views
from .models import *
from django.apps import apps
from import_export import resources
from xadmin.layout import Main, Fieldset, Side


# Register your models here.
class TbManageResource(resources.ModelResource):
    class Meta:
        model = TbManage
        skip_unchanged = True
        # 导入数据时，如果该条数据未修改过，则会忽略
        report_skipped = True
        import_id_fields = ('m_no',)
        # 对象标识的默认字段是m_no，您可以选择在导入时设置哪些字段用作m_no
        fields = (
            'm_no',
            'm_name',
            'm_sex',
            'm_tele',
            'image',
        )
        exclude = (
            'create_time',
            'update_time',
        )


class TbManageAdmin:
    # 列表显示字段
    list_display = ('m_no', 'm_name', 'm_sex', 'm_tele','image')
    # 给admin添加搜索功能
    search_fields = ('m_no', 'm_name')
    # 添加筛选功能
    list_filter = ('m_no', 'm_name')
    # 排序功能
    ordering = ('m_no',)
    # 列表可直接修改的字段
    list_editable = ('m_no', 'm_name', 'm_sex', 'm_tele','image')
    # 分页
    list_per_page = 10
    import_export_args = {
        'import_resource_class': TbManageResource,
    }


class TbApartmentResource(resources.ModelResource):
    class Meta:
        model = TbApartment
        skip_unchanged = True
        # 导入数据时，如果该条数据未修改过，则会忽略
        report_skipped = True
        import_id_fields = ('room_no',)
        # 对象标识的默认字段是room_no，您可以选择在导入时设置哪些字段用作room_no
        fields = (
            'room_no',
            'bed_no',
            'kz_number',
            'xz_number',
            's_no',
            'm_no',
            'lou_no',
        )
        exclude = (
            'create_time',
            'update_time',
        )


class TbApartmentAdmin:
    list_display = ('room_no', 'bed_no', 'kz_number', 'xz_number', 's_no', 'm_no', 'lou_no', 'state')
    search_fields = ('room_no', 'bed_no', 'state')
    list_filter = ('room_no', 'bed_no', 'state')
    ordering = ('bed_no',)
    list_editable = ('room_no', 'bed_no', 'kz_number', 'xz_number', 's_no', 'm_no', 'lou_no')
    # 分页
    list_per_page = 10
    import_export_args = {
        'import_resource_class': TbApartmentResource,
    }


class TbFloorResource(resources.ModelResource):
    class Meta:
        model = TbFloor
        skip_unchanged = True
        # 导入数据时，如果该条数据未修改过，则会忽略
        report_skipped = True
        import_id_fields = ('lou_no',)
        # 对象标识的默认字段是lou_no，您可以选择在导入时设置哪些字段用作lou_no
        fields = (
            'lou_no',
            'rooms',
            'm_no',
        )
        exclude = (
            'create_time',
            'update_time',
        )


class TbFloorAdmin:
    list_display = ('lou_no', 'rooms', 'm_no')
    search_fields = ('lou_no', 'rooms')
    list_filter = ('lou_no', 'rooms')
    ordering = ('lou_no',)
    list_editable = ('lou_no', 'rooms', 'm_no')
    # 分页
    list_per_page = 10
    import_export_args = {
        'import_resource_class': TbFloorResource,
    }


class TbIllegalResource(resources.ModelResource):
    class Meta:
        model = TbIllegal
        skip_unchanged = True
        # 导入数据时，如果该条数据未修改过，则会忽略
        report_skipped = True
        import_id_fields = ('s_no',)
        # 对象标识的默认字段是s_no，您可以选择在导入时设置哪些字段用作s_no
        fields = (
            's_no',
            'lou_no',
            'room_no',
            'stamp_time',
            'wreason',
        )
        exclude = (
            'create_time',
            'update_time',
        )


class TbIllegalAdmin:
    list_display = ('s_no', 'lou_no', 'room_no', 'stamp_time', 'wreason')
    search_fields = ('s_no', 'lou_no', 'room_no')
    list_filter = ('s_no', 'stamp_time', 'wreason')
    ordering = ('stamp_time',)
    list_editable = ('s_no', 'lou_no', 'room_no', 'stamp_time', 'wreason')
    # 分页
    list_per_page = 10
    import_export_args = {
        'import_resource_class': TbIllegalResource,
    }


class TbLxResource(resources.ModelResource):
    class Meta:
        model = TbLx
        skip_unchanged = True
        # 导入数据时，如果该条数据未修改过，则会忽略
        report_skipped = True
        import_id_fields = ('s_no',)
        # 对象标识的默认字段是s_no，您可以选择在导入时设置哪些字段用作s_no
        fields = (
            's_no',
            'room_no'
            'bed_no',
            'l_time',
            'l_reason',
        )
        exclude = (
            'create_time',
            'update_time',
        )


class TbLxAdmin:
    list_display = ('s_no', 'room_no', 'bed_no', 'l_time', 'l_reason')
    search_fields = ('s_no', 'l_time', 'l_reason')
    list_filter = ('s_no',)
    ordering = ('l_time',)
    list_editable = ('s_no', 'room_no', 'l_time', 'l_reason')
    # 分页
    list_per_page = 10
    import_export_args = {
        'import_resource_class': TbLxResource,
    }


class TbSdbResource(resources.ModelResource):
    class Meta:
        model = TbSdb
        skip_unchanged = True
        # 导入数据时，如果该条数据未修改过，则会忽略
        report_skipped = True
        import_id_fields = ('lou_no',)
        # 对象标识的默认字段是lou_no，您可以选择在导入时设置哪些字段用作lou_no
        fields = (
            'lou_no',
            'room_no',
            'month_field',
            'elect',
            'electric',
            'water',
            'waterc',
        )
        exclude = (
            'create_time',
            'update_time',
        )


class TbSdbAdmin:
    list_display = ('lou_no', 'room_no', 'month_field', 'elect', 'electric', 'water', 'waterc')
    search_fields = ('lou_no', 'room_no', 'elect', 'electric', 'water', 'waterc')
    list_filter = ('lou_no', 'month_field', 'elect', 'water')
    ordering = ('elect', 'water')
    list_editable = ('lou_no', 'room_no', 'month_fiel', 'elect', 'electric', 'water', 'waterc')
    # 分页
    list_per_page = 10
    import_export_args = {
        'import_resource_class': TbSdbResource,
    }


class TbSgyResource(resources.ModelResource):
    class Meta:
        model = TbSgy
        skip_unchanged = True
        # 导入数据时，如果该条数据未修改过，则会忽略
        report_skipped = True
        import_id_fields = ('sgy_no',)
        # 对象标识的默认字段是sgy_no，您可以选择在导入时设置哪些字段用作sgy_no
        fields = (
            'sgy_no',
            'password',
            'sgy_name',
            'sgy_sex',
            'sgy_age',
            'sgy_tele',
            'sgy_rz',
            'lou_no',
            'image',
        )
        exclude = (
            'create_time',
            'update_time',
        )


class TbSgyAdmin:
    list_display = ('sgy_no','password', 'sgy_name', 'sgy_sex', 'sgy_age', 'sgy_tele', 'sgy_rz', 'lou_no', 'image')
    search_fields = ('sgy_no', 'sgy_name', 'sgy_rz', 'lou_no')
    list_filter = ('sgy_no', 'sgy_name', 'sgy_rz', 'lou_no')
    ordering = ('sgy_no',)
    list_editable = ('sgy_no', 'password','sgy_name', 'sgy_sex', 'sgy_age', 'sgy_tele', 'sgy_rz', 'lou_no', 'image')
    # 分页
    list_per_page = 10
    import_export_args = {
        'import_resource_class': TbSgyResource,
    }


class TbSswsResource(resources.ModelResource):
    class Meta:
        model = TbSsws
        skip_unchanged = True
        # 导入数据时，如果该条数据未修改过，则会忽略
        report_skipped = True
        import_id_fields = ('lou_no',)
        # 对象标识的默认字段是lou_no，您可以选择在导入时设置哪些字段用作lou_no
        fields = (
            'lou_no',
            'room_no',
            'scores',
            'descores',
            'comment_time',
            'comment_name',
            'image'
        )
        exclude = (
            'create_time',
            'update_time',
        )


class TbSswsAdmin:
    list_display = ('lou_no', 'room_no', 'scores', 'descores', 'comment_time', 'comment_name', 'image')
    search_fields = ('lou_no', 'room_no', 'scores', 'comment_time')
    list_filter = ('lou_no', 'scores', 'comment_time')
    ordering = ('scores',)
    list_editable = ('lou_no', 'room_no', 'scores', 'descores', 'comment_time', 'comment_name', 'image')
    # 分页
    list_per_page = 10
    import_export_args = {
        'import_resource_class': TbSswsResource,
    }


class TbSthFixResource(resources.ModelResource):
    class Meta:
        model = TbSthFix
        skip_unchanged = True
        # 导入数据时，如果该条数据未修改过，则会忽略
        report_skipped = True
        import_id_fields = ('lou_no',)
        # 对象标识的默认字段是lou_no，您可以选择在导入时设置哪些字段用作lou_no
        fields = (
            'content',
            'lou_no',
            'room_no',
            'report_time',
            'reporter',
            'fix_time',
            'fixer',
            'state',
            'image'
        )
        exclude = (
            'create_time',
            'update_time',
        )


class TbSthFixAdmin:
    list_display = ('content', 'lou_no', 'room_no', 'report_time', 'reporter', 'fix_time', 'fixer', 'state', 'image')
    search_fields = ('content', 'report_time', 'reporter')
    list_filter = ('content',)
    ordering = ('lou_no',)
    list_editable = ('content', 'lou_no', 'room_no', 'report_time', 'reporter', 'fix_time', 'fixer', 'state', 'image')
    # 分页
    list_per_page = 10
    import_export_args = {
        'import_resource_class': TbSthFixResource,
    }


class TbStudentResource(resources.ModelResource):
    # def __init__(self):
    #     super(TbStudentResource, self).__init__()
    #     field_list = apps.get_model('student', 'TbStudent')._meta.fields
    #     self.verbose_name_dict = {}
    #     for i in field_list:
    #         self.verbose_name_dict[i.name] = i.verbose_name
    #
    # def get_export_fields(self):
    #     fields = self.get_fields()
    #     for field in fields:
    #         field_name = self.get_field_name(field)
    #         if field_name in self.verbose_name_dict.keys():
    #             field.column_name = self.verbose_name_dict[field_name]
    #     return fields

    class Meta:
        model = TbStudent
        skip_unchanged = True
        # 导入数据时，如果该条数据未修改过，则会忽略
        report_skipped = True
        import_id_fields = ('s_no',)
        # 对象标识的默认字段是s_no，您可以选择在导入时设置哪些字段用作s_no
        fields = (
            's_no',
            's_name',
            's_sex',
            's_age',
            's_tele',
            's_college',
            'm_no',
            'image',
        )
        exclude = (
            'create_time',
            'update_time',
        )


class TbStudentAdmin:
    # 要显示的字段列表
    list_display = ('s_no', 's_name', 's_sex', 's_age', 's_tele', 's_college', 'm_no', 'image')
    # 按照id顺序排列，如果是倒序-id
    search_fields = ('s_no', 's_name')
    # 要筛选的字段
    list_filter = ('s_no', 's_name', 's_sex', 's_tele')
    # 按照id顺序排列，如果是倒序-id
    ordering = ('s_no',)
    # 列表可直接修改的字段
    list_editable = ('s_no', 's_name', 's_sex', 's_age', 's_tele', 's_college', 'm_no','image')
    # 分页
    list_per_page = 10
    import_export_args = {
        'import_resource_class': TbStudentResource,
    }


class BaseSetting:
    enable_themes = True
    use_bootswatch = True


class GlobalSetting:
    global_search_models = [TbStudent]
    site_title = '测试平台'
    site_footer = '测试部'
    menu_style = 'accordion'
    apps_icons = {
        'product': 'fa fa-music',
    }
    global_search_icon = {
        TbStudent: 'fa fa-film',
    }


class TbVisitResource(resources.ModelResource):
    class Meta:
        model = TbApartment
        skip_unchanged = True
        # 导入数据时，如果该条数据未修改过，则会忽略
        report_skipped = True
        import_id_fields = ('visitor_name',)
        # 对象标识的默认字段是visitor_name，您可以选择在导入时设置哪些字段用作visitor_name
        fields = (
            'visitor_name',
            'visitor_tele',
            'visit_time',
            'end_time',
            'visit_sy',
            'zbr',
            'hoster_name',
            'hoster_no',
        )
        exclude = (
            'create_time',
            'update_time',
        )


class TbVisitAdmin:
    list_display = (
        'visitor_name', 'visitor_tele', 'visit_time', 'end_time', 'visit_sy', 'zbr', 'hoster_name', 'hoster_no')
    search_fields = ('visitor_name', 'hoster_no')
    list_filter = ('visitor_name', 'hoster_name')
    ordering = ('visitor_name',)
    list_editable = (
        'visitor_name', 'visitor_tel', 'visit_time', 'end_time', 'visit_sy', 'zbr', 'hoster_name', 'hoster_no')
    # 分页
    list_per_page = 10
    import_export_args = {
        'import_resource_class': TbVisitResource,
    }


class ManageModelResource(resources.ModelResource):
    class Meta:
        model = ManageModel
        skip_unchanged = True
        # 导入数据时，如果该条数据未修改过，则会忽略
        report_skipped = True
        import_id_fields = ('mid',)
        # 对象标识的默认字段是mid，您可以选择在导入时设置哪些字段用作mid
        fields = (
            'mid',
            'email',
            'password',
            'gender',
            'phone',
            'image',
            'mname'
        )
        exclude = (
            'create_time',
            'update_time',
        )


class ManageModelAdmin:
    list_display = ('mid', 'email', 'password', 'gender', 'phone', 'image', 'mname')
    search_fields = ('mid', 'email', 'mname')
    list_filter = ('mid', 'mname')
    ordering = ('mid',)
    list_editable = ('mid', 'email', 'password', 'gender', 'phone', 'image', 'mname')
    # 分页
    list_per_page = 10
    import_export_args = {
        'import_resource_class': ManageModelResource,
    }


class StudentModelResource(resources.ModelResource):
    class Meta:
        model = StudentModel
        skip_unchanged = True
        # 导入数据时，如果该条数据未修改过，则会忽略
        report_skipped = True
        import_id_fields = ('stuid',)
        # 对象标识的默认字段是stuid，您可以选择在导入时设置哪些字段用作stuid
        fields = (
            'stuid',
            'email',
            'password',
            'stuname',
            'gender',
            'phone',
            'image'
        )
        exclude = (
            'create_time',
            'update_time',
        )


class StudentModelAdmin:
    list_display = ('stuid', 'email', 'password', 'stuname', 'gender', 'phone', 'image')
    list_filter = ('stuid', 'email', 'stuname')
    search_fields = ('stuid', 'stuname', 'email')
    ordering = ('stuid',)
    list_editable = ('stuid', 'email', 'password', 'stuname', 'gender', 'phone', 'image')
    # 分页
    list_per_page = 10
    import_export_args = {
        'import_resource_class': StudentModelResource,
    }


class CommentResource(resources.ModelResource):
    class Meta:
        model = Comment
        skip_unchanged = True
        # 导入数据时，如果该条数据未修改过，则会忽略
        report_skipped = True
        import_id_fields = ('id',)
        # 对象标识的默认字段是id，您可以选择在导入时设置哪些字段用作id
        fields = (
            'id',
            'user_id',
            'news_id'
            'content',
            'publish_time',
            'state',
            'restore',
            'restore_user',
        )
        exclude = (
            'create_time',
            'update_time',
        )


class CommentAdmin:
    list_display = ('id', 'user_id', 'news_id', 'content', 'publish_time', 'state', 'restore', 'restore_user')
    list_filter = ('id',)
    search_fields = ('id',)
    ordering = ('id',)
    list_editable = ('id', 'user_id', 'news_id', 'publish_time', 'state', 'restore', 'restore_user')
    # 分页
    list_per_page = 10
    import_export_args = {
        'import_resource_class': CommentResource,
    }


class ContentResource(resources.ModelResource):
    class Meta:
        model = Content
        ski_unchanged = True
        # 导入数据时，如果该条数据未修改过，则会忽略
        report_skipped = True
        import_id_fields = ('id',)
        # 对象标识的默认字段是m_no，您可以选择在导入时设置哪些字段用作m_no
        fields = (
            'id',
            'user_id',
            'type_id',
            'title',
            'picture',
            'content',
            'image',
            'publish_time',
            'clicked'
        )
        exclude = (
            'create_time',
            'update_time',
        )


class ContentAdmin:
    # 列表显示字段
    list_display = ('id', 'user_id', 'type_id', 'title', 'picture', 'content', 'publish_time', 'image','clicked')
    # 给admin添加搜索功能
    search_fields = ('id', 'title', 'user_id')
    # 添加筛选功能
    list_filter = ('title', 'user_id')
    # 排序功能
    ordering = ('id',)
    # 列表可直接修改的字段
    list_editable = ('id', 'user_id', 'type_id', 'title', 'picture', 'content','publish_time','image', 'clicked')
    # 分页
    list_per_page = 10
    import_export_args = {
        'import_resource_class': ContentResource,
    }


xadmin.site.register(TbManage, TbManageAdmin)
xadmin.site.register(TbApartment, TbApartmentAdmin)
xadmin.site.register(TbFloor, TbFloorAdmin)
xadmin.site.register(TbIllegal, TbIllegalAdmin)
xadmin.site.register(ManageModel, ManageModelAdmin)
xadmin.site.register(TbStudent, TbStudentAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(StudentModel, StudentModelAdmin)
xadmin.site.register(TbLx, TbLxAdmin)
xadmin.site.register(TbSdb, TbSdbAdmin)
xadmin.site.register(TbSgy, TbSgyAdmin)
xadmin.site.register(TbSsws, TbSswsAdmin)
xadmin.site.register(TbSthFix, TbSthFixAdmin)
xadmin.site.register(TbVisit, TbVisitAdmin)
xadmin.site.register(Content, ContentAdmin)
xadmin.site.register(Comment, CommentAdmin)
