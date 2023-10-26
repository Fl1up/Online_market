from django.contrib import admin


from main.market.models import BaseModel, Factory, Ip, Retail

# @admin.register(BaseModel)
# class BaseModelAdmin(admin.ModelAdmin):
#     list_display = ("name",)


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "city",
        "model_product",
    )  # отображение на дисплее
    list_filter = ("city",)  # фильтр
    search_fields = ("name", "city", "supplier__name",)  # поля поиска


@admin.register(Retail)
class RetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'supplier_link', 'debt')
    list_filter = ('city',)
    search_fields = ('name', 'supplier__factory_supplier')
    actions = ['clear_debt']

    def supplier_link(self, obj):
        return '/admin/app/factory/%s">%s</a>' % (
            obj.supplier.id, obj.supplier)

    supplier_link.allow_tags = True
    supplier_link.short_description = 'Поставщик'

    def clear_debt(self, request, queryset):
        updated_count = queryset.update(debt=0)
        self.message_user(request, f'{updated_count} объектов было обновлено')

    clear_debt.short_description = 'Очистить задолженность'


@admin.register(Ip)
class IpAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'supplier_link', 'debt')
    list_filter = ('city',)
    search_fields = ('name', 'supplier__factory_supplier')
    actions = ['clear_debt']

    def supplier_link(self, obj):
        return '/admin/app/factory/%s">%s</a>' % (
            obj.supplier.id, obj.supplier)

    supplier_link.allow_tags = True
    supplier_link.short_description = 'Поставщик'

    def clear_debt(self, request, queryset):
        updated_count = queryset.update(debt=0)
        self.message_user(request, f'{updated_count} объектов было обновлено')

    clear_debt.short_description = 'Очистить задолженность'
