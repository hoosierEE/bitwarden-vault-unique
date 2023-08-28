import json,sys

with open(sys.argv[1]) as f:
    d = json.load(f)

dd = {}
beforelen = len(d['items'])
for item in d['items']:
    remove = {'id':0,'folderId':0,'revisionDate':0,'creationDate':0,'deletedDate':0}
    key = repr({**item, **remove})
    if key in dd:
        name = item['name']
        user = '('+(str(item['login']['username']) if 'login' in item else '')+')'
        print('removing duplicate:  ',name,user)
    dd[key] = item

d['items'] = list(dd.values())
with open(sys.argv[2], 'w', encoding='utf-8') as f:
    json.dump(d, f, indent=2)

afterlen = len(d['items'])
print('Summary:')
print(f'  {sys.argv[1]}: {beforelen} items')
print(f'  {sys.argv[2]}: {afterlen} items')
print(f'  (Removed {beforelen-afterlen} duplicates.)')
