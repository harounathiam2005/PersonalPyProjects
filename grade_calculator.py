# This program will take the number of questions you got right out of the total amount of questions to calculate your
# percentage.

def percentage(x, y):
    div = x / y
    if div < 1:
        ints = [str(i) for i in str(div)]
        items = len(ints)
        if items == 3:
            ints.append('0')
        score = ints[2] + ints[3]
        if int(score) < 60:
            print(score, "% F")
            print("https://www.khanacademy.org/")
        elif 60 <= int(score) < 70:
            print(score, "% D")
            print("https://www.khanacademy.org/")
        elif 70 <= int(score) < 80:
            print(score, "% C")
            print("https://www.khanacademy.org/")
        elif 80 <= int(score) < 90:
            print(score, "% B")
        elif 90 <= int(score) < 100:
            print(score, "% A")
    else:
        ints = [str(i) for i in str(div)]
        items = len(ints)
        if items == 3:
            score = ints[0] + ints[2] + '0'
            print(score, '% A')
        elif items == 4:
            score = ints[0] + ints[2] + ints[3]
            print(score, '% A')
        else:
            if int(ints[4]) > 5:
                int3 = int(ints[3]) + 1
                intt = str(int3)
                intt3 = [intt]
                score = ints[0] + ints[2] + intt3[0]
                print(score, '% A')
            else:
                score = ints[0] + ints[2] + ints[3]
                print(score, '% A')


percentage(29, 40)
