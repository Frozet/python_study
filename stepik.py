command = 'select all'
ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
print(*map(lambda x: x in command, ignore))