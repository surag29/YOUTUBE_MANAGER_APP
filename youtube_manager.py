import json

def load_data():
    try :
        with open('youtube.text', 'r') as file:
            test = json.load(file)
            # print(type(test))
            return test

    except FileNotFoundError:
        return []
    

def save_data_helper(videos):

    with open('youtube.text', 'w') as file:
        json.dump(videos , file)



def list_all_videos(videos): 

    print('\n')
    print("*" * 70)

    for index , video in enumerate(videos, start = 1):
        print(f"{index} ,   name : {video['name']} ,  duration : {video['time']}.")
    



def add_video(videos):
    name = input("ENTER THE NAME OF THE VIDEO")
    time = input("ENTER THE time OF THE VIDEO")

    videos.append({'name': name ,  'time': time})

    save_data_helper(videos)



def update_video(videos):
    list_all_videos(videos)

    index = int(input("ENTER THE VIDEO NUMBER TO UDPDATE:"))
    if 1<= index <= len(videos):
        name = input("ENTER THE NEW NAME OF THE VIDEO")
        time = input("ENTER THE NEW time OF THE VIDEO")
        videos[index-1] = {'name': name ,  'time': time}
        save_data_helper(videos)
    
    else:
        print('invalid video number!')



def delete_video(videos):
    list_all_videos(videos)

    index = int(input("ENTER THE VIDEO NUMBER TO DELETE:"))

    if 1<= index <= len(videos):

        del videos[index-1]
        save_data_helper(videos)

    else:

     print(" INVALID VIDEO NUMBER! ")

    


def main():
    videos = load_data()
    while True:
        print("\n YOUTUBE MANAGER")
        print(" 1 . LIST FAV YOUTUBE VIDEOS")
        print(" 2 .  ADD A YOUTUBE VIDEO")
        print(" 3 .  UPDATE THE YOUTUBE VIDEO DETAILS")
        print(" 4 .  DELETE A YOUTUBE VIDEO")
        print(" 5 .  EXIT THE APP")

        CHOICE = input(" ENTER YOUR CHOICE: ")
        # print(videos)

        match CHOICE:
            case "1" :

                list_all_videos(videos)
            
            case "2" :

                add_video(videos)
            
            case "3" :

                update_video(videos)
            
            case "4" :

                delete_video(videos)
            
            case "5" :

                print(" EXITING THE APP... BYE! ")
                break

            case _:
                print(" INVALID CHOICE! PLEASE TRY AGAIN. ")


if __name__ == "__main__":
    main()
            