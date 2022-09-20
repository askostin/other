"""
Convert text file with dates in format DD.MM.YYYY are writen in lines
and separated by ',', and where each line relates to the selected month of the given year, to the format:
'@Month_name(RU)\n' + listof_dates(DD.MM.YY)
"""
import re

months = {
    1: 'Январь', 2: 'Февраль', 3: 'Март',
    4: 'Апрель', 5: 'Май', 6: 'Июнь',
    7: 'Июль', 8: 'Август', 9: 'Сентябрь',
    10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'
}

with open('./dates.txt', 'r', encoding='utf8') as file_in, open('./dates2.txt', 'a', encoding='utf8') as file_out:
    for monthly_note in file_in:
        first_date = re.search(r'\d{0,1}\d\.(\d\d)\.(\d\d\d\d)', monthly_note)
        file_out.write(f"{months[int(first_date.group(1))]} {first_date.group(2)}:\n")
        file_out.write(re.sub(r'20(\d\d)', r'\1', monthly_note))