student_scores = [150, 143, 45, 55, 60, 99, 122, 140, 139, 51, 198, 95, 101, 105, 188]

total_exam_score = sum(student_scores)
print(total_exam_score)

sum = 0
for score in student_scores:
    sum += score
print(sum)

# =======================================

max_total_score = max(student_scores)
print(max_total_score)

highest = 0
for max in student_scores:
    if max > highest:
        highest = max

print(f"This is the highest score {highest}")
