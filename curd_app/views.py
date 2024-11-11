from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import AccountType,SubAccount,Transaction
# Create your views here.

def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request,'transactions/list.html',{'transactions':transactions})

def transaction_create(request):
    account_types = AccountType.objects.all()
    sub_accounts = SubAccount.objects.all()

    if request.method == "POST":
        code = request.POST["code"]
        name = request.POST["name"]
        account_type = AccountType.objects.get(id=request.POST["account_type"])
        sub_account = SubAccount.objects.get(id=request.POST["sub_account"])
        action = request.POST["action"]
        description = request.POST["description"]
        remarks = request.POST["remarks"]

        transaction = Transaction.objects.create(
            code=code,
            name=name,
            account_type=account_type,
            sub_account=sub_account,
            action=action,
            description=description,
            remarks=remarks,
        )
        return redirect("transaction_list")

    return render(
        request,
        "transactions/create.html",
        {"account_types": account_types},
    )

def get_sub_accounts(request,account_type_id):
    sub_accounts = SubAccount.objects.filter(account_type_id=account_type_id)
    data = [
        {"id": sub_account.id, "name": sub_account.name} for sub_account in sub_accounts
    ]
    return JsonResponse(data, safe=False)


def transaction_edit(request, id):
    transaction = get_object_or_404(Transaction, id=id)
    account_types = AccountType.objects.all()
    sub_accounts = SubAccount.objects.filter(account_type=transaction.account_type)

    if request.method == "POST":
        transaction.code = request.POST["code"]
        transaction.name = request.POST["name"]
        transaction.account_type = AccountType.objects.get(
            id=request.POST["account_type"]
        )
        transaction.sub_account = SubAccount.objects.get(id=request.POST["sub_account"])
        transaction.action = request.POST["action"]
        transaction.description = request.POST["description"]
        transaction.remarks = request.POST["remarks"]
        transaction.save()
        return redirect("transaction_list")

    return render(
        request,
        "transactions/edit.html",
        {
            "transaction": transaction,
            "account_types": account_types,
            "sub_accounts": sub_accounts,
        },
    )


def transaction_delete(request, id):
    transaction = get_object_or_404(Transaction, id=id)
    transaction.delete()
    return redirect("transaction_list")
