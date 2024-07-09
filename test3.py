import datetime

unix_time = 1720507943
date_time = datetime.datetime.fromtimestamp(unix_time)

formatted_date_time = date_time.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date_time)