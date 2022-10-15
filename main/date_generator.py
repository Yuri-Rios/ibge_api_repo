import datetime
from dateutil.relativedelta import relativedelta

start_date = datetime.datetime(2010, 12, 1)
end_date = datetime.datetime(2012, 12, 1)
step_date = start_date + relativedelta(months=-1)

result = []
a=2
while step_date < end_date:
    result.append(step_date.strftime('%Y%m'))
    step_date = step_date + relativedelta(months=+1)

print(result)
print(set().union(*result))


def concatenate_list_data(list_data):
    concat = ''
    for element in list_data:
        concat += str(element) +'|'
    return concat

print(concatenate_list_data(result))
