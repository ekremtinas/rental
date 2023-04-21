from django.contrib import admin
from .models import iha,iha_model,iha_kategori,iha_marka,kiralama
# Register your models here.



class iha_marka_admin(admin.ModelAdmin):
    list_display = ('marka_adi',)

class iha_model_admin(admin.ModelAdmin):
    list_display = ('model_adi','marka_id',)

class iha_kategori_admin(admin.ModelAdmin):
    list_display = ('kategori_adi',)

class iha_admin(admin.ModelAdmin):
    list_display = ('iha_adi','agirlik','saatlik_fiyati','resim','model_id','kategori_id',)
class kiralama_admin(admin.ModelAdmin):
    list_display = ('iha_id','user_id','kiralama_baslangic','kiralama_bitis','kiralama_ucret',)

admin.site.register(iha,iha_admin)
admin.site.register(iha_model,iha_model_admin)
admin.site.register(iha_kategori,iha_kategori_admin)
admin.site.register(iha_marka,iha_marka_admin)
admin.site.register(kiralama,kiralama_admin)