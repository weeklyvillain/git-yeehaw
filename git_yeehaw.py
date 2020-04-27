import urllib.request, json, random, os

data = "no data :("

base_url = "https://api.github.com/repositories?since="

def get_json(url):
    response = urllib.request.urlopen(url)
    global data
    return json.loads(response.read())

def get_random_integer():
    return random.randint(1, 345345)

def get_random_project(json_data):
    return random.choice(json_data)

if __name__ == "__main__":
    random_url = base_url + str(get_random_integer())
    json_data = get_json(random_url)
    
    project = get_random_project(json_data)
    
    print("Beep Boop")
    os.system("git clone " + project['html_url'])
    
