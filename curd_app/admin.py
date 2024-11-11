from django.contrib import admin
from .models import AccountType,SubAccount,Transaction


admin.site.register(AccountType)
admin.site.register(SubAccount)
admin.site.register(Transaction)
