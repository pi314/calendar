from __future__ import print_function
#from pprint import pprint as p

number = [2, 1, 9, 2, 1, 8, 7, 6, 9, 3, 0, 12, 3, 3, 11, 10, 10, 11, 11, 11, 11, 2, 1, 10, 2, 2, 8, 6, 6, 8, 3, 2, 8, 3, 3, 9, 7, 7, 7, 7, 6, 9, 2, 1, 9, 2, 2, 8, 7, 7, 9, 2, 2, 10, 3, 4, 11, 8, 8, 8, 8, 8, 10, 2, 1, 8, 1, 1, 7, 6, 6, 6, 2, 1, 8, 4, 5, 10, 7, 7, 8, 8, 8, 10, 2, 1, 9, 1, 1, 7, 7, 7, 8, 2, 1, 10, 3, 4, 10, 9, 9, 9, 9, 9, 11, 2, 1, 9, 1, 1, 7, 7, 7, 9, 2, 1, 10, 4, 6, 9, 9, 9, 9, 9, 9, 11, 2, 1, 9, 1, 1, 7, 7, 7, 9, 2, 1, 10, 3, 4, 12, 10, 10, 10, 10, 10, 12, 2, 1, 9, 1, 1, 7, 7, 7, 9, 2, 1, 10, 3, 5, 8, 6, 6, 6, 6, 6, 8, 2, 1, 9, 1, 1, 7, 7, 7, 9, 2, 1, 11, 3, 6, 10, 8, 8, 9, 9, 9, 11, 2, 1, 9, 1, 1, 7, 7, 7, 9, 2, 1, 10, 4, 6, 9, 9, 9, 9];

dates = [
    'Mon 24', 'Tue 25', 'Wed 26', 'Thu 27', 'Fri 28', 'Sat 29', 'Sun 30', 'Mon 31',
    'Tue 1', 'Wed 2', 'Thu 3', 'Fri 4', 'Sat 5', 'Sun 6', 'Mon 7', 'Tue 8', 'Wed 9', 'Thu 10', 'Fri 11', 'Sat 12', 'Sun 13', 'Mon 14', 'Tue 15', 'Wed 16', 'Thu 17', 'Fri 18', 'Sat 19', 'Sun 20', 'Mon 21', 'Tue 22', 'Wed 23', 'Thu 24', 'Fri 25', 'Sat 26', 'Sun 27', 'Mon 28', 'Tue 29', 'Wed 30',
    'Thu 1', 'Fri 2', 'Sat 3', 'Sun 4', 'Mon 5', 'Tue 6', 'Wed 7', 'Thu 8', 'Fri 9', 'Sat 10', 'Sun 11', 'Mon 12', 'Tue 13', 'Wed 14', 'Thu 15', 'Fri 16', 'Sat 17', 'Sun 18', 'Mon 19', 'Tue 20', 'Wed 21', 'Thu 22', 'Fri 23', 'Sat 24', 'Sun 25', 'Mon 26', 'Tue 27', 'Wed 28', 'Thu 29', 'Fri 30', 'Sat 31',
]


# data which is merged with date and number
data = [ [date]+number[3*i: 3*i+3] for i,date in enumerate(dates) ]
data = [['']*4] + data
#p(data)

# data which is split to partition by week
data = [ data[i:i+7] for i in range(0,len(data),7)]
#p(data)


def output_week_block(data_of_week):
    template = ' '.join(('{:^6}',)*7) + '\n'
    #p(zip(*data_of_week))
    #p((data_of_week))
    output = ''.join( template.format(*line) for line in zip(*data_of_week) )
    return output
#output_week_block(data[0])


def output_all_data(data):
    output = '\n\n'.join(output_week_block(wdata) for wdata in data)
    return output


if __name__=='__main__':
    print(output_all_data(data))
