from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
# Create your views here.

class AboutView(View):
    def get(self,request):
        data = {
            "ID":1,
            "full_name":"Alisha Baiju",
            "title":"FullStack Developer Intern",
            "bio":"A passionate tech enthusiast who is currently working as a developer intern",
            "DOB":"18/03/2004",
            "email":"alishabaiju29@gmail.com",
            "contact":"9778139934",
            "location":"Idukki",
            "GitHub_URL":"https://github.com/in/alishabaiju",
            "Linkedin_URL":"https://linkedin.com/in/alishabaiju"
        }
        
        return JsonResponse(data)
    
class EducationView(View):
    def get(self,request):
        data = {
            "ID":1,
            "institution":"Mangalam College of Engineering",
            "Course":"BTech",
            "University":"KTU",
            "Location":"Kottayam",
            "Starting_year":"2022",
            "Ending_year":"2026",
            "CGPA":"7.89",
            "Description":"gratuate btech student"
        }
        return JsonResponse(data)
    
class ProjectView(View):
    def get(self,request):
        projects =[
            {
                "id": 1,
                "title": "DietLense",
                 "short_description": "AI-powered food recognition application.",
                "long_description": """An application that analyzes food images and provides nutritional information.""",
                "technologies_used": ["Python","Django","Google GenAI SDK"],
                "live_url": "https://dietlense.example.com",
                "github_url": "https://github.com/username/dietlense",
                "image_url": "https://example.com/dietlense.jpg",
                "featured": True
            },
            
            {
                "id": 2,
                "title": "Interview Prep Blog",
                "short_description": "Educational application for programming interviews.",
                "long_description": """A platform for practicing technical interview questions and reading programming articles.""",
                "technologies_used": ["Python","Django","JavaScript" ],
                "live_url": "https://prep.example.com",
                "github_url": "https://github.com/username/interview-prep",
                "image_url": "https://example.com/interview.jpg",
                "featured": False
            }
                 
        ]
        
        return JsonResponse(projects,safe=False)
    
class SkillView(View):
    def get(self,request):
        skill =[
            {
                "id": 1,
                "skill_name": "Python",
                "category": "Programming Language",
                "proficiency": "Advanced",
                "years_of_experience": 4

            },
            {
                "id": 2,
                "skill_name": "Django",
                "category": "Backend",
                "proficiency": "Advanced",
                "years_of_experience":3
            },
            {
                "id": 3,
                "skill_name": "React",
                "category": "Frontend",
                "proficiency": "Intermediate",
                "years_of_experience":2
            }
        ]
        
        return JsonResponse(skill,safe = False)