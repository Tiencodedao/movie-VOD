import { Component } from '@angular/core';
import { RequestService } from '../service/request.service';
import { FormsModule } from '@angular/forms';
import { MovieCardComponent } from '../movie-card/movie-card.component';
import { PaginationComponent } from '../pagination/pagination.component';
import { PaginationService } from '../service/pagnation.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-search-page',
  imports: [FormsModule, MovieCardComponent, PaginationComponent],
  templateUrl: './search-page.component.html',
  styleUrl: './search-page.component.css',
})
export class SearchPageComponent {
  searchResults: any = [];
  totalPages: number = 0;
  currentPage: number = 1;
  constructor(
    private requestService: RequestService,
    private route: ActivatedRoute,
    private router: Router
  ) {}

  ngOnInit() {
    this.route.params.subscribe((params) => {
      if (params['search']) {
        console.log(params);
        this.searchData = params['search'];
        this.currentPage = +params['page'] || 1;
        this.search();
      }
    });
  }

  loadMovies(page: number): void {
    this.requestService
      .getSearchResults(this.searchData, page)
      .subscribe((data: any) => {
        this.searchResults = data.results;
        this.totalPages = data.total_pages;
        this.currentPage = page;
      });
  }

  onPageChange(page: number): void {
    this.loadMovies(page);
    this.router.navigate(['/search', this.searchData, page]);
  }

  searchData: string = '';
  searchedQuery: string = '';

  search() {
    this.loadMovies(this.currentPage);
    this.searchedQuery = this.searchData;
    this.router.navigate(['/search', this.searchData, this.currentPage]);
  }
}
