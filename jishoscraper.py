class Kanji:
	def __init__(self, kanji):
		self.kanji = kanji
		url = 'https://jisho.org/search/' + self.kanji + '%20%23kanji'
		import requests
		self.page = requests.get(url)
		from bs4 import BeautifulSoup
		self.soup = BeautifulSoup(self.page.content, 'html.parser')
		self.all_dts = self.soup.find_all('dt')

	def meaning(self):
		main_meanings = self.soup.find('div', attrs={'class': 'kanji-details__main-meanings'})
		return main_meanings.text.strip().split(', ')

	def readings(self):
		self.readingsdict = {'onyomi': None, 'kunyomi': None}
		readings = self.soup.find('div', attrs={'class': 'kanji-details__main-readings'})

		if readings != None:
			onyomiclass = readings.find('dl', attrs={'class': 'dictionary_entry on_yomi'})
			if onyomiclass != None:
				onyomi = onyomiclass.find('dd', attrs={'class': 'kanji-details__main-readings-list'})
				onyomi = onyomi.text.strip().split('、')
				self.readingsdict['onyomi'] = onyomi

			kunyomiclass = readings.find('dl', attrs={'class': 'dictionary_entry kun_yomi'})
			if kunyomiclass != None:
				kunyomi = kunyomiclass.find('dd', attrs={'class': 'kanji-details__main-readings-list'})
				kunyomi = kunyomi.text.strip().split('、')
				self.readingsdict['kunyomi'] = kunyomi

		return self.readingsdict


	def reading_compounds(self):
		self.reading_compounds = {'On': None, 'Kun': None}
		on_reading_compounds_list = []
		kun_reading_compounds_list = []

		compounds_list = self.soup.find('div', attrs={'class': 'row compounds'}).find_all('h2')

		for title in compounds_list:
			if title.text == 'On reading compounds':
				on_reading_compounds = title.find_next_sibling('ul').find_all('li')

				for compound in on_reading_compounds:
					on_compound_elements = compound.text.strip().split('\n')
					on_compound_elements_dict = {'word': on_compound_elements[0].strip(), 'furigana': on_compound_elements[1].strip().strip('【').strip('】'), 'definition': on_compound_elements[2].strip()}

					on_reading_compounds_list.append(on_compound_elements_dict)

			elif title.text == 'Kun reading compounds':
				kun_reading_compounds = title.find_next_sibling('ul').find_all('li')

				for compound in kun_reading_compounds:
					kun_compound_elements = compound.text.strip().split('\n')
					kun_compound_elements_dict = {'word': kun_compound_elements[0].strip(), 'furigana': kun_compound_elements[1].strip().strip('【').strip('】'), 'definition': kun_compound_elements[2].strip()}
					kun_reading_compounds_list.append(kun_compound_elements_dict)

		self.reading_compounds['On'] = on_reading_compounds_list if on_reading_compounds_list else None
		self.reading_compounds['Kun'] = kun_reading_compounds_list if kun_reading_compounds_list else None

		return self.reading_compounds

	def radical(self):
		radical_dict = {'radical': None, 'meaning': None}

		for dt in self.all_dts:
			if dt.text == 'Radical:':
				radical_data = dt.find_next_sibling('dd')
				break
		radical_data_list = radical_data.text.strip().split('\n            \n\n          ')
		radical_dict['radical'] = radical_data_list[1]
		radical_dict['meaning'] = radical_data_list[0]

		return radical_dict

	def parts(self):
		parts_list = []

		for dt in self.all_dts:
			if dt.text == 'Parts:':
				parts_data = dt.find_next_sibling('dd')
				break
		for part in parts_data.find_all('a'):
			parts_list.append(part.text)

		return parts_list if parts_list else None

	def num_strokes(self):
		no_of_strokes = self.soup.find('div', attrs={'class': 'kanji-details__stroke_count'}).find('strong')

		return no_of_strokes.text
			
	def stroke_diagram(self):
		hexcode = str(hex(ord(self.kanji))[2:]).zfill(5)
		path = '/kanji/' + hexcode + '.svg'
		return path





