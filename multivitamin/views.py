from django.shortcuts import render
from multivitamin.models import Product
# Create your views here.

selection_list = []

# 수정 필요. 처음 페이지 보여줄 용으로 만듬


def index(req):
    product = Product.objects.all()
    name = req.POST.get("choice", '')
    selection_list.append(name)
    context = {
        "product": product,
        "selectionList": selection_list[-2:]
    }
    return render(req, "index.html", context=context)

# 비교할 제품명 추가 form


# 비교하는 버튼 form


def showProduct(req):
    productList = []
    for name in selection_list[-2:]:
        productList += Product.objects.filter(name=name)
    context = {
        "productList": productList
    }
    return render(req, "compare.html", context=context)
