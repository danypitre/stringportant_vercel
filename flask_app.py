import random
import csv
from flask import *
from random import randint
word_list = []

with open('words.csv', 'r') as words:
    reader = csv.reader(words)

    for row in reader:
        word_list.append("" + row[0] + "")


new_list = ', '.join(str(x) for x in word_list)
splitted_list = new_list.split("'")


fname_list = []

with open('fname.csv', 'r') as fname:
    reader = csv.reader(fname)

    for row in reader:
        fname_list.append("" + row[0] + "")


fname_new_list = ', '.join(str(x) for x in fname_list)
fname_splitted_list = fname_new_list.split("'")


lname_list = []

with open('lname.csv', 'r') as lname:
    reader = csv.reader(lname)

    for row in reader:
        to_add = row[0]
        to_add = to_add.lower()
        to_add = to_add[0].upper() + to_add[1:]
        lname_list.append("" + to_add + "")


lname_new_list = ', '.join(str(x) for x in lname_list)
lname_splitted_list = lname_new_list.split("'")


app = Flask(__name__)

app.config['SECRET_KEY'] = 'salkdh92rh3kul2y839dhdhnuxe783290xyred389rvb81ry481'


@app.route('/', methods=['GET', 'POST'])
@app.route('/words', methods=['GET', 'POST'])
def words():
    words_length = len(word_list)
    print(words_length)

    requestList = []
    length = 0
    start = 0
    finish = 58000

    if request.method == 'POST':
        number = request.form.get("number")
        if int(number) <= 0:
            flash("Number of words must be greater than zero (0)", category='error')
            return redirect('/')

        elif int(number) >= 1000000:
            flash("The maximum amount of words is 999 999", category='error')
            return redirect('/')

        language = request.form.get("language")
        caps = request.form.get("caps")
        letter = request.form.get("letter")
        duplicate = request.form.get("duplicate")
        array_type = request.form.get("arrayType")
        print(letter, caps, duplicate)

        if letter != 'All leters' and duplicate == 'on':
            amount = 0
            checked_first = False
            checked_last = False
            while checked_first == False and checked_last == False:
                while checked_first == False:
                    for w in word_list:
                        if w[0].upper() == letter:
                            start = word_list.index(w)
                            checked_first = True
                            print("START: " + str(start))
                            break
                while checked_last == False:
                    for w in range(start, 60000):
                        word_to_check = word_list[w]
                        print(word_to_check)
                        if word_to_check[0].upper() != letter:
                            finish = word_list.index(word_to_check) - 1
                            checked_last = True
                            print("LAST: " + str(finish))
                            break

            print(word_list[start], word_list[finish])

            for w in word_list:
                if w[0].upper() == letter:
                    amount += 1
            if amount < int(number):
                number = str(amount)

        i = 0

        while i < int(number):
            print("tried")
            tried = []
            selector = random.randint(start, finish)
            if selector in tried:
                continue

            word = word_list[selector]
            if duplicate != 'on' and letter == 'All leters':
                if caps != 'on':
                    requestList.append(word)
                elif caps == 'on':
                    requestList.append(word.upper())

                i += 1

            elif duplicate == 'on' and letter == 'All leters':
                tried.append(selector)
                not_in = False

                while not_in == False:
                    if word in requestList:
                        word = word_list[random.randint(0, 58000)]

                    else:
                        not_in = True
                        if caps != 'on':
                            requestList.append(word)
                        else:
                            requestList.append(word.upper())
                        i += 1

            elif duplicate == 'on' and letter != 'All leters':
                tried.append(selector)

                not_in = False
                letter_check = False
                while not_in == False and letter_check == False:
                    if word in requestList:
                        word = word_list[random.randint(0, 58000)]
                    else:
                        not_in = True
                        if word[0].upper() == letter:
                            if caps != 'on':
                                requestList.append(word)
                            else:
                                requestList.append(word.upper())
                            letter_check = True
                            i += 1
                        else:
                            word = word_list[random.randint(0, 58000)]
            elif duplicate != 'on' and letter != 'All leters':
                letter_check = False
                while letter_check == False:
                    if word[0].upper() == letter:
                        if caps != 'on':
                            requestList.append(word)
                        else:
                            requestList.append(word.upper())
                        letter_check = True
                        i += 1
                    else:
                        word = word_list[random.randint(0, 58000)]
            length = len(requestList)

        if language == 'python' or language == 'js':
            if array_type == 'dictionnary':
                dict_list = ''
                count = 1
                for i in requestList:
                    if count != len(requestList):
                        dict_list = dict_list + \
                            str(count) + ":" + i + "," + " "
                    else:
                        dict_list = dict_list + str(count) + ":" + i

                    count += 1
                requestList = "{" + dict_list + "}"

        if language == 'c#' or language == 'c':
            requestList = "{" + ", ".join(repr(e) for e in requestList) + "}"
        if language == 'php':
            requestList = 'array(' + ", ".join(repr(e)
                                               for e in requestList) + ")"

    return render_template("words.html", list=requestList, length=length, option='words')


@app.route("/numbers", methods=["GET", "POST"])
def numbers():
    requestList = []

    if request.method == 'POST':
        length = request.form.get("number")
        language = request.form.get("language")
        only = request.form.get("only")

        digit = request.form.get("digit")

        if int(length) <= 0:
            flash("Number of words must be greater than zero (0)", category='error')
            return redirect('/')

        elif int(length) >= 5000000:
            flash("The maximum amount of numbers is 4 999 999", category='error')
            return redirect('/')

        # default 1 digit no limit

        if only == 'only':
            for i in range(0, int(length)):
                count = 0
                temp = ''
                while count < int(digit):
                    if temp == '':
                        rnd_digit = random.randint(1, 9)
                    else:
                        rnd_digit = random.randint(0, 9)

                    temp = temp + str(rnd_digit)
                    count += 1
                requestList.append(int(temp))
        elif only == 'upto':
            for i in range(0, int(length)):
                count = 0
                max = random.randint(1, int(digit))
                temp = ''
                while count < max:
                    if temp == '':
                        rnd_digit = random.randint(1, 9)
                    else:
                        rnd_digit = random.randint(0, 9)

                    temp = temp + str(rnd_digit)
                    count += 1
                requestList.append(int(temp))

    return render_template("numbers.html", list=requestList, option='numbers', length=len(requestList))


@app.route("/names", methods=["GET", "POST"])
def names():
    requestList = []

    if request.method == 'POST':
        language = request.form.get("language")
        number = request.form.get("number")

        for i in range(0, int(number)):
            rnd_number_fname = random.randint(0, 999)
            rnd_number_lname = random.randint(0, 503)
            name = fname_list[rnd_number_fname] + \
                " " + lname_list[rnd_number_lname]
            requestList.append(name)

        if language == 'c#' or language == 'c':
            requestList = "{" + ", ".join(repr(e) for e in requestList) + "}"
        if language == 'php':
            requestList = 'array(' + ", ".join(repr(e)
                                               for e in requestList) + ")"
    list_len = len(requestList)

    return render_template("names.html", list=requestList, length=list_len, option='names')


if (__name__ == '__main__'):
    app.run()
