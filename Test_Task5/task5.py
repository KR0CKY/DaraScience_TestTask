def word_in_quieres_percentage(queries):
    word_count_arr = {}

    for query in queries:
        words = query.split()
        word_count = len(words)
        if word_count in word_count_arr:
            word_count_arr[word_count] += 1
        else:
            word_count_arr[word_count] = 1

    total_queries = sum(word_count_arr.values())

    for word_count, count in sorted(word_count_arr.items()):
        percentage = (count / total_queries) * 100
        if word_count < 2:
            str = "слово"
        elif word_count < 5:
            str = "слова"
        else:
            str = "слов"
        print(f"{word_count} {str}: {percentage:.0f}%")