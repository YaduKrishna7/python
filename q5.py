words=['apple','banana','apple','orange','banana','apple']
unique=set(words)
word_count=dict(map(lambda word:(word,words.count(word)),unique))
print("output:",word_count)