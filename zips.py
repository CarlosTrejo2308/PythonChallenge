import zipfile

archvie = zipfile.ZipFile('channel.zip', 'r')

start = '90052'

comments = ""

while True:
    info = archvie.read(start + '.txt').decode('utf-8')
    comments += archvie.getinfo(start + '.txt').comment.decode('utf-8')
    print(info)
    start = info.split(' ')[-1]
    if not start.isnumeric():
        break

print(comments)