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


def format_timestamp(total_ms: int) -> str:
    '''
    Переводит милисекунды в строки типа "чч:мм:сс,мсмсмс" 
    '''
    ms = total_ms
    h = f"{ms // 3_600_000:02}"
    ms = ms % 3_600_000

    m = f"{ms // 60_000:02}"
    ms = ms % 60_000

    s = f"{ms // 1000:02}"
    ms_str = f"{ms % 1000:03}"

    return f"{h}:{m}:{s},{ms_str}"
