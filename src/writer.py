from src.models import SubtitleFile

def write_srt(sub_file: SubtitleFile, path: str):
    with open(path, "w", encoding='utf-8') as file:
        for i, sub in enumerate(sub_file.subtitles, start=1):
            srt_block = sub.to_srt_block(i)

            file.write(srt_block)
