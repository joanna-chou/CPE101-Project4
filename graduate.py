# Project 4 – Graduate Rate (2017-2018) Main Program
# Name: Joanna Chou
# Instructor: Dr. S. Einakian
# Section: 07

from graduate_funcs import *

def main():
    data = read_file("graduate_rate.csv")
    create_grad = create_graduate(data)
    create_div = create_division(data)
    create_files(data,create_div, create_grad)
    total_average = find_total_avg(create_div, create_grad)
    graduate_rate = find_graduate_rate("Agriculture general", create_grad)
    print(create_div)
    total_students_value = str(total_students('computer', create_div, create_grad))
    average_gender_value = str(average_gender('computer',create_div, create_grad))
    total_m_f_value = str(total_m_f(create_grad))
    compare_grad_rate_value = str(compare_grad_rate('computer',create_div, create_grad))

    print("Total OF Processed Graduate in Computer and information sciences and support: " + total_students_value)
    print("Average of Processed Female and Male in Computer and information sciences and support: " + average_gender_value)
    print("Total of all Females and Males Graduate in all Majors: " + total_m_f_value)
    print("Compare total graduate rate of Computer and information sciences and support to all other Majors: " + compare_grad_rate_value)

if __name__ == "__main__":
    main()

