# Can we make Xander sound Drents?

import re
import os

def to_Drents(text):
	# This function takes in a Dutch text and returns the text with a Drents accent
	# This is meant as a fun exercise to practise regular expression and has no
	# intention to make fun of or insult any person speaking Drents.
	# dijk = diek --- 'ij' or 'y' -> 'ie'
	# paard = peerd --- 'aa'+medeklinker -> 'ee'
	# door = deur --- 'oo'+medeklinker -> 'eu' 

	y_pattern = (r'ij|y|ei') #ij or y
	aa_pattern = (r'aa')
	oo_pattern = (r'oo')
	y_replace = ('ie')
	aa_replace = ('ee')
	oo_replace = ('eu')

	text = re.sub(y_pattern, y_replace, text)
	text = re.sub(aa_pattern, aa_replace, text)
	text = re.sub(oo_pattern, oo_replace, text)
	
	return text

def instant_Drents(sent):
	drents = to_Drents(sent.lower())
	items_to_speak = ["Nederlands", sent, "Drents", drents]

	for item in items_to_speak:
		bash_command = "say -v Xander {0}".format(item)

		os.system(bash_command)	



if __name__ == "__main__":

	sent = 'Er loopt een paard over de dijk.'
	sent2 =	'Mag ik van jou de krant?'
	sent3 = "Er staat een paard in de wei"


	instant_Drents(sent)
	instant_Drents(sent2)
	instant_Drents(sent3)