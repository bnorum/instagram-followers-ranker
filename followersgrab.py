# Get instance
import instaloader

def getfollowers():
    L = instaloader.Instaloader()


    username = ""
    f = open("password.txt", "r")
    password = f.read()
    L.login(username, password) 
    f.close()


    profile = instaloader.Profile.from_username(L.context, username)


    follow_list = []
    count = 0
    for followee in profile.get_followers():
        follow_list.append(followee.username)
        file = open("followersunsorted.txt", "a+")
        file.write(follow_list[count])
        file.write("\n")
        file.close()
        print(follow_list[count])
        count = count + 1