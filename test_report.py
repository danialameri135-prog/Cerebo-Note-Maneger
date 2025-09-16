import unittest
import report

class TestNoteManagement(unittest.TestCase):
    def setUp(self):
        # ۱. آماده‌سازی در setUp برای اطمینان از تمیز بودن هر تست
        self.data = {"id_one":{"note": "Hello World","date" : "2025-2-17" ,"Tags" : [False] ,"priority": 1 , "status" : "ToDo"}}
        self.nm = report.Note_Management(self.data)

    def test_add_note(self):
        # ۲. اجرا کردن متد
        self.nm.add("salam")
        # ۳. بررسی اثر جانبی: آیا دیکشنری واقعاً تغییر کرده؟
        self.assertEqual(len(self.data), 2)
        # و آیا محتوای آن درست است؟
        note_id = list(self.data.keys())[0]
        self.assertEqual(self.data[note_id]['note'], "Hello World")
    def test_view(self):       
        self.assertEqual(self.nm.view("id_one"),"your note : Hello World")
    def test_list_note(self):
        result = self.nm.list_note()
        self.assertEqual(result,[f"(id : id_one , Part_of_the_text :{self.data['id_one']['note'][:10]})"])
    def test_delete(self):
        result = self.nm.delete("id_one")   
        self.assertTrue(result) 
    def test_search(self):
        result = self.nm.search("Hello")
        self.assertEqual(result,[f"(id : id_one ,note : {self.data['id_one']['note'][:10]}...)"])
class Tagging_System(unittest.TestCase):
    def setUp(self):
        # ۱. آماده‌سازی در setUp برای اطمینان از تمیز بودن هر تست
        self.data = {"id_one":{"note": "Hello World","date" : "2025-2-17" ,"Tags" : [True,"World"] ,"priority": 1 , "status" : "ToDo"}}
        self.ts = report.Tagging_System(self.data) 
    def test_Tags(self):
        result = self.ts.Tags("id_one","Hello") 
        self.assertEqual(len(self.data["id_one"]["Tags"]),3)
    def test_Tags_search(self):
        result = self.ts.Tags_search(["World"])
        self.assertEqual(result,["id_one"])     
class TestEdit(unittest.TestCase):
    def setUp(self):
        self.data = {"id_one":{"note": "Hello World","date" : "2025-2-17" ,"Tags" : [True,"World"] ,"priority": 1 , "status" : "ToDo"}}
        self.e  = report.Edit(self.data)
    def test_status_method(self):
        result = self.e.status_method("id_one","Do")
        self.assertEqual(self.data["id_one"]["status"],"Do")
    def test_priority_method(self):
        result = self.e.priority_method("id_one",2)
        self.assertEqual(self.data["id_one"]["priority"],2)
    def test_sort_method(self):
        result = self.e.sort_method("priority")
        self.assertEqual(result, {"id_one":{"note": "Hello World","date" : "2025-2-17" ,"Tags" : [True,"World"] ,"priority": 1 , "status" : "ToDo"}})
        result = self.e.sort_method("status")
        self.assertEqual(result,{"id_one":{"note": "Hello World","date" : "2025-2-17" ,"Tags" : [True,"World"] ,"priority": 1 , "status" : "ToDo"}})
       
class TestSavedfile(unittest.TestCase):
    def setUp(self):
        self.data = {"id_one":{"note": "Hello World","date" : "2025-2-17" ,"Tags" : [True,"World"] ,"priority": 1 , "status" : "ToDo"}}
        self.sf = report.Saved_file(self.data) 
    def test_saved_csv(self):
        result = self.sf.saved_csv()
        self.assertEqual(result,"csv saved")       
        result = self.assertEqual
    def test_saved_json(self):
        result = self.sf.saved_json()
        self.assertEqual(result,"json saved")
class stats(unittest.TestCase):
    def setUp(self):
        self.data = {"id_one":{"note": "Hello World","date" : "2025-3-17" ,"Tags" : [True,"World"] ,"priority": 1 , "status" : "ToDo"},"id_two":{"note": "Hello","date" : "2025-2-18" ,"Tags" : [True,"World"] ,"priority": 1 , "status" : "ToDo"}}
        self.s = report.stats(self.data) 
    def test_len_data(self):
        self.s.procses()
        result = self.s.len_data()
        self.assertEqual(result,2)
    def test_tag_max(self):
        self.s.procses()   
        result = self.s.tag_max()
        self.assertEqual(result,("World",2))
    def test_sort_month_year(self):
        self.s.procses()
        result = self.s.sort_month_year()
        self.assertEqual(result,{"id_two":{"note": "Hello","date" : "2025-2-18" ,"Tags" : [True,"World"] ,"priority": 1 , "status" : "ToDo"},"id_one":{"note": "Hello World","date" : "2025-3-17" ,"Tags" : [True,"World"] ,"priority": 1 , "status" : "ToDo"}})
    def report(self):
        total = ['Number of notes: 2,Most used tag : (World,2),Sort note by month of the year : "id_two":{"note": "Hello","date" : "2025-2-18" ,"Tags" : [True,"World"] ,"priority": 1 , "status" : "ToDo"},"id_one":{"note": "Hello World","date" : "2025-3-17" ,"Tags" : [True,"World"] ,"priority": 1 , "status" : "ToDo"']
        result = self.s.report()
        
        self.assertEqual(result,total)
if __name__ == "__main__":
    unittest.main()