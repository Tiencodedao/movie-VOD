import { Component, HostListener } from '@angular/core';

@Component({
  selector: 'app-scroll-to-top',
  imports: [],
  templateUrl: './scroll-to-top.component.html',
  styleUrl: './scroll-to-top.component.css'
})
export class ScrollToTopComponent {
  isVisible = false;

  @HostListener('window:scroll', [])

  onWindowScroll(){
    this.isVisible = window.scrollY > 400;
  }

  toTop() {
    window.scrollTo({
      top: 0,
      behavior: 'smooth',
    });
  }
}
