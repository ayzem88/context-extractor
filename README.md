# مستخرج سياقات للألفاظ / Context Extractor for Words

<div dir="rtl">

## نظرة عامة

أداة متقدمة لاستخراج السياقات المحيطة للألفاظ من المدونات النصية العربية. تدعم مطابقة تامة وجزئية للتشكيل والحروف.

## المميزات

- 📝 **استخراج السياقات**: استخراج السياقات المحيطة للألفاظ
- 🔍 **مطابقة تامة**: مطابقة تامة للتشكيل والحروف
- 🔎 **مطابقة جزئية**: مطابقة جزئية للتشكيل وتامة للحروف
- 📚 **دعم مدونات متعددة**: معالجة مدونات كبيرة
- 📊 **تصدير Excel**: تصدير النتائج بصيغة Excel

## التثبيت

### المتطلبات

- Python 3.7 أو أحدث
- openpyxl (لتصدير Excel)

### خطوات التثبيت

1. استنسخ المستودع:
```bash
git clone https://github.com/ayzem88/context-extractor.git
cd context-extractor
```

2. قم بتثبيت المتطلبات:
```bash
pip install openpyxl
```

## الاستخدام

### الإصدار 0.1

```bash
python "0.1 الإصدار/سياقات مع مصادر مرة واحدة في إكسل.py"
```

### الإصدار 0.2 - مطابقة تامة

```bash
python "0.2 الإصدار/السياقات - مطابقة تامة التشكيل والحروف.py"
```

### الإصدار 0.2 - مطابقة جزئية

```bash
python "0.2 الإصدار/السياقات - مطابقة جزئية للتشكيل وتامة للحروف.py"
```

## هيكل المشروع

```
مستخرج سياقات للألفاظ/
├── 0.1 الإصدار/
│   ├── سياقات مع مصادر مرة واحدة في إكسل.py
│   └── المدونة/
├── 0.2 الإصدار/
│   ├── السياقات - مطابقة تامة التشكيل والحروف.py
│   ├── السياقات - مطابقة جزئية للتشكيل وتامة للحروف.py
│   ├── الألفاظ.txt
│   └── المدونة/
│       └── [ملفات المدونة]
```

## الملفات الرئيسية

- **السياقات - مطابقة تامة التشكيل والحروف.py**: مطابقة تامة
- **السياقات - مطابقة جزئية للتشكيل وتامة للحروف.py**: مطابقة جزئية

## ملاحظات مهمة

⚠️ **ملاحظة**: 
- ضع الألفاظ المراد البحث عنها في ملف `الألفاظ.txt`
- ضع ملفات المدونة في مجلد `المدونة/`
- النتائج تُحفظ في مجلد `النتائج/`

## التطوير المستقبلي

- [ ] واجهة رسومية (GUI)
- [ ] تحسين الأداء للمدونات الكبيرة
- [ ] دعم المزيد من خيارات المطابقة
- [ ] تصدير بصيغ متعددة

## المساهمة

نرحب بمساهماتكم! يرجى قراءة [CONTRIBUTING.md](CONTRIBUTING.md) للمزيد من التفاصيل.

## الترخيص

هذا المشروع مخصص للاستخدام الأكاديمي والبحثي.

## منهج التطوير

أُعتمد في مشاريعي البرمجية على منهج Vibe Coding؛ أسلوب يتجاوز كتابة كلّ سطر يدوياً، إذ أوجّه نماذج الذكاء الاصطناعي بوصف منطقي وواضح للوظيفة المطلوبة، ثم أُقيّم النتائج وأُدخِل التحسينات.

هذا النهج يعزّز السرعة في إنشاء النماذج الأولية والوِحدات البرمجية، ويمنحني تركيزاً أكبر على التصوّر العام والتصميم بدلاً من التفاصيل الدقيقة.

في هذا المستودع، تجد أدوات ومشاريع بُنيت بهذه المقاربة — يُرحّب بتجربتها والمساهمة فيها.

## المطور

تم تطوير هذا المشروع بواسطة **أيمن الطيّب بن نجي** ([ayzem88](https://github.com/ayzem88))

---

# [English]

<div dir="ltr">

## Overview

An advanced tool for extracting surrounding contexts for words from Arabic text corpora. Supports exact and partial matching for diacritics and letters.

## Features

- 📝 **Extract Contexts**: Extract surrounding contexts for words
- 🔍 **Exact Matching**: Exact matching for diacritics and letters
- 🔎 **Partial Matching**: Partial matching for diacritics and exact for letters
- 📚 **Multiple Corpus Support**: Process large corpora
- 📊 **Excel Export**: Export results in Excel format

## Installation

### Requirements

- Python 3.7 or later
- openpyxl (for Excel export)

### Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/ayzem88/context-extractor.git
cd context-extractor
```

2. Install requirements:
```bash
pip install openpyxl
```

## Usage

### Version 0.1

```bash
python "0.1 الإصدار/سياقات مع مصادر مرة واحدة في إكسل.py"
```

### Version 0.2 - Exact Matching

```bash
python "0.2 الإصدار/السياقات - مطابقة تامة التشكيل والحروف.py"
```

### Version 0.2 - Partial Matching

```bash
python "0.2 الإصدار/السياقات - مطابقة جزئية للتشكيل وتامة للحروف.py"
```

## Project Structure

```
context-extractor/
├── 0.1 الإصدار/
│   ├── سياقات مع مصادر مرة واحدة في إكسل.py
│   └── المدونة/
├── 0.2 الإصدار/
│   ├── السياقات - مطابقة تامة التشكيل والحروف.py
│   ├── السياقات - مطابقة جزئية للتشكيل وتامة للحروف.py
│   ├── الألفاظ.txt
│   └── المدونة/
│       └── [Corpus files]
```

## Main Files

- **السياقات - مطابقة تامة التشكيل والحروف.py**: Exact matching
- **السياقات - مطابقة جزئية للتشكيل وتامة للحروف.py**: Partial matching

## Important Notes

⚠️ **Note**: 
- Place words to search for in `الألفاظ.txt` file
- Place corpus files in `المدونة/` folder
- Results are saved in `النتائج/` folder

## Future Development

- [ ] Graphical user interface (GUI)
- [ ] Performance improvements for large corpora
- [ ] Support for more matching options
- [ ] Export in multiple formats

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## License

This project is intended for academic and research use.

## Development Approach

I adopt the Vibe Coding paradigm in my software projects: rather than writing every line manually, I direct AI models with clear natural-language descriptions of the desired functionality, then evaluate and refine the generated code.

This approach accelerates prototype and module creation, allowing me to focus more on concept and design than on low-level implementation details.

In this repository you'll find tools and projects developed with this mindset — feel free to explore and contribute.

## Developer

Developed by **Ayman Atieb ben NJi** ([ayzem88](https://github.com/ayzem88))

</div>

