import requests

# создание вызова АРI и сохранение ответа
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept' : 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# сохранение ответа АРI в переменной
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# анализ информации о репозиториях
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:

	print(f"\nName: {repo_dict['name']}")
	print(f"Owner: {repo_dict['owner']['login']}")
	print(f"Stars: {repo_dict['stargazers_count']}")
	print(f"Reposirory: {repo_dict['html_url']}")
	print(f"Created: {repo_dict['created_at']}")
	print(f"Updated: {repo_dict['updated_at']}")
	print(f"Description: {repo_dict['description']}")

print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
	print(key)


# обработка результатов
print(response_dict.keys())