
create database dbtest;

use dbtest;
 
create table EmployeeInfo (EmpID int, EmpFname varchar(20), EmpLname varchar(20), Department varchar(10), project varchar(10), Address varchar(30), DOB date, Gender char(1) );
 desc EmployeeInfo;
 
 insert into EmployeeInfo values
 (1, "Sanjay", "Mehra", "HR", "P1","Hyderabad(HYD)","1976-12-01","M"), 
 (2, "Ananya","Mishra", "Admin","P2", "Delhi(DEL)","1968-05-02","F"),
 (3,"Rohan", "Diwan","Account","P3", "Mumbai(BOM)","1980-01-01","M"),
 (4,"Sonia","Kulkarni","HR","P1","Hyderabad(HYD)","1992-05-02","F"),
 (5,"Ankit","Kapoor","Admin","P2","Delhi(DEL)","1994-07-03","M");
 
 select * from  EmployeeInfo;
 
 create table EmployeePosition( EmpID int, EmpPosition varchar(20), DateOfJoining date, Salary double);
 
 desc EmployeePosition;
 
 insert into EmployeePosition values
 (1, "Manager", "2022-05-01",500000),
 (2,"Executive","2022-05-02",75000),
 (3,"Manager","2022-05-01",90000),
 (2,"Lead","2022-05-02",85000),
 (1,"Executive","2022-05-01",300000);
 
 select * from  EmployeePosition;
  

-- 1) write a query to fetch the empfname from the employeeinfo table in upper case and use the alias name as empname;

select EmpFname, upper(EmpFname) as EmpName from EmployeeInfo;

-- 2) write a query to fetch the no of employees working in dept HR;


select count(*) from employeeinfo where department in("HR");

--  3) write a querry  to get current date ?
select curdate();
select curdate() as curr_date;

-- 4) write a querry to retrieve the first 4 characters of empname from the employeeinfo table ?
select substr(empname,1,4)from employeeinfo;



select emplname, substring(emplname,1,4) from employeeinfo;

-- 5) write a querry to create a new table which consists of data and structure copied from the other table?  (SUB QUERY QUESTION)
create table Office (select EmpID , EmpPosition , DateOfJoining , Salary from employeeposition);
select * from office;
select * from Office; 
-- 6) write a query to find all the employees whose salary is between 50000 to 100000?

select * from employeeposition where salary between 50000 and 100000;

-- 7) write a query to find the names of employees that begin with "S"?
select * from  employeeinfo  where empfname like "S%";

-- 8) write a query to fetch top 4 records from the employeeinfo table?
select * from employeeinfo limit 0,4;

-- 9) write a query to retrieve the empfname and emplanme in a single column as FullName the fname and lname must be seperated with space?
select concat(empfname, " ",emplname) as FullName from employeeinfo ;

-- 10) write a query find no of employees whose dob is between 02/05/1970 to 31/12/1975 and are grouped according to gender?
select count(*) from employeeinfo where DOB between "1970-05-02" and "1975-12-31" order by Gender;    -------------------

-- 11) write a query to fetch all the records from the employeeinfo table order by emplname in descending order aned department in the ascending oreder?
select * from employeeinfo order by emplname desc, department ;

-- 12) write a query to fetch details of employees lname ends with an alplabet A and contains 5 alplabets?
select * from employeeinfo where emplname like "____A";

-- 13) write a query to fetch details of all employees excluding the employees with fname "Sanjay" and "Sonia" from employeeinfo table?
select * from employeeinfo where empfname not in ("Sanjay","Sonia");

-- 14) write a querry  to fetch details of employees with the address as delhi(del)?
select * from employeeinfo where address in ("DELHI(DEL)");
select * from employeeinfo where address ="DELHI(DEL)";

-- 15) write a querry to fetch all employees who also hold the manageral position?
select * from employeeinfo e inner join employeeposition p on e.empid = p.empid;
select * from employeeinfo inner join employeeposition on employeeinfo.empid = employeeposition.empid where empposition = "Manager";
select * from employeeposition where empposition = "Manager";

-- 16) write a query to fetch the department wise count of employees sortedd by department count in ascending order ?
select count(*) from employeeinfo order by department ;
select department ,count(*)  from employeeinfo group by department order by department;

-- 17) write a query to retrieve two minimum and maximum salaries from the empposition table?-------------------
select * from employeeposition order by salary desc limit 0,2;
select * from employeeposition order by salary limit 0,2;

-- 18) write a query to retrieve 5th highest salary from the table?
select * from employeeposition order by salary desc limit 4,1;

-- 19) write a query to retrieve the list of employees working in same department?-------------------------
select * from employeeinfo group by department;
select * from employeeinfo order  by department;
select distinct department from employeeinfo group by department;

-- 20) write a query to retrieve the duplicate records from the table?-------------

-- 21) write a query to find the 3rd highest salary from the empposition table?
select * from employeeposition order by salary desc limit 2,1;

-- 22) write a query to display first and the last record from the empinfo table?--------------------------
select * from employeeinfo order by empid limit 1;
select * from employeeinfo order by empid desc limit 1;
select * from employeeinfo where empid = (select min(empid) from employeeinfo);
select * from employeeinfo where empid = (select max(empid) from employeeinfo);

-- 23) write a query to retrieve departments who have less than 2 employees working in it?

select department , count(*) from employeeinfo group by department having count(*)<2;

-- 24) write a query to retrieve empposition along with total salaries paid for each of them?


-- 25) write a query to fetch 50% records from the empinfo table?








