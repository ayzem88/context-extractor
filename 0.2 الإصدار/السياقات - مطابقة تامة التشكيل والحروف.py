import os
import glob

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def extract_context(words, idx, n_before, n_after):
    start_index = max(0, idx - n_before)
    end_index = min(len(words), idx + n_after + 1)
    context = ' '.join(words[start_index:end_index])
    return context

# تحميل الكلمات من الملف
search_words_file = r"الألفاظ.txt"
with open(search_words_file, 'r', encoding='utf-8') as file:
    search_words = [line.strip() for line in file]

input_directory = r"المدونة"
results_directory = r"النتائج"  # مجلد النتائج
ensure_dir(results_directory)  # التأكد من وجود المجلد أو إنشاؤه

max_results = 10000

results = {word: {'sentences': [], 'books': []} for word in search_words}

# استعراض جميع الملفات بصيغة txt في المجلد
for file_path in glob.glob(os.path.join(input_directory, '*.txt')):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_text = file.read()
            words = file_text.split()
            book_name = os.path.basename(file_path)  # اسم الكتاب

            for idx, word in enumerate(words):
                if word in search_words and len(results[word]['sentences']) < max_results:
                    for n in range(7, 3, -1):
                        context = extract_context(words, idx, n, n)
                        if len(context.split()) == (2 * n + 1):
                            results[word]['sentences'].append(context)
                            results[word]['books'].append(book_name)
                            break
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

# حفظ النتائج في ملفات داخل مجلد النتائج
not_found_words = []
for search_word in search_words:
    if len(results[search_word]['sentences']) == 0:
        not_found_words.append(search_word)
    else:
        output_file_path = os.path.join(results_directory, f'{search_word}.txt')
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            for index, result in enumerate(results[search_word]['sentences'], start=1):
                book_name = results[search_word]['books'][index-1]
                output_file.write(f'{index}. {result} (مصدر السياق من: {book_name})\n')

# حفظ الكلمات التي لم يتم العثور عليها في ملف جديد داخل مجلد النتائج
not_found_words_file_path = os.path.join(results_directory, 'ألفاظ لم أعثر عليها؛ للأسف!.txt')
with open(not_found_words_file_path, 'w', encoding='utf-8') as output_file:
    for word in not_found_words:
        output_file.write(f'{word}\n')
