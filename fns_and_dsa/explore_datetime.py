from datetime import datetime,timedelta
def display_current_datetime():
    current_date=datetime.now()
    format='%Y-%m-%d %H:%M:%S'
    print(f'Current date and time: {current_date.strftime(format)}')

def calculate_future_date(no_days):
    future_date=timedelta(days=no_days)+datetime.now()
    format='%Y-%m-%d'
    print(f'Future date: {future_date.strftime(format)}')
    
display_current_datetime()
no_days=int(input("Enter the number of days to add to the current date: "))
calculate_future_date(no_days)
