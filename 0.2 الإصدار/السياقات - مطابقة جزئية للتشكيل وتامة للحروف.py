import os
import glob
import re

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def extract_context(words, idx, n_before, n_after):
    start_index = max(0, idx - n_before)
    end_index = min(len(words), idx + n_after + 1)
    context = ' '.join(words[start_index:end_index])
    return context

def remove_diacritics(word):
    # قائمة الحركات والتشكيل في اللغة العربية
    arabic_diacritics = re.compile("""
                             ّ    | # Tashdid
                             َ    | # Fatha
                             ً    | # Tanwin Fath
                             ُ    | # Damma
                             ٌ    | # Tanwin Damm
                             ِ    | # Kasra
                             ٍ    | # Tanwin Kasr
                             ْ    | # Sukun
                             ـ     # Tatwil/Kashida
                         """, re.VERBOSE)
    return re.sub(arabic_diacritics, '', word)

def remove_punctuation(word):
    # إزالة علامات الترقيم من بداية ونهاية الكلمة
    # يمكن تعديل قائمة الأحرف حسب الحاجة
    punctuation = re.compile(r'^[\(\)\.\،\!\؟\;\:\-\"\'«»“”]+|[\(\)\.\،\!\؟\;\:\-\"\'«»“”]+$')
    return re.sub(punctuation, '', word)

# تحميل الكلمات من الملف وتطبيعها بدون حركات وعلامات ترقيم
search_words_file = r"الألفاظ.txt"
with open(search_words_file, 'r', encoding='utf-8') as file:
    search_words_original = [line.strip() for line in file]
# إنشاء مجموعة للكلمات المطبوعة بدون تشكيل وعلامات ترقيم للبحث السريع
search_words_stripped = set(
    remove_diacritics(remove_punctuation(word)) for word in search_words_original
)

input_directory = r"المدونة"
results_directory = r"النتائج"  # مجلد النتائج
ensure_dir(results_directory)  # التأكد من وجود المجلد أو إنشاؤه

max_results = 10000

# تهيئة النتائج بناءً على الكلمات الأصلية
results = {word: {'sentences': [], 'books': []} for word in search_words_original}

# استعراض جميع الملفات بصيغة txt في المجلد
for file_path in glob.glob(os.path.join(input_directory, '*.txt')):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_text = file.read()
            words = file_text.split()
            book_name = os.path.basename(file_path)  # اسم الكتاب

            for idx, word in enumerate(words):
                # إزالة التشكيل وعلامات الترقيم
                word_clean = remove_diacritics(remove_punctuation(word))
                if word_clean in search_words_stripped:
                    # إيجاد الكلمة الأصلية المطابقة
                    matching_words = [orig_word for orig_word in search_words_original 
                                      if remove_diacritics(remove_punctuation(orig_word)) == word_clean]
                    for search_word in matching_words:
                        if len(results[search_word]['sentences']) < max_results:
                            for n in range(7, 3, -1):
                                context = extract_context(words, idx, n, n)
                                if len(context.split()) == (2 * n + 1):
                                    results[search_word]['sentences'].append(context)
                                    results[search_word]['books'].append(book_name)
                                    break
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

# حفظ النتائج في ملفات داخل مجلد النتائج
not_found_words = []
for search_word in search_words_original:
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
