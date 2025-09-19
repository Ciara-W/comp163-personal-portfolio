print("================================================================")
print("            PERSONAL ACADEMIC & LIFE PORTFOLIO            ")
print("================================================================")

print("Student: Jordan Smith | Email: jsmith@ncat.edu")
print("From: Charlotte, NC | Graduating: Spring 2028")
print("Major: Computer Science")

print("=== ACADEMIC PROFILE ===")
print("Current Semester: 12 credits across 4 courses")
print("Cumulative GPA: 3.48")
print("Weekly Study Time: 25 hours")
print("Academic Investment: $5.0 per study hour")

current_courses = ["COMP 163", "MATH 150", "ENG 101", "HIS 105"]
courses_credits = {
    current_courses[0]: "3 credits - Prof. Rhodes - M-Eric 300",
    current_courses[1]: "3 credits - Dr. Lee - Marteena 201",
    current_courses[2]: "3 credits - Dr. Martinez - Crosby 121",
    current_courses[3]: "3 credits - Dr. Brown - Crosby 210",
}
print("Current Courses:")
print(current_courses[0], "-", courses_credits[current_courses[0]])
print(current_courses[1], "-", courses_credits[current_courses[1]])
print(current_courses[2], "-", courses_credits[current_courses[2]])
print(current_courses[3], "-", courses_credits[current_courses[3]])

print("=== PERSONAL DEVELOPMENT ===")
current_skills = {"Time management", "Photography", "Problem solving",  "HTML", "Python basics"}
skills_set = current_skills
print("Current Skills:", skills_set)
learn_skills = {"Data structures", "Web design", "JavaScript", "Git", "Public speaking"}
skills_learn = learn_skills
print("Learning Goals:", skills_learn)
career_interests = {"Software development", "Game development", "Web development", "Data science"}
skills_career = career_interests
print("Career Interests:", skills_career)
skills_have = len(skills_set)
print("Skills Currently Have:", skills_have)
skills_want = len(skills_learn)
print("Skills Want to Learn:", skills_want)

print("=== FINANCIAL OVERVIEW ===")

monthly_budget = {
    "food_budget": (150 * 3),
    "entertain_budget": 200 ,
    "book_budget": 125,
    "transport_budget": 100,
}

monthly_total = sum((450,200,125,100))
print(f"Monthly Budget: ${monthly_total}")
food = monthly_budget["food_budget"]
food_day = food /30
print(f"Food: ${food} (${food_day}/day)")
entertain = monthly_budget["entertain_budget"]
print(f"Entertainment: ${entertain}")
books = monthly_budget["book_budget"]
print(f"Books: ${books}")
transportation = monthly_budget["transport_budget"]
print(f"Transportation: ${transportation}")
annual_total = monthly_total * 12
print(f"Annual Projection: ${annual_total}")

print("=== CONNECTIONS & CONTACTS ===")
emergency = ("Hannah Smith (Mom)", "-", "704-555-0199")
print("Emergency Contact:", emergency[0], emergency[1], emergency[2])
address = ("456 Oak Street,", "Charlotte, NC", "28202")
print("Home Address:", address[0], address[1], address[2])
social_media = ("439 followers across", "2 platforms")
print("Social Media Presence:", social_media[0], social_media[1])
key_conacts = ("3 people", "in directory")
print("Key Contacts:", key_conacts[0], key_conacts[1])

print("=== LIFE STATISTICS ===")
completed_courses = ["Biology", "Chemistry", "Calculus", "Spanish II", "World History"]
complete = len(completed_courses)
print("Total Courses Completed:", complete)
credit_hours = [3, 3, 3, 3]
academic_load = sum(credit_hours) + 25
print("Current Academic Load:", academic_load, "weekly commitments")
entertainment_set = {"One Piece", "Barry", "Life", "Incantation", "Memento"}
entertain = len(entertainment_set)
print("Entertainment Backlog:", entertain, "items")
hobbies_set = {"Gaming", "Photography", "Reading", "Soccer", "Music"}
hobbies = len(hobbies_set)
print("Current Hobbies:", hobbies, "activities" )
print("================================================================")


gpa_history = ["3.2", "3.6", "3.4", "3.7"]