from datetime import date
import calendar
import pandas as pd

holidays_since_2013 = pd.DataFrame(data = {
    'month': [1]*8 + [2, 3, 5, 5, 6, 11],
    'day': list(range(1, 9)) + [23, 8, 1, 9, 12, 4]
    })

holidays_till_2013 = pd.DataFrame(data = {
    'month': [1]*6 + [2, 3, 5, 5, 6, 11],
    'day': list(range(1, 6)) + [7] + [23, 8, 1, 9, 12, 4]
    })

holidays = []

for year in years:
    days_and_months = holidays_till_2013 if (year <= 2012) else holidays_since_2013
    dates = []
    for index, row in days_and_months.iterrows():
        dates.append(date(year, row['month'], row['day']))
    holidays = holidays + dates

moved_weekends = \
    [date(2012, 1, 6),  date(2012, 1, 9),  date(2012, 3, 9)] + \
    [date(2012, 4, 30), date(2012, 5, 7),  date(2012, 5, 8)] + \
    [date(2012, 6, 11), date(2012, 11, 5), date(2012, 12, 31)] + \
    [date(2013, 2, 23), date(2013, 3, 8)] + \
    [date(2013, 5, 2),  date(2013, 5, 3), date(2013, 5, 10)] + \
    [date(2014, 3, 10)] + \
    [date(2014, 5, 2)] + \
    [date(2014, 6, 13), date(2014, 11, 3)] + \
    [date(2015, 1, 9), date(2015, 3, 9)] + \
    [date(2015, 5, 4), date(2015, 5, 11)] + \
    [date(2016, 2, 22), date(2016, 3, 7)] + \
    [date(2016, 5, 2),  date(2016, 5, 3)] + \
    [date(2016, 6, 13)] + \
    [date(2017, 2, 24)] + \
    [date(2017, 5, 8)] + \
    [date(2017, 11, 6)] + \
    [date(2018, 3, 9), date(2018, 4, 30), date(2018, 5, 2)] + \
    [date(2018, 6, 11), date(2018, 11, 5), date(2018, 12, 31)] + \
    [date(2019, 5, 2),  date(2019, 5, 3),  date(2019, 5, 10)] + \
    [date(2020, 2, 24), date(2020, 3, 9)] + \
    [date(2020, 5, 4),  date(2020, 5, 5),  date(2020, 5, 11)] + \
    [date(2021, 2, 22)] + \
    [date(2021, 5, 3),  date(2021, 5, 10)] + \
    [date(2021, 6, 14), date(2021, 11, 5), date(2021, 12, 31)] + \
    [date(2022, 3, 7)] + \
    [date(2022, 5, 2),  date(2022, 5, 3),  date(2022, 5, 10)] + \
    [date(2022, 6, 13)] + \
    [date(2023, 2, 24)] + \
    [date(2023, 5, 8)] + \
    [date(2023, 11, 6)]

working_weekends = \
    [date(2012, 3, 11), date(2012, 4, 28), date(2012, 5, 5)] + \
    [date(2012, 5, 12), date(2012, 6, 9),  date(2012, 12, 29)] + \
    [date(2016, 2, 20)] + \
    [date(2018, 4, 28), date(2018, 6, 9),  date(2018, 12, 29)] + \
    [date(2021, 2, 20)] + \
    [date(2022, 3, 5)]

short_workdays = \
    [date(2012, 2, 22), date(2012, 3, 7),  date(2012, 4, 28)] + \
    [date(2012, 5, 12), date(2012, 6, 9),  date(2012, 12, 29)] + \
    [date(2013, 2, 22), date(2013, 3, 7),  date(2013, 4, 30)] + \
    [date(2013, 5, 8),  date(2013, 6, 11), date(2013, 12, 31)] + \
    [date(2014, 2, 24), date(2014, 3, 7),  date(2014, 4, 30)] + \
    [date(2014, 5, 8),  date(2014, 6, 11), date(2014, 12, 31)] + \
    [date(2015, 4, 30), date(2015, 5, 8),  date(2015, 6, 11)] + \
    [date(2015, 11, 3), date(2015, 12, 31)] + \
    [date(2016, 2, 20), date(2016, 11, 3)] + \
    [date(2017, 2, 22), date(2017, 3, 7),  date(2017, 11, 3)] + \
    [date(2018, 2, 22), date(2018, 3, 7),  date(2018, 4, 28)] + \
    [date(2018, 5, 8),  date(2018, 6, 9),  date(2018, 12, 29)] + \
    [date(2019, 2, 22), date(2019, 3, 7),  date(2019, 4, 30)] + \
    [date(2019, 5, 8),  date(2019, 6, 11), date(2019, 12, 31)] + \
    [date(2020, 4, 30), date(2020, 5, 8), date(2020, 6, 11)] + \
    [date(2020, 11, 3), date(2020, 12, 31)] + \
    [date(2021, 2, 20), date(2021, 4, 30)] + \
    [date(2021, 6, 11), date(2021, 11, 3)] + \
    [date(2022, 2, 22), date(2022, 3, 5),  date(2022, 11, 3)] + \
    [date(2023, 2, 22), date(2023, 3, 7),  date(2023, 11, 3)]

def get_weekdays(year):
    weekends = [] # Saturdays and Sundays
    workdays = [] # all other weekdays
    c = calendar.TextCalendar(calendar.MONDAY)
    for month in range(1, 13):
        for day in c.itermonthdays(year, month):
            #calendar constructs months with leading zeros (days belonging to the previous month)
            if day != 0:
                d = date(year, month, day)
                if d.weekday() == 5 or d.weekday() == 6: # if it is Saturday or Sunday
                    weekends.append(d)
                else:
                    workdays.append(d)
    return dict({'workdays': workdays, 'weekends': weekends})

work_days = set()
rest_days = set()

for year in years:
    all_days = get_weekdays(year)
    work_days = work_days.union(all_days['workdays'])
    rest_days = rest_days.union(all_days['weekends'])

holidays_set = set(holidays)
moved_weekends_set = set(moved_weekends)
working_weekends_set = set(working_weekends)

work_days = sorted(
    working_weekends_set.union(
        work_days.difference(holidays_set, moved_weekends_set)
    )
)

rest_days = sorted(
    holidays_set.union(
        moved_weekends_set,
        rest_days.difference(working_weekends_set)
    )
)

class WorkTable:
    def __init__(self, year):
        assert year >= 2012
        self.year = year
        self.work_days = sorted([x for x in work_days if x.year == year])
        self.rest_days = sorted([x for x in rest_days if x.year == year])
        self.short_workdays = sorted([x for x in short_workdays if x.year == year])
        self.working_weekends = sorted([x for x in working_weekends if x.year == year])
        self.moved_weekends = sorted([x for x in moved_weekends if x.year == year])

    def workhours_year(self, daily_hours):
        return len(self.work_days)*daily_hours - len(self.short_workdays)

    def workhours_month(self, daily_hours, month):
        return len([x for x in self.work_days if x.month == month])*daily_hours - \
            len([x for x in self.short_workdays if x.month == month])

    def is_leap(self):
        return calendar.isleap(self.year)

    def days_year(self):
        return 366 if self.is_leap() else 365

    def days_month(self, month):
        return calendar.monthrange(self.year, month)[1]

    def hours_month(self, month):
        return 24*self.days_month(month)
