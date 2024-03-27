import requests
url = 'https://api.github.com/search/repositories'
url += '?q=language:Visual Basic+sort:stars+stars:>=10000'

headers = {'Accept':"application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code:{r.status_code}")

response_dict = r.json()

print(f"Total_repositories:{response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

repo_dicts = response_dict['items']
print(f"Repsoitories returned:{ len(repo_dicts)}")

repo_dict= repo_dicts[0]
print("\n Selected information about the first repository:")
for repo_dict in repo_dicts:
    print(f"\nName:{repo_dict['name']}")
    print(f"Owner:{repo_dict['owner']['login']}")
    print(f"Stars:{repo_dict['stargazers_count']}")
    print(f"Repository:{repo_dict['html_url']}")
    print(f"Created:{repo_dict['created_at']}")
    print(f"Updated:{repo_dict['updated_at']}")
    print(f"Description:{repo_dict['description']}")
    print(f"Language:{repo_dict['language']}")
    print(f"Watchers:{repo_dict['watchers_count']}")
    print(f"Forks:{repo_dict['forks_count']}")
    print(f"Open Issues:{repo_dict['open_issues_count']}")
    print(f"URL:{repo_dict['html_url']}")
    print(f"Size:{repo_dict['size']}")
    print(f"Archived:{repo_dict['archived']}")
    print(f"Forks URL:{repo_dict['forks_url']}")
    print(f"Commits URL:{repo_dict['commits_url']}")
    print(f"Contributors URL:{repo_dict['contributors_url']}")
    print(f"Deployments URL:{repo_dict['deployments_url']}")


