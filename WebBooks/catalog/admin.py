from django.contrib import admin

from .models import Author, Ganre, Book, Language, Status, BookInstance


# admin.site.register(Author)
admin.site.register(Ganre)
#admin.site.register(Book)
admin.site.register(Language)
admin.site.register(Status)
#admin.site.register(BookInstance)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("last_name","first_name","date_of_birth","date_of_death")
    fields = ['first_name','last_name',('date_of_birth','date_of_death')]
admin.site.register(Author,AuthorAdmin)

class BooksIntanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title","genre","display_author")
    list_filter = ('genre','author')
    inlines = [BooksIntanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('book','status')
    fieldsets = (("Экземпляр книги",{
        'fields':('book','imprint','inv_nom')
    }),
    ('Статус окончание и его действия',{
        'fields': ('status', 'due_back','borrower')
    }),)
# Register your models here.
