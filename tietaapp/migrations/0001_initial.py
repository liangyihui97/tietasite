# Generated by Django 2.2 on 2021-05-26 23:25

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('c_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('c_name', models.CharField(max_length=20)),
                ('t_id', models.CharField(max_length=20)),
                ('t_id2', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'verbose_name_plural': 'Courses',
                'db_table': 'Course',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='StationCodeInfo',
            fields=[
                ('id', models.BigIntegerField(blank=True, null=True)),
                ('requiredConfirmCode', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('stationCode', models.CharField(blank=True, max_length=100, null=True)),
                ('orgSaleId', models.CharField(blank=True, max_length=20, null=True)),
                ('orgSaleIdNum', models.CharField(blank=True, max_length=5, null=True)),
                ('stationName', models.CharField(blank=True, max_length=100, null=True)),
                ('towerType', models.CharField(blank=True, max_length=20, null=True)),
                ('roomType', models.CharField(blank=True, max_length=20, null=True)),
                ('towerShareNum', models.IntegerField(blank=True, null=True)),
                ('roomShareNum', models.IntegerField(blank=True, null=True)),
                ('productServiceFee', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('addTime', models.DateTimeField(auto_now_add=True)),
                ('lastTime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': '订单级管理',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='StationInfo',
            fields=[
                ('id', models.BigIntegerField(blank=True, null=True)),
                ('orgSaleId', models.CharField(blank=True, max_length=20, null=True)),
                ('orgSaleIdNum', models.CharField(blank=True, max_length=5, null=True)),
                ('sceneDivide', models.CharField(blank=True, max_length=20, null=True)),
                ('stationName', models.CharField(blank=True, max_length=100, null=True)),
                ('stationNameDx', models.CharField(blank=True, max_length=100, null=True)),
                ('stationCode', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('stationType', models.CharField(blank=True, max_length=20, null=True)),
                ('stationDetail', models.CharField(blank=True, max_length=255, null=True)),
                ('powerRate', models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)),
                ('venueFee', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('demolishTime', models.CharField(blank=True, max_length=20, null=True)),
                ('demolishReason', models.CharField(blank=True, max_length=50, null=True)),
                ('contract', models.CharField(blank=True, max_length=20, null=True)),
                ('notes', models.TextField(blank=True, max_length=500, null=True)),
                ('addTime', models.DateTimeField(auto_now_add=True)),
                ('lastTime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': '站址级管理',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='zujin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stationCode', models.CharField(blank=True, max_length=100, null=True)),
                ('zhangqi', models.CharField(blank=True, max_length=50, null=True)),
                ('payment', models.CharField(blank=True, max_length=5, null=True)),
                ('amount', models.CharField(blank=True, max_length=50, null=True)),
                ('note', models.CharField(blank=True, max_length=100, null=True)),
                ('z', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tietaapp.StationCodeInfo')),
            ],
            options={
                'verbose_name_plural': '租金信息',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='dianfei',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zhangqi', models.CharField(blank=True, max_length=50, null=True)),
                ('stationCode', models.CharField(blank=True, max_length=100, null=True)),
                ('dianbiao', models.CharField(blank=True, max_length=100, null=True)),
                ('starttime', models.CharField(blank=True, max_length=50, null=True)),
                ('startreading', models.CharField(blank=True, max_length=50, null=True)),
                ('endtime', models.CharField(blank=True, max_length=50, null=True)),
                ('endreading', models.CharField(blank=True, max_length=50, null=True)),
                ('powerRate', models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)),
                ('average', models.CharField(blank=True, max_length=50, null=True)),
                ('share', models.CharField(blank=True, max_length=50, null=True)),
                ('sharedetail', models.CharField(blank=True, max_length=50, null=True)),
                ('amount', models.CharField(blank=True, max_length=50, null=True)),
                ('zhangqidetail', models.CharField(blank=True, max_length=50, null=True)),
                ('d', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tietaapp.StationInfo')),
            ],
            options={
                'verbose_name_plural': '电费信息',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('mobile', models.CharField(blank=True, max_length=11, null=True, verbose_name='手机')),
                ('birday', models.DateField(blank=True, null=True, verbose_name='生日')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=10, verbose_name='性别')),
                ('image', models.ImageField(blank=True, max_length=200, null=True, upload_to='users/%Y/%m', verbose_name='头像')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
