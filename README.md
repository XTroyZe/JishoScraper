# JishoScraper
## A simple scraper for Jisho.org in Python
*This library and its author(s) are not affiliated/associated with jisho.org in any way.*

**NOTE: THIS PROJECT IS INCOMPLETE**

## Usage
```python
kanji = js.Kanji('中')
```
Creates an object from the Kanji.
## Methods
**Get the meanings of the kanji** (comma separated, returns a list):
```python
kanji.meaning()
```
```python
['in', 'inside', 'middle', 'mean', 'center']
```
----
**Get the readings of the kanji** (returns a dict with two keys: 'onyomi' and 'kunyomi' where the values are a list of the readings, returns *None* if not available):
```python
kanji.readings()
```
```python
{'onyomi': ['チュウ'], 'kunyomi': ['なか', ' うち', ' あた.る']}
```
----
**Get the On and Kun reading compounds** (returns a dict with two keys: 'On' and 'Kun' where the values are a list containing the relevant words. Each word is split into a dict with three keys: 'word', 'furigana' and 'definition' which is self explanatory(see example below or website). returns *None* if not available.)
```python
print(kanji.reading_compounds())
```
```python
{'On': [{'word': '中', 'furigana': 'チュウ', 'definition': 'medium, average, middle, moderation, middle school, China, volume two (of three), during (a certain time when one did or is doing something), under (construction, etc.), while, in, out of, of the'}, 
{'word': '中央線', 'furigana': 'チュウオウセン', 'definition': 'Chuo Line (central railway line in Tokyo)'}, 
{'word': '宮中', 'furigana': 'キュウチュウ', 'definition': 'imperial court'}, 
{'word': '訪中', 'furigana': 'ホウチュウ', 'definition': 'visit to China'}],

'Kun': [{'word': '中', 'furigana': 'なか', 'definition': 'inside, in, among, within, center (centre), middle, during, while'}, 
'word': '中島', 'furigana': 'なかじま', 'definition': 'island in a pond or river'}, 
{'word': '野中', 'furigana': 'のなか', 'definition': 'in the middle of a field'}, 
{'word': '火中', 'furigana': 'かちゅう', 'definition': 'in the fire, in the flames, burning (something)'}, 
{'word': '内', 'furigana': 'うち', 'definition': 'inside, within, while, among, amongst, between, we, our, my spouse, imperial palace grounds, emperor, I, me'}, 
{'word': '此の内', 'furigana': 'このうち', 'definition': 'meanwhile, the other day, recently'}, 
{'word': '腹の中', 'furigana': 'はらのなか', 'definition': "in the belly, in one's heart of hearts"}, 
{'word': '当たる', 'furigana': 'あたる', 'definition': 'to be hit, to strike, to touch, to be in contact, to be affixed, to be equivalent to, to be applicable, to apply to, to be right on the money (of a prediction, criticism, etc.), to be selected (in a lottery, etc.), to win, to be successful, to go well, to be a hit, to face, to confront, to lie (in the direction of), to undertake, to be assigned, to be stricken (by food poisoning, heat, etc.), to be afflicted, to be called on (e.g. by a teacher), to treat (esp. harshly), to lash out at, to be unnecessary, to be hitting well, to be on a hitting streak, (in fishing) to feel a bite, (of fruit, etc.) to be bruised, to spoil, to feel (something) out, to probe into, to check (i.e. by comparison), to shave, to be a relative of a person, to stand in a relationship'}]}
```
----
**Get the radical and radical meaning of the kanji** (returns a dict with keys 'radical' and 'meaning' with the radical and meaning as values respectively. Values are assigned to *None* if not avaiable)
```python
kanji.radical()
```
```python
{'radical': '丨', 'meaning': 'line'}
```
----
**Get the parts of the kanji** (returns list of all the parts of the kanji, returns *None* if not available)
```python
kanji.parts()
```
```python
['｜', '口']
```
----
**Get the number of strokes** (returns an int for the number of strokes of the kanji)
```python
kanji.num_strokes()
```
```python
4
```
----
**Get the path to the stroke order diagram (CREDIT: https://github.com/cayennes/kanji-colorize)** (returns /kanji/\*hexcode\*.svg)
```python
kanji.stroke_diagram()
```
```python
/kanji/04e2d.svg
```
----
Thank you for viewing my project! I am grateful for any suggestions, improvements, or general feedback on this project!

### To do ##









