from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from main.market.models import Ip, Retail, Factory, BaseModel
from main.market.serializers import BaseModelCreateSerializer,\
    BaseModelSerializer, IpCreateSerializer, IpSerializer, \
    RetailSerializer, RetailCreateSerializer, FactoryCreateSerializer,\
    FactorySerializer
from main.users.permissions import IsPublic


class BaseModelCreateAPIView(generics.CreateAPIView):
    """BaseModel Create"""
    serializer_class = BaseModelCreateSerializer
    permission_classes = [IsPublic]


class BaseModelListAPIView(generics.ListAPIView):
    """BaseModel List"""
    serializer_class = BaseModelSerializer
    queryset = BaseModel.objects.all()
    permission_classes = [IsPublic]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('country', "city")


class BaseModelRetrieveAPIView(generics.RetrieveAPIView):
    """BaseModel Retrive"""
    serializer_class = BaseModelSerializer
    queryset = BaseModel.objects.all()
    permission_classes = [IsPublic]

    def get_queryset(self):
        return BaseModel.objects.filter(country=self.request.country)


class BaseModelUpdateAPIView(generics.UpdateAPIView):
    """BaseModel Updaate"""
    serializer_class = BaseModelSerializer
    queryset = BaseModel.objects.all()
    permission_classes = [IsPublic]

    def get_queryset(self):
        return BaseModel.objects.filter(country=self.request.country)


class BaseModelDestroyAPIView(generics.DestroyAPIView):
    """BaseModel Delete"""
    queryset = BaseModel.objects.all()
    permission_classes = [IsPublic]

    def get_queryset(self):
        return BaseModel.objects.filter(country=self.request.country)


class FactoryCreateAPIView(generics.CreateAPIView):
    """Factory Create"""
    serializer_class = FactoryCreateSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('country')
    permission_classes = [IsPublic]

    def get_queryset(self):
        return Factory.objects.filter(country=self.request.country)


class FactoryListAPIView(generics.ListAPIView):
    """Factory List"""
    serializer_class = FactorySerializer
    permission_classes = [IsPublic]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('country', "city")

    def get_queryset(self):
        queryset = Factory.objects.all()
        code = self.request.query_params.get('code', None)
        if code is not None:
            queryset = queryset.filter(code=code)
        return queryset


class FactoryRetrieveAPIView(generics.RetrieveAPIView):
    """Factory Retrive"""
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()
    permission_classes = [IsPublic]

    def get_queryset(self):
        return Factory.objects.filter(country=self.request.country)


class FactoryUpdateAPIView(generics.UpdateAPIView):
    """Factory Updaate"""
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()
    permission_classes = [IsPublic]

    def get_queryset(self):
        return Factory.objects.filter(country=self.request.country)


class FactoryDestroyAPIView(generics.DestroyAPIView):
    """Factory Delete"""
    queryset = Factory.objects.all()
    permission_classes = [IsPublic]

    def get_queryset(self):
        return Factory.objects.filter(country=self.request.country)


class RetailCreateAPIView(generics.CreateAPIView):
    """Retail Create"""
    serializer_class = RetailCreateSerializer
    permission_classes = [IsPublic]

    def get_queryset(self):
        return Retail.objects.filter(country=self.request.country)


class RetailListAPIView(generics.ListAPIView):
    """Retail List"""
    serializer_class = RetailSerializer
    queryset = Retail.objects.all()
    permission_classes = [IsPublic]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('country', "city")

    def get_queryset(self):
        return Retail.objects.filter(country=self.request.country)


class RetailRetrieveAPIView(generics.RetrieveAPIView):
    """Retail Retrive"""
    serializer_class = RetailSerializer
    queryset = Retail.objects.all()
    permission_classes = [IsPublic]

    def get_queryset(self):
        return Retail.objects.filter(country=self.request.country)


class RetailUpdateAPIView(generics.UpdateAPIView):
    """Retail Updaate"""
    serializer_class = RetailSerializer
    queryset = Retail.objects.all()
    permission_classes = [IsPublic]

    def get_queryset(self):
        return Retail.objects.filter(country=self.request.country)


class RetailDestroyAPIView(generics.DestroyAPIView):
    """Retail Delete"""
    queryset = Retail.objects.all()
    permission_classes = [IsPublic]

    def get_queryset(self):
        return Retail.objects.filter(country=self.request.country)


class IpCreateAPIView(generics.CreateAPIView):
    """Ip Create"""
    serializer_class = IpCreateSerializer
    permission_classes = [IsPublic]

    def get_queryset(self):
        return Ip.objects.filter(country=self.request.country)


class IpListAPIView(generics.ListAPIView):
    """Ip List"""
    serializer_class = IpSerializer
    queryset = Ip.objects.all()
    permission_classes = [IsPublic]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('country', "city")

    def get_queryset(self):
        return Ip.objects.filter(country=self.request.country)


class IpRetrieveAPIView(generics.RetrieveAPIView):
    """Ip Retrive"""
    serializer_class = IpSerializer
    queryset = Ip.objects.all()
    permission_classes = [IsPublic]

    def get_queryset(self):
        return Ip.objects.filter(country=self.request.country)


class IpUpdateAPIView(generics.UpdateAPIView):
    """Ip Updaate"""
    serializer_class = IpSerializer
    queryset = Ip.objects.all()
    permission_classes = [IsPublic]

    def get_queryset(self):
        return Ip.objects.filter(country=self.request.country)


class IpDestroyAPIView(generics.DestroyAPIView):
    """Ip Delete"""
    queryset = Ip.objects.all()
    permission_classes = [IsPublic]

    def get_queryset(self):
        return Ip.objects.filter(country=self.request.country)
