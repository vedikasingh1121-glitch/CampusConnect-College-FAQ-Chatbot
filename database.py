import sqlite3

# ============================================================
# DATABASE CONNECTION
# ============================================================

conn = sqlite3.connect("college_faq.db")
cursor = conn.cursor()

# ============================================================
# CREATE FAQ TABLE
# ============================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS faqs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL
)
""")

# ============================================================
# REMOVE OLD FAQs
# ============================================================

cursor.execute("DELETE FROM faqs")

# Reset ID counter
cursor.execute("DELETE FROM sqlite_sequence WHERE name='faqs'")

# ============================================================
# 100 IPS ACADEMY - ENGLISH FAQs
# ============================================================

ips_faqs = [

    # -------------------- GENERAL & ADMISSION --------------------

    (
        "Where is IPS Academy Institute of Engineering and Science located?",
        "IPS Academy Institute of Engineering and Science is located in Indore, Madhya Pradesh."
    ),

    (
        "When was IPS Academy Institute of Engineering and Science established?",
        "The Institute of Engineering and Science, IPS Academy was established in 1999."
    ),

    (
        "Is IPS Academy Institute of Engineering and Science autonomous?",
        "Yes, the Institute of Engineering and Science, IPS Academy is a UGC autonomous institute."
    ),

    (
        "Which university is IPS Academy affiliated with?",
        "The Institute of Engineering and Science, IPS Academy is affiliated with RGPV Bhopal."
    ),

    (
        "Is IPS Academy approved by AICTE?",
        "Yes, the institute is approved by AICTE."
    ),

    (
        "How can I apply for admission to IPS Academy?",
        "Admission is conducted according to the applicable admission rules and programme requirements. Check the latest official admission notification."
    ),

    (
        "What is the eligibility for admission?",
        "Eligibility depends on the programme. Students should check the latest official admission notification for exact requirements."
    ),

    (
        "Are admission dates the same every year?",
        "No. Admission dates may change for different academic sessions."
    ),

    (
        "Where can I find the latest admission information?",
        "The latest admission information should be checked on the official institute website and admission notices."
    ),

    (
        "Does IPS Academy offer undergraduate programmes?",
        "Yes, IPS Academy offers several undergraduate programmes, including engineering programmes."
    ),

    # -------------------- COURSES & DEPARTMENTS --------------------

    (
        "Does IPS Academy offer Computer Science and Engineering?",
        "Yes, Computer Science and Engineering is offered at the institute."
    ),

    (
        "Does IPS Academy offer CSIT?",
        "Yes, Computer Science and Information Technology (CSIT) is offered at the institute."
    ),

    (
        "Does IPS Academy offer Artificial Intelligence and Machine Learning?",
        "Yes, a CSE-AI&ML programme is available."
    ),

    (
        "Does IPS Academy offer Data Science?",
        "Yes, a CSE-Data Science programme is available."
    ),

    (
        "Does IPS Academy offer an IoT programme?",
        "Yes, a CSE-IoT programme is available."
    ),

    (
        "Does IPS Academy offer Cyber Security and Blockchain?",
        "Yes, the institute offers CSE-IoT and Cyber Security including Blockchain Technology."
    ),

    (
        "Does IPS Academy offer postgraduate programmes?",
        "Yes, the institute offers postgraduate programmes."
    ),

    (
        "Does IPS Academy offer M.E. Data Science?",
        "Yes, M.E. Data Science is available at the institute."
    ),

    (
        "Are AI and ML minors or honours available?",
        "AI and ML related minor and honours opportunities are available according to the applicable academic structure."
    ),

    (
        "Does IPS Academy provide practical exposure in computer science?",
        "Yes, students can gain practical exposure through laboratories, projects, internships and technology-related activities."
    ),

    # -------------------- ACADEMICS & EXAMS --------------------

    (
        "Does IPS Academy follow an academic calendar?",
        "Yes, academic activities are conducted according to the institute's academic calendar."
    ),

    (
        "Where can I find the academic calendar?",
        "The latest academic calendar can be checked through official institute notices and the official website."
    ),

    (
        "Are internal examinations conducted?",
        "Yes, students are evaluated through applicable internal assessments and examinations."
    ),

    (
        "When are semester examinations conducted?",
        "Semester examination dates are scheduled according to the academic calendar and official examination notices."
    ),

    (
        "Where can I check the examination timetable?",
        "The latest examination timetable can be checked through official examination notices."
    ),

    (
        "Does IPS Academy conduct practical examinations?",
        "Yes, practical or laboratory evaluations are conducted where applicable."
    ),

    (
        "Is attendance important at IPS Academy?",
        "Yes, students are required to follow the prescribed attendance requirements."
    ),

    (
        "Where can students get information about examination rules?",
        "Students should refer to official examination notices or contact the examination section."
    ),

    (
        "Where can I find information about examination results?",
        "Latest examination results should be checked through the official examination portal or institute notices."
    ),

    (
        "Where can I clarify an academic doubt?",
        "Students can contact the concerned faculty member or academic department for clarification."
    ),

    # -------------------- FEES & SCHOLARSHIPS --------------------

    (
        "How much is the B.Tech fee at IPS Academy?",
        "The fee may vary according to the programme and academic year. Check the latest official fee structure."
    ),

    (
        "Can fees vary between different programmes?",
        "Yes, the fee structure may vary depending on the programme."
    ),

    (
        "How can students pay their fees?",
        "Students can pay fees through the payment methods prescribed by the institute."
    ),

    (
        "Can students pay fees in installments?",
        "Installment facilities depend on the applicable institute rules and policies."
    ),

    (
        "Where can I get my fee receipt?",
        "A fee receipt can be obtained through the prescribed fee payment system after successful payment."
    ),

    (
        "Does IPS Academy provide scholarship opportunities?",
        "Eligible students may apply for applicable government or institute scholarship schemes."
    ),

    (
        "What is the eligibility for scholarships?",
        "Scholarship eligibility depends on the specific scheme and its applicable conditions."
    ),

    (
        "What documents are required for a scholarship?",
        "Required documents vary according to the scholarship scheme. Students should check the latest scholarship notification."
    ),

    (
        "When can students apply for scholarships?",
        "Scholarship application dates depend on the concerned scholarship scheme and official notification."
    ),

    (
        "Where can I get scholarship information?",
        "Students should check official institute notices and the applicable government scholarship portal."
    ),

    # -------------------- HOSTEL & TRANSPORT --------------------

    (
        "Does IPS Academy provide hostel facilities?",
        "Hostel facilities are available. Students should confirm current availability and rules with the institute."
    ),

    (
        "How can I apply for hostel accommodation?",
        "Hostel admission is conducted according to the prescribed process and availability."
    ),

    (
        "Is hostel accommodation available for students?",
        "Hostel accommodation is available subject to the institute's current arrangements and availability."
    ),

    (
        "How much does hostel accommodation cost?",
        "Hostel fees may vary according to the accommodation type and academic year."
    ),

    (
        "Are hostel rules applicable to students?",
        "Yes, hostel residents must follow the prescribed hostel rules and regulations."
    ),

    (
        "Is a mess facility available in the hostel?",
        "Mess facility availability depends on the current hostel arrangements."
    ),

    (
        "Does IPS Academy provide transport facilities?",
        "Transport facilities and routes depend on the institute's current transport arrangements."
    ),

    (
        "Where can I find college bus routes?",
        "The latest bus routes and timings can be obtained from the transport section or official notices."
    ),

    (
        "Who should I contact for a hostel-related issue?",
        "Students should contact the concerned hostel administration or warden."
    ),

    (
        "Who should I contact for a transport-related issue?",
        "Students should contact the concerned transport section for transport-related queries."
    ),

    # -------------------- LIBRARY & LABS --------------------

    (
        "Does IPS Academy have a library?",
        "Yes, the institute provides library facilities for students and academic activities."
    ),

    (
        "Who can use the library?",
        "Eligible students and institute members can use the library according to the prescribed rules."
    ),

    (
        "Are academic books available in the library?",
        "Yes, academic books and learning resources are available for students."
    ),

    (
        "Are reference books available in the library?",
        "Yes, reference resources are available according to academic requirements."
    ),

    (
        "Does the library provide a study facility?",
        "Yes, students can use the library for academic study and reference work."
    ),

    (
        "Where can I check library timings?",
        "The latest library timings can be checked with the library section or official notices."
    ),

    (
        "Does IPS Academy have computer laboratories?",
        "Yes, the institute has modern computer and technology-oriented laboratories."
    ),

    (
        "Does IPS Academy provide practical laboratory learning?",
        "Yes, laboratory activities provide students with practical academic experience."
    ),

    (
        "Does IPS Academy provide internet or digital facilities?",
        "Applicable digital and network facilities are provided to support academic requirements."
    ),

    (
        "Where can I get information about library rules?",
        "Library rules and services can be checked with the library section or official notices."
    ),

    # -------------------- TRAINING & PLACEMENT --------------------

    (
        "Does IPS Academy provide internship opportunities?",
        "Students may get internship opportunities through academic departments and industry-oriented activities."
    ),

    (
        "Does IPS Academy provide industry exposure?",
        "Yes, students can gain industry exposure through internships, industrial visits and industry-oriented activities."
    ),

    (
        "Are industrial visits conducted?",
        "Yes, industrial visits may be conducted by departments to provide practical exposure."
    ),

    (
        "Does IPS Academy provide placement support?",
        "Students can receive career and placement support through training and placement-related activities."
    ),

    (
        "Does IPS Academy conduct training programmes?",
        "Yes, training activities can be conducted to improve students' technical and professional skills."
    ),

    (
        "Does IPS Academy conduct workshops?",
        "Yes, workshops are conducted to help students develop technical and practical skills."
    ),

    (
        "Does IPS Academy conduct seminars?",
        "Yes, seminars and expert sessions may be conducted for academic and professional development."
    ),

    (
        "Does IPS Academy conduct technical events?",
        "Yes, students can participate in technical and technology-related events."
    ),

    (
        "How can students improve their technical skills?",
        "Students can improve technical skills through coding practice, projects, workshops, internships and technical activities."
    ),

    (
        "Does IPS Academy provide career guidance?",
        "Students can receive career guidance through career development and placement-oriented activities."
    ),

    # -------------------- TECHNOLOGY & INNOVATION --------------------

    (
        "Does IPS Academy have a robotics laboratory?",
        "Yes, the institute has an e-Yantra IIT Bombay Robotics Lab."
    ),

    (
        "Does IPS Academy have an AICTE IDEA Lab?",
        "Yes, an AICTE IDEA Lab is available at the institute."
    ),

    (
        "Does IPS Academy have an AR/VR laboratory?",
        "Yes, the institute has an AR/VR Lab."
    ),

    (
        "Does IPS Academy have an electric vehicle workshop?",
        "Yes, the institute has an advanced E-Vehicle workshop."
    ),

    (
        "Does IPS Academy support innovation activities?",
        "Yes, students can participate in innovation, entrepreneurship and technology-based activities."
    ),

    (
        "Does IPS Academy conduct research activities?",
        "Yes, research and innovation activities are conducted at the institute."
    ),

    (
        "Are AI and ML activities available?",
        "Yes, AI and ML related academic programmes and technology activities are available."
    ),

    (
        "Does IPS Academy support project-based learning?",
        "Yes, projects help students develop practical knowledge and technical skills."
    ),

    (
        "Can students participate in technology activities?",
        "Yes, students can participate in various technical and technology-related activities."
    ),

    (
        "Does IPS Academy provide experiential learning?",
        "Yes, the institute supports experiential and practical learning along with academic education."
    ),

    # -------------------- CAMPUS & STUDENT ACTIVITIES --------------------

    (
        "Does IPS Academy have sports facilities?",
        "Sports and recreational facilities are available for students according to institute arrangements."
    ),

    (
        "Does IPS Academy have a canteen?",
        "Canteen or food facilities may be available on campus according to current arrangements."
    ),

    (
        "Does IPS Academy conduct cultural activities?",
        "Yes, students can participate in cultural and extracurricular activities."
    ),

    (
        "Does IPS Academy have student clubs?",
        "Students can participate in academic, technical and extracurricular clubs or activities."
    ),

    (
        "Does IPS Academy organize college events?",
        "Yes, academic, technical, cultural and extracurricular events may be organized."
    ),

    (
        "Does IPS Academy provide student support services?",
        "Students can receive academic, administrative and student-related support from the concerned sections."
    ),

    (
        "Does IPS Academy issue student ID cards?",
        "Student identity cards are issued according to the institute's prescribed process."
    ),

    (
        "How is student attendance maintained?",
        "Attendance is maintained according to the institute's prescribed academic system."
    ),

    (
        "How is academic performance evaluated?",
        "Academic performance may include internal assessment, examinations, practicals and other applicable academic components."
    ),

    (
        "How can students develop practical skills?",
        "Students can develop practical skills through laboratories, projects, workshops, internships and industry-oriented activities."
    ),

    # -------------------- GENERAL INFORMATION --------------------

    (
        "Can students work on academic projects?",
        "Yes, students can work on individual or team projects according to their academic requirements."
    ),

    (
        "Is a final year project required in B.Tech?",
        "Applicable B.Tech programmes include major or final-year project work according to the curriculum."
    ),

    (
        "How can students improve their professional skills?",
        "Students can improve professional skills through training, seminars, workshops, internships and extracurricular activities."
    ),

    (
        "Where can I find the syllabus?",
        "Programme and semester-wise syllabus can be obtained from the official academic department or source."
    ),

    (
        "Where can I find the latest institute notices?",
        "The latest notices can be checked on the official institute website and notice sections."
    ),

    (
        "Where can I find official contact information?",
        "Official contact details can be checked on the institute's official website."
    ),

    (
        "Where can I find admission-related information?",
        "Admission-related information can be checked through official admission notices and the institute website."
    ),

    (
        "Where can I report a fee-related issue?",
        "Students should contact the concerned accounts or fee section for fee-related issues."
    ),

    (
        "Where can I report a scholarship-related issue?",
        "Students should contact the concerned scholarship or administration section."
    ),

    (
        "Where can I report an examination-related issue?",
        "Students should contact the concerned department or examination section for examination-related issues."
    )
]

# ============================================================
# INSERT ALL 100 FAQs
# ============================================================

cursor.executemany(
    "INSERT INTO faqs (question, answer) VALUES (?, ?)",
    ips_faqs
)

# ============================================================
# SAVE DATABASE
# ============================================================

conn.commit()

print("==========================================")
print("      CAMPUSCONNECT FAQ DATABASE")
print("==========================================")
print(f"{len(ips_faqs)} English IPS-specific FAQs added successfully!")
print("Old FAQs removed successfully.")
print("Database updated successfully.")
print("==========================================")

# ============================================================
# CLOSE DATABASE
# ============================================================

conn.close()