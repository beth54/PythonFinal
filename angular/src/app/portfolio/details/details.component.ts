import { Component } from '@angular/core';
import { PortfolioService } from '../services/portfolio.service';
import { ActivatedRoute, ParamMap } from '@angular/router';
import { NgbModal, NgbModalRef } from '@ng-bootstrap/ng-bootstrap';
import { tap, switchMap, of, finalize } from 'rxjs';
import { Portfolio } from '../models/portfolio';
import { AuthService } from '../../core';

@Component({
  selector: 'app-details',
  templateUrl: './details.component.html',
  styleUrl: './details.component.css',
})
export class DetailsComponent {
  loading = false;
  id = '';
  details: Portfolio | null = null;
  creator = '';
  identif = '';
  profileImg = '';
  img = '';
  desc = '';
  busy = false;
  canUpdate = false;

  private modalRef?: NgbModalRef;

  constructor(
    private route: ActivatedRoute,
    private readonly authSvc: AuthService,
    private readonly svc: PortfolioService,
    private modalService: NgbModal
  ) {}
  ngOnInit(): void {
    this.route.paramMap
      .pipe(
        tap((_) => (this.loading = true)),
        switchMap((params: ParamMap) => {
          this.id = params.get('id') ?? '';
          if (this.id) {
            return this.svc
              .getPortfolioDetails(this.id)
              .pipe(finalize(() => (this.loading = false)));
          } else {
            return of(null);
          }
        })
      )
      .subscribe((x) => {
        this.details = x;
        this.canUpdate = this.authSvc.user.username === x?.creator;
      });
  }
  open(content: any) {
    this.creator = this.details!.creator;
    this.identif = this.details!.identif;
    this.profileImg = this.details!.profileImg;
    this.img = this.details!.img;
    this.desc = this.details!.desc;

    this.modalRef = this.modalService.open(content, {
      size: 'lg',
      ariaLabelledBy: 'modal-title',
      backdrop: 'static',
    });
  }

  update(content: any) {
    this.busy = true;
    this.svc
      .updatePortfolioDetails(
        this.id,
        this.creator,
        this.identif,
        this.profileImg,
        this.img,
        this.desc,
      )
      .pipe(finalize(() => (this.busy = false)))
      .subscribe((x) => {
        this.details = x;
        this.modalRef?.close();
        this.open(content);
      });
  }
}
