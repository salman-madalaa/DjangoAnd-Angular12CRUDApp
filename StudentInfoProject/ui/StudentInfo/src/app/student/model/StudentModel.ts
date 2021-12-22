import { Moment } from "moment";

export interface Student1{
   rollNo : number;
   name : string;
   dob : Moment;
   marks : number
   email : string;
   phoneNumber: number
   address : string
}

export class Student{
  rollNo!: number;
  name! : string;
  dob! : Moment;
  marks! : number
  email! : string;
  phoneNumber!: number
  address! : string
}

