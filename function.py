import json
import datetime

def load_notes():
    try:
        with open("notes.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_notes(notes):
    with open("notes.json", "w") as f:
        json.dump(notes, f)

def add_note():
    notes = load_notes()
    note_id = len(notes) + 1
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    created_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    last_updated_time = created_time
    note = {"id": note_id, "title": title, "body": body, "created_time": created_time, "last_updated_time": last_updated_time}
    notes[note_id] = note
    save_notes(notes)

def edit_note():
    note_id = int(input("Введите номер заметки: "))
    with open("notes.json", "r") as f:
        notes = json.load(f)
    if str(note_id) in notes:
        note = notes[str(note_id)]
        print(f"> Заметка №{note_id}")
        print(f"> Заголовок: {note['title']}")
        print(f"> Текст: {note['body']}")
        new_title = input("Введите новый заголовок (оставьте пустым, чтобы не изменять): ")
        new_body = input("Введите новый текст (оставьте пустым, чтобы не изменять): ")
        if new_title:
            note['title'] = new_title
        if new_body:
            note['body'] = new_body
        note['last_updated_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("notes.json", "w") as f:
            json.dump(notes, f)
        print(f"Заметка №{note_id} успешно обновлена.")
    else:
        print(f"Заметка №{note_id} не найдена.")

def view_notes():
    notes = load_notes()
    if notes:
        for note_id, note in notes.items():
            print(f"\tЗаметка №{note_id}")
            print(f"\tЗаголовок: {note['title']}")
            print(f"\tТекст: {note['body']}")
            print(f"\tДата создания: {note['created_time']}")
            print(f"\tДата последнего изменения: {note['last_updated_time']}")
    else:
        print("Заметок пока нет.")

def delete_note():
    note_id = int(input("Введите номер заметки: "))
    with open("notes.json", "r") as f:
        notes = json.load(f)
    if str(note_id) in notes:
        print(f"Удаление заметки №{note_id}")
        confirmation = input("Вы действительно хотите удалить эту заметку? (y/n) ")
        if confirmation.lower() == "y":
            del notes[str(note_id)]
            with open("notes.json", "w") as f:
                json.dump(notes, f)
            print(f"Заметка №{note_id} успешно удалена.")
        else:
            print(f"Удаление заметки №{note_id} отменено.")
    else:
        print(f"Заметка №{note_id} не найдена.")

def view_note():
    note_id = int(input("Введите номер заметки: "))
    with open("notes.json", "r") as f:
        notes = json.load(f)
    if str(note_id) in notes:
        note = notes[str(note_id)]
        print(f"\tЗаметка №{note_id}")
        print(f"\tЗаголовок: {note['title']}")
        print(f"\tТекст: {note['body']}")
        print(f"\tДата создания: {note['created_time']}")
        print(f"\tДата последнего изменения: {note['last_updated_time']}")
    else:
        print(f"Заметка №{note_id} не найдена.")