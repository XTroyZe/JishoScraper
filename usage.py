import jishoscraper as js


kanji = js.Kanji('中')

print("MEANING: ")
print(kanji.meaning())
print()

print("READINGS: ")
print(kanji.readings())
print()

print("READING COMPOUNDS:")
print(kanji.reading_compounds())
print()

print("RADICAL: ")
print(kanji.radical())
print()

print("PARTS: ")
print(kanji.parts())
print()

print("NUM OF STROKES: ")
print(kanji.num_strokes())
print()

print("PATH TO STROKE DIAGRAM: ")
print(kanji.stroke_diagram())
print()