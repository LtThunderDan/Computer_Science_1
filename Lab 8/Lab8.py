# Blake Lawton and Daniel Williamson and Logan Brewer
# Lab 8 Grade Calculator 2
# This will calculate grades only as long as
# the text file has >= 5 different categories

# This opens our file and saves it as the variable filehandle
filehandle = open("lab8input.txt", "r")
# This is our dictionary to hold all values from the text file
Grade_book_dict = {}


# This function strips and splits the text file and
# stores them in the correct lists.
def read_grade_data(filehandle):
    for line in filehandle:
        max_possible_points_list = []
        points_received_list = []
        category = line.strip()
        content = category.split(' ')
        grades = ' '.join(content[2:])
        grade_list = grades.split(',')
        category_percentages = content[1]
        weights = int(category_percentages.strip('%')) / 100
        for i, element in enumerate(grade_list):
            grade_list[i] = element.strip()
        for i in range(len(grade_list)):
            points_received = grade_list[i].split('/')[0]
            points_received = points_received.strip()
            points_received = int(points_received)
            points_received_list.append(points_received)
            max_possible_points = grade_list[i].split('/')[1]
            max_possible_points = max_possible_points.strip()
            max_possible_points = int(max_possible_points)
            max_possible_points_list.append(max_possible_points)
        Grade_book_dict[content[0]] =\
            [weights, points_received_list, max_possible_points_list]
read_grade_data(filehandle)
# print(Grade_book_dict)

filehandle.close()

# This calculates the average of each category
calculated_grades = []
for key in Grade_book_dict:
    grade_values = Grade_book_dict[key]
    average_grade = sum(grade_values[1])/sum(grade_values[2])
    calculated_grades.append(average_grade)
# print(calculated_grades)

# This calculates which letter grade which matches
# the average grade for each category
letter_grades = []
for i in calculated_grades:
    if i >= .9:
        letter_grades.append("A")
    elif i >= .8:
        letter_grades.append("B")
    elif i >= .7:
        letter_grades.append("C")
    elif i >= .6:
        letter_grades.append("D")
    else:
        letter_grades.append("F")
# print(letter_grades)

# This calculates the decimal value for the overall
# contribution percentage or each category
overall_contribution = []
for key in Grade_book_dict:
    for i in Grade_book_dict[key]:
        overall_contribution.append(i)
        break
# print(overall_contribution)

# This calculates the value for overall contribution
# to the final grade for each category
actual_overall = []
actual_overall.append(calculated_grades[0]*overall_contribution[0])
actual_overall.append(calculated_grades[1]*overall_contribution[1])
actual_overall.append(calculated_grades[2]*overall_contribution[2])
actual_overall.append(calculated_grades[3]*overall_contribution[3])
actual_overall.append(calculated_grades[4]*overall_contribution[4])
# print(actual_overall)

# This saves the names of each of the categories in a list
titles = []
for key in Grade_book_dict:
    titles.append(key)
# print(titles)

# This calculates the overall grade for all of the category averages
overall_grade = []
overall_grade.append(sum(calculated_grades)/len(calculated_grades))

# This calculates the letter grade based on the overall grade
final_letter_grade = []
for i in overall_grade:
    if i >= .9:
        final_letter_grade.append("A")
    elif i >= .8:
        final_letter_grade.append("B")
    elif i >= .7:
        final_letter_grade.append("C")
    elif i >= .6:
        final_letter_grade.append("D")
    else:
        final_letter_grade.append("F")

# This is the code to write out the HTML file
filehandle = open("lab8output.html", "w")


def write_grade_report(filehandle):
    filehandle.write('<h1> ' + titles[0] + ' Statistics(' +
                     str(overall_contribution[0]*100) + ')</h1> \n')
    filehandle.write('<ul>')
    filehandle.write(' <li><b>Average:</b> %s </li> \n' %
                     calculated_grades[0])
    filehandle.write(' <li><b>Letter Grade: </b> %s </li> \n' %
                     letter_grades[0])
    filehandle.write(' <li><b>Overall Grade Contribution: </b> %s </li> \n' %
                     actual_overall[0])
    filehandle.write('</ul>')
    filehandle.write('<h1> ' + titles[1] + ' Statistics(' +
                     str(overall_contribution[1]*100) + ')</h1> \n')
    filehandle.write('<ul>')
    filehandle.write(' <li><b>Average:</b> %s </li> \n' %
                     calculated_grades[1])
    filehandle.write(' <li><b>Letter Grade: </b> %s </li> \n' %
                     letter_grades[1])
    filehandle.write(' <li><b>Overall Grade Contribution: </b> %s </li> \n' %
                     actual_overall[1])
    filehandle.write('</ul>')
    filehandle.write('<h1> ' + titles[2] + ' Statistics(' +
                     str(overall_contribution[2]*100) + ')</h1> \n')
    filehandle.write('<ul>')
    filehandle.write(' <li><b>Average:</b> %s </li> \n' %
                     calculated_grades[2])
    filehandle.write(' <li><b>Letter Grade: </b> %s </li> \n' %
                     letter_grades[2])
    filehandle.write(' <li><b>Overall Grade Contribution: </b> %s </li> \n' %
                     actual_overall[2])
    filehandle.write('</ul>')
    filehandle.write('<h1> ' + titles[3] + ' Statistics(' +
                     str(overall_contribution[3]*100) + ')</h1> \n')
    filehandle.write('<ul>')
    filehandle.write(' <li><b>Average:</b> %s </li> \n' %
                     calculated_grades[3])
    filehandle.write(' <li><b>Letter Grade: </b> %s </li> \n' %
                     letter_grades[3])
    filehandle.write(' <li><b>Overall Grade Contribution: </b> %s </li> \n' %
                     actual_overall[3])
    filehandle.write('</ul>')
    filehandle.write('<h1> ' + titles[4] + ' Statistics(' +
                     str(overall_contribution[4]*100) + ')</h1> \n')
    filehandle.write('<ul>')
    filehandle.write(' <li><b>Average:</b> %s </li> \n' %
                     calculated_grades[4])
    filehandle.write(' <li><b>Letter Grade: </b> %s </li> \n' %
                     letter_grades[4])
    filehandle.write(' <li><b>Overall Grade Contribution: </b> %s </li> \n' %
                     actual_overall[4])
    filehandle.write('</ul>')
    filehandle.write('<h1>Cumulative Grade</h1> \n')
    filehandle.write('<ul>')
    filehandle.write(' <li><b>Average:</b> %s </li> \n' %
                     overall_grade[0])
    filehandle.write(' <li><b>Letter Grade:</b> %s </li> \n' %
                     final_letter_grade[0])
    filehandle.write('</ul>')

write_grade_report(filehandle)
