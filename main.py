from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from src.parser import read_srt
from src.writer import write_srt
from tkinter.messagebox import (
    showinfo,
    showerror,
    showwarning
)
import os
import sys
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def main():
    root = Tk()
    root.iconbitmap(resource_path('assets/icon.ico'))
    root.withdraw()  # скрывает главное окно tkinter

    first_file_path = askopenfilename(
        title='Выберите первый .srt файл',
        filetypes=[('SRT files', '*.srt')]
    )
    if not first_file_path:
        return

    second_file_path = askopenfilename(
        title='Выберите второй .srt файл',
        filetypes=[('SRT files', '*.srt')]
    )
    if not second_file_path:
        return

    try:
        file1 = read_srt(first_file_path)
        if not file1.subtitles:
            showerror(
                title='Ошибка',
                message=f'Файл {first_file_path} пуст' 
            )
        file2 = read_srt(second_file_path)
        if not file2.subtitles:
            showerror(
                title='Ошибка',
                message=f'Файл {second_file_path} пуст' 
            )
    except Exception as e:
        showerror(
            title='Ошибка',
            message=str(e)
        )
    else:
        merged_file = file1.merge(file2).sort()
        removed_count = merged_file.remove_duplicates()

        if removed_count != 0:
            showwarning(
                title='Внимание',
                message=f'Удалено {removed_count} дубликатов!'   
            )

        # Предупреждение о наложениях
        overlaps_count = merged_file.count_overlaps()
        if overlaps_count != 0:
            showwarning(
                title='Внимание',
                message=f'Найдено {overlaps_count} пересечений!'
            )
        
        save_path = asksaveasfilename(
            title='Сохранить как',
            filetypes=[('SRT files', '*.srt')],
            defaultextension='.srt',
            initialfile='merged_subs.srt'
        )

        if not save_path:
            return

        write_srt(merged_file, save_path)

        showinfo(
            title='Готово',
            message='Субтитры успешно объединены'
        )

    root.destroy()

if __name__ == '__main__':
    main()
    