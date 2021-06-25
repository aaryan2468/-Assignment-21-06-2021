time = float(input("Input time in seconds: "))
time = time % (24 * 3600)
hour = time // 3600
time %=3600
minutes = time //60

time %= 60
seconds = time

hour_int = int(hour)
hour_str = str(hour_int)
hour_zero = hour_str.zfill(2)

minutes_int = int(minutes)
minutes_str = str(minutes_int)
minutes_zero = minutes_str.zfill(2)

seconds_int = int(seconds)
seconds_str = str(seconds_int)
seconds_zero = seconds_str.zfill(2)


print(hour_zero,":",minutes_zero ,":",seconds_zero)
