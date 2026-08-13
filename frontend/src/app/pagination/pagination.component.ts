import { Component, EventEmitter, Input, Output } from '@angular/core';
import { PaginationService } from '../service/pagnation.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-pagination',
  imports: [CommonModule],
  templateUrl: './pagination.component.html',
  styleUrl: './pagination.component.css',
})
export class PaginationComponent {
  @Input() totalPages: number = 1;
  @Input() currentPage: number = 1;
  @Output() pageChange = new EventEmitter<number>();

  visiblePages: number[] = [1, 2, 3];

  constructor(private paginationService: PaginationService) {}

  updateVisiblePages(): void {
    this.visiblePages = this.paginationService.getVisiblePages(
      this.totalPages,
      this.currentPage
    );
  }

  changePage(page: number): void {
    if (page >= 1 && page <= this.totalPages) {
      this.currentPage = page;
      this.updateVisiblePages();
      this.pageChange.emit(page);
    }
  }
}
