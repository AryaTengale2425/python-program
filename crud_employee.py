import csv
CSV_FILE='data/employees.csv'

def read_csv():
    with open(CSV_FILE,mode='r',newline='')as file:
        reader=csv.DictReader(file)
        return list(reader)

def write_csv(data):
    with open(CSV_FILE,mode='w',newline='')as file:
        writer =csv.DictWriter(file,fieldnames=['ID','Name','Salary','City','Mob_no','Email_Id','P_date','A_date'])
        writer.writeheader()
        writer.writerows(data)

def create_employees(Id,Name,Salary,City,Mob_no,Email_Id,P_date,A_date):
    data=read_csv()
    new_employees={'Id': Id,'Name': Name,'Salary': Salary,'City': City,'Mob_no': Mob_no,'Email_Id': Email_Id,'P_date': P_date,'A_date': A_date}
    data.append(new_employees)
    write_csv(data)

def read_employee():
    employees=read_csv()
    if not employees:
        print("no employee data found")
        return

# determine the maximum width for each column
headers=['ID','Name','Salary','City','Mob_no','Email_Id','P_date','A_date']
col_widths={header: len(header) for header in headers}

for employee in create_employees:
    for header in headers:
        col_widths[header]=max(col_widths[header],
len(employee[header.lower().replace('','_')]))
        
# create a horizontal separator
separator='+-'+'-+-'.join(['-'*col_widths[header]for header in headers]) +'+-'

# create a header row
header_row='| ' + ' | '.join[header.lgust(col_widths[header]for header in headers) + ' |']

print(separator)
print(header_row)
print(separator)

# print each employee record
for employee in employee:
    row ='| ' + ' | '.join([employee[header.lower().replace('','_')].ljust(col_widths[header]) for headers in headers]) + ' |' 
    print(row)

print(separator)

def update_emp(Id,Name,salary,city,Mob_no,Email_Id,P_date,A_date):
    data=read_csv()
    for emp in data: 
     if emp['Id']==Id:
      if Name:
       emp['Name']=Name
       if salary:
        emp['salary']=salary
       if city:
        emp['city']=city
       if Mob_no:
        emp['mob_no']=Mob_no
       if Email_Id:
        emp['Email_Id']=Email_Id
       if P_date:
        emp['P_date']=P_date
       if A_date:
        emp['A_date']=A_date
      break
    write_csv(data)         

def delete_emp(Id):
 data=read_csv()
 data=[employee for employee in data if employee['Id'] != Id]
 write_csv(data)                    
           
          

