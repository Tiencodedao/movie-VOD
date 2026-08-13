import { Component, OnInit } from '@angular/core';
import { RouterLink } from '@angular/router';
import { WishlistService } from '../service/wishlist.service';

@Component({
  selector: 'app-nav-bar',
  imports: [RouterLink],
  templateUrl: './nav-bar.component.html',
  styleUrl: './nav-bar.component.css',
})
export class NavBarComponent implements OnInit {
  wishlistCount = 0;

  constructor(private wishlistService: WishlistService) {}

  ngOnInit() {
    this.wishlistService.wishlistCount$.subscribe((count) => {
      this.wishlistCount = count; // Updates wishlist count in navbar
    });
  }
}
