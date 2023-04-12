from django.contrib import admin
from .models import Article,region,secteur,eglise,bureau,poste,motpresident,titre,pasteur,rang
from .models import Article
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor_uploader.fields import RichTextUploadingField


admin.site.register(region)
admin.site.register(secteur)
admin.site.register(eglise)
admin.site.register(poste)
admin.site.register(bureau)
admin.site.register(titre)
admin.site.register(pasteur)
admin.site.register(rang)



class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        RichTextUploadingField: {'widget': CKEditorUploadingWidget},
    }

admin.site.register(Article, ArticleAdmin)
admin.site.register(motpresident,ArticleAdmin)

admin.site.site_header = 'Administration du site'
admin.site.site_title = 'Région Abidjan-Ouest 2'
