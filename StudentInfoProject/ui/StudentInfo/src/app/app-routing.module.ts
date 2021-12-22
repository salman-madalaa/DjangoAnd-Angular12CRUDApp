import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AllStudentsComponent } from './student/all-students/all-students.component';
import { RegistrationComponent } from './student/registration/registration.component';

const routes: Routes = [
  {path: '', redirectTo: 'allStudents', pathMatch: 'full'},
  {path:'allStudents',component:AllStudentsComponent},
  {path:'newStudent',component:RegistrationComponent},
  {path:'editStudent/:id',component:RegistrationComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
