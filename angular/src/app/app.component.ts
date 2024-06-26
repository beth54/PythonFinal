import { Component } from '@angular/core';
import { AuthService } from './core';

@Component({
  selector: 'app-root',
  template: `
    <header>
      <nav class="navbar navbar-expand-lg navbar-dark bg-dark px-3">
        <a class="navbar-brand" routerLink="">Event Planner</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto">
            <li class="nav-item" routerLinkActive="active">
              <a class="nav-link" routerLink="events">Events</a>
            </li>
            <li class="nav-item" routerLinkActive="active">
              <a class="nav-link" routerLink="admin">Admin</a>
            </li>
          </ul>
          <div class="form-inline">
            <button
              class="btn btn-outline-success my-2 my-sm-0"
              type="button"
              *ngIf="username"
              (click)="logout()"
            >
              Logout
            </button>
          </div>
        </div>
      </nav>
    </header>
    <main class="d-flex flex-column flex-grow-1 h-100 w-100">
      <router-outlet></router-outlet>
    </main>
  `,
  styles: [],
})
export class AppComponent {
  username = '';
  constructor(private authService: AuthService) {
    this.username = authService.user.username;
  }

  ngOnInit(): void {}

  logout() {
    this.authService.logout();
  }
}
