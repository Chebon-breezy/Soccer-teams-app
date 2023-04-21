import csv
import sys


class SoccerAnalyzer:
    def __init__(self, filename):
        self.filename = filename

    def group_play_summary(self):
        with open(self.filename, 'r') as f:
            wc_stats_reader = csv.reader(f)
            for line in wc_stats_reader:
                print(f'{line[0]} {line[1]}-{line[2]} {line[3]} ({line[4]}) {line[5]}-{line[6]} {line[7]}')

    def command2(self):
        with open(self.filename, 'r') as f:
            header = []
            wc_stats_reader = csv.reader(f)
            for row in wc_stats_reader:
                if not header:
                    header = row
                    continue
                maximum_value = float(row[header.index("GoalsScored")])
                country = [row[header.index("Team")]]
                for i in range(1, 4):
                    column = header.index(f"GoalsConceded{i}")
                    if float(row[column]) > maximum_value:
                        maximum_value = float(row[column])
                        country = [row[header.index(f"Opponent{i}")]]
                    elif float(row[column]) == maximum_value:
                        country.append(row[header.index(f"Opponent{i}")])
                print(f'Team(s) with highest number of goals conceded in a game ({int(maximum_value)}):')
                for q in sorted(country):
                    print("  ", q)

    def command3(self):
        with open(self.filename, 'r') as f:
            wc_stats_reader = csv.reader(f)
            header = next(wc_stats_reader)
            data = list(wc_stats_reader)

        stat = input('Enter statistics name to report:\n')
        while stat not in header:
            stat = input('Enter statistics name to report:\n')
        column = header.index(stat)

        minimum_value = float(data[0][column])
        country = [data[0][4]]
        for row in data[1:]:
            if float(row[column]) < minimum_value:
                minimum_value = float(row[column])
                country = [row[4]]
            elif float(row[column]) == minimum_value:
                country.append(row[4])

        print(f'Team(s) with lowest number of {stat} ({int(minimum_value)}):')
        for q in sorted(country):
            print("  ", q)

    def command4(self):
        with open(self.filename, 'r') as f:
            wc_stats_reader = csv.reader(f)
            header = next(wc_stats_reader)
            data = list(wc_stats_reader)

        stat = input('Enter statistics name to report:\n')
        while stat not in header:
            stat = input('Enter statistics name to report:\n')
        column = header.index(stat)

        total = 0
        count = 0
        for row in data:
            if row[column]:
                total += float(row[column])
                count += 1
        if count > 0:
            average = total / count
            print(f"Team(s) with {stat} greater than average ({average}):")
            above_average = []
            for row in data:

                if row[column] and float(row[column]) > average:
                    above_average.append(row[4])
                for q in sorted(above_average):
                    print("  ", q)
            else:
                print('No data available for this statistic')

            def command5(self):
                with open(self.filename, 'r') as f:
                    wc_stats_reader = csv.reader(f)
                    header = next(wc_stats_reader)
                    data = list(wc_stats_reader)

                team = input('Enter team name:\n')
                while team not in [row[4] for row in data]:
                    team = input('Enter team name:\n')
                print(f'Statistics for {team}:')
                for i in range(len(header)):
                    if i == 4:
                        continue
                    print(f'  {header[i]}: {data[[row[4] for row in data].index(team)][i]}')

    def run(self):
                while True:
                    command = input('Enter command: ')
                    if command == 'group_play_summary':
                        self.group_play_summary()
                    elif command == 'command2':
                        self.command2()
                    elif command == 'command3':
                        self.command3()
                    elif command == 'command4':
                        self.command4()
                    elif command == 'command5':
                        self.command5()
                    elif command == 'exit':
                        sys.exit()
                    else:
                        print('Invalid command, please try again')


if __name__ == '__main__':
    filename = input('Enter filename: ')
    analyzer = SoccerAnalyzer(filename)
    analyzer.run()
