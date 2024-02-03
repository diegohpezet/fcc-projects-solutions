class Time:
    def __init__(self, hours, minutes, period = False):
        self.hours = int(hours)
        self.minutes = int(minutes)
        self.period = period

def build_time_from_string(time_string: str):
    ### Return time object from string
    if 'PM' in time_string or 'AM' in time_string:
        time = time_string.split(':')
        time.append(time[-1].split()[1])
        time[-2] = time[-2].split()[0]

        hours, minutes, period = time 
        time_object = Time(hours, minutes, period)
    else:
        time = time_string.split(':')
        hours, minutes = time 
        time_object = Time(hours, minutes)

    return time_object

def add_time(start, duration, current_day = ''):
    days = 0
    list_of_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    if current_day:
        current_day = current_day.capitalize()

    # Build time object from parameter timestrings
    start_time = build_time_from_string(start)
    duration_time = build_time_from_string(duration)

    # Get time
    if start_time.period == 'PM':
        total_hours = start_time.hours + 12 + duration_time.hours
    else:
        total_hours = start_time.hours + duration_time.hours

    total_minutes = start_time.minutes + duration_time.minutes

    if total_minutes >= 60:
        total_minutes -= 60
        total_hours += 1
        # Check if a day has already passed before adding time
        if (start_time.hours + 12) + 1 == 24 and start_time.period == 'PM':
            days += 1
            if current_day:
                current_day = list_of_days[list_of_days.index(current_day) + 1]

    # Get amount of days
    while total_hours > 24:
        days += 1
        total_hours -= 24
        if current_day: 
            if current_day == list_of_days[len(list_of_days) -1]:
                current_day = list_of_days[0]
            else:
                current_day = list_of_days[list_of_days.index(current_day) + 1]

    # Check for correct period and arrange time format
    if total_hours < 12:
        period = 'AM'
    elif total_hours == 24:
        period = 'AM'
        total_hours -= 12
    elif total_hours > 12:
        period = 'PM'
        total_hours -= 12
    else:  # total_hours == 12
        period = 'PM'

    if total_minutes < 10:
        total_minutes = f"0{total_minutes}"

    # Build days message if necessary
    days_message = ''
    if days > 0:
        days_message = "(next day)" if days == 1 else f"({days} days later)"
        if current_day:
            return f"{total_hours}:{total_minutes} {period}, {current_day} {days_message}"
        else:
            return f"{total_hours}:{total_minutes} {period} {days_message}"
    
    if current_day: 
        return f"{total_hours}:{total_minutes} {period}, {current_day}"
    
    return f"{total_hours}:{total_minutes} {period}"