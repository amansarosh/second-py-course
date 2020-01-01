import re

text = "random string. MyName123@website.com . some more random text. your_Name.8-8-8@company.net"

pattern = re.compile("[a-zA-Z0-9\.\-\_]+\@[a-zA-Z0-9]+\.[a-zA-z]+")

result = pattern.findall(text)

print(result)
