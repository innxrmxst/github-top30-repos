import requests
from plotly.graph_objs import Bar
from plotly import offline

url =  'https://api.github.com/search/repositories?q=language:python&sort=stars'

headers = {'Accept': 'application/vnd.github.v3+json'}

r = requests.get(url, headers=headers)
response_dict = r.json()
response_repos = response_dict['items']
# repo_names = []
stars, labels, repo_links = [], [], []
response_total_repose = response_dict['total_count']
response_incomplete_results = response_dict['incomplete_results']

# print("---")
# print(f"Status code: {r.status_code}")
# print(f"Incomplete results: {response_incomplete_results}")
# print(f"Repositories returned: {len(response_repos)}")
# print(f"GitHub ammount of all repositories: {response_dict['total_count']}")
# print("---\n")

# selected_repo = response_repos[0]

# print(f"Keys: {len(selected_repo.keys())}\n")
# for i in sorted(selected_repo.keys()):
#     print(i)

# print("Selected information about repository(es):")
for i in response_repos:
    # repo_names.append(i['name'])
    stars.append(i['stargazers_count'])
    
    owner = i['owner']['login']
    description = i['description']
    label = f"{owner}<br />{description}"
    labels.append(label)

    repo_name = i['name']
    repo_url = i['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

data = [{
    'type': 'bar',
    # 'x': repo_names,
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]
my_layout = {
    'title': "Most-Starred Python Projects on GitHub",
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 30},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
#     print(f"Name: {i['name']}")
#     print(f"Owner: {i['owner']['login']}")
#     print(f"Stars: {i['stargazers_count']}")
#     print(f"Repository: {i['html_url']}")
#     print(f"Created: {i['created_at']}")
#     print(f"Updated: {i['updated_at']}")
#     print(f"Description: {i['description']}")

