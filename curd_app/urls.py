from django.urls import path
from . import views

urlpatterns = [
    path("", views.transaction_list, name="transaction_list"),
    path("create/", views.transaction_create, name="transaction_create"),
    path(
        "sub-accounts/<int:account_type_id>/",
        views.get_sub_accounts,
        name="get_sub_accounts",
    ),
    path(
        "transactions/<int:id>/edit/", views.transaction_edit, name="transaction_edit"
    ),
    path(
        "transactions/<int:id>/delete/",
        views.transaction_delete,
        name="transaction_delete",
    ),
]
