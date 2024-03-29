from django.contrib import admin
from django.utils.html import mark_safe
from . import models

# Register your models here.


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()

    pass


class PhotoInline(admin.TabularInline):
    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """Room Admin Definition"""

    inlines = (PhotoInline,)

    fieldsets = (
        ("Sapces", {"fields": ("beds", "bedrooms", "baths")}),
        (
            "Basic Info",
            {
                "fields": (
                    "name",
                    "description",
                    "country",
                    "adress",
                    "city",
                    "price",
                    "guests",
                )
            },
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        (
            "More About the Sapces",
            {"fields": ("amenities", "facilities", "house_rules")},
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    ordering = ("name", "price", "bedrooms")
    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "adress",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    list_filter = (
        "instant_book",
        "city",
        "room_type",
        "host__superhost",
        "host__gender",
        "amenities",
        "facilities",
        "house_rules",
        "country",
    )

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )
    raw_id_fields = ("host",)

    search_fields = ("=city", "^host__username")

    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "count Photos"
    count_amenities.short_description = "count Amenities"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Photo Admin Definition"""

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"
