# Project 4 – Graduate Rate (2017-2018) Functions
# Name: Joanna Chou
# Instructor: Dr. S. Einakian
# Section: 07

# Purpose statement: This class creates class Division.
class Division:
    def __init__(self, id: int, division_name: str) -> None:
        self.id = id
        self.division_name = division_name
    def __repr__(self) -> str:
        return ('{}, {}'.format(self.id , self.division_name))
    def __eq__(self, other) -> str:
        return type(self) == type(other) == Division and self.id == other.id and self.division_name == other.division_name

# Purpose statement: This class creates class Graduate and is able to check equality.
class Graduate:
    def __init__(self, id: int, major: str, bachelor: tuple, master: tuple, doctor: tuple) -> None:
        self.id = id
        self.major = major
        self.bachelor = bachelor
        self.master = master
        self.doctor = doctor
    def __eq__(self, other) -> str:
        return type(self) == type(other) == Graduate and self.bachelor == other.bachelor and self.master == other.master and self.doctor == other.doctor
    def __repr__(self) -> str:
        return ('{}, {}, {}, {}, {}, {}, {}, {}'.format(self.id , self.major, self.bachelor[0], self.bachelor[1], self.master[0], self.master[1], self.doctor[0], self.doctor[1]))


# Purpose statement: This function reads a file and returns a list of strings (header and data).
def read_file(file_name: str) -> tuple:
    try:
        file = open(file_name, "r")
    except FileNotFoundError:
        exit("File not found. Please input a valid file.")
    data_list = []
    header_list = []
    for line in file:
        data_list.append(line)
        header_list.append(line)
    file.close()
    return (header_list[:3], data_list[3:])


# Purpose statement: This function takes an input of a list of strings, each representing a line from graduate_rate.csv, and returns a list of Divison objects.
def create_division(list_of_data: tuple) -> list[Division]:
    data_Division = []
    for line in list_of_data[1]:
        line = line.split(',')
        id = int(line[0])
        division_string = str(line[1]).split()
        division = division_string[0].lower()
        if id % 100 == 0:
            obj_division = Division(id, division)
            data_Division.append(obj_division)
    return data_Division

# Purpose statement: This function takes an input of a list of strings, each repreenting a line from gradute_rate.csv, and returns a list of Graduate objects for each unique majors in each Divison.
def create_graduate(list_of_data: tuple) -> list[Graduate]:
    data_graduate = []
    for line in list_of_data[1]:
        line = line.split(',')
        data_splited = []
        if int(line[0]) % 100 != 0:
            for obj in line:
                obj = obj.strip()
                data_splited.append(obj)
        if len(data_splited) > 0:
            data_graduate.append(Graduate(data_splited[0], data_splited[1], (data_splited[2], data_splited[3]), (data_splited[4], data_splited[5]), (data_splited[6], data_splited[7])))
    return data_graduate
    
# Purpose statement: This function creates a file for each division.
def create_files(header: tuple, list_of_div: list[Division], list_of_grad: list[Graduate]) -> None:
    for division in list_of_div:
        try:
            f_div = open('{}.csv'.format(division.division_name), 'w')
        except:
            exit("No such file found")
            
        for line in header[0]:
            f_div.write(line)
        for graduate in list_of_grad:
            text = '{}, {}, {}, {}, {}\n'.format(graduate.id, graduate.major, int(graduate.bachelor[0]) + int(graduate.bachelor[1]),
                    int(graduate.master[0]) + int(graduate.master[1]),  int(graduate.doctor[0]) + int(graduate.doctor[1]))
            if int(graduate.id) in range(int(division.id), int(division.id)+200):
                f_div.write(text)
        f_div.close()

# Purpose statement: This function takes a list of Division objects and returns a list of tuples that has the total and average graduate rate for the given division.
def find_total_avg(list_of_div: list[Division], list_of_grad: list[Graduate]) -> list[tuple]:    
    result = []
    for division in list_of_div:
        num_of_major = 0
        div_total = 0
        for graduate in list_of_grad:
            if int(graduate.id) in range(int(division.id), int(division.id) +200):
                num_of_major += 1
                div_total += int(graduate.bachelor[0]) + int(graduate.bachelor[1]) + \
                    int(graduate.master[0]) + int(graduate.master[1]) + int(graduate.doctor[0])+ int(graduate.doctor[1])
        avg = div_total / num_of_major  
        result.append((div_total,avg))
    return result

# Purpose statement: This function finds the male and female graduation rate.
def find_graduate_rate(major: str, list_of_grad: list[Graduate]) -> tuple:
    tupl = ()
    for graduate in list_of_grad:
        if graduate.major == major:
            male = int(graduate.bachelor[0]) + int(graduate.doctor[0]) + int(graduate.master[0])
            female = int(graduate.bachelor[1]) + int(graduate.doctor[1]) + int(graduate.master[1])
            tupl = (male, female)
    return tupl
            
# Purpose statement: This function computes the total number of graduates based on a given division.
def total_students(input_div_name: str, list_of_div: list[Division], list_of_grad: list[Graduate]) -> int:
    list_of_div = list(filter(lambda div: div.division_name == input_div_name, list_of_div))
    total_avg = find_total_avg(list_of_div, list_of_grad)
    return total_avg[0][0]

# Purpose statement: This function computes the average number of females and males across the majors the Computer division.
def average_gender(input_div_name: str, list_of_div: list[Division], list_of_grad: list[Graduate]) -> tuple:
    div = list(filter(lambda div: div.division_name == input_div_name, list_of_div))[0]
    total_male = 0
    total_female = 0
    major = 0
    for graduate in list_of_grad:
        if int(graduate.id) in range(int(div.id), int(div.id)+200):
            male = int(graduate.bachelor[0]) + int(graduate.doctor[0]) + int(graduate.master[0])
            female = int(graduate.bachelor[1]) + int(graduate.doctor[1]) + int(graduate.master[1])
            total_male += male
            total_female += female
            major += 1
    if major == 0:
        major = 1
    return (total_male / major, total_female/ major)

# Purpose statement: This function computes the total number of gradutes across all majors.
def total_m_f (grad_objs: list[Graduate]) -> int:
    total = 0
    for graduates in grad_objs:
        graduates = str(graduates).split(', ')
        total += int(graduates[2]) + int(graduates[3]) + int(graduates[4]) + int(graduates[5]) + int(graduates[6]) + int(graduates[7])
    return total

# Purpose Statement: This function compares the graduation rate of majors in the Computer division against the majors in the other divisions.
def compare_grad_rate(input_div_name: str, list_of_div: list[Division], list_of_grad: list[Graduate]) -> tuple:
    div_list = list(filter(lambda div: div.division_name == input_div_name, list_of_div))
    other_div_list = list(filter(lambda div: div.division_name != input_div_name, list_of_div))
    
    total_avg = find_total_avg(div_list, list_of_grad)
    other_total_avg = find_total_avg(other_div_list, list_of_grad)
    return (total_avg[0][0]/other_total_avg[0][0], total_avg[0][0]/other_total_avg[1][0], total_avg[0][0]/other_total_avg[2][0])