#1
list1 = [1,2,3,4,5,6,7,9,10]
list2 = [a for a in list1]
print list2

#2
list3 = [i**(1./2) for i in list1]
print list3

#3
list4 = [i**2 for i in list1]
print list4

#4
list5 = [i for i in list1 if i%2==0]
print list5


#5
list6 = [i for i in list1 if i%2==1]
print list6

#6
listpos = [1,2,3,-1,-2,-3]
list7 = [i for i in listpos if i>0]
print list7

#7
numlist = [10, 15, 18, 22, 78, 100, 66]
numlist2 = ([str(j) for i in numlist for j in range(2,i) if i%j==0])
print numlist2

#8
sent = "hi the sky seems cloudy today"
sentTokens=sent.split(" ")
print sentTokens

#using list
list8 = [(i+" = "+str(len(i))) for i in sentTokens if (i != "the")]
print list8
#using set
list9 = {(i+" = "+str(len(i))) for i in sentTokens if (i != "the")}
print list9

#using dictionary
list10 = {i:len(i) for i in sentTokens if (i != "the")}
print list10

#9

word = "AaronE"
vowels="aeiou"
listset = {i for i in word.lower() if (i in vowels)}
print listset
print type(listset)

#10
num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
num1 = [i*2 if i%2==0 else i-i*2 for i in num]
print num1


#11
sent1 = "the quick brown fox jumps over the lazy dog"
sent2=''.join([chr(ord(i)+1) if i != "z" and i != " " else i for i in sent1])
print sent2

#12
num2 = [i for i in range(1,1000) if (i%7==0)]
print num2

#13

num3 = [i for i in range(1,1000) if "3" in str(i)]
print num3

#14

#a = raw_input("Enter the string ")
a="it was sunny day"
b = [i for i in a if i==" "]
print len(b)

#15

vowels1 = "it was sunny day"

text1 = ''.join([i for i in vowels1 if i not in vowels])
print text1

#16

class1 = ["Aaron" ,"Aakash" ,"Roge" , "hell" ,"neymar"]
class2 = [i for i in class1 if len(i)<5]
print class2

#17

word1 = "it was sunny day"
sentTokens1=word1.split(" ")
word2 = {i:len(i) for i in sentTokens1}
print word2

#18

text2 =[i for i in range(1,1001) for j in range(2,10) if i%j==0]
print set(text2)


#19
#using list
text3 =[j for i in range(1,1001) for j in range(2,10) if i%j==0]
print set(text3)

#using dictionary
text3 ={i:j for i in range(1,1001) for j in range(2,10) if i%j==0}
print text3