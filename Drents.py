# Can we make Xander sound Drents?

import re
import os

def instant_Drents(text):
	# This function takes in a Dutch text and returns the text with a Drents accent
	# This is meant as a fun exercise to practise regular expression and has no
	# intention to make fun of or insult any person speaking Drents.
	# dijk = diek --- 'ij' or 'y' -> 'ie'
	# paard = peerd --- 'aa'+medeklinker -> 'ee'
	# door = deur --- 'oo'+medeklinker -> 'eu' 

	y_pattern = (r'ij|y') #ij or y
	aa_pattern = (r'aa')
	oo_pattern = (r'oo')
	y_replace = ('ie')
	aa_replace = ('ee')
	oo_replace = ('eu')

	text = re.sub(y_pattern, y_replace, text)
	text = re.sub(aa_pattern, aa_replace, text)
	text = re.sub(oo_pattern, oo_replace, text)

	return text


if __name__ == "__main__":



	sent = 'Er loopt een paard over de dijk.'
	sent2 =	"""
		Dan komt haar eerste minnaar -- die vroeger klerk was aan 't kopieboek, 
		maar nu schatryk -- op-eens terug, en trouwt haar.
		"""
	
	drents1 = instant_Drents(sent)
	drents2 = instant_Drents(sent2)

	items_to_speak = ["Nederlands", sent, "Drents", drents1]

	for item in items_to_speak:
		bash_command = "say -v Xander {0}".format(item)

		os.system(bash_command)