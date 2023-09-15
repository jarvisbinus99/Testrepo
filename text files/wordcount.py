def count_words(file_name):
    with open(file_name,"r") as a:
        a_data=a.read()
        a_list=a_data.lower().split()
        a_list.sort()
        frequent_words={}
        for i in a_list :
            if i.isalpha():
                count=a_list.count(i)
                frequent_words[i]=count

    for x in frequent_words:
        print(x,":",frequent_words[x])
file_name=r"C:\Users\hp\Desktop\practice exercises\Python-S1\replace.txt"
count_words(file_name)
