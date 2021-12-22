import { AfterViewInit, Component, OnInit } from '@angular/core';
import { StudentServiceService } from '../studentSer/student-service.service';
import {MatPaginator} from '@angular/material/paginator';
import {MatSort} from '@angular/material/sort';
import { ViewChild } from '@angular/core';
import { Student, Student1 } from '../model/StudentModel';
import { MatTableDataSource } from '@angular/material/table';
import { Router } from '@angular/router';

@Component({
  selector: 'app-all-students',
  templateUrl: './all-students.component.html',
  styleUrls: ['./all-students.component.css']
})
export class AllStudentsComponent implements OnInit,AfterViewInit  {
  resultsLength = 0;
  ELEMENT_DATA : any;
  displayedColumns: string[] = ['id','rollNo', 'name','dob', 'marks','email','phoneNumber','address','actions'];

  dataSource = new MatTableDataSource<Student>();

  @ViewChild(MatPaginator) paginator: MatPaginator;
  @ViewChild(MatSort) sort : MatSort ;

  constructor(private _stuService: StudentServiceService,private _router:Router) { }

  ngOnInit(): void {
    this.getAllStudents();
  }

  ngAfterViewInit() {
    //  this.dataSource.paginator = this.paginator;
    //  this.dataSource.sort = this.sort;
  }

  getAllStudents(){
    this._stuService.getAllStudents().subscribe(data => {
      this.dataSource = new MatTableDataSource(data);
      this.dataSource.paginator = this.paginator;
      this.resultsLength = data.length;
      console.log(data);
    },(error)=>{
      console.log(error.error);
    });
  }

  edit(id:any){
    this._router.navigateByUrl('editStudent/'+id);
    // alert(id);
  }

  delete(id:number){
    if(confirm('Are you sure delete ??')){
    this._stuService.deleteStu(id).subscribe(data => {
      console.log(data);
      this.getAllStudents();
    })
  }
  }

}
