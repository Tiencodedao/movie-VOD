import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { NavBarComponent } from './nav-bar/nav-bar.component';
import { MovieCardComponent } from './movie-card/movie-card.component';
import { ScrollToTopComponent } from "./scroll-to-top/scroll-to-top.component";

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, NavBarComponent, ScrollToTopComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'movie-app';
}
