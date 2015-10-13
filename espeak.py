#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess, unidecode, pdb

#language= u'fr'
#word = u'été'

def espeak(language, word):
	commandString = u'LC_ALL=en_US.UTF8 espeak -q -v '+language+u' --ipa "'+word+u'"'
	test = subprocess.check_output(commandString, shell=True).decode('utf-8')
	test_edited = test.replace(u'ˈ',u'').replace(' ','').replace(u'\n','').replace(u'-','')
	unidecoded = unidecode.unidecode(test_edited) 
	return({'original_unicode':word,'transcription':test_edited, 'length_unidecode':len(unidecoded), 'unidecoded':unidecoded})



#speak_test =  espeak(language, word)
#print espeak_test
#print espeak_test['original_unicode']

#need to confirm that utf8 symbols are really being handled correctly in SRILM—clearly there are dragons here


#should be able to see in the character-based models if single UTF-8 characters are being treated as such