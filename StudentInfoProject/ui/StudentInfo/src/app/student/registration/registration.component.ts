import { Component, OnInit } from '@angular/core';
import { DateAdapter } from '@angular/material/core';
import { ActivatedRoute } from '@angular/router';
import { Student } from '../model/StudentModel';
import { StudentServiceService } from '../studentSer/student-service.service';

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css']
})
export class RegistrationComponent implements OnInit {

  isEdit:number;
  constructor(private _stuService : StudentServiceService,private route: ActivatedRoute) {

   }

  student = new Student();

  ngOnInit(): void {
   this.isEdit = this.route.snapshot.params.id;
   this.getStudent(this.isEdit);
  }

  register(ob:any){
    this._stuService.newStudent(ob).subscribe((data)=>{
      console.log("data sended properly");
      console.log(data);
    })
  }

  getStudent(isEdit:number){
    this._stuService.getStudent(isEdit).subscribe((data)=>{
      console.log(data);
      this.student.rollNo = data.rollNo;
      this.student.name = data.name;
      this.student.dob = data.dob;
      this.student.marks = data.marks;
      this.student.email = data.email;
      this.student.phoneNumber = data.phoneNumber;
      this.student.address = data.address;
    });
  }

  update(ob:any){
    this._stuService.updateStudent(this.isEdit,ob).subscribe((data)=>{
      console.log(data);
      console.log("Student Updated Successfully");
    });
  }

}
