from django.shortcuts import render
import random

first_names=["nika","data","gio","toma","mate","levani","irakli","dachi","tazo","saba"]
last_names=["mekvabishvili","gogaladze","surmava","kurtsikidze","bakhia","barnovi","khundadze","qenkadze","nozadze"]
courses=["1","2","3","4"]
def get_random_students(studentebis_raodenoba):
    students=[]
    for i in range(studentebis_raodenoba):
        first_name=random.choice(first_names)
        last_name=random.choice(last_names)
        course=random.choice(courses)
        gpa=round(random.uniform(1.0,4.0),0)
        students.append({
            'name' : f"{first_name} {last_name}",
            'course':course,
            'gpa':gpa,
        })
    return students


def main_page_view(request):
    selected_student=random.choice(get_random_students(100))
    context={
        'student':selected_student
    }
    return render(request,"main_page.html",context)

def students_page_view(request):
    all_students=get_random_students(100)
    context={
        'students':all_students
    }
    return render(request,"students_page.html",context)