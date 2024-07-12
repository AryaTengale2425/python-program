import pandas as pd

def generate_report():
    data=pd.read_csv ('project1.csv')
    if data.empty:
        print("no employee data found")
        return
    report=data.groupby('designation').agg({ 'name':'count'}).reset_index()
    report.coloumn = ['city','salary','present_days']
    print("report:")
    print(report.to_string(index=False))

if __name__ == "__main__":
    generate_report()