# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateContactForm
from django.http import HttpResponseRedirect
from .models import Contact


def index(request):
    if request.method == 'POST':
        print("Got post request")
        # create a form instance and populate it with data from the request:
        form = CreateContactForm(request.POST)

        print(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CreateContactForm(label_suffix="")

    return render(request, 'createContact.html', {'form': form})


def thanks(request):
    print(list(Contact.objects.all()))

    return render(request, 'thanks.html', {})


def fixtures(request):
    print("Fixtures")

    myData = [
        [
            [{"name": "Paddy C", "id": "erik-zettersten", "seed": 1, "displaySeed": "D1", "score": 47},
             {"name": "Andrew Miller", "id": "andrew-miller", "seed": 2}],
            [{"name": "James Coutry", "id": "james-coutry", "seed": 3},
             {"name": "Sam Merrill", "id": "sam-merrill", "seed": 4}],
            [{"name": "Anothy Hopkins", "id": "anthony-hopkins", "seed": 5},
             {"name": "Everett Zettersten", "id": "everett-zettersten", "seed": 6}],
            [{"name": "John Scott", "id": "john-scott", "seed": 7},
             {"name": "Teddy Koufus", "id": "teddy-koufus", "seed": 8}],
            [{"name": "Arnold Palmer", "id": "arnold-palmer", "seed": 9},
             {"name": "Ryan Anderson", "id": "ryan-anderson", "seed": 10}],
            [{"name": "Jesse James", "id": "jesse-james", "seed": 1},
             {"name": "Scott Anderson", "id": "scott-anderson", "seed": 12}],
            [{"name": "Josh Groben", "id": "josh-groben", "seed": 13},
             {"name": "Sammy Zettersten", "id": "sammy-zettersten", "seed": 14}],
            [{"name": "Jake Coutry", "id": "jake-coutry", "seed": 15},
             {"name": "Spencer Zettersten", "id": "spencer-zettersten", "seed": 16}]
        ],
        [
            [{"name": "Erik Zettersten", "id": "erik-zettersten", "seed": 1},
             {"name": "James Coutry", "id": "james-coutry", "seed": 3}],
            [{"name": "Anothy Hopkins", "id": "anthony-hopkins", "seed": 5},
             {"name": "Teddy Koufus", "id": "teddy-koufus", "seed": 8}],
            [{"name": "Ryan Anderson", "id": "ryan-anderson", "seed": 10},
             {"name": "Scott Anderson", "id": "scott-anderson", "seed": 12}],
            [{"name": "Sammy Zettersten", "id": "sammy-zettersten", "seed": 14},
             {"name": "Jake Coutry", "id": "jake-coutry", "seed": 15}]
        ],
        [
            [{"name": "Erik Zettersten", "id": "erik-zettersten", "seed": 1},
             {"name": "Anothy Hopkins", "id": "anthony-hopkins", "seed": 5}],
            [{"name": "Ryan Anderson", "id": "ryan-anderson", "seed": 10},
             {"name": "Sammy Zettersten", "id": "sammy-zettersten", "seed": 14}]
        ],
        [
            [{"name": "Erik Zettersten", "seed": 1}, {"name": "Ryan Anderson", "seed": 10}]
        ],
        [
            []
        ]
    ]

    myData2 = [
        [
            [{"name": "Erik Zettersten", "id": "erik-zettersten", "seed": 1, "displaySeed": "D1", "score": 47},
             {"name": "Andrew Miller", "id": "andrew-miller", "seed": 2}],
            [{"name": "James Coutry", "id": "james-coutry", "seed": 3},
             {"name": "Sam Merrill", "id": "sam-merrill", "seed": 4}],
            [{"name": "Anothy Hopkins", "id": "anthony-hopkins", "seed": 5},
             {"name": "Everett Zettersten", "id": "everett-zettersten", "seed": 6}],
            [{"name": "John Scott", "id": "john-scott", "seed": 7},
             {"name": "Teddy Koufus", "id": "teddy-koufus", "seed": 8}],
            [{"name": "Arnold Palmer", "id": "arnold-palmer", "seed": 9},
             {"name": "Ryan Anderson", "id": "ryan-anderson", "seed": 10}],
            [{"name": "Jesse James", "id": "jesse-james", "seed": 1},
             {"name": "Scott Anderson", "id": "scott-anderson", "seed": 12}],
            [{"name": "Josh Groben", "id": "josh-groben", "seed": 13},
             {"name": "Sammy Zettersten", "id": "sammy-zettersten", "seed": 14}],
            [{"name": "Jake Coutry", "id": "jake-coutry", "seed": 15},
             {"name": "Spencer Zettersten", "id": "spencer-zettersten", "seed": 16}]
        ],
        [
            [{"name": "Erik Zettersten", "id": "erik-zettersten", "seed": 1},
             {"name": "James Coutry", "id": "james-coutry", "seed": 3}],
            [{"name": "Anothy Hopkins", "id": "anthony-hopkins", "seed": 5},
             {"name": "Teddy Koufus", "id": "teddy-koufus", "seed": 8}],
            [{"name": "Ryan Anderson", "id": "ryan-anderson", "seed": 10},
             {"name": "Scott Anderson", "id": "scott-anderson", "seed": 12}],
            [{"name": "Sammy Zettersten", "id": "sammy-zettersten", "seed": 14},
             {"name": "Jake Coutry", "id": "jake-coutry", "seed": 15}]
        ],
        [
            [{"name": "Erik Zettersten", "id": "erik-zettersten", "seed": 1},
             {"name": "Anothy Hopkins", "id": "anthony-hopkins", "seed": 5}],
            [{"name": "Ryan Anderson", "id": "ryan-anderson", "seed": 10},
             {"name": "Sammy Zettersten", "id": "sammy-zettersten", "seed": 14}]
        ],
        [
            [{"name": "Erik Zettersten", "id": "erik-zettersten", "seed": 1},
             {"name": "Ryan Anderson", "id": "ryan-anderson", "seed": 10}]
        ],
        [
            [{"name": "Erik Zettersten", "id": "erik-zettersten", "seed": 1}]
        ]
    ];
    print("below is myData1")
    print(myData)
    # print("below is 222")
    #
    # dict = {"myData":myData}
    #
    all_people = Contact.objects.all()
    # print("///////////////////////")
    # print(len(all_people))
    # print(type(all_people[1]))
    # ps = str(all_people[1])
    # print(ps)
    # print(type(ps))
    # round 1
    count = 3
    new_arr = []
    salesforceData = []
    for person in all_people:
        if len(new_arr) == 2:
            salesforceData.append(new_arr)
            new_arr = []
        newobj = {"name": str(person)}
        new_arr.append(newobj)

        # print(person)
    print("///////////")
    print(salesforceData)
    half = int(len(all_people) / 2)
    print(half)
    halfAlist = all_people[::5]
    print("halfAlist")
    print(halfAlist)
    round2 = []

    for person in halfAlist:
        if len(new_arr) == 2:
            round2.append(new_arr)
            new_arr = []
        newobj = {"name": str(person)}
        new_arr.append(newobj)

    print("round2")
    print(round2)
    round3 = []
    round4 = []
    round5 = []
    tiptop = []
    tiptop.append(salesforceData)
    # tiptop.append(round2)
    salesforceData.append(round2)
    salesforceData2 = salesforceData
    print("salesforceData")
    print(salesforceData)
    print("salesforceData2")
    print(salesforceData2)

    topLevelArr = []
    topLevelArr.append(salesforceData)
    # print(topLevelArr)
    myData = topLevelArr
    # myData = [[
    #     [{"name": "Erik Zettersten", "id": "erik-zettersten", "seed": 1, "displaySeed": "D1", "score": 47},
    #      {"name": "Andrew Miller", "id": "andrew-miller", "seed": 2}],
    #     [{"name": "James Coutry", "id": "james-coutry", "seed": 3},
    #      {"name": "Sam Merrill", "id": "sam-merrill", "seed": 4}],
    #     [{"name": "Anothy Hopkins", "id": "anthony-hopkins", "seed": 5},
    #      {"name": "Everett Zettersten", "id": "everett-zettersten", "seed": 6}],
    #     [{"name": "John Scott", "id": "john-scott", "seed": 7},
    #      {"name": "Teddy Koufus", "id": "teddy-koufus", "seed": 8}],
    #     [{"name": "Arnold Palmer", "id": "arnold-palmer", "seed": 9},
    #      {"name": "Ryan Anderson", "id": "ryan-anderson", "seed": 10}],
    #     [{"name": "Jesse James", "id": "jesse-james", "seed": 1},
    #      {"name": "Scott Anderson", "id": "scott-anderson", "seed": 12}],
    #     [{"name": "Josh Groben", "id": "josh-groben", "seed": 13},
    #      {"name": "Sammy Zettersten", "id": "sammy-zettersten", "seed": 14}],
    #     [{"name": "Jake Coutry", "id": "jake-coutry", "seed": 15},
    #      {"name": "Spencer Zettersten", "id": "spencer-zettersten", "seed": 16}],[ {"name" : "Erik Zettersten", "id" : "erik-zettersten", "seed" : 1, "displaySeed": "D1", "score" : 47 }, {"name" : "Andrew Miller", "id" : "andrew-miller", "seed" : 2} ],
    #
    # 			]]
    # people_persons = []
    # people_persons.append(myData)
    #
    #
    # myData2 = [
    #     [
    #         [{"name": "Erik Zettersten", "id": "erik-zettersten", "seed": 1, "displaySeed": "D1", "score": 47},
    #          {"name": "Andrew Miller", "id": "andrew-miller", "seed": 2}],
    #         [{"name": "James Coutry", "id": "james-coutry", "seed": 3},
    #          {"name": "Sam Merrill", "id": "sam-merrill", "seed": 4}],
    #
    #     ],
    #     [
    #         [{"name": "Erik Zettersten", "id": "erik-zettersten", "seed": 1},
    #          {"name": "James Coutry", "id": "james-coutry", "seed": 3}],
    #
    #     ],
    #     [
    #         [{"name": "James Coutry", "id": "james-coutry", "seed": 3}],
    #     ]
    # ];
    # print("myData")
    # print(myData2)
    print("tiptop")
    print(tiptop)
    # dict = {"myData": myData}
    # dict = {"myData": myData2}
    dict = {"myData": tiptop}

    return render(request, 'fixtures.html', {"dict2": dict})


def players(request):
    print(list(Contact.objects.all()))

    all_people = Contact.objects.all()
    persons = []
    for person in all_people:
        persons.append(person)
        # print(person)

    # print(persons)

    dict = {"persons": persons}

    return render(request, 'players.html', {"dict2": dict})
