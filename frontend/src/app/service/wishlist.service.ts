import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class WishlistService {
  private wishlist: any[] = [];
  private wishlistCount = new BehaviorSubject<number>(0);
  wishlistCount$ = this.wishlistCount.asObservable();

  constructor() {
    this.loadWishlist(); // Load wishlist from local storage on initialization
  }

  private updateCount() {
    this.wishlistCount.next(this.wishlist.length); // Update wishlist counter
  }

  private loadWishlist() {
    const savedWishlist = JSON.parse(localStorage.getItem('wishlist') || '[]'); // Load from local storage
    this.wishlist = savedWishlist;
    this.updateCount();
  }

  getWishlist(): any[] {
    return this.wishlist;
  }

  addToWishlist(movie: any) {
    if (!this.isInWishlist(movie.id)) {
      this.wishlist.push(movie);
      this.saveWishlist(); // Save to local storage
    }
  }

  removeFromWishlist(movieId: number) {
    this.wishlist = this.wishlist.filter((movie) => movie.id !== movieId);
    this.saveWishlist(); // Save to local storage
  }

  isInWishlist(movieId: number): boolean {
    return this.wishlist.some((movie) => movie.id === movieId);
  }

  private saveWishlist() {
    localStorage.setItem('wishlist', JSON.stringify(this.wishlist)); // Save to local storage
    this.updateCount();
  }
}
