from htmlCalendar import generate_month, create_calendar_html, create_html
from datetime import datetime

now = datetime.now()

month_length = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}
if ((now.year-2016)%4 == 0):
    month_length[2] = 29

# Events can be specified in form of Dictionary --> {Day of Month: (type of event, title of event, url of event if applicable)}
January_events = {
    12: ('exec', 'Executive Committee Meeting', '#')
}

February_events = {
}

March_events = {
    10: ('exec', 'Executive Committee Meeting', '#')
}

April_events = {
    14: ('exec', 'Executive Committee Meeting', '#'),
}

May_events = {
    12: ('exec', 'Executive Committee Meeting', '#')
}

June_events = {

}

July_events = {
}

August_events = {
}

September_events = {
}

October_events = {
}

November_events = {
}

December_events = {
}

month_events = {
    1: January_events,
    2: February_events,
    3: March_events,
    4: April_events,
    5: May_events,
    6: June_events,
    7: July_events,
    8: August_events,
    9: September_events,
    10: October_events,
    11: November_events,
    12: December_events
}

# Layout= (4,3)
calendar_body = ''
month = 1
for i in range(0, 4):
    calendar_body += '<div class="row"> <!-- Start of row number ' + str(i+1) + ' -->' + '\n'
    for j in range(0,3):
        calendar_body += '<div class="col-sm-4 col-md-4 col-lg-4"> <!--Start of month-->' + '\n'
        calendar_body += generate_month(month, month_length[month], month_events[month]) + '\n'
        calendar_body += '</div> <!--End of month-->' + '\n'
        month += 1
    calendar_body += '</div> <!--End of row number ' + str(i+1) + ' -->' + '\n'

create_html('2016_Calendar', create_calendar_html('2016', '', '', calendar_body))
