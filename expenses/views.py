from rest_framework import viewsets
from .models import Expense
from .serializers import ExpenseSerializer

import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all().order_by('-date')
    serializer_class = ExpenseSerializer


@api_view(['GET'])
def convert_currency(request):
    amount = request.GET.get('amount')
    from_currency = request.GET.get('from')
    to_currency = request.GET.get('to')

    url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"
    response = requests.get(url)
    data = response.json()

    return Response(data)