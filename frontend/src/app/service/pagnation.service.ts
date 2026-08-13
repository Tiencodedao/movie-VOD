import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root',
})
export class PaginationService {
  private readonly apiUrl = 'https://api.themoviedb.org/3/movie/popular';
  private readonly apiKey = 'bf924e9ed29a996837e588664b5d0316';

  constructor(private http: HttpClient) {}

  fetchPageData(page: number): Observable<any> {
    return this.http.get(`${this.apiUrl}?api_key=${this.apiKey}&page=${page}`);
  }

  getVisiblePages(totalPages: number, currentPage: number): number[] {
    const pages: number[] = [];
    const start = Math.max(1, currentPage - 2);
    const end = Math.min(totalPages, currentPage + 2);

    for (let i = start; i <= end; i++) {
      pages.push(i);
    }

    return pages;
  }
}
