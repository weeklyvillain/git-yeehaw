import urllib.request, json, random, os

base_url = "https://api.github.com/repositories?since="

def get_json(url):
    response = urllib.request.urlopen(url)
    return json.loads(response.read())

def get_random_integer():
    return random.randint(1, 345345)

def get_random_project(json_data):
    return random.choice(json_data)

def get_repo_size(repo_name):
    url = 'https://api.github.com/repos/' + repo_name
    response = urllib.request.urlopen(url)
    project_json = json.loads(response.read())
    size = int(project_json['size'])
    return size

if __name__ == "__main__":
    random_url = base_url + str(get_random_integer())
    json_data = get_json(random_url)
    
    project = get_random_project(json_data)
    
    print("Beep Boop")
    print("Oooh look at this repo: " + str(project['name']))
    print('Size is: ' + str(get_repo_size(project['full_name'])) + "KB")
    value = input("Do you want to continue? (yes, no): ")
    if value.lower() == 'yes':
        os.system("git clone " + project['html_url'])
    print("Exiting git yeehaw...")


    
