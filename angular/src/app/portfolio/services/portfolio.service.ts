import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../../environments/environment';
import { Observable } from 'rxjs';
import { Portfolio } from '../models/portfolio';

@Injectable({ providedIn: 'root' })
export class PortfolioService {
  private readonly apiUrl = environment.apiUrl + `portfolio`;
  constructor(private httpClient: HttpClient) {}

  getAllPortfolio(): Observable<Portfolio[]> {
    return this.httpClient.get<Portfolio[]>(this.apiUrl);
  }

  getPortfolioDetails(id: string): Observable<Portfolio> {
    return this.httpClient.get<Portfolio>(`${this.apiUrl}/${id}`);
  }

  createPortfolio(
    creator: string,
    identif: string,
    profileImg: string,
    img: string,
    desc: string,

  ): Observable<any> {
    return this.httpClient.post(`${this.apiUrl}/new`, {
      creator,
      identif,
      profileImg,
      img,
      desc,

    });
  }

  updatePortfolioDetails(
    id: string,
    creator: string,
    identif: string,
    profileImg: string,
    img: string,
    desc: string,

  ): Observable<Portfolio> {
    return this.httpClient.put<Portfolio>(`${this.apiUrl}/${id}`, {
      creator,
      identif,
      profileImg,
      img,
      desc,
    });
  }

  deleteEvent(id: string): Observable<any> {
    return this.httpClient.delete(`${this.apiUrl}/${id}`);
  }
}
