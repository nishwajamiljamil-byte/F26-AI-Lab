def check_eligibility (score, documents_complete, attendence, assignments):
    if(score>=70 and documents_complete== True and attendence>=75 and assignments>=4):
        return "pass"
    else: 
        return "fail"

test_cases =[(82, True, 80, 5, "pass", "All conditions datisfied"), (85, True, 70, 5, "fail", "Attendence is 70 which is below 75"), (80, True, 80, 2, "fail", "Assignments are less than 4"), (70, True, 75, 4, "pass", "All values are exactly on the minimum threshold")]

print("Testing Rule-Based System:\n") 
for score, doc, att, assign, expected, reason in test_cases:
     actual= check_eligibility(score, doc, att, assign)
     print (f"Input: score={score}, documents={doc}, attendence={att}%, assignments={assign}")
     print (f"Expected:{expected} | Actual:{actual} | Reason: {reason}")
     print (f"Status: {'Correct' if expected== actual 
                       else 
                       'Error'} \n")
