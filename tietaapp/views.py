from django.shortcuts import render, render_to_response
from django.http import HttpResponse
# 登录注册
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.hashers import make_password
from .forms import RegForm, LoginForm
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import resolve, reverse
# 验证明文密码与加密密码是否一致
from django.contrib.auth.hashers import check_password

from .models import StationInfo, StationCodeInfo, User
# 引入Q对象用于查询功能
from django.db.models import Q, Avg, Max, Min, Sum, Count

# 引入分页模块
from django.core.paginator import Paginator

# 引入ajax异步获取json
from django.http import JsonResponse


class RegView(View):
    """
    用户注册
    """
    def get(self, request):  # 用户访问注册页面
        return render(request, "tietaapp/reg.html", {})

    def post(self, request):
        regform = RegForm(request.POST)  # 通过注册表单获取用户提交的内容(form表单中的name字段),然后创建实例regform
        if regform.is_valid():  # 若表单有效性验证成功
            username = request.POST.get("username", "")
            tel= request.POST.get("tel", "")
            password = request.POST.get("password", "")
            user = User()  # 创建用户实例
            user.username = username
            user.mobile = tel
            user.password = password
            user.password = make_password(password)  # 将密码加密处理
            user.save()  # 保存到数据库(除了用save,也可以用create方式)
            return render(request, "tietaapp/login.html")  # 验证有效之后,返回登录页面
        else:
            return render(request, "tietaapp/reg.html", {"regform": regform})  # 如果表单验证失败,则停留在注册页面


class LoginView(View):
    """
    用户登录
    """
    def get(self, request):  # 用户访问登录页面
        return render(request, "tietaapp/login.html", {})

    def post(self, request):
        tel = request.POST.get('tel')
        password = request.POST.get('password')
        if not all([tel, password]):
            return render(request, 'tietaapp/login.html', {"error": '信息不完整'})
        try:
            user = User.objects.get(mobile=tel)
            pwd = user.password
            if check_password(password, pwd):
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('tieta:index', ))
                else:
                    return render(request, 'tietaapp/login.html', {"error": '用户未激活'})
            else:
                return render(request, 'tietaapp/login.html', {"error": '密码错误'})
        except User.DoesNotExist:
            return render(request, 'tietaapp/login.html', {"error": '此用户未注册'})


class LogoutView(View):
    """
    用户登出
    """
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('tieta:index', ))


# Create your views here.
# 【规范】这里的template也采用命名空间格式'tietaapp/index.html'
def index(request):
    # 查询白云平均场地费
    avg_venuefee = StationInfo.objects.aggregate(avg_venuefee=Avg('venueFee'))
    # 查询白云平均服务费，数据格式{'sum_productservicefee': Decimal('48981848.31')}
    sum_productservicefee = StationCodeInfo.objects.aggregate(sum_productservicefee=Sum('productServiceFee'))
    # 去重计数,(count=Count('id', distinct=True))中的count为自定义字典名称
    count_productservicefee = StationCodeInfo.objects.aggregate(count_productservicefee=Count('id', distinct=True))
    avg_productservicefee = sum_productservicefee['sum_productservicefee']/count_productservicefee['count_productservicefee']
    context = {
        'avg_venuefee': avg_venuefee,
        'sum_productservicefee': sum_productservicefee,
        'count_productservicefee': count_productservicefee,
        'avg_productservicefee': avg_productservicefee,
    }
    return render(request, 'tietaapp/index.html', context)

#def
# vote(request, question_id):
#        return HttpResponse("You're voting on question %s." % question_id)


def stationinfo(request):
    # 查询功能
    search = request.GET.get('search')
    error_msg = ''
    if search:
        station_list = StationInfo.objects.filter(
            Q(stationName__contains=search) |
            Q(stationNameDx__contains=search) |
            Q(stationDetail__contains=search) |
            Q(stationCode__iexact=search)
        ).order_by('-powerRate').order_by('-venueFee')  # 按场地费排序
    else:
        search = ''
        station_list = StationInfo.objects.all()
    if len(station_list) >= 8:
        paginator = Paginator(station_list, 8)
        page = request.GET.get('page')
    else:
        paginator = Paginator(station_list, len(station_list))
        page = request.GET.get('page')
    stations = paginator.get_page(page)
    context = {'text': stations, 'search': search,}
    return render(request, 'tietaapp/StationInfo.html', context)

    # text = StationInfo.objects.all()
    # context = {'text': text}
    # return render(request, 'tietaapp/StationInfo.html', context)


def stationcodeinfo(request):
    # 查询功能
    search = request.GET.get('search')
    if search:
        station_list = StationCodeInfo.objects.filter(
            Q(stationName__contains=search) |
            Q(requiredConfirmCode__iexact=search) |
            Q(stationCode__iexact=search)
        ).order_by('-productServiceFee')  # 按场地费排序
    else:
        search = ''
        station_list = StationCodeInfo.objects.all()
    if len(station_list) >= 8:
        paginator = Paginator(station_list, 8)
        page = request.GET.get('page')
    else:
        paginator = Paginator(station_list, len(station_list))
        page = request.GET.get('page')
    stations = paginator.get_page(page)
    context = {'text': stations, 'search': search}
    return render(request, 'tietaapp/StationCodeInfo.html', context)


def stationdetail(request, id):
    station_info = StationInfo.objects.get(id=id)
    station_code_info = StationCodeInfo.objects.filter(id=id)
    context = {'station_info': station_info, 'station_code_info': station_code_info}
    return render(request, 'tietaapp/StationDetail.html', context)


def view_404(request,exception):
    return render(request, 'tietaapp/error404.html', context={'error':'访问有误:页面不存在'}, status=404)


def view_500(request):
    return render(request, 'tietaapp/error404.html', context={'error':'访问有误:服务器错误'}, status=500)


def echarts_data(request):
    # 每个营服的场地费
    venuefee = StationInfo.objects.values('orgSaleId').annotate(venuefee=Sum('venueFee'))
    # 每个营服的服务费
    productservicefee = StationCodeInfo.objects.values('orgSaleId').annotate(productservicefee=Sum('productServiceFee')).order_by('orgSaleIdNum')
    jsondata = {
        '营服': [i['orgSaleId'] for i in productservicefee],
        '服务费': [i['productservicefee'] for i in productservicefee],
    }
    return JsonResponse(jsondata)