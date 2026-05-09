from dataclasses import dataclass
from src.time_utils import format_timestamp

@dataclass
class Subtitle:
    start_ms: int
    end_ms: int
    text: str

    def check_overlaps(self, other: "Subtitle") -> bool:
        return (
            self.start_ms < other.end_ms
            and self.end_ms > other.start_ms
        )
    
    def to_srt_block(self, index:int) -> str:
        block = (
            f"{index}\n"
            f"{format_timestamp(self.start_ms)} --> "
            f"{format_timestamp(self.end_ms)}\n"
            f"{self.text}\n\n"
        )
        return block


class SubtitleFile:
    def __init__(self, subtitles: list[Subtitle]):
        self.subtitles: list[Subtitle] = subtitles

    def __repr__(self):
        return f"SubtitleFile(subtitles={len(self.subtitles)})"

    def merge(self, other: "SubtitleFile") -> "SubtitleFile":
        '''
        Объединяет два объекта класса SubtitleFile в один новый и возвращает его
        '''     
        return SubtitleFile(self.subtitles + other.subtitles)

    def sort(self):
        '''
        Сортирует строки subtitles внутри SubtitleFile
        '''
        self.subtitles.sort(key=lambda s: s.start_ms)
        return self

    def count_overlaps(self) -> int:
        overlaps_count = 0
        for current, next_sub in zip(
            self.subtitles,
            self.subtitles[1:]
        ):
            if current.check_overlaps(next_sub):
                overlaps_count += 1

        return overlaps_count

    def remove_duplicates(self) -> int:
        before = len(self.subtitles)
        seen = set()
        unique = []

        for sub in self.subtitles:
            key = (sub.start_ms, sub.end_ms, sub.text)
            if key not in seen:
                seen.add(key)
                unique.append(sub)

        self.subtitles = unique
        removed = before - len(unique)

        return removed
        
    