import re
documents= {
    "DOC1": """
    RULE: Students must submit their assignments before the deadline.
    EXCEPTION: Students with approved medical leave can request extra   time.
    The university provides an online learning system for students.
    Students can use this system to check their course materials and announcements.
    Teachers upload lecture slides and other learning resources on this system.
    Students should regularly check announcements for important information.
    Assignments must be completed according to teacher instructions.
    Late submissions may receive fewer marks from the teacher.
    Students can contact their teachers if they face any problems in study.
    The library provides books and research materials for learning purposes.
    Students should use these resources to improve their knowledge and skills.
    Group projects help students develop teamwork and communication skills.
    Each group member should complete their assigned work on time.
    Teachers may arrange meetings to discuss student progress and problems.
    Students are expected to attend their classes regularly every week.
    Attendance records are maintained by the department for all students.
    Students should keep copies of their submitted assignments for record.
    The online system also provides examination schedules for students.
    Students can check their results through the student portal easily.
    The university encourages students to follow all academic rules.
    These rules help maintain a fair learning environment for everyone.
    Students should ask questions whenever they need guidance from teachers.
    Learning becomes easier when students manage their time properly daily.
    Regular practice also helps students understand difficult topics easily.
    The university wants every student to achieve academic success in life.
    """,
    "DOC2": """
    RULE: Library books must be returned within fourteen days.
    EXCEPTION: Students working on approved research projects can request an extension.
    The university library provides different types of books for students.
    Students can borrow books using their university identification cards.
    Every borrowed book is recorded in the library system by staff.
    Students should keep books in good condition while using them.
    Damaged books may result in a replacement charge for students.
    The library has separate sections for different subjects and topics.
    Students can find computer science, mathematics and science books easily.
    Quiet study areas are available for individual learning in library.
    Students should maintain silence inside the library at all times.
    Food and drinks are not allowed near library books and computers.
    Students can ask library staff for help if they need anything.
    The library also provides access to online research journals for students.
    These journals help students find useful academic information for assignments.
    Students should use reliable sources in their assignments and projects.
    Library computers are available for educational purposes only for students.
    Students can search for books using the library catalogue system.
    The library updates its collection regularly according to student needs.
    New books are added according to student requirements every semester.
    Students should return borrowed materials on time without any delay.
    This allows other students to use the same resources for study.
    Library staff help students understand borrowing procedures in detail.
    Students can visit the library during working hours for study.
    The library supports students in their academic activities every day.
    """,
    "DOC3": """
    RULE: Students must maintain at least seventy-five percent attendance.
    EXCEPTION: Approved medical leave may be considered by the department.
    The department checks attendance records throughout the semester regularly.
    Students should attend lectures and practical laboratory sessions every week.
    Teachers explain important concepts during classroom activities for students.
    Students are encouraged to participate in discussions in class.
    Class activities help students understand their subjects in better way.
    Students should complete their homework regularly after every lecture.
    Teachers may provide additional exercises for practice to students.
    Students should prepare before attending their lectures in class.
    The department shares important academic announcements for students regularly.
    Students should check these announcements regularly on notice board.
    This is a very long sentence made for testing the sentence chunking method and it contains more than forty words because it keeps on going with extra details about classroom learning and student participation and academic activities and teacher guidance and regular practice and homework completion and overall progress throughout the semester at the university for all students.
    Students should contact their teachers when they need help in study.
    The department provides guidance about academic matters to students.
    Students can discuss their difficulties with their teachers easily.
    Regular attendance improves classroom participation for all students.
    Good study habits help students achieve better results in exams.
    The university encourages responsible student behaviour in campus.
    """
}
def get_words(text):
    return list(re.finditer(r'\S+', text))
def word_chunks(text, window_size,overlap_size, doc_id):
    if overlap_size <0 or overlap_size>= window_size:
        raise ValueError("Invalid overlap value")
    words= get_words(text)
    chunks=[]
    step=window_size - overlap_size
    for i in range (0,len(words), step):
        start=words[i].start()
        end= words[min(i+ window_size, len(words))-1].end()
        chunks.append({
         "id": doc_id + "_W"+ str(overlap_size)+ "_" + str(len(chunks)+1),
         "start":start,
         "end": end,
         "text": text[start:end]   
        })
    return chunks
def sentence_chunks(text, word_budget, doc_id):
        sentences= re.finditer(r'[^.!?]+(?:[.!?]+|$)',text)
        chunks=[]
        current_start=None
        current_end=None
        current_word_count=0
        for s in sentences:
            start,end=s.start(), s.end()
            while start <end and text[start].isspace():
                start +=1
            while end>start and text[end-1].isspace():
                end -=1
            words=get_words(text[start:end])
            count= len(words)
            if count== 0:
                continue
            if count>word_budget:
                if current_start is not None:
                    chunks.append({"id": doc_id+ "_S"+ str(len(chunks)+1), "start":current_start, "end": current_end, "text": text[current_start:current_end]})
                    current_start=None
                    current_word_count= 0
                for i in range(0,count, word_budget):
                    first=words[i]
                    last= words[min(i+ word_budget, count)-1]
                    chunks.append({"id": doc_id + "_S" + str(len(chunks)+1),"start": start+first.start(), "end":start+last.end(), "text": text[start+first.start(): start+last.end()]})
            elif current_word_count + count<= word_budget:
                if current_start is None:
                    current_start=start
                current_end=end
                current_word_count += count
            else:
                chunks.append({"id": doc_id +"_S" + str(len(chunks)+1),"start": current_start, "end":current_end, "text" : text[current_start:current_end]})
                current_start,current_end,current_word_count= start,end,count
        if current_start is not None:
            chunks.append({"id": doc_id + "_S" + str(len(chunks)+1), "start": current_start, "end": current_end, "text": text[current_start:current_end]})
        return chunks
labels ={
    "DOC1": ["RULE: Students must submit their assignments before the deadline.", "EXCEPTION: Students with approved medical leave can request extra time." ],
    "DOC2": ["RULE: Library books must be returned within fourteen days.", "EXCEPTION: Students working on approved research projects can request an extension."],
    "DOC3": ["RULE:Students must maintain at least seventy-five percent attendance.", "EXCEPTION: Approved medical leave may be considered by the department."]
}
for doc_id,text in documents.items():
    print("\n === ", doc_id, "===")
    print("Original Words:", len(get_words(text)))
    methods={
        "Overlap 0":word_chunks(text,40, 0, doc_id),
        "Overlap 10": word_chunks(text, 40, 10,doc_id),
        "Sentence Aware": sentence_chunks(text,40,doc_id)   
    }
    for name,chunks in methods.items():
        print("\nMethod:", name, "| Total Chunks:", len(chunks))
        total=0
        for c in chunks:
            wc=len(get_words(c["text"]))
            total += wc
            print(f"\n{c['id']} | Start:{c['start']} End: {c['end']} Words:{wc}")
            print(c["text"])
        print("\nRepeated Words:",total - len(get_words(text)))
        for label in labels[doc_id]:
                found=any (label in c["text"] for c in chunks)
                print(label.split(":")[0], "survives in one chunks:", found)
print("\n=== TEST CASES ===")
print("Empty Text Chunks:", len(word_chunks("",40, 0,"EMPTY")))
short= "This is a short document with only a few words."
print("Short Doc Chunks:", len(word_chunks(short, 40,0, "SHORT")))
try:
    word_chunks("test",40, 40, "INVALID")
except ValueError as e:
    print("Invalid Overlap Test:",e)
long_sentence ="This is a very long test sentence made to check what happens when one sentence is longer than the forty word budget and it keeps going with more details about students and teachers and classroom learning and assignments and regular practice and academic progress and university life for everyone in the class today."
long_result = sentence_chunks(long_sentence, 40, "LONG")
print("\nLong Sentence Chunks:", len(long_result))
for c in long_result:
    print(c["id"],"| Words:",len(get_words(c["text"])))
    print(c["text"])

print("\n=== EXPLANATION ===")
print("1. Word chunking divides text into fixed 40 word groups.")
print("2. Overlap 10 repeats some words from the previous chunk.")
print("3. Sentence aware chunking keeps complete sentences together.")
print("4. Sentence splitting can fail with abbreviations like Dr. or Mr.")
print("5. It treats Dr. as the end of a sentence, even though it is not.")