import json
import csv
from datetime import datetime
from hashlib import sha256
from collections import Counter
class Note_Management:
    def __init__(self,data):
        self.data = data
            # متد  اضافه کردن یادداشت
    def add(self,note,priority = 0 ,status = "ToDo"):  
        try:         
            now = datetime.now() 
          #. فرمت دلخواه: YYYY/MM/DD 
            time_now_first = now.strftime("%Y-%m-%d;%Hh")
            time_now_two = now.strftime("%Y-%m-%d")
          #ساخت id منحصر بفرد یادداشت
            my_password = [note,time_now_first]
            my_password = " ".join(my_password)
            id = sha256(my_password.encode('utf-8')).hexdigest()
            id = str(id)
            #ساخت دیکشنری برای ذخیره متن یادداشت و اعمال تغییرات
            self.data[id] = {"note" : note ,"date" : time_now_two ,"Tags" : [False],"priority": priority ,"status" : status}
       #برگردوندن خطا درصورت بروز خطا 
        except Exception as e: 
            return f"Error in returnning , e = {e}" 
 # متد نمایش متن یادداشت    
    def view(self,id):
        try:
            note = self.data[f"{id}"]["note"]        
            return f"your note : {note}"    
        except KeyError as e:
            return f"this is for KeyError , e = {e}"               
        except Exception as e:    
            return f"Error in returnning , e = {e}" 
    # نمایش کل یادداشت های موجود        
    def list_note(self):
        try:
            #ساخت لیستی از  یادداشت های موجود
            total_list= [ f"(id : {i} , Part_of_the_text :{self.data[i]['note'][:10]})" for i in self.data]
            return total_list
        except Exception as e:    
            return f"Error in returnning , e = {e}" 
    #پاک کردن یک یادداشت باتوجه به id داده شده    
    def delete(self,id):
        try:           
            del self.data[id]
            
            return True            
        except:
            return False 
#خروجی True یعنی یادداشت پاک شد خروجی False یعنی پاک نشده

#متد سرچ کردن و پیدا کردن یادداشت با توجه به عبارت داده شده
    def search(self,phrase):
        try:
# استفاده از لیست کامپرهنشن برای سرچ کردن
            searching = [f"(id : {k} ,note : {v['note'][:10]}...)" for k,v in self.data.items() if phrase in self.data[k]["note"]]             
            return searching
        except Exception as e:    
            return f"Error in returnning , e = {e}" 
# ساخت کلاس تگ گذاری و سرچ تگ
class Tagging_System:
     # متد تگ گذاری
     def __init__(self,data):
         self.data = data
     def Tags(self,id,Tags):
# اگر توی لیست تگ Treu بود تگ جدی را append کن  
          try:
              if self.data[id]["Tags"][0] == True:
                  self.data[id]["Tags"].append(Tags)
# در غیر این صورت False را تبدیل به True کن و سپس append کن
              else:
                 self.data[id]["Tags"][0] = True
                 self.data[id]["Tags"].append(Tags)
# متد سرچ باتوجه به تگ داده شده    
          except Exception as e:
              return f"Error in returnning , e = {e}"       
     def Tags_search(self,Tags):
         list_search = [ ]
         try:
             for i in self.data:
                 if self.data[i]["Tags"][0] == True:
                     Tag = [j in self.data[i]["Tags"][1:] for j in Tags]
                     if Tag:
                         list_search.append(i)
             return list_search
         except Exception as e:    
            return f"Error in returnning , e = {e}" 
#کلاس ویرایش
class Edit:
    def __init__(self,data):
        self.data = data
     #متد وضعیت یادداشت : ToDo یا Do یا Done
    def status_method(self,id,status):
        try:
            self.data[id]["status"] = status
            return f"The note is in {status} status."
        except Exception as e:    
            return f"Error in returnning , e = {e}" 
     #متد اولویت یادداشت مثلا اولویت 1
    def priority_method(self,id,priority):
        try:
            self.data[id]["priority"] = priority
            return f"The note was prioritized as {priority}."
        except Exception as e:
            return f"Error in returnning , e = {e}"
     #متد مرتب سازی یادداشت بر اساس اولویت یا وضعیت
    def sort_method(self,sort):
        try:
            #مرتب سازی بر اساس اولویت
            if sort == "priority":         
                sorted_items = sorted(self.data.items(), key=lambda item: item[1]['priority']) 
                sorted_dict = dict(sorted_items)
                return sorted_dict
        except Exception as e :
            return f"Error in rerurnning 1, e = {e}"
            #مرتب سازی براساس وضعیت
        try:
            if sort == "status":      
        # 3 اولویت را برای sorted میزاریم توی لیست
                status_order = ['ToDo','Done', 'Doing']
# به sorted میگیم مرتب کن بر اساس لیستی که میدم
                sorted_items = sorted(self.data.items(), key=lambda item: status_order.index(item[1]['status']))
            sorted_dict = dict(sorted_items)
            return sorted_dict
        except KeyError as e:
            return f"this is for KeyError ,e = {e}"
        except Exception as e :
            return f"Error in rerurnning 1, e = {e}"     

# کلاس ذخیره یادداشت ها  
class Saved_file:
    def __init__(self,data):
        self.data = data
#ذخیره به صورت csv         
    def saved_csv(self):
        field = ['id', 'note', 'date', 'Tags', 'priority', 'status']
        with open("report.csv","w",newline = "",encoding = "utf-8") as f:
             writer = csv.DictWriter(f,fieldnames = field)
             writer.writeheader()
#مرتب سازی دیکشنری به صورتی که بشه درست ذخیره کرد
             for key,value in self.data.items():
                  row = {"id" : key,
                  "note" : value["note"],
                  "date" : value["date"],
                  "Tags": value["Tags"],
                  "priority": value["priority"],
                  "status": value['status'] 
                  }
                  writer.writerow(row)
        return "csv saved"
# ذخیره بصورت json
    def saved_json(self):
        with open("report.json", "w",encoding="utf-8") as f:
            json.dump(self.data,f,indent = 2)
        return "json saved"
#کلاس  نمایش آمار
class stats:
    def __init__(self,data):
        self.data = data
        self.lengh_data = None
        self.sort_data = None
        self.maximum_data = None
# متدپردازشگر
    def procses(self):    
        max_tag = [ ]
        num = len(self.data)
        #تعداد یادداشت ها یا وظایف
        self.lengh_data = num
        #مرتب سازی یادداشت ها بر اساس ماه و سال ایجاد
        try:
            self.sort_data = sorted(self.data.items(),key = lambda item : item[1]["date"])
        except Exception as e:
            return f"Error in returnning , e = {e}"
        # تعیین پر استفاده ترین تگ
        try:
            for i in self.data.values():   
                if "Tags" in i:
                    [max_tag.append(tag) for tag in i["Tags"]]
            
            max_tag = [item for item in max_tag if item != False and item != True]
            counts = dict(Counter(max_tag))
        except Exception as e:
            return f"Error in returnning , e = {e}"
        try: 
            self.maximum_data = max(counts.items() , key = lambda item : item[1])
        except Exception as e:
            return f"Error in returnning , e = {e}"
     #متد تعداد یادداشت ها یا وظایف
    def len_data(self):
        return self.lengh_data
    #متد تعیین پر استفاده ترین تگ
    def tag_max(self):
        return self.maximum_data
    # متد مرتب سازی یادداشت ها بر اساس سال و ماه 
    def sort_month_year(self):
        return self.sort_data
     #متد نمایش 3 متد بالا بصورت یکجا
    def report(self):
        total = [f"Number of notes: {self.lengh_data}",f"Most used tag : {self.maximum_data}",f"Sort note by month of the year : {self.sort_data}"]
        return total
          
data = { } 
d = Note_Management(data)
#اضافه کردن یادداشت ها
d.add("salam")
d.add("im ok what you?")
d.add("i ok",2,"Done")
print(data)
#ه id بدی برات یادداشت را نمایش میده
print(d.view('fa0dde4f849fe090489eec995905e1f922a2b47b75c5cb8241a56572384fe2c4' ),"\n")

#نمایش کل یادداشت های موجود
print(d.list_note())
#حذف یادداشت خاص
#print(d.delete('01467cebe6d9b9587fc1ee8064f952720146bda64e7327fa39e9871e56af9e27'),"\n")

#سرچ ،آیدی یادداشت ها را میده
print(d.search("salam"))


#کلاس تگ 
c = Tagging_System(data)
#اضافه کردن تگ
c.Tags('fa0dde4f849fe090489eec995905e1f922a2b47b75c5cb8241a56572384fe2c4' ,"salam")
#نمایش یادداشت های دارای تگ مشابه
print(c.Tags_search(["salam"]))

#کلاس ویرایش
d = Edit(data)
#تغییر وضعیت یادداشت ها به ToDo ، Doing یا Done
print(d.status_method('fa0dde4f849fe090489eec995905e1f922a2b47b75c5cb8241a56572384fe2c4',"Doing"))
#تعیین اولویت برای یادداشت ها
print(d.priority_method('fa0dde4f849fe090489eec995905e1f922a2b47b75c5cb8241a56572384fe2c4',1))
#مرتب سازی بر اساس اولویت (priority)  یا وضعیت (status)
print(d.sort_method("status"))

#کلاس نمایش آمار
e = stats(data)
#فعالسازی متد پردازشگر
e.procses()
#تعداد یادداشت ها
print(e.len_data())
#پر استفاده ترین تگ
print(e.tag_max())
#مرتب سازی بر اساس ماه و سال
print(e.sort_month_year())
#نمایش کل آمار
print(e.report())

#کلاس ذخیره یادداشت ها
f = Saved_file(data)
#ذخیره توی فایل csv
print(f.saved_csv())
# ذخیره توی فایل json
print(f.saved_json())
