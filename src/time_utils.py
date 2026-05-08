def parse_timestamp(time_str: str) -> int:
    '''
    Переводит строки типа "чч:мм:сс,мсмсмс" в милисекунды
    '''

    splitted_ms = time_str.split(',')
    hours, minutes, seconds = splitted_ms[0].split(':')

    hours_ms = int(hours) * 3_600_000
    minutes_ms = int(minutes) * 60_000
    seconds_ms = int(seconds) * 1_000
    milliseconds = int(splitted_ms[1])

    return milliseconds + seconds_ms + minutes_ms + hours_ms


def format_timestamp(ms: int) -> str:
    '''
    Переводит милисекунды в строки типа "чч:мм:сс,мсмсмс" 
    '''

            


# parse_timestamp('01:09:20,924')
print(parse_timestamp('01:09:20,924'))
# вывод - 4160924