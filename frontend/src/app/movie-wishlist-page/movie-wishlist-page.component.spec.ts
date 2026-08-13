import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MovieWishlistPageComponent } from './movie-wishlist-page.component';

describe('MovieWishlistPageComponent', () => {
  let component: MovieWishlistPageComponent;
  let fixture: ComponentFixture<MovieWishlistPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MovieWishlistPageComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MovieWishlistPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
