import requests

url = 'https://api.github.com/search/repositories'
url += '?q=language:Ruby+sort:stars+stars:>10000'

headers = {"Accept":"application/vnd.github.v3+json"}
r= requests.get(url,headers=headers)
print(f"status code:{r.status_code}")

response_dict = r.json()

print(f"Total_repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

repo_dicts= response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

repo_dict = repo_dicts[0]
print("\nSelected information about the first repositories:")
for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")
    print(f"Watchers: {repo_dict['watchers_count']}")