
def first_team(count_):
    print('В команде Мастера кода участников: %s' % (count_))

first_team(5)

def sum_teams(team1_num, team2_num):
    print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))

sum_teams(5,6)

def task_team2(score_2):
    print('Команда Волшебники данных решила задач: {}'.format(score_2))

task_team2(42)

def decision_time_team2(team2_time):
    print('Волшебники данных решили задачи за {} c'.format(team2_time))

decision_time_team2(18015.2)

def completed_tasks(score1, score2):
    print(f'Команды решили {score1} и {score2} задач')

completed_tasks(40,42)

def victories(score_1, score_2, team1_time, team2_time):
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        challenge_result = 'Победа команды Мастера кода!'
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        challenge_result = 'Победа команды Волшебники Данных!'
    else:
        challenge_result = 'Ничья'
    print(f'Результат битвы: {challenge_result}')

victories(40,42, 1552.512, 2153.31451 )

def work_scope(tasks_total, time_avg):
    print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')

work_scope(82, 45.2)




