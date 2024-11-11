from django.db import models


class AccountType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class SubAccount(models.Model):
    name = models.CharField(max_length=50)
    account_type = models.ForeignKey(AccountType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.account_type}-{self.name}"


class Transaction(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    account_type = models.ForeignKey(AccountType, on_delete=models.CASCADE)
    sub_account = models.ForeignKey(SubAccount, on_delete=models.CASCADE)
    action = models.CharField(max_length=50)
    description = models.TextField()
    remarks = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.code} - {self.name}"
