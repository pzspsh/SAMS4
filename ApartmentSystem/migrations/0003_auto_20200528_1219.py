# Generated by Django 3.0.6 on 2020-05-28 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ApartmentSystem', '0002_tbsgy_password'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='managemodel',
            options={'verbose_name_plural': '管理员用户密码管理'},
        ),
        migrations.AlterModelOptions(
            name='studentmodel',
            options={'verbose_name_plural': '学生用户密码管理'},
        ),
        migrations.AlterModelOptions(
            name='tbapartment',
            options={'verbose_name_plural': '公寓号信息管理'},
        ),
        migrations.AlterModelOptions(
            name='tbfloor',
            options={'verbose_name_plural': '公寓楼管理'},
        ),
        migrations.AlterModelOptions(
            name='tbillegal',
            options={'verbose_name_plural': '违规记录管理'},
        ),
        migrations.AlterModelOptions(
            name='tblx',
            options={'verbose_name_plural': '离校信息管理'},
        ),
        migrations.AlterModelOptions(
            name='tbmanage',
            options={'verbose_name_plural': '管理员信息管理'},
        ),
        migrations.AlterModelOptions(
            name='tbsdb',
            options={'verbose_name_plural': '水电管理'},
        ),
        migrations.AlterModelOptions(
            name='tbsgy',
            options={'verbose_name_plural': '宿管员信息管理'},
        ),
        migrations.AlterModelOptions(
            name='tbssws',
            options={'verbose_name_plural': '宿舍卫生信息管理'},
        ),
        migrations.AlterModelOptions(
            name='tbsthfix',
            options={'verbose_name_plural': '报修管理信息管理'},
        ),
        migrations.AlterModelOptions(
            name='tbstudent',
            options={'verbose_name_plural': '学生信息管理'},
        ),
        migrations.AlterModelOptions(
            name='tbvisit',
            options={'verbose_name_plural': '来访者登记管理'},
        ),
        migrations.AlterModelTable(
            name='managemodel',
            table='管理员用户密码管理',
        ),
        migrations.AlterModelTable(
            name='studentmodel',
            table='学生用户密码管理',
        ),
        migrations.AlterModelTable(
            name='tbapartment',
            table='公寓号信息管理',
        ),
        migrations.AlterModelTable(
            name='tbfloor',
            table='公寓楼管理',
        ),
        migrations.AlterModelTable(
            name='tbillegal',
            table='违规记录管理',
        ),
        migrations.AlterModelTable(
            name='tblx',
            table='离校信息管理',
        ),
        migrations.AlterModelTable(
            name='tbmanage',
            table='管理员信息管理',
        ),
        migrations.AlterModelTable(
            name='tbsdb',
            table='水电管理',
        ),
        migrations.AlterModelTable(
            name='tbsgy',
            table='宿管员信息管理',
        ),
        migrations.AlterModelTable(
            name='tbssws',
            table='宿舍卫生信息管理',
        ),
        migrations.AlterModelTable(
            name='tbsthfix',
            table='报修管理信息管理',
        ),
        migrations.AlterModelTable(
            name='tbstudent',
            table='学生信息管理',
        ),
        migrations.AlterModelTable(
            name='tbvisit',
            table='来访者登记管理',
        ),
    ]
