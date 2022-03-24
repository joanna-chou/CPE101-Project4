# Project 4 – Graduate Rate (2017-2018) Test Cases
# Name: Joanna Chou
# Instructor: Dr. S. Einakian
# Section: 07

import unittest
from graduate_funcs import *

class TestCases(unittest.TestCase):
    # No need to test read_file() function
    def test_create_division(self):
        data1 = (0, ['3200,Agriculture operations and related sciences\n', '3201,Agriculture general ,1096,1098,120,181,11,3\n', '3202,Agricultural business and management general,745,379,40,26,0,1\n', '3400,Computer Science\n', '3204,Agricultural economics,1046,485,175,161,80,51\n'])
        div_data1 = create_division(data1)
        div_data1_res = [Division(3200, 'agriculture'), Division(3400, 'computer')]
        self.assertEqual(div_data1, div_data1_res)
       
        data2 = (0, ['999,Another divison major ,1096,1098,120,181,11,3\n','1000,Foreign language\n', '1001,Language general ,1096,1098,120,181,11,3\n', '3202,Agricultural business and management general,745,379,40,26,0,1\n'])
        div_data2 = create_division(data2)
        div_data2_res = [Division(1000, 'foreign')]
        self.assertEqual(div_data2, div_data2_res)

        data3 = (0, ['999,Another divison major ,1096,1098,120,181,11,3\n', '1001,Language general ,1096,1098,120,181,11,3\n', '3202,Agricultural business and management general,745,379,40,26,0,1\n'])
        div_data3 = create_division(data3)
        div_data3_res = []
        self.assertEqual(div_data3, div_data3_res)

    def test_create_graduate(self):
        data1 = (0, ['3201,Agriculture general,1096,1096,120,181,11,3\n', '3202,Agricultural business and management general,745,379,40,26,0,1\n'])
        grad_data1 = create_graduate(data1)
        grad_data1_res = [Graduate('3201', 'Agriculture general',('1096','1096'),('120','181'),('11','3')), Graduate('3202', 'Agricultural business and management general', ('745', '379'), ('40', '26'), ('0', '1'))]
        self.assertEqual(grad_data1, grad_data1_res)

        data2 = (0, [])
        grad_data2 = create_graduate(data2)
        grad_data2_res = []
        self.assertEqual(grad_data2, grad_data2_res)

        data3 = (0, ['999,Another divison major ,1096,1098,120,181,11,3\n','1000,Foreign language\n', '1001,Language general ,1096,1098,120,181,11,3\n', '3202,Agricultural business and management general,745,379,40,26,0,1\n'])
        grad_data3 = create_graduate(data3)
        grad_data3_res = [Graduate('999', 'Another divison major',('1096','1098'),('120','181'),('11','3')), Graduate('1001', 'Language general', ('1096', '1098'), ('120', '181'), ('11', '3')), Graduate('3202', 'Agricultural business and management general', ('745', '379'), ('40', '26'), ('0', '1'))]
        self.assertEqual(grad_data3, grad_data3_res)


    def test_find_total_avg(self):
        create_div1 = create_division(read_file("graduate_rate.csv"))
        create_grad1 = create_graduate(read_file("graduate_rate.csv"))
        self.assertEqual(find_total_avg(create_div1, create_grad1), [(11269, 341.4848484848485), (128083, 4574.392857142857), (241768, 2492.453608247423), (51372, 870.7118644067797)])

        create_div2 = [Division(3200, 'agriculture')]
        create_grad2 = [Graduate('3201', 'Agriculture general',('1096','1096'),('120','181'),('11','3')), Graduate('3202', 'Agricultural business and management general', ('745', '379'), ('40', '26'), ('0', '1'))]
        self.assertEqual(find_total_avg(create_div2, create_grad2), [(3698, 1849.0)])

        create_div3 = []
        create_grad3 = []
        self.assertEqual(find_total_avg(create_div3, create_grad3), [])

    def test_find_graduate_rate(self):
        data = create_graduate(read_file("graduate_rate.csv"))
        self.assertEqual(find_graduate_rate("Agriculture general", data), (1227, 1282))
        self.assertEqual(find_graduate_rate("Information technology", data), (11005, 4094))
        self.assertEqual(find_graduate_rate("Engineering tech. and engineering-related fields other", data), (736, 143))

    def test_total_students(self):
        div_data = create_division(read_file("graduate_rate.csv"))
        grad_data = create_graduate(read_file("graduate_rate.csv"))
        self.assertEqual(total_students('agriculture', div_data, grad_data), 11269)
        self.assertEqual(total_students('computer', div_data, grad_data), 128083)
        self.assertEqual(total_students('education', div_data, grad_data), 241768)

    def test_average_gender(self):
        div_data = create_division(read_file("graduate_rate.csv"))
        grad_data = create_graduate(read_file("graduate_rate.csv"))
        self.assertEqual(average_gender('agriculture', div_data, grad_data), (187.8181818181818, 153.66666666666666))
        self.assertEqual(average_gender('computer', div_data, grad_data), (3452.8928571428573, 1121.5))
        self.assertEqual(average_gender('education', div_data, grad_data), (537.6288659793814, 1954.8247422680413))

    def test_total_m_f(self):
        grad_data1 = create_graduate(read_file("graduate_rate.csv"))
        grad_data2 = [Graduate('3201', 'Agriculture general',('1096','1096'),('120','181'),('11','3'))]
        grad_data3 = []
        self.assertEqual(total_m_f(grad_data1), 432492)
        self.assertEqual(total_m_f(grad_data2), 2507)
        self.assertEqual(total_m_f(grad_data3), 0)

    def test_compare_grad_rate(self):
        div_data = create_division(read_file("graduate_rate.csv"))
        grad_data = create_graduate(read_file("graduate_rate.csv"))
        self.assertEqual(compare_grad_rate('agriculture', div_data, grad_data), (0.08798201166431142, 0.04661080043678237, 0.21936074125983027))
        self.assertEqual(compare_grad_rate('computer', div_data, grad_data), (11.36595971248558, 0.5297764799311737, 2.493245347660204))
        self.assertEqual(compare_grad_rate('education', div_data, grad_data), (21.4542550359393, 1.8875885168211237, 4.706221287861092))

    def test_Graduate_eq(self):
        agri_grad1 = Graduate('3201','Agriculture general',('1096','1098'),('120','181'),('11','3'))
        agri_grad2 = Graduate('3201','Agriculture general',('1096','1098'),('120','181'),('11','3'))
        engi_grad = Graduate('3835','Mining technology/technician',('1','0'),('0','0'),('0','0'))
        self.assertFalse(agri_grad1.__eq__(engi_grad))
        self.assertTrue(agri_grad1.__eq__(agri_grad1))
        self.assertTrue(agri_grad1.__eq__(agri_grad2))
    # No need to test Dvision Class

# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
