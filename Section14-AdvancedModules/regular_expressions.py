import re

text = "The agent's phone is 12345"

pattern = 'phone'

match = re.search(pattern, text)

print(match.span())

print(match.end())

text = "my phone twice my phone"

matches = re.findall('phone', text)
print(matches)
print(len(matches))

for match in re.finditer('phone', text):
    print(match.group())

    
text = "My phone number is 408-555-1232"
phone = re.search("408-555-1234", text)
print(phone)
# Character identifiers
phone = re.search(r"\d\d\d-\d\d\d-\d\d\d\d", text)
print(phone)
# Quantifiers
phone = re.search(r"\d{3}-\d{3}-\d{4}", text)
print(phone)

# Compile
phone_pattern = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
results = re.search(phone_pattern, text)
print(results.group())
print(results.group(1))
print(results.group(2))
print(results.group(3))

# Wildcards

# OR operator
# Returns None
print(re.search(r"cat", "The dog is here"))

# | is the OR operator
print(re.search(r"cat|dog", "The dog is here"))

# . is the any character
# Only returns 'at'
print(re.findall(r"at", "The cat in the hat sat there"))
# Returns 'at' with character before it
print(re.findall(r".at", "The cat in the hat sat there"))

# Starts with ^, ends with $
print(re.findall(r"^\d", "The 2 is a number"))
print(re.findall(r"^\d", "2 is a number"))

# Exclude identifer []
phrase = "There are 3 numbers 34 inside 5 this sentence"
pattern = r"[^\d]"
print(re.findall(pattern,phrase))

pattern = r"[^\d]+"
print(re.findall(pattern,phrase))

text = "Only find the hypen-words in this sentence. But you do not know how long-ish these words are"
pattern = r"[\w]+-[\w]+"
print(re.findall(pattern, text))