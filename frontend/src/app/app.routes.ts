import { Routes } from '@angular/router';
import { MovieListPageComponent } from './movie-list-page/movie-list-page.component';
import { MovieWishlistPageComponent } from './movie-wishlist-page/movie-wishlist-page.component';
import { MovieDetailsPageComponent } from './movie-details-page/movie-details-page.component';
import { SearchPageComponent } from './search-page/search-page.component';
import { NotFoundComponent } from './not-found/not-found.component';

export const routes: Routes = [
  {
    path: '',

    component: MovieListPageComponent,

    title: 'Home | Movie Best',
  },

  {
    path: 'search',
    component: SearchPageComponent,
    title: 'Search',
  },

  {
    path: 'search/:search/:page',
    component: SearchPageComponent,
    title: 'Search',
  },

  {
    path: 'watchlist',

    component: MovieWishlistPageComponent,

    title: 'Watch List',
  },

  {
    path: 'movie/:id',

    component: MovieDetailsPageComponent,

    title: 'Details',
  },

  {
    path: '**',
    component: NotFoundComponent,
    title: 'Not Found',
  },
];
