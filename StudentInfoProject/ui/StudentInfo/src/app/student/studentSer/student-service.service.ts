import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class StudentServiceService {

  BaseUrl = 'http://127.0.0.1:8000/';

  constructor(private http:HttpClient) { }

  getAllStudents():Observable<any> {
    return this.http.get(this.BaseUrl+'testApp/allStudents');
  }

  newStudent(ob:any){
    let body=JSON.stringify(ob);
    let options = { headers: new HttpHeaders().set('Content-Type', 'application/json') };
    return this.http.post(this.BaseUrl+'testApp/newStudent',body,options)
  }

  deleteStu(id: number){
    return this.http.delete(this.BaseUrl+'testApp/deleteStudent/'+id);
  }

  getStudent(id: number):Observable<any>{
    return this.http.get(this.BaseUrl + 'testApp/getStudent/'+id);
  }

  updateStudent(id:number,ob:any){
    let body=JSON.stringify(ob);
    let options = { headers: new HttpHeaders().set('Content-Type', 'application/json') };
    return this.http.put(this.BaseUrl+'testApp/updateStudent/'+ id,body,options);
  }

}
