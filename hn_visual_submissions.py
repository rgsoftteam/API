import requests

from plotly.graph_objs import Bar
from plotly import offline

from operator import itemgetter

# создание вызова API и сохранение ответа.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# обработка информации о каждой статье.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:5]:
    # создание отдельного вызова API для каждой статьи.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    
    # построение словаря для каждой статьи.
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict["descendants"],
    }
    submission_dicts.append(submission_dict)
    
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            reverse=True)

titles, links, comments = [], [], []
for submission_dict in submission_dicts:
	subm_title = submission_dict['title']
	subm_url = submission_dict['hn_link']
	subm_link = f"<a href='{subm_url}'>{subm_title}</a>"
	subm_comment = submission_dict['comments']
	titles.append(subm_title)
	links.append(subm_link)
	comments.append(subm_comment)


for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")

# построение визуализации
data = [{
	'type': 'bar',
	'x' : links,
	'y': comments,
	'hovertext': titles,
	'marker': {
	'color': 'rgb(60, 100, 150)',
	'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
	},
	'opacity': 0.6,
}]
my_layout = {
	'title': 'Most-Starred Submissions on Hacker News',
	'titlefont': {'size': 28},
	'xaxis': {
		'title': 'Submission',
		'titlefont': {'size': 24},
		'tickfont': {'size': 14},
	},
	'yaxis': {
		'title': 'Comments',
		'titlefont': {'size': 24},
		'tickfont': {'size': 14},
	},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='Hacker_News.html')