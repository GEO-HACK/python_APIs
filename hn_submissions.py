from operator import itemgetter
import requests

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)

print(f"status code: {{r.status_code}}")

submission_ids = r.json()
submission_dicts =[]
for submission_id in submission_ids[:5]:
    #make a new Api call for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    #build a dictionary for each article
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': "https://news.ycombinator.com/item?id=" + str(submission_id),
        'comments': response_dict['descendants']
    }
    submission_dicts.append(submission_dict)

submission_dict = sorted(submission_dicts, key = itemgetter('comments'),reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"comments: {submission_dict['comments']}")

