#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess, unidecode, pdb

#language= u'en'
#word = u'pronunciation'

def espeak(language, word):	
	commandString = u'LC_ALL=en_US.UTF8 espeak -q -v '+language+u' --ipa=3 "'+word+u'"'
	test = subprocess.check_output(commandString, shell=True).decode('utf-8')
	test_edited = test.replace(u'ˈ',u'').replace(' ','').replace(u'\n','').replace(u'-','').replace(u'ˌ',u'').replace(u'ː',u'')
	test_array = [x for x in test_edited.split('_') if x is not None and x is not '']	
	return({'word':word, 'transcription':test_array, 'nSounds':len(test_array)})

#print u''.join(espeak(language, word)).encode('utf-8')

#espeak_test =  espeak(language, word)
#print espeak_test
#print espeak_test['transcription']

#need to confirm that utf8 symbols are really being handled correctly in SRILM—clearly there are dragons here

#should be able to see in the character-based models if single UTF-8 characters are being treated as such