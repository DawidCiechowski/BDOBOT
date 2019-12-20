import json
from datetime import date, datetime

from time_converter import TimeConverter


class BotFunctions():

    # Variables
    tc = TimeConverter()
    after_10_15 = tc.compare_times(hour1=datetime.now(
    ).hour, hour2=22, minute1=datetime.now().minute, minute2=15)

    bossy_bdo = None
    days_of_the_week = ["Monday", "Tuesday",
                        "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    today = datetime.today().weekday()

    # Read json file upon init
    def __init__(self):
        with open("bosses.json", "r") as bossy:
            self.bossy_bdo = json.load(bossy)

    # Return next boss
    def next_boss(self):

        if(self.after_10_15 == False):
            return self.todays_next_boss()
        else:
            return self.first_boss_tomorrow()

    # If it's before 10.15pm return this
    def todays_next_boss(self):
        time_of_next_boss = ""
        next_boss = ""
        todays_day = self.days_of_the_week[int(datetime.now().weekday())]
        todays_bosses = self.bossy_bdo["bosses"]["days"][todays_day]

        for i in range(len(todays_bosses)):
            time = todays_bosses[i][1].split(":")
            if(self.tc.compare_times(hour1=time[0], hour2=datetime.now().hour, minute1=int(time[1]) + 10, minute2=datetime.now().minute)):
                time_of_next_boss = time
                next_boss = todays_bosses[i][0]
                break

        return f"\n**Nastepny boss:**\n\n{next_boss} - {time[0]}:{time[1]}"

    # If it's after 10.15pm return this
    def first_boss_tomorrow(self):
        next = self.bossy_bdo["bosses"]["days"][self.days_of_the_week[datetime.now(
        ).weekday() + 1]][0][0]
        time = self.bossy_bdo["bosses"]["days"][self.days_of_the_week[datetime.now(
        ).weekday() + 1]][0][1]

        return f"**Nastepny boss:**\n\n{next} - {time}"

    # Return all the bosses for today
    def all_todays_bosses(self):
        next_boss_index = self.todays_next_index()
        bosses = "\n**Dzisiejsze bossy:** \n\n"
        todays_day = self.days_of_the_week[int(datetime.now().weekday())]
        todays_bosses = self.bossy_bdo["bosses"]["days"][todays_day]
        for i in range((len(todays_bosses))):
            if(i == next_boss_index):
                bosses += f"**{todays_bosses[i][0]}: {todays_bosses[i][1]} - nastepny/obecny boss\n**"
            else:
                bosses += f"{todays_bosses[i][0]}: {todays_bosses[i][1]}\n"

        return bosses

    # Return index of the next boss until (t+10)

    def todays_next_index(self):
        index = None

        if(not self.after_10_15):
            todays_day = self.days_of_the_week[int(datetime.now().weekday())]
            todays_bosses = self.bossy_bdo["bosses"]["days"][todays_day]

            for i in range(len(todays_bosses)):
                time = todays_bosses[i][1].split(":")
                if(self.tc.compare_times(hour1=time[0], hour2=datetime.now().hour, minute1=int(time[1]) + 10, minute2=datetime.now().minute)):
                    index = i
                    break

        return index

    def all_tomorrows_bosses(self):
        next_boss_index = self.todays_next_index()
        bosses = "\n**Jutrzejsze bossy:** \n\n"
        if(datetime.now().weekday() == 6):
            tomorrow = self.days_of_the_week[0]
        else:
            tomorrow = self.days_of_the_week[int(
                datetime.now().weekday()) + 1]

        tomorrows_bosses = self.bossy_bdo["bosses"]["days"][tomorrow]
        for i in range((len(tomorrows_bosses))):
                bosses += f"{tomorrows_bosses[i][0]}: {tomorrows_bosses[i][1]}\n"

        return bosses
