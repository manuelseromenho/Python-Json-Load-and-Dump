import json


with open('source_file_2.json') as json_file:
    data = json.load(json_file)
    managers = []
    watchers = []
    managers_list = []
    watchers_list = []
    for p in data:
        for manager in p['managers']:
            managers.append(manager)
        for watcher in p['watchers']:
            watchers.append(watcher)

    managers = list(set(managers))

            
    for manager in managers:
        manager_dict = {}
        manager_projects = []
        manager_projects_list = []
        for p in data: 
            if manager in p['managers']:
                manager_projects.append((p['name'], p['priority']))
                manager_projects = sorted(manager_projects, key=lambda x: x[1])
                manager_projects_list = [proj[0] for proj in manager_projects]
                manager_dict.update({manager: manager_projects_list})
        managers_list.append(manager_dict)

    for watcher in watchers:
        watcher_dict = {}
        watcher_projects = []
        watcher_projects_list = []
        for p in data: 
            if watcher in p['watchers']:
                watcher_projects.append((p['name'], p['priority']))               
                watcher_projects = sorted(watcher_projects, key=lambda x: x[1])
                watcher_projects_list = [proj[0] for proj in watcher_projects]
                watcher_dict.update({manager: watcher_projects_list})
        watchers_list.append(watcher_dict)



with open('managers.json', 'w') as outfile:
    json.dump(managers_list, outfile)

with open('watchers.json', 'w') as outfile:
    json.dump(watchers_list, outfile)

