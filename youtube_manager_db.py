import sqlite3

conn = sqlite3.connect('youtube_manager.db')

cursor = conn.cursor()

cursor.execute('''
    
    CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               time TEXT NOT NULL
               )

''')


def list_all_videos():
   print("\n")
   print("*" * 70)
   cursor.execute("SELECT * FROM videos")

   for row in cursor.fetchall():
       print(row)


def add_video(name , time):
    cursor.execute("insert into videos (name , time) values (? ,?)", (name, time))
    conn.commit()

def update_video(video_id, name, time):
    cursor.execute(" update videos set name = ? , time = ? where id = ?", (name , time , video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute(" delete from videos where id = ?", (video_id,))
    conn.commit()



def main():

    while True:
        print("\n YOUTUBE MANAGER with DATABASE")
        print(" 1 . LIST FAV YOUTUBE VIDEOS")
        print(" 2 .  ADD A YOUTUBE VIDEO")
        print(" 3 .  UPDATE THE YOUTUBE VIDEO DETAILS")
        print(" 4 .  DELETE A YOUTUBE VIDEO")
        print(" 5 .  EXIT THE APP")

        CHOICE = input(" ENTER YOUR CHOICE: ")

        if CHOICE == "1":

            list_all_videos()
        
        elif CHOICE == "2":
            name = input(" enter the video name ")
            time = input(" enter the video time ")

            add_video(name , time)
        
        elif CHOICE == "3":

            video_id = input(" enter video id to udpate : ")
            name = input(" enter the video name :  ")
            time = input(" enter the video time : ")

            update_video( video_id, name , time)

        elif CHOICE == "4":

            video_id = input(" enter video id to delete : ")
            delete_video( video_id)

        elif CHOICE == "5":
            print(" EXITING THE APP... BYE! ")
            break

        else:
            print(" INVALID CHOICE! PLEASE TRY AGAIN. ")
    
    conn.close()


if __name__ == "__main__":
    main()