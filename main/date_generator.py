import datetime
from dateutil.relativedelta import relativedelta


class DateGen:
    def __init__(self):
        self.result = None
        self.step_date = None
        self.end_date = None
        self.start_date = None

    def generate_date(self, initial_year, ending_year, initial_month, ending_month):
        self.start_date = datetime.datetime(initial_year, initial_month, 1)
        self.end_date = datetime.datetime(ending_year, ending_month, 1)
        self.step_date = self.start_date + relativedelta(months=-1)

        result = []

        while self.step_date < self.end_date:
            result.append(self.step_date.strftime('%Y%m'))
            self.step_date = self.step_date + relativedelta(months=+1)

        set().union(*result)

        def concatenate_list_data(list_data):
            concat = ''
            for element in list_data:
                concat += str(element) + '|'
            return concat

        self.result = concatenate_list_data(result)

    def __str__(self):
        return str(self.result)


if __name__ == "__main__":
    object_date = DateGen()
    object_date.generate_date(2019, 2020, 10, 10)
    print(object_date)
