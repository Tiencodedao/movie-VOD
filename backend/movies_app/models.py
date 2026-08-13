from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


# ==========================================
# 1. THỂ LOẠI & DANH MỤC (GENRE & CATEGORY)
# ==========================================

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Genres"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


# ==========================================
# 2. DIỄN VIÊN & ĐẠO DIỄN (PERSON)
# ==========================================

class Person(models.Model):
    ACTOR = "actor"
    DIRECTOR = "director"
    BOTH = "both"

    ROLE_CHOICES = [
        (ACTOR, "Diễn viên"),
        (DIRECTOR, "Đạo diễn"),
        (BOTH, "Cả hai"),
    ]

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=ACTOR)
    avatar = models.URLField(blank=True, help_text="Ảnh chân dung")
    bio = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.get_role_display()})"


# ==========================================
# 3. PHIM, MÙA PHIM & TẬP PHIM (MOVIE VOD)
# ==========================================

class Movie(models.Model):
    MOVIE = "movie"
    SERIES = "series"

    TYPE_CHOICES = [
        (MOVIE, "Phim lẻ"),
        (SERIES, "Phim bộ"),
    ]

    AGE_RATING_CHOICES = [
        ("P", "Phổ thông (P)"),
        ("K", "Dưới 13 tuổi (K)"),
        ("T13", "13+"),
        ("T16", "16+"),
        ("T18", "18+"),
    ]

    title = models.CharField(max_length=255)
    original_title = models.CharField(max_length=255, blank=True, help_text="Tên gốc tiếng Anh/Hàn...")
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()

    release_year = models.PositiveIntegerField()
    duration = models.PositiveIntegerField(
        blank=True,
        null=True,
        help_text="Thời lượng tính theo phút (dành cho Phim lẻ)"
    )
    country = models.CharField(max_length=100, blank=True, default="Việt Nam")
    age_rating = models.CharField(
        max_length=10,
        choices=AGE_RATING_CHOICES,
        default="P"
    )

    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
        default=MOVIE
    )

    genres = models.ManyToManyField(
        Genre,
        related_name="movies",
        blank=True
    )
    categories = models.ManyToManyField(
        Category,
        related_name="movies",
        blank=True
    )
    persons = models.ManyToManyField(
        Person,
        related_name="movies",
        blank=True,
        help_text="Diễn viên & Đạo diễn"
    )

    poster = models.URLField(blank=True, help_text="Ảnh poster dọc")
    banner = models.URLField(blank=True, help_text="Ảnh banner ngang")

    video_url = models.URLField(
        blank=True,
        help_text="Link video phát trực tiếp (chỉ dùng cho Phim lẻ)"
    )
    trailer_url = models.URLField(blank=True)

    is_free = models.BooleanField(default=True)
    is_vip_only = models.BooleanField(default=False, help_text="Yêu cầu tài khoản VIP mới được xem")
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        help_text="Giá mua/thuê lẻ (VNĐ)"
    )

    is_published = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False, help_text="Hiển thị ở Slider/Đề xuất trang chủ")
    views_count = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Season(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="seasons"
    )
    season_number = models.PositiveIntegerField(default=1)
    title = models.CharField(max_length=255, blank=True, help_text="Tên mùa (Ví dụ: Mùa 1)")
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["season_number"]
        unique_together = ("movie", "season_number")

    def __str__(self):
        return f"{self.movie.title} - Mùa {self.season_number}"


class Episode(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="episodes"
    )
    season = models.ForeignKey(
        Season,
        on_delete=models.CASCADE,
        related_name="episodes",
        null=True,
        blank=True
    )
    episode_number = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    thumbnail = models.URLField(blank=True, help_text="Ảnh xem trước tập phim")
    video_url = models.URLField(help_text="Link phát video HLS/MP4")
    duration = models.PositiveIntegerField(
        default=0,
        help_text="Thời lượng tập phim (phút)"
    )
    is_free = models.BooleanField(default=False, help_text="Cho xem thử miễn phí (VD: Tập 1 free)")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["episode_number"]
        unique_together = ("movie", "season", "episode_number")

    def __str__(self):
        return f"{self.movie.title} - Tập {self.episode_number}: {self.title}"


# ==========================================
# 4. GÓI DỊCH VỤ VIP & THÀNH VIÊN
# ==========================================

class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=100, help_text="Tên gói (VD: VIP Hàng Tháng)")
    code = models.SlugField(max_length=50, unique=True, help_text="Mã gói (VD: vip_monthly)")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Giá gói (VNĐ)")
    duration_days = models.PositiveIntegerField(help_text="Số ngày sử dụng")
    max_resolution = models.CharField(max_length=20, default="1080p", help_text="Chất lượng (720p, 1080p, 4K)")
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.price:,.0f} VNĐ)"


class UserSubscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="subscription")
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.SET_NULL, null=True, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def is_valid(self):
        return self.is_active and self.end_date >= timezone.now()

    def __str__(self):
        status = "Còn hạn" if self.is_valid() else "Hết hạn"
        return f"VIP {self.user.username} ({status})"


# ==========================================
# 5. TƯƠNG TÁC & LỊCH SỬ XEM
# ==========================================

class Review(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Đánh giá từ 1 đến 5 sao"
    )
    comment = models.TextField(blank=True)
    is_approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("user", "movie")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.username} - {self.movie.title} ({self.rating}/5)"


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="favorites"
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="favorites"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "movie")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.username} - {self.movie.title}"


class WatchHistory(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="watch_histories"
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="watch_histories"
    )
    episode = models.ForeignKey(
        Episode,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="watch_histories"
    )
    watch_time = models.PositiveIntegerField(
        default=0,
        help_text="Thời gian đã xem (giây)"
    )
    duration = models.PositiveIntegerField(
        default=0,
        help_text="Tổng thời lượng video (giây)"
    )
    completed = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("user", "movie", "episode")
        ordering = ["-updated_at"]

    def __str__(self):
        ep_info = f" (Tập {self.episode.episode_number})" if self.episode else ""
        return f"{self.user.username} - {self.movie.title}{ep_info}"
