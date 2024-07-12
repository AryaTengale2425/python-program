import csv
CSV_FILE='project1.csv'

def read_csv():
    with open(CSV_FILE,mode='r',newline='')as file:
        reader=csv.DictReader(file)
        return list(reader)

def write_csv(data):
    with open(CSV_FILE,mode='w',newline='')as file:
        writer =csv.DictWriter(file,fieldnames=['id','name','salary','city','designation','present_days'])
        writer.writeheader()
        writer.writerows(data)


def create_employee(id,name,salary,city,designation,present_days):
    data=read_csv()
    new_employees={'id': id,'name': name,'salary': salary,'city': city,'designation': designation,'present_days':present_days }
    data.append(new_employees)
    write_csv(data)


def delete_employee(id):
   data=read_csv()
   data=[employee for employee in data if employee['id'] != id]
   write_csv(data)   

def read_employee():
     employees=read_csv()
     if not employees:
         return
     headers=['id','name','salary','city','designation','present_days']
     col_widths={header: len(header) for header in headers}

     for employee in employees:
        for header in headers:
            col_widths[header]=max(col_widths[header],len(employee[header.lower().replace(' ','_')]))
        
# create a horizontal separator
     separator = '+-' + '-+-' .join(['-' * col_widths[header] for header in headers]) + '+-'

# create a header row
     header_row = '| ' + ' | ' .join([header.ljust(col_widths[header]) for header in headers]) + ' |'

     print(separator)
     print(header_row)
     print(separator)

# print each employee record
     for employee in employees:
         row = '| ' + ' | ' .join([employee[header.lower().replace(' ','_')].ljust(col_widths[header]) for header in headers]) + ' |' 
         print(row)
     print(separator)

def update_employee(id,name,salary,city,designation,present_days):
    data=read_csv()
    for emp in data: 
     if emp['id']==id:
      if name:
       emp['name']=name
       if salary:
        
        emp['salary']=salary
       if city:
        emp['city']=city
       if designation:
        emp['designation']=designation
       if present_days:
          emp['present_days']=present_days 
      break
    write_csv(data)   

def delete_employee(id):
   data=read_csv()
   data=[employee for employee in data if employee['id'] != id]
   write_csv(data)