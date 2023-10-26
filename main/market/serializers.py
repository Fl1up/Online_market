from rest_framework import serializers

from main.market.models import Factory, Retail, Ip, BaseModel


class BaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseModel
        fields = '__all__'
        # Задолженность перед поставщиком будет только для чтения
        read_only_fields = ('debt',)

    def update(self, instance, validated_data):
        # Запретить обновление поля "Задолженность перед поставщиком"
        if 'debt' in validated_data:
            raise serializers.ValidationError(
                "Обновление поля 'Задолженность перед поставщиком' запрещено")


class BaseModelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseModel
        fields = '__all__'

    def create(self, validated_data):
        base_item = BaseModel.objects.create(**validated_data)
        return base_item


class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = '__all__'
        # Задолженность перед поставщиком будет только для чтения.
        read_only_fields = ('debt',)


class FactoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = "__all__"

    def create(self, validated_data):
        artist_item = Factory.objects.create(**validated_data)
        return artist_item


class RetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retail
        fields = "__all__"
        # Задолженность перед поставщиком будет только для чтения
        read_only_fields = ('debt',)

    def update(self, instance, validated_data):
        # Запретить обновление поля "Задолженность перед поставщиком"
        if 'debt' in validated_data:
            raise serializers.ValidationError(
                "Обновление поля 'Задолженность перед поставщиком' запрещено")


class RetailCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retail
        fields = "__all__"

    def create(self, validated_data):
        artist_item = Retail.objects.create(**validated_data)
        return artist_item


class IpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ip
        fields = "__all__"
        # Задолженность перед поставщиком будет только для чтения
        read_only_fields = ('debt',)

    def update(self, instance, validated_data):
        # Запретить обновление поля "Задолженность перед поставщиком"
        if 'debt' in validated_data:
            raise serializers.ValidationError(
                "Обновление поля 'Задолженность перед поставщиком' запрещено")


class IpCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ip
        fields = "__all__"

    def create(self, validated_data):
        artist_item = Ip.objects.create(**validated_data)
        return artist_item
