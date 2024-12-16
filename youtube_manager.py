import json


# this taking data from file as List [{},{},....] like this
def load_data():
    try:
        with open('youtub.txt','r') as file:
            result = json.load(file)
            return result
    except FileNotFoundError:
        return []   
    
def save_data(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)    

def display_all_youtube_videos(videos):
    print("\n")
    print("*" * 80)
    for index,video in enumerate(videos,start=0):
        print(f"{index+1}. {video['name']}, Duration: {video['time']}")
    print("\n")
    print("*" * 80)


def add_youtube_videos(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data(videos)
    print("\n")
    print("You are succesfully added youtube video!!")

def update_youtube_videos(videos):
    display_all_youtube_videos(videos)
    index = int(input("Enter the video number to update : "))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name : ")
        time = input("Enter the new video time : ")
        videos[index-1] = {'name':name, 'time': time}
        save_data(videos)
    else:
        print("Invalid index selected")
    print("\n")    
    print("You are succesfully updated youtube video!!")    

def delete_youtube_videos(videos):
    display_all_youtube_videos(videos)
    index = int(input("Enter the video number to be deleted : "))
    
    if 1<= index <= len(videos):
        del videos[index-1]
        save_data(videos)
    else:
        print("Invalid video index selected")
    print("\n")
    print("You are succesfully deleted youtube video!!")






# main function
def main():
    videos=load_data()
    while True:
        print("\n ************************************* Welcome to youTube Manager App ***************************************")
        print("1. Display the list of all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video")
        print("4. Delete a youtube video")
        print("5. Exist from the app")
        choice = input("Enter your choice : ")
      
        match choice:
            case '1':
                display_all_youtube_videos(videos)
            case '2':
                add_youtube_videos(videos)
            case '3':
                update_youtube_videos(videos)
            case '4':
                delete_youtube_videos(videos)
            case '5':
                break
            case _:
                print("Invalid choice plzz choose correct choice ")

                    

                



    




# For the execution of main function
if __name__ =="__main__": 
    main()
