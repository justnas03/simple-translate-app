import deep_translator
from deep_translator import GoogleTranslator

# print(googletrans.LANGUAGES)



t = GoogleTranslator()
a = t.translate("con mèo", src="vi", dest="en")

print(a)
