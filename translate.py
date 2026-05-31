from googletrans import Translator, LANGUAGES

translator = Translator()

def TransLate(str, lang):
    try:
        code = CodeLang(lang).lower()
        result = translator.translate(str, dest=code)
        return result.text
    except Exception as e:
        return f"Помилка перекладу: {e}"

def LangDetect(txt):
    try:
        detected = translator.detect(txt)
        return f"Detected(lang={detected.lang}, confidence={detected.confidence})"
    except Exception as e:
        return f"Помилка визначення мови: {e}"

def CodeLang(lang):
    lang = lang.strip()
    if lang.lower() in LANGUAGES:
        return LANGUAGES[lang.lower()].capitalize()
    for code, name in LANGUAGES.items():
        if name.lower() == lang.lower():
            return code
    return "Мову не знайдено"

# Основна програма
txt = "Доброго дня. Як справи?"
lang = input("Введіть мову перекладу (наприклад: en або English): ")
print(txt)
print(LangDetect(txt))
print(TransLate(txt, lang))
print(CodeLang("en"))
print(CodeLang("English"))