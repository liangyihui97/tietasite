from django import forms


# 用户注册表单
class RegForm(forms.Form):
    # 用户名
    username = forms.CharField(required=True, min_length=5, error_messages={'required': '最小5位'})
    # 手机号
    tel = forms.CharField(required=True, min_length=11, max_length=11, error_messages={'required': '请输入11位手机号'})
    # 用户密码
    password = forms.CharField(required=True, min_length=6, error_messages={'required': '密码最小长度为6位'})


# 用户登录表单
class LoginForm(forms.Form):
    # 必填项
    # 手机号
    tel = forms.CharField(required=True, min_length=11, max_length=11, error_messages={'required': '请输入11位手机号'})
    # 用户密码
    password = forms.CharField(required=True, min_length=6, error_messages={'required': '密码最小长度为6位'})