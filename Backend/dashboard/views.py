from django.shortcuts import render, redirect
from urllib import request
from django.contrib.auth.models import User
from django.db import connection
import json
from django.http import JsonResponse
# import django.db
# from dashboard.models import MyModel
# Create your views here.

def HOME(request):
    print(1)
    return render(request, "home.html")

def insurance_details(request):
    print(3 ) 
    return render(request, "insurance_details.html")


# def doctor_api(request):
    

#     print(models)
#     dd = {}

#     return JsonResponseon(dd)


def doctor_details(request):
    asdas = dict()

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Doctors")
        rows = cursor.fetchall()


    for j,rr in enumerate(rows):
        dd = {}
        for i,data in enumerate(rr):
            dd[i] = data
            
        asdas[j] = dd
        print(asdas)

    return JsonResponse(asdas)

def appointmnet_details(request):
    asdas = dict()

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Appointments")
        rows = cursor.fetchall()

    for j,rr in enumerate(rows):
        dd = {}
        for i,data in enumerate(rr):
            dd[i] = data
            
        asdas[j] = dd
        # print(asdas)

    return JsonResponse(asdas)

def Insurance_Plans_details(request):
    asdas = dict()

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Insurance_Plans")
        rows = cursor.fetchall()

    for j,rr in enumerate(rows):
        dd = {}
        for i,data in enumerate(rr):
            dd[i] = data
            
        asdas[j] = dd
        # print(asdas)

    return JsonResponse(asdas)

def Insurance_Provider_details(request):
    
    asdas = dict()

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Insurance_Provider")
        rows = cursor.fetchall()

    for j,rr in enumerate(rows):
        dd = {}
        for i,data in enumerate(rr):
            dd[i] = data
            
        asdas[j] = dd
        # print(asdas)

    return JsonResponse(asdas)

def Medical_History_details(request):
    asdas = dict()

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Medical_History")
        rows = cursor.fetchall()


    for j,rr in enumerate(rows):
        dd = {}
        for i,data in enumerate(rr):
            dd[i] = data
            
        asdas[j] = dd
        # print(asdas)

    return JsonResponse(asdas)

def Patients_details(request):
    asdas = dict()

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Patients")
        rows = cursor.fetchall()


    for j,rr in enumerate(rows):
        dd = {}
        for i,data in enumerate(rr):
            dd[i] = data
            
        asdas[j] = dd
        # print(asdas)

    return JsonResponse(asdas)

def Symptom_Specialities_details(request):
    asdas = dict()

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Symptom_Specialities")
        rows = cursor.fetchall()


    for j,rr in enumerate(rows):
        dd = {}
        for i,data in enumerate(rr):
            dd[i] = data
            
        asdas[j] = dd
        # print(asdas)

    return JsonResponse(asdas)

def Users_details(request):
    asdas = dict()

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Users")
        rows = cursor.fetchall()


    for j,rr in enumerate(rows):
        dd = {}
        for i,data in enumerate(rr):
            dd[i] = data
            
        asdas[j] = dd
        # print(asdas)

    return JsonResponse(asdas)    