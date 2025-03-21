from django.core.validators import RegexValidator
from django.db import models

# Create your models here.

class ActiveBaseModel(models.Model):
    active = models.SmallIntegerField(verbose_name="状态", default=1, choices=((1, "激活"), (0, "删除"),))

    class Meta:
        abstract = True


class LoginLog(models.Model):
    """登录日志"""
    login_time = models.DateTimeField(verbose_name="登录时间", auto_now_add=True)
    login_ip = models.CharField(verbose_name="登录ip", max_length=18)
    login_city = models.CharField(verbose_name="登录城市", max_length=64,null=True,blank=True)
    login_province =  models.CharField(verbose_name="登录省份", max_length=64,null=True,blank=True)
    login_device_type = models.CharField(verbose_name="设备类型", max_length=64,null=True,blank=True)
    login_os = models.CharField(verbose_name="操作系统", max_length=64,null=True,blank=True)
    login_browser = models.CharField(verbose_name="浏览器名称", max_length=64,null=True,blank=True)
    map_location = models.CharField(verbose_name="地图定位", max_length=256,null=True,blank=True)
    exact_address = models.CharField(verbose_name="精确地址", max_length=256,null=True,blank=True)
    # 关联管理员（可以为空）
    administrator = models.ForeignKey(
        verbose_name="管理员",
        to="Administrator",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="login_logs",
    )
    # 关联客户（可以为空）
    customer = models.ForeignKey(
        verbose_name="客户",
        to="Customer",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="login_logs",
    )

class Administrator(ActiveBaseModel):
    """ 管理员表 """
    username = models.CharField(verbose_name="用户名", max_length=32, db_index=True)
    password = models.CharField(verbose_name="密码", max_length=64)
    mobile = models.CharField(verbose_name="手机号", max_length=11, db_index=True)
    create_date = models.DateTimeField(verbose_name="创建日期", auto_now_add=True)


class Level(ActiveBaseModel):
    """ 级别表 """
    title = models.CharField(verbose_name="标题", max_length=32)
    percent = models.IntegerField(verbose_name="折扣", help_text="填入0-100整数表示百分比，例如：90，表示90%")

    def __str__(self):
        return self.title


class Customer(ActiveBaseModel):
    """ 客户表 """
    username = models.CharField(verbose_name="用户名", max_length=32, db_index=True)
    password = models.CharField(verbose_name="密码", max_length=64)
    mobile = models.CharField(verbose_name="手机号", max_length=11, db_index=True,validators=[RegexValidator(r'^\d{11}$','手机格式错误'),],)
    balance = models.DecimalField(verbose_name="账户余额", default=0, max_digits=10, decimal_places=2)
    level = models.ForeignKey(verbose_name="级别", to="Level", on_delete=models.CASCADE,null=True,blank=True)
    create_date = models.DateTimeField(verbose_name="创建日期", auto_now_add=True)
    creator = models.ForeignKey(verbose_name="创建者", to="Administrator", on_delete=models.CASCADE)

    def __str__(self):
        return self.username

class PricePolicy(models.Model):
    """ 价格策略（原价，后续可以根据用级别不同做不同折扣）
    1  1000 10
    2  2000 18
    """
    count = models.IntegerField(verbose_name="数量")
    price = models.DecimalField(verbose_name="价格", default=0, max_digits=10, decimal_places=2)


class Order(ActiveBaseModel):
    """ 订单表 """
    status_choices = (
        (1, "待执行"),
        (2, "正在执行"),
        (3, "已完成"),
        (4, "失败"),
        (5, "已撤单"),
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices, default=1)

    # 202211022123123123
    oid = models.CharField(verbose_name="订单号", max_length=64, unique=True)
    url = models.URLField(verbose_name="视频地址", db_index=True)
    count = models.IntegerField(verbose_name="数量")

    price = models.DecimalField(verbose_name="价格", default=0, max_digits=10, decimal_places=2)
    real_price = models.DecimalField(verbose_name="实际价格", default=0, max_digits=10, decimal_places=2)

    old_view_count = models.CharField(verbose_name="原播放量", max_length=32, default="0")

    create_datetime = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    customer = models.ForeignKey(verbose_name="客户", to="Customer", on_delete=models.CASCADE)
    memo = models.TextField(verbose_name="备注", null=True, blank=True)


class TransactionRecord(ActiveBaseModel):
    """ 交易记录 """
    charge_type_class_mapping = {
        1: "success",
        2: "danger",
        3: "default",
        4: "info",
        5: "primary",
    }
    charge_type_choices = ((1, "充值"), (2, "扣款"), (3, "创建订单"), (4, "删除订单"), (5, "撤单"),)
    charge_type = models.SmallIntegerField(verbose_name="类型", choices=charge_type_choices)

    customer = models.ForeignKey(verbose_name="客户", to="Customer", on_delete=models.CASCADE)
    amount = models.DecimalField(verbose_name="金额", default=0, max_digits=10, decimal_places=2)

    creator = models.ForeignKey(verbose_name="管理员", to="Administrator", on_delete=models.CASCADE, null=True, blank=True)

    order_oid = models.CharField(verbose_name="订单号", max_length=64, null=True, blank=True, db_index=True)
    create_datetime = models.DateTimeField(verbose_name="交易时间", auto_now_add=True)
    memo = models.TextField(verbose_name="备注", null=True, blank=True)

class Boss(models.Model):
    """用于测试上传功能--Form"""
    name = models.CharField(verbose_name='姓名',max_length=32)
    age = models.IntegerField(verbose_name='年龄')
    img = models.CharField(verbose_name='头像',max_length=128)

class CityModelFrom(models.Model):
    """用于测试上传功能---ModelForm"""
    name = models.CharField(verbose_name='名称',max_length=32)
    count = models.IntegerField(verbose_name='人口')
    #本质上数据库也是CharField，自动保存数据
    img = models.FileField(verbose_name='Logo',max_length=128,upload_to='city')

class CityForm(models.Model):
    """用于测试上传功能---ModelForm"""
    name = models.CharField(verbose_name='名称',max_length=32)
    count = models.IntegerField(verbose_name='人口')
    #本质上数据库也是CharField，自动保存数据
    img = models.FileField(verbose_name='Logo',max_length=128)
    url = models.CharField(verbose_name='url值',max_length=256,null=True,blank=True)

