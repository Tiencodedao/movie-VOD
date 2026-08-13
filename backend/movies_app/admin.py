from django.contrib import admin
from .models import (
    Genre, Category, Person, Movie, Season, Episode,
    SubscriptionPlan, UserSubscription, Review, Favorite, WatchHistory
)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ["name", "role", "slug"]
    list_filter = ["role"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ("name",)}


class SeasonInline(admin.TabularInline):
    model = Season
    extra = 1


class EpisodeInline(admin.TabularInline):
    model = Episode
    extra = 1


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["title", "type", "release_year", "age_rating", "is_free", "is_vip_only", "is_published", "views_count"]
    list_filter = ["type", "is_free", "is_vip_only", "is_published", "is_featured", "age_rating", "release_year"]
    search_fields = ["title", "original_title", "description"]
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ["genres", "categories", "persons"]
    inlines = [SeasonInline, EpisodeInline]


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ["movie", "season_number", "title"]
    search_fields = ["movie__title", "title"]


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ["movie", "season", "episode_number", "title", "duration", "is_free"]
    list_filter = ["is_free"]
    search_fields = ["movie__title", "title"]


@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(admin.ModelAdmin):
    list_display = ["name", "code", "price", "duration_days", "max_resolution", "is_active"]
    list_filter = ["is_active"]
    prepopulated_fields = {"code": ("name",)}


@admin.register(UserSubscription)
class UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = ["user", "plan", "start_date", "end_date", "is_active"]
    list_filter = ["is_active"]
    search_fields = ["user__username", "user__email"]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["user", "movie", "rating", "is_approved", "created_at"]
    list_filter = ["rating", "is_approved"]
    search_fields = ["user__username", "movie__title", "comment"]


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ["user", "movie", "created_at"]
    search_fields = ["user__username", "movie__title"]


@admin.register(WatchHistory)
class WatchHistoryAdmin(admin.ModelAdmin):
    list_display = ["user", "movie", "episode", "watch_time", "completed", "updated_at"]
    list_filter = ["completed"]
    search_fields = ["user__username", "movie__title"]
