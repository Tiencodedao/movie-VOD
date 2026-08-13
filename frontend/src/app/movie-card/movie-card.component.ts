import { DatePipe, NgClass } from '@angular/common';
import { Component, Input } from '@angular/core';
import { RouterLink } from '@angular/router';
import { WishlistService } from '../service/wishlist.service';
import { RatingCircleComponent } from '../rating-circle/rating-circle.component';

@Component({
  selector: 'app-movie-card',
  imports: [DatePipe, NgClass, RouterLink, RatingCircleComponent],
  templateUrl: './movie-card.component.html',
  styleUrl: './movie-card.component.css',
})
export class MovieCardComponent {
  @Input() movie: any;
  constructor(private wishlistService: WishlistService) {}

  getPoster(movie: any) {
    return `https://image.tmdb.org/t/p/w500/${movie.poster_path}`;
  }

  handlePosterErr(e: Event) {
    const img: any = e.target;
    img.src = 'Image-not-found.png';
  }

  movieRatingPercent(movie: any) {
    return Math.round(movie.vote_average * 10);
  }

  // wishList
  toggleWishlist() {
    if (this.isWishlisted()) {
      this.wishlistService.removeFromWishlist(this.movie.id);
    } else {
      this.wishlistService.addToWishlist(this.movie);
    }
  }

  isWishlisted(): boolean {
    return this.wishlistService.isInWishlist(this.movie.id); // Checks if movie is in wishlist
  }
}
