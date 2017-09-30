import nltk
import urllib.request
import ssl

#retrieve the raw data from web and save it as txt
ssl._create_default_https_context = ssl._create_unverified_context
url = urllib.request.urlretrieve("https://raw.githubusercontent.com/AIHackers/DeepLearningStartUp/master/happiness_seg.txt","tt.txt")
#open and read it in python
fr = open("tt.txt","r",encoding="utf-8")
text_test = fr.read()
text_test_str = str(text_test)
fr.close()
#make the raw data as a list, splitted by "space"
wordlist = text_test_str.split(" ")
#to test what it looks like
print (wordlist[:30])
#make adjacent words combine together
twowordslist = []
for j in range(len(wordlist)-1):
    twowordslist.append(wordlist[j]+wordlist[j+1])
#have a check
print (twowordslist[:30])
#check the frequency of each combined word
fdist = nltk.FreqDist(twowordslist)
#make a dictionary which stores frequency as key, combined words as value
dictionaryword = {}
for word in fdist:
    if '，'  in word or '。' in word or '――' in word:
        continue  #first remove “，”，“。”
    dictionaryword[fdist[word]] = word
#check what it looks like
print (dictionaryword)
#create a list with frequency numbers in it and reverse sort the list from highest to lowest
frequencylist = []
for num in dictionaryword:
    frequencylist.append(num)

print (frequencylist)
frequencylist.sort(reverse=True)
print (frequencylist)
#print out the combined word and its correspond frequency by line
for i in frequencylist:
    print (dictionaryword[i], "->", i)

# top 10:
# 的人 -> 921
# 他的 -> 503
# 自己的 -> 479
# 上的 -> 355
# 他们的 -> 334
# 人的 -> 293
# 的时候 -> 261
# 就会 -> 225
# 的东西 -> 207
# 都是 -> 206

