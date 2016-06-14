from string import Template
from datetime import datetime


def create_html(file_name, file_content):
    file_path = 'Generated Calendars/' + file_name + '.html'
    with open (file_path, 'w') as html_file:
        print(file_content, file=html_file)


def create_calendar_html(the_title, the_events_col1, the_events_col2, the_calendar):
    with open('Templates/calendar_skeleton.html') as calendar_template:
        calendar_text = calendar_template.read()
    the_calendar_text = Template(calendar_text)
    the_calendar_text = the_calendar_text.substitute(title=the_title,
                                           events_col1 = the_events_col1,
                                           events_col2 = the_events_col2,
                                           calendar = the_calendar
                                           )
    return the_calendar_text


def insert_event(day, event_type, event_title, link):
    event_class = {'exec': 'executive-meeting',
                   'comm': 'community-event'}
    event_text = ''
    event_text += '<td class="' + event_class[event_type] + '" align="center" height="25">'

    if (link == '#'):
        event_text += str(day) + '</td>' + '\n'
    else:
        event_text += '<a href="' + link + '" title="' + event_title + '">' + str(day)
        event_text += '</a></td>' + '\n'

    return event_text


def generate_month(month_number, month_length, month_events):

    now = datetime.now()
    this_year = str(now.year)
    start_day = datetime(now.year, month_number, 1).weekday()

    month_names = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June',
                   7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}

    day_titles = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

    month_text = ''
    month_text += '<table class="table-condensed"><tbody><tr>' + '\n'
    month_text += '<td class="month-title" colspan="7" align="center">' + month_names[month_number] + '   ' + this_year + '</td></tr>' + '\n'
    month_text += '<tr>' + '\n'

    for day_title in day_titles:
        month_text += '<td class="day-title" align="center" width="30" height="25">' + day_title + '</td>' + '\n'

    month_text += '</tr><tr>' + '\n'

    for i in range(0, start_day+1):
        month_text += '<td class="day" align="center" height="25"></td>' + '\n'

    day = 1

    # events = {15: ('exec', 'Executive Committee Meeting', 'www..com')}

    for i in range(start_day+1, 7):

        if (day in month_events.keys()):
            month_text += insert_event(day, month_events[day][0], month_events[day][1], month_events[day][2])
        else:
            month_text += '<td class="day" align="center" height="25">' + str(day) + '</td>' +'\n'

        day += 1
    month_text += '</tr>'

    number_of_rows = 1
    while (number_of_rows < 6):

        month_text += '<tr>'
        number_of_rows += 1

        for i in range(0, 7):

            if (day <= month_length):
                if (day in month_events.keys()):
                    month_text += insert_event(day, month_events[day][0], month_events[day][1], month_events[day][2])
                else:
                    month_text += '<td class="day" align="center" height="25">' + str(day) + '</td>' + '\n'
                day += 1
            else:
                month_text += '<td class="day" height="25"></td>' + '\n'

        month_text += '</tr>' + '\n'

    month_text += '</tbody></table>' + '\n'

    return month_text
