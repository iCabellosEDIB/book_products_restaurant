from django.contrib import admin
from .models import Member, Product, Buuking, TableBuuking


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class MemberAdmin(admin.ModelAdmin):
    pass


@admin.register(Buuking)
class MemberAdmin(admin.ModelAdmin):
    pass


@admin.register(TableBuuking)
class MemberAdmin(admin.ModelAdmin):
    pass
