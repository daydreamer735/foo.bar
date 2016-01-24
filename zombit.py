def answer(meetings):
    schedule = []
    sortmeetings = sorted(meetings, key = lambda meetings: meetings[1])
    for meeting in sortmeetings:
        indicator = True
        for element in schedule:
            if meeting[1] > element[0]:
                if meeting[0] < element[1]:
                    indicator = False
            elif meeting[0] < elemtn[1]:
                if meeting[1] > elemtn[0]:
                    indicator = False
        if indicator:
            schedule.append(meeting)
    return len(schedule)
