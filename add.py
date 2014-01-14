import os, shutil, string
from sets import Set


LocalDictionary = os.path.join(os.getenv("HOME"), 'Library/Spelling/LocalDictionary')
HostedDictionaryPath = os.path.join(os.path.dirname(__file__), 'dictionaries') 


# Make initial backup of old file
if not os.path.exists(LocalDictionary + '.backup'):
	shutil.copyfile(LocalDictionary, LocalDictionary + '.backup')


# Read LocalDictionary
d = Set(map(string.strip, open(LocalDictionary).readlines()))
length = len(d)

# Add words
for fileName in os.listdir(HostedDictionaryPath):
	if os.path.isfile(os.path.join(HostedDictionaryPath, fileName)):
		
		print 'Reading %s' % (fileName)

		# Read new words
		newWords = map(string.strip, open(os.path.join(HostedDictionaryPath, fileName)).readlines())

		# Remove comments and empty lines
		newWords = [x for x in newWords if not x.startswith('#') or x != '']
	
		# Update set
		d.update(Set(newWords))

# Save back
LocalDictionaryFile = open(LocalDictionary, 'w')
LocalDictionaryFile.write("\n".join(d))
LocalDictionaryFile.close()

print 'Added %s words to your dictionary.' % (len(d) - length)