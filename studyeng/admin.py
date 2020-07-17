from django.utils.safestring import mark_safe
from django.contrib import admin
from . models import Category, Theme, Level, Word


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','icon', "headshot_image")
    readonly_fields = ["headshot_image"]

    def headshot_image(self, obj):
        return mark_safe('<img src="{url}" '
                         'width="{width}" height="{height}" />'
            .format(
            url=obj.icon.url,
            width=obj.icon.width,
            height=obj.icon.height,
        )
        )
    headshot_image.short_description = 'изображение'

class ThemeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'photo',
              'category', 'level', 'headshot_image')
    readonly_fields = ["headshot_image"]

    def headshot_image(self, obj):
        return mark_safe('<img src="{url}" '
                         'width="{width}" height="{height}" />'
            .format(
            url=obj.photo.url,
            width=obj.photo.width,
            height=obj.photo.height,
        )
        )
    headshot_image.short_description = 'изображение'

class WordAdmin(admin.ModelAdmin):
    list_display = ('id',
              'name', 'translation', 'transcription',
              'example', 'sound','headshot_image')
    readonly_fields = ["headshot_image"]

    def headshot_image(self, obj):
        return mark_safe(r"<audio controls><source src="
                         r'""{{% static {url} %}}""</audio>>'
            .format(url=obj.sound.url)
        )
    headshot_image.short_description = 'проигрыватель'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(Level)
admin.site.register(Word, WordAdmin)