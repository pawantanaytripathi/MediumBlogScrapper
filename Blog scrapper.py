# dependencies - pip install beautifulsoup4
#                pip install requests



def BlogScrapper(url):
    import requests
    import re
    import json
    from bs4 import BeautifulSoup


    c = requests.get(url)
    soup = BeautifulSoup(c.content,'lxml')



    ############# for getting the title & author name of the blog ##############


    match = soup.title.find(string= True)
    match = str(match)

    a = match.index("|")

    try:                           # will try to find first full stop
        x = match.index(".")       # if not found then exception is thrown so
    except ValueError:             # we'll use the first "|" that can be found
        x = a
    
    b = match.find("|", a+1)
    c = match.find("by ", a)
    d = c + 3

    print("Author: ", end= "")
    print(match[d:b])              # author name
    
    print("Title: ", end= "")
    if x < a:
        print(match[:x])           # title of blog   ------- logic for full stop case 
    else:
        print(match[:a])



    ############# for getting details including "read time", "date written" ##################


    match2 = soup.body.find_all(string=True)
    
    try:
        r = match2.index(" min read")
        read = match2[r-2] + match2[r]                  # read time
        
    except ValueError:
        
         for i in match2:
             if i.find(" min read") != -1:
                 read = i                
                 

             
    print("Read time: ", end= "")
    print(read)

    match3 = soup.body.find_all(string=True)
    y = 0

    for i in match3:
        y += 1
        if i == "Follow":
            break

    print("Dated: ", end= "")
    print(match3[y])            # date of the blog


    
    ################### for getting blog content ###########################
    

    match4 = soup.body.find_all(string=True)

    # there are multiple "Follow" buttons on the page, we can observe that between
    # the first two "follow" buttons lies the content of the blog so we've extracted
    # and cleaned the content betweeen the two "follow" buttons on the page.

    content = ""
    flag = 0
    flag2 = False

    for i in match4:
    
        if i == "Follow":                 # finds the first follow button and increases the value
            flag += 1                     # to 2 if the second one is found to stop as the content
                                          # is finished.
    
        if i == "Follow" and flag == 2:   # follows the upper if logic to stop the loop
            break
        
        if flag == 1:
            if i.find(" min read") != -1: # finds the "min read" as after that the 
                flag2 = True              # the content starts on all blog pages.
        
            elif flag2 == True:           # after finding the "mins read" the content
                content += i              # is put inside the "content" variable

    print("CONTENT: [" , end = "")
    print(content, end = "]")
    print("\n")


    
    ############## for getting tags from blog, topic & publication name ############

    x = soup.find('script', type='application/ld+json')

    jsonify = json.loads(x.string)
    findingTags = jsonify["keywords"]
    Tags = []
    Publication = ""
    Topic = ""


    # finding the substrings named "tags:", "publication:", "topic:" in json object
    # in findingTags and then extracting it, for further info try - print(findingTags)

    for i in findingTags:
        u = i.find("Tag:")
        v = i.find("Topic:")
        w = i.find("Publication:")
    
        if u != -1:
            Tags.append(i[u+4:])     
    
        elif v != -1:
            Topic += i[v+6:]
            Topic += " "
        
        elif w != -1:
            Publication += i[w+12:]

    print("TAGS: ", end = "")
    print(Tags)
    print("Topic of the blog: ", end = "")
    print(Topic)
    print("Publication name: ", end = "")
    print(Publication)



# main

if __name__ == "__main__":
    x = "https://medium.com/hackernoon/the-future-of-cyber-security-in-the-fintech-era-78b9d7f7c0f0"
    BlogScrapper(x)



# some tested urls below:
#url = "https://medium.com/hackernoon/the-future-of-cyber-security-in-the-fintech-era-78b9d7f7c0f0"
#url = "https://medium.com/bugbountywriteup/guide-to-bypassing-mfa-in-2020-4b9495ab384c"
#url = "https://medium.com/bugbountywriteup/ecpptv2-exam-review-f7c4efb6f9aa"
#url = "https://medium.com/codex/how-you-can-protect-your-data-when-you-die-7f897e77cbb9"
#url = "https://simranjotsinghsran.medium.com/is-end-to-end-encryption-a-myth-6b3f229e99c"
#url = "https://medium.com/analytics-vidhya/multiple-choice-qa-using-deep-learning-44689618a253"

# 4th url showing garbage in blog content (exception case)




    














    

