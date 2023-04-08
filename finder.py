import re
import time

def count_it(text, classNames):
    import re
    pattern = fr'\b({classNames})\b'
    count = len(re.findall(pattern, text))
    #print(f'"{classNames}" : {count}')
    return count
def open_html(file_name):
    with open(file_name + ".html", "r", encoding="utf-8") as f:
        data = f.read()
        f.close()
    return data


def parser(class_name, tag_name, html, looper):
    val = ""
    for i in range(looper):
        cnSpan= re.search(class_name, html)
        html = html[cnSpan.span()[1]:]
        tnSpan = re.search(tag_name, html)
        temp = html[:tnSpan.span()[0] - 2]
        temp = temp.replace(" ", "")
        #print(temp.replace('">', ""))
        #print(cnSpan,tnSpan)
        val = val + temp.replace('">', "")
    return val
    

def create_txt(txt_name, data):
    with open(txt_name + ".txt", "w", encoding="utf-8") as f:
        f.write(data)
        f.close()

def find_diff(followers, following):
    with open(followers,"r") as f:
        fs = f.read()
        f.close()
    with open(following,"r") as f:
        fg = f.read()
        f.close()
    s1 = fg
    s2 = fs
    s1 = s1.split()
    unfollowers = ""
    for i in s1:
        if i not in s2:

            unfollowers = unfollowers + i + "\n"
    return unfollowers



def main():
    class_name = "x9f619 xjbqb8w x1rg5ohu x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x6s0dn4 x1oa3qoh x1nhvcw1"
    tag_name = "div"
    html = open_html("followers")
    looper = count_it(text=html, classNames = 'x9f619 xjbqb8w x1rg5ohu x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x6s0dn4 x1oa3qoh x1nhvcw1')
    print(looper)
    data = parser(class_name=class_name, tag_name=tag_name, html=html, looper=looper)
    create_txt(txt_name="followers", data=data)
    html = open_html("following")
    looper = count_it(text=html, classNames = 'x9f619 xjbqb8w x1rg5ohu x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x6s0dn4 x1oa3qoh x1nhvcw1')
    print(looper)
    data = parser(class_name=class_name, tag_name=tag_name, html=html, looper=looper)
    create_txt(txt_name="following", data=data)
    time.sleep(2)
    result = find_diff(followers="followers.txt", following="following.txt")
    
    with open("unfollowers.txt", "w") as f:
        f.write(result)
        f.close()
    
    print(result)


main()
