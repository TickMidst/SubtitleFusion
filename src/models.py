from dataclasses import dataclass

@dataclass
class Subtitle:
    start_ms: int
    end_ms: int
    text: str

    def overlaps(self, other: "Subtitle") -> bool:
        return (
            self.start_ms < other.end_ms
            and self.end_ms > other.start_ms
        )
            
class SubtitleFile:
    def __init__(self, subtitles: list[Subtitle]):
        self.subtitles: list[Subtitle] = subtitles

    def merge(self, other: "SubtitleFile") -> "SubtitleFile":
        '''
        Объединяет два объекта класса SubtitleFile в один новый и возвращает его
        '''     
        return SubtitleFile(self.subtitles + other.subtitles)

    def sort(self):
        '''
        Сортирует строки subtitles внутри SubtitleFile
        '''
        self.subtitles.sort(key= lambda s: s.start_ms)
