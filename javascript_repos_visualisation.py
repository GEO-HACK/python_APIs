import requests
import plotly.express as px

#make an API call and store the repsonse
url = 'https://api.github.com/search/repositories'
url+= '?q=language:JavaScript+sort:stars+stars:>10000'

headers = {"Accept":"application/vnd.github.v3+json"}
r= requests.get(url, headers=headers)
print(f"status code : {r.status_code}")

#convert the response box into a dictionary
response_dict = r.json()
#working eith dictionaries
print(f"Total_repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

#Explore information about the repositorie
repo_dicts = response_dict['items']
repo_links, stars,hover_texts = [], [], []

for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    #build hover text for each point
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

# make visualization
title = "Most starred javascript projects on Github"
labels = {'x': 'repositories', 'y': 'stars'}  # Fix: Use dictionary instead of list

fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, hover_name=hover_texts)

fig.update_layout(title_font_size=28,xaxis_title_font_size=20 ,yaxis_title_font_size=20)
fig.show()
