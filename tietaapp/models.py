# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractUser


class Course(models.Model):
    c_id = models.CharField(primary_key=True, max_length=20)
    c_name = models.CharField(max_length=20)
    t_id = models.CharField(max_length=20)
    t_id2 = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Course'
        verbose_name_plural = 'Courses'


class User(AbstractUser):
    """
    用户
    """
    # name = models.CharField(verbose_name="别名", max_length=100, default="")
    # email = models.CharField(verbose_name="邮箱", max_length=100)
    # password = models.CharField(verbose_name="密码", max_length=128)
    mobile = models.CharField(verbose_name='手机', max_length=11, blank=True, null=True)
    birday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    gen = (
        ("male", "男"),
        ("female", "女"),
    )
    gender = models.CharField(verbose_name="性别", choices=gen, default="male", max_length=10)
    image = models.ImageField(verbose_name="头像", upload_to="users/%Y/%m", max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


# 站址级信息
class StationInfo(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    orgSaleId = models.CharField(max_length=20, blank=True, null=True)
    orgSaleIdNum = models.CharField(max_length=5, blank=True, null=True)
    sceneDivide = models.CharField(max_length=20, blank=True, null=True)
    stationName = models.CharField(max_length=100, blank=True, null=True)
    stationNameDx = models.CharField(max_length=100, blank=True, null=True)
    stationCode = models.BigIntegerField(primary_key=True)
    stationType = models.CharField(max_length=20, blank=True, null=True)
    stationDetail = models.CharField(max_length=255, blank=True, null=True)
    powerRate = models.DecimalField(max_digits=5, decimal_places=4, blank=True, null=True)
    venueFee = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    demolishTime = models.CharField(max_length=20, blank=True, null=True)
    demolishReason = models.CharField(max_length=50, blank=True, null=True)
    contract = models.CharField(max_length=20, blank=True, null=True)
    notes = models.TextField(max_length=500, blank=True, null=True)
    addTime = models.DateTimeField(auto_now_add=True)
    lastTime = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        verbose_name_plural = '站址级管理'


# 订单级信息
class StationCodeInfo(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    requiredConfirmCode = models.BigIntegerField(primary_key=True)
    stationCode = models.BigIntegerField(blank=True, null=True)
    orgSaleId = models.CharField(max_length=20, blank=True, null=True)
    orgSaleIdNum = models.CharField(max_length=5, blank=True, null=True)
    stationName = models.CharField(max_length=100, blank=True, null=True)
    towerType = models.CharField(max_length=20, blank=True, null=True)
    roomType = models.CharField(max_length=20, blank=True, null=True)
    towerShareNum = models.IntegerField(blank=True, null=True)
    roomShareNum = models.IntegerField(blank=True, null=True)
    # 保留2位小数，最大长度为9
    productServiceFee = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    addTime = models.DateTimeField(auto_now_add=True)
    lastTime = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        verbose_name_plural = '订单级管理'
