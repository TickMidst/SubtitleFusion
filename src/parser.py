import re
from src.models import Subtitle, SubtitleFile
from src.time_utils import parse_timestamp

def read_srt(path:str) -> SubtitleFile:
    pattern = r'\d+\n\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}'
    timing_delimeter = ' --> '

    subtitles = []

    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
        matches = list(re.finditer(pattern, content))

        for i in range(len(matches)):

            start = matches[i].start()

            if i < len(matches) - 1:
                end = matches[i + 1].start()
            else:
                end = len(content)

            block = content[start:end].strip()  

            lines = block.split('\n')

            timing = lines[1]
            start_ms = parse_timestamp(timing.split(timing_delimeter)[0])
            end_ms = parse_timestamp(timing.split(timing_delimeter)[1])
            text = '\n'.join(lines[2:])

            sub = Subtitle(
                start_ms=start_ms,
                end_ms=end_ms,
                text=text
            )
            subtitles.append(sub)
    
    return SubtitleFile(subtitles)
