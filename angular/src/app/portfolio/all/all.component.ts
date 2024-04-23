import { Component, OnInit } from '@angular/core';
import { Portfolio } from '../models/portfolio';
import { PortfolioService } from '../services/portfolio.service';
import { NgbModalRef, NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { AuthService } from '../../core';
import { finalize } from 'rxjs';

@Component({
  selector: 'app-all',
  templateUrl: './all.component.html',
  styleUrl: './all.component.css',
})
export class AllComponent implements OnInit {
  portfolio: Portfolio[] = [];
  creator = '';
  identif = '';
  profileImg = '';
  img = '';
  desc = '';
  busy = false;
  username = '';

  private modalRef?: NgbModalRef;
  constructor(
    authSvc: AuthService,
    private readonly svc: PortfolioService,
    private modalService: NgbModal
  ) {
    this.username = authSvc.user.username;
  }

  ngOnInit(): void {
    this.svc.getAllPortfolio().subscribe((x) => (this.portfolio = x));
  }

  open(content: any) {
    this.modalRef = this.modalService.open(content, {
      size: 'lg',
      ariaLabelledBy: 'modal-title',
      backdrop: 'static',
    });
  }


  create(content: any) {
    this.busy = true;
    this.svc
      .createPortfolio(
        this.creator,
        this.identif,
        this.profileImg,
        this.img,
        this.desc,

      )
      .pipe(finalize(() => (this.busy = false)))
      .subscribe((_) => {
        this.ngOnInit();
        this.modalRef?.close();
        this.open(content);
      });
  }

  delete(id: string) {
    this.svc.deleteEvent(id).subscribe((_) => {
      this.ngOnInit();
      this.modalRef?.close();
    });
  }
}
