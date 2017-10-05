hw_pts = [39, 40, 29, 40, 0, 5]
qu_pts = [10, 10, 9, 2, 10, 10, 10]
test_pts = [293, 284, 300]
max_hw_pts = [40, 40, 40, 40, 40, 5]
max_qu_pts = [10, 10, 10, 10, 10, 10, 10]
max_test_pts = [300, 300, 300]
hw_weight = .2
qu_weight = .2
test_weight = .6
# created our lists to be graded

def percentage_per_category(score_list, max_list):
    score_list = sum(score_list)
    max_list = sum(max_list)
    pctg = score_list / max_list
    return pctg
# def function to calc percent score

hw_grade = (percentage_per_category(hw_pts, max_hw_pts) * 100)
qu_grade = (percentage_per_category(qu_pts, max_qu_pts) * 100)
test_grade = (percentage_per_category(test_pts, max_test_pts) * 100)


def letter_grade(percent):
    if percent >= 90:
        return ("A")
    elif percent >= 80:
        return ("B")
    elif percent >= 70:
        return ("C")
    elif percent >= 60:
        return ("D")
    else:
        return ("F")
# def function to assign letter grade 

hw_letter_grade = (letter_grade(hw_grade))
qu_letter_grade = (letter_grade(qu_grade))
test_letter_grade = (letter_grade(test_grade))


def weighted_score(percentage, weight):
    p_w = percentage * weight
    return p_w
# def function to calc weighted score for final score

hw_w_scr = (weighted_score(hw_grade, .2))
qu_w_scr = (weighted_score(qu_grade, .2))
test_w_scr = (weighted_score(test_grade, .6))
final_score = (hw_w_scr + qu_w_scr + test_w_scr)
final_letter_grade = (letter_grade(final_score))
print("Homework grade: ", round(hw_grade), hw_letter_grade)
print("Quiz grade: ", round(qu_grade), qu_letter_grade)
print("Test grade: ", round(test_grade), test_letter_grade)
print("Final score: ", round(final_score), final_letter_grade)
