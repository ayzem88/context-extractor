import os
import glob
import pandas as pd

def extract_context(words, idx, n_before, n_after):
    start_index = max(0, idx - n_before)
    end_index = min(len(words), idx + n_after + 1)
    return ' '.join(words[start_index:end_index])

# تحميل الكلمات المطلوبة من الملف وتحويلها لمجموعة للبحث السريع
search_words_file = "الألفاظ.txt"
with open(search_words_file, 'r', encoding='utf-8') as f:
    search_words = [line.strip() for line in f if line.strip()]
search_set = set(search_words)

# إعداد مسارات المجلد والملف الناتج
input_directory = r"E:\00 - الموارد\00 - المدونة\27 - مدونة المركز العربي"
output_file = 'النتائج.xlsx'

max_results_per_word = 5   # عدد النتائج لكل كلمة
n_before = 7               # عدد الكلمات قبل اللفظ (سنستخدم نفس العدد بعده)
# بنية النتائج: لكل كلمة قائمة من (السياق، اسم الكتاب) ومجموعة لمراقبة الكتب المضافة
results = {word: {'results': [], 'books': set()} for word in search_words}
incomplete_words = set(search_words)  # الكلمات التي لم تصل بعد إلى الحد المطلوب

# معالجة ملفات النصوص داخل المجلد
for file_path in glob.glob(os.path.join(input_directory, '*.txt')):
    if not incomplete_words:
        break  # إن انتهت جميع الكلمات المطلوبة
    book_name = os.path.basename(file_path)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
    except Exception as e:
        print(f"خطأ في قراءة الملف {file_path}: {e}")
        continue
    words = text.split()
    for idx, word in enumerate(words):
        # معالجة فقط الكلمات الموجودة في search_set والغير مكتملة النتائج
        if word in search_set and word in incomplete_words:
            # تجنب استخراج أكثر من سياق من نفس الكتاب لنفس الكلمة
            if book_name in results[word]['books']:
                continue
            # تجربة استخراج سياق كامل بأطوال متناقصة من 7 إلى 4
            for n in range(n_before, 3, -1):
                context = extract_context(words, idx, n, n)
                # نضيف السياق إذا لم يكن مقتطعاً (أي يحتوي على (2*n+1) كلمة)
                if len(context.split()) == (2 * n + 1):
                    results[word]['results'].append((context, book_name))
                    results[word]['books'].add(book_name)
                    break
            # عند وصول الكلمة لعدد النتائج المطلوب، نزيلها من قائمة الكلمات الغير مكتملة
            if len(results[word]['results']) >= max_results_per_word:
                incomplete_words.remove(word)

# إضافة الكلمات التي لم يتم العثور عليها نهائياً إلى النتائج
results_list = []
for word in search_words:
    if results[word]['results']:
        for context, book in results[word]['results']:
            results_list.append([word, context, book])
    else:
        results_list.append([word, "لم يتم العثور على سياقات", "غير متوفر"])


# حفظ النتائج في ملف Excel
df = pd.DataFrame(results_list, columns=['الكلمة', 'السياق', 'اسم الكتاب'])
df.to_excel(output_file, index=False)
print(f"تم حفظ النتائج في الملف {output_file}")
