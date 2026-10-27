import sqlite3

conn = sqlite3.connect("college_faq.db")
cursor = conn.cursor()

# Create FAQ table
cursor.execute("""
CREATE TABLE IF NOT EXISTS faqs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL
)
""")

# 80 FAQs
faqs = [
    ("What is the admission process?",
     "Admissions are completed according to the college admission schedule and eligibility requirements."),

    ("What are the eligibility requirements for admission?",
     "Eligibility depends on the course and the admission guidelines of the college."),

    ("How can I apply for admission?",
     "Students can apply through the prescribed admission process and submit the required documents."),

    ("What documents are required for admission?",
     "Required documents generally include academic certificates, identification proof and other documents specified during admission."),

    ("Is there an entrance exam for admission?",
     "Entrance requirements depend on the course and applicable admission rules."),

    ("When does the admission process start?",
     "The admission process starts according to the official admission schedule."),

    ("How can I check my admission status?",
     "Admission status can be checked through the official admission portal or college administration."),

    ("Whom should I contact for admission-related queries?",
     "Contact the college admission office for admission-related queries."),

    ("What is the fee structure?",
     "The fee structure depends on the course and can be checked through the official fee information."),

    ("How can I pay my college fees?",
     "College fees can be paid through the available payment methods provided by the college."),

    ("What payment methods are available?",
     "Available payment methods may include online payment and other methods specified by the college."),

    ("Can I pay the fees online?",
     "Yes, online fee payment can be made through the college's designated payment facility."),

    ("What is the last date for fee payment?",
     "The fee payment deadline is mentioned in the official college notifications."),

    ("Is there a late fee for delayed payment?",
     "Late payment rules depend on the college's fee policies."),

    ("Can I get a fee receipt after payment?",
     "Yes, a fee receipt can generally be obtained after successful payment."),

    ("Whom should I contact for fee-related issues?",
     "Contact the accounts or fee section for fee-related issues."),

    ("When are the semester exams conducted?",
     "Semester exams are conducted according to the official academic and examination schedule."),

    ("Where can I check the exam timetable?",
     "The exam timetable can be checked through the official examination section."),

    ("How can I download my exam schedule?",
     "Students can download the exam schedule from the official examination portal or notification."),

    ("What is the examination process?",
     "Students need to follow the examination schedule, eligibility requirements and instructions issued by the college."),

    ("What happens if I miss an exam?",
     "Students should contact the examination department for guidance regarding a missed exam."),

    ("How can I check my exam results?",
     "Exam results can be checked through the official result portal or college notification."),

    ("What is the procedure for supplementary exams?",
     "Supplementary examination procedures are announced by the examination department."),

    ("Whom should I contact for exam-related queries?",
     "Contact the examination department for exam-related queries."),

    ("What courses are offered by the college?",
     "The college offers various undergraduate and postgraduate courses according to its academic programs."),

    ("Where can I find the syllabus?",
     "The syllabus can be found through the official academic department or college website."),

    ("How can I download the syllabus?",
     "Students can download the syllabus from the official academic resources."),

    ("What subjects are included in my semester?",
     "Semester subjects depend on the selected course and semester curriculum."),

    ("How can I check my course curriculum?",
     "The course curriculum can be checked through the respective academic department."),

    ("What is the credit system?",
     "Credits represent the academic value assigned to a course or subject."),

    ("Can I get previous semester syllabus details?",
     "Previous semester syllabus details can be obtained from the respective department or academic resources."),

    ("Whom should I contact for academic queries?",
     "Contact your respective academic department for academic queries."),

    ("Is hostel accommodation available?",
     "Hostel availability depends on the facilities and availability provided by the college."),

    ("How can I apply for hostel accommodation?",
     "Students can apply through the prescribed hostel admission process."),

    ("What documents are required for hostel admission?",
     "Required documents are specified during the hostel admission process."),

    ("What facilities are available in the hostel?",
     "Hostel facilities depend on the accommodation provided by the college."),

    ("Is hostel accommodation available for all students?",
     "Hostel accommodation depends on availability and the applicable hostel rules."),

    ("What are the hostel rules?",
     "Students must follow the rules and guidelines issued by the hostel administration."),

    ("How can I contact the hostel department?",
     "Contact the college hostel administration for hostel-related queries."),

    ("Where can I get information about hostel fees?",
     "Hostel fee information can be obtained from the hostel administration."),

    ("What are the library timings?",
     "Library timings are decided by the college library department and may vary according to the academic schedule."),

    ("How can I get a library membership?",
     "Students can get library membership according to the library's registration procedure."),

    ("How many books can I issue from the library?",
     "The number of books that can be issued depends on the library rules."),

    ("How long can I keep an issued book?",
     "The borrowing period depends on the library's lending rules."),

    ("What happens if I lose a library book?",
     "Students should report the lost book to the library and follow the applicable library policy."),

    ("Is digital library access available?",
     "Digital library access depends on the facilities provided by the college."),

    ("Can I access academic journals through the library?",
     "Academic journals can be accessed according to the library resources and subscriptions."),

    ("Whom should I contact for library-related issues?",
     "Contact the college library department for library-related issues."),

    ("What scholarships are available for students?",
     "Scholarships depend on the schemes and eligibility criteria applicable to students."),

    ("Who is eligible for scholarships?",
     "Eligibility depends on the rules of the respective scholarship scheme."),

    ("How can I apply for a scholarship?",
     "Students can apply through the prescribed scholarship application process."),

    ("What documents are required for scholarship applications?",
     "Required documents depend on the scholarship scheme and its guidelines."),

    ("Where can I check scholarship information?",
     "Scholarship information can be checked through official scholarship portals and college notifications."),

    ("Is there a scholarship renewal process?",
     "Some scholarships require renewal according to the applicable scheme guidelines."),

    ("When is the scholarship application deadline?",
     "The deadline depends on the respective scholarship scheme and official notification."),

    ("Whom should I contact for scholarship-related queries?",
     "Contact the college scholarship or student support section."),

    ("What is the academic calendar?",
     "The academic calendar provides important dates related to the academic session."),

    ("Where can I find the academic calendar?",
     "The academic calendar can be checked through the official college or academic department."),

    ("When does the new semester begin?",
     "The semester begins according to the official academic calendar."),

    ("When are the semester breaks?",
     "Semester breaks are mentioned in the academic calendar."),

    ("Where can I check the holiday schedule?",
     "The holiday schedule can be checked through the official academic calendar."),

    ("When are internal examinations conducted?",
     "Internal examinations are conducted according to the academic schedule."),

    ("When does the semester end?",
     "The semester end date is mentioned in the official academic calendar."),

    ("Are academic calendar dates subject to change?",
     "Yes, dates may change due to official updates or unforeseen circumstances."),

    ("What facilities are available on campus?",
     "Campus facilities may include classrooms, laboratories, library, sports and other student facilities."),

    ("Is Wi-Fi available on campus?",
     "Wi-Fi availability depends on the facilities provided by the college."),

    ("Are computer labs available for students?",
     "Computer laboratories are available according to the facilities provided by the respective department."),

    ("Is there a cafeteria on campus?",
     "Cafeteria availability depends on the campus facilities."),

    ("Are sports facilities available?",
     "Sports facilities depend on the facilities provided by the college."),

    ("Are medical facilities available on campus?",
     "Medical facilities depend on the arrangements provided by the college."),

    ("Is there a transportation facility for students?",
     "Transportation facilities depend on the services provided by the college."),

    ("Where can I get information about campus facilities?",
     "Information about campus facilities can be obtained from the college administration."),

    ("Where is the college located?",
     "The college is located in Indore, Madhya Pradesh."),

    ("What are the college working hours?",
     "College working hours depend on the official schedule and department timings."),

    ("How can I contact the college administration?",
     "Students can contact the college administration through the official contact channels."),

    ("How can I contact my department?",
     "Students can contact their respective department through the official college communication channels."),

    ("Where can I find official college notifications?",
     "Official notifications can be checked through the college website and notice boards."),

    ("Where can I find important college announcements?",
     "Important announcements are published through official college communication channels."),

    ("How can I contact the student help desk?",
     "Students can contact the help desk through the official college support channels."),

    ("Where can I get general information about the college?",
     "General information can be obtained through the official college website or administration.")
]

# Insert FAQs
cursor.executemany(
    "INSERT INTO faqs (question, answer) VALUES (?, ?)",
    faqs
)

conn.commit()
conn.close()

print("80 FAQs added successfully!")