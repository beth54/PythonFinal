import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { PortfolioRoutingModule } from './portfolio-routing.module';
import { AllComponent } from './all/all.component';
import { DetailsComponent } from './details/details.component';
import { NgbModalModule } from '@ng-bootstrap/ng-bootstrap';
import { SpinnerModule } from '@uiowa/spinner';
import { FormsModule } from '@angular/forms';

@NgModule({
  declarations: [AllComponent, DetailsComponent],
  imports: [
    CommonModule,
    PortfolioRoutingModule,
    FormsModule,
    NgbModalModule,
    SpinnerModule,
  ],
})
export class PortfolioModule {}
