import matplotlib.pyplot as plt
import numpy as np
import csv
import logging


class ChartGenerator(object):
    users_dict = {}
    label_loc = np.arange(0, 24 * 2, 2)
    bar_width = 0.55

    def __init__(self):
        logging.basicConfig(level=logging.INFO)

    def generate(self):
        self.read_data_from_file()

        total_number_of_users = len(self.users_dict.keys())
        fig, ax = plt.subplots(figsize=(5 * total_number_of_users, 5))

        # Creating the bars.
        bar_start = ((total_number_of_users / 2) * 0.55) * -1
        for user in self.users_dict:
            ax.bar(self.label_loc + bar_start, self.users_dict.get(user).values(), self.bar_width, label=user)
            bar_start += self.bar_width

        # Setting the axes
        ax.set_ylabel('Messages')
        ax.set_title('Messages by hour and user')
        ax.set_xticks(self.label_loc)
        ax.tick_params(labelsize=3 * total_number_of_users)
        ax.set_xticklabels(self.build_chart_dict().keys(), rotation=0)
        ax.yaxis.grid(True)
        ax.legend()

        # Show the plot
        plt.show()

    def read_data_from_file(self):
        with open('data_processed.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                time = row[1]
                name = row[2]
                if name not in self.users_dict:
                    self.users_dict.update({name: self.build_chart_dict()})
                self.users_dict[name][time] += 1

    def build_chart_dict(self):
        return {
            '12 AM': 0,
            '1 AM': 0,
            '2 AM': 0,
            '3 AM': 0,
            '4 AM': 0,
            '5 AM': 0,
            '6 AM': 0,
            '7 AM': 0,
            '8 AM': 0,
            '9 AM': 0,
            '10 AM': 0,
            '11 AM': 0,
            '12 PM': 0,
            '1 PM': 0,
            '2 PM': 0,
            '3 PM': 0,
            '4 PM': 0,
            '5 PM': 0,
            '6 PM': 0,
            '7 PM': 0,
            '8 PM': 0,
            '9 PM': 0,
            '10 PM': 0,
            '11 PM': 0,
        }