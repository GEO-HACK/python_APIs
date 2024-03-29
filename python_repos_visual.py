import requests
import plotly.express as px

# make an api call and store the repsonse
url = "https://api.github.com/search/repositories"
url+= "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)


print(f"status code: {r.status_code}")

#process overall reuslts
response_dict = r.json()
print(f"complete results: {not response_dict['incomplete_results']}")

#process repository informaation
repo_dicts = response_dict['items']
repo_links, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    #turn reponames into repolinks
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])
    
    #Building hover texts.
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)



#make visualization
title ="Most-starred HAskell projects on github"   
labels = {'x':'Repository', 'y':'stars'} 
fig = px.bar(x=repo_links, y=stars, title=title, labels =labels, hover_name=hover_texts)

fig.show()        