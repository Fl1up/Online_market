from django.urls import path
from rest_framework.routers import DefaultRouter

from main.market.apps import MarketConfig
from main.market.views import FactoryCreateAPIView, FactoryRetrieveAPIView, \
    FactoryUpdateAPIView, FactoryDestroyAPIView, IpDestroyAPIView,\
    IpUpdateAPIView,\
    IpRetrieveAPIView, IpListAPIView, \
    IpCreateAPIView, FactoryListAPIView, RetailDestroyAPIView,\
    RetailUpdateAPIView,\
    RetailRetrieveAPIView, \
    RetailCreateAPIView, RetailListAPIView, BaseModelCreateAPIView,\
    BaseModelListAPIView,\
    BaseModelUpdateAPIView, \
    BaseModelRetrieveAPIView, BaseModelDestroyAPIView

app_name = MarketConfig.name

router = DefaultRouter()

urlpatterns = [
    path(
        "base/create/",
        BaseModelCreateAPIView.as_view(),
        name="basemodel_create"),
    path("base/", BaseModelListAPIView.as_view(), name="basemodel_list"),
    path(
        "base/detail/<int:pk>/",
        BaseModelRetrieveAPIView.as_view(),
        name="basemodel_detail"),
    path(
        "base/update/<int:pk>/",
        BaseModelUpdateAPIView.as_view(),
        name="basemodel_update"),
    path(
        "base/delete/<int:pk>/",
        BaseModelDestroyAPIView.as_view(),
        name="basemodel_delete"),

    path(
        "factory/create/",
        FactoryCreateAPIView.as_view(),
        name="factory_create"),
    path("factory/", FactoryListAPIView.as_view(), name="factory_list"),
    path(
        "factory/detail/<int:pk>/",
        FactoryRetrieveAPIView.as_view(),
        name="factory_detail"),
    path(
        "factory/update/<int:pk>/",
        FactoryUpdateAPIView.as_view(),
        name="factory_update"),
    path(
        "factory/delete/<int:pk>/",
        FactoryDestroyAPIView.as_view(),
        name="factory_delete"),

    path(
        "retailL/create/",
        RetailCreateAPIView.as_view(),
        name="retailL_create"),
    path("retailL/", RetailListAPIView.as_view(), name="retailL_list"),
    path(
        "retailL/detail/<int:pk>/",
        RetailRetrieveAPIView.as_view(),
        name="retailL_detail"),
    path(
        "retailL/update/<int:pk>/",
        RetailUpdateAPIView.as_view(),
        name="retailL_update"),
    path(
        "retailL/delete/<int:pk>/",
        RetailDestroyAPIView.as_view(),
        name="retailL_delete"),

    path("ip/create/", IpCreateAPIView.as_view(), name="ip_create"),
    path("ip/", IpListAPIView.as_view(), name="ip_list"),
    path(
        "ip/detail/<int:pk>/",
        IpRetrieveAPIView.as_view(),
        name="ip_detail"),
    path(
        "ip/update/<int:pk>/",
        IpUpdateAPIView.as_view(),
        name="ip_update"),
    path(
        "ip/delete/<int:pk>/",
        IpDestroyAPIView.as_view(),
        name="ip_delete"),

] + router.urls
