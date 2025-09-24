from operator import index

from Note import Note
import datetime

def menu():
    print("1: Display Notes")
    print("2: New Note")
    print("3: Delete Note")


def main():
    print("===>>>   Note Manager   <<<====")
    listOfNotes = []
    while True:
        menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            if len(listOfNotes) != 0:
                for i in listOfNotes:
                    print(i.__str__())
            else:
                print("No Notes Found")
                print("Write a new Note")

        if choice == 2:
            title = str(input("Enter the Your Note: ")).strip()
            s = str(input("Enter Your Note: ")).strip()

            note = Note(title, s, datetime.datetime.now())
            listOfNotes.append(note)

            print(f"""Titel: {title} \n Date: {datetime.datetime.now()} \n Note: {s} \n""")

        if choice == 3:
            title = input("Enter the Your Note: ")
            ch = 0
            for i in listOfNotes:
                if i.Note.getTitle() == title:
                    ch = index(i)
                    break
            tmp = listOfNotes[ch]
            listOfNotes.pop(ch)

            print("Deleted Note")
            print(f"""Tile: {tmp.Note.getTitle()} \n Date: {tmp.Note.getDate()} \n Content: {tmp.Note.getContent()} \n""")





if __name__ == '__main__':
    main()