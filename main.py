import puzzleclass

word_list = ['ADD','ADO','AGE','AGO','AID','AIL','AIM','AIR','AND',
'ANY','APE','APT','ARC','ARE','ARK','ARM','ART','ASH','ASK','AUK',
'AWE','AWL','AYE','BAD','BAG','BAN','BAT','BEE','BOA','EAR','EEL',
'EFT','FAR','FAT','FIT','LEE','OAF','RAT','TAR','TIE']
x = puzzleclass.puzzle(word_list)
print(x.ID)
x.insertVariable("A1","TIE")
x.insertVariable("A2","ADD")
x.insertVariable("D1","TAR")
print(x.ID)
u = x.checkUnassigned()
print(u)
#print(x.ID)