def mapper(text):
    word_counts = []
    for word in text.lower().split(): 
        word_counts.append((word, 1))  
    return word_counts

def shuffle(mapped_data):
    shuffled_data = {}
    for word, count in mapped_data:
        if word in shuffled_data:
            shuffled_data[word].append(count)
        else:
            shuffled_data[word] = [count]
    return shuffled_data

def reducer(shuffled_data, target_word):
    return sum(shuffled_data.get(target_word.lower(), []))

# Read file 
file_path = "BDA2.txt" 
target_word = "data"  

# Read file content
with open(file_path, "r", encoding="utf-8") as file:
    text_data = file.read()

# Apply MapReduce
mapped_results = mapper(text_data)
shuffled_results = shuffle(mapped_results)
frequency = reducer(shuffled_results, target_word)

print(f"Frequency of '{target_word}': {frequency}")
