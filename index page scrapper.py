
def indexScrapper(topic):

    import requests
    import re
    from bs4 import BeautifulSoup
    import json

    default_url = "https://medium.com/topic/" + topic
    c = requests.get(default_url)
    soup = BeautifulSoup(c.content,'lxml')

    x = soup.find_all("script")
    y = x[9]
    f = 0
    y = y.string
    u = 0
    count = 0
    flag2 = 0

    while u != -1:
  
        u = y.find("title", f)
        f = u + 4
        count += 1
    
    
    ############# for getting title & preview content of blog one by one ######################
    
        if 2 < count < 43:      # first two "titles" are of no use so taking next 10
                                # change 33 to a higher/lesser no. to scrap more/less blogs content (WARNING : might give index out of range error)
                        # take the number as argument for function
        
            flag2 += 1
            t = str(y[u:u + 150])
            lastColon = t.find(t[5], 8)
            title = t[8:lastColon]
        
            if flag2 == 1:
                print("Title: " + title)            # Title of the blog + content
            else:                                   # once it will print title of the blog then it 
                print("Preview Content: " + title)  # will print preview content of the blog, alternatively, and then so on for the next one.
        
        
    ##################### for getting name/author of the blog ##################################
        
            if flag2 == 1:       # only to be run once as content does not contain author name only title does.
            
                t_temp = str(y[u-600:u-150])
                find_user = t_temp.find("username")
                new_string = t_temp[find_user+10:]
            
                if find_user != -1:
                    colonFind = new_string.find(new_string[0],1)
                    username = new_string[1: colonFind]             # username of the blog author
                    print("Author's Username: " + username)
                
    ############ for getting name of the blog writer #########################
    
                    name = t_temp.find("name", find_user+7)
                    colonFind2 = t_temp.find(new_string[0],name + 9)
                    author_name = t_temp[name+7:colonFind2]
                    print("Author name: " + author_name)
        
        
            if flag2 == 2:         # this if check just checks whether both title &
                print("\n")        # and content are printed and then prints a new line.
                flag2 = 0




if __name__ == "__main__":
    
    topic = "machine-learning"
    #topic = "cybersecurity"
    #topic = "machine-learning"
    indexScrapper(topic)
    

    
