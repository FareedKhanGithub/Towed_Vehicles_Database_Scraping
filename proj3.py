import sqlite3
import operator


def open_database(db_name):
    conn = sqlite3.connect(db_name)
    return conn

def create_table(cursor):
    sql = "create table towvehicles (tow_Date text, make text, style text, color text, state text)"
    try:
       cursor.execute(sql)
    except:


def add_data_to_db(cursor, str_datafile_name):                             
    with open(str_datafile_name, 'r') as f:
        for line in f:
            if not line.startswith("tow_Date"):                          #skips the first line
                L = line.split(",")                                    #separates the data into comma separated values
                sql = "insert into towvehicles (tow_date, make, style, color, state) values (:tow_date, :make, :style, :color, :state)"
                cursor.execute(sql, {"tow_date":L[0], "make":L[1], "style":L[2], "color":L[3], "state":L[4].replace("\n","").replace(" ","")})               #how it is organizd




#NUMBER 1
###180 kilobytes is the size of the data base 




#NUMBER 2
def how_many_car_makers(cursor): #74
    sql = """SELECT DISTINCT make FROM towvehicles"""
    makers = cursor.execute(sql)
    v =list(makers)
    r = len(v)                         
    z = r - 1                         #because you dont want to count the make sign
    print(z)


#NUMBER 3
def from_outof_state(cursor):  #613
    note = """SELECT state FROM towvehicles WHERE state != "IL" """ 
    data = cursor.execute(note)
    o = list(data)
    l = len(o)                     
    q = l-1
    print(q)






#NUMBER 4                                     #Date with the highest amount of towed vehicles (('11/22/2017',), 167)
def most_cars_towed_date(cursor):                 
    note2 = """SELECT tow_date FROM towvehicles"""
    dcurobj = cursor.execute(note2)
    datalist = list(dcurobj)
    D = {}
    for i in datalist:
        if i not in D:
            #print("pluss")
            D.update({i:1})            #make new element in list            #update the number in the dictionary values
        else:
            D[i] += 1                               #update the number in the dictionary values
    sorted_d = sorted(D.items(), key=operator.itemgetter(1))
    print('Date with the highest amount of towed vehicles',sorted_d[-1])





def main():
    conn = open_database("towplace.db")
    cursor = conn.cursor()
    create_table(cursor)
    add_data_to_db(cursor,"/Users/zeba/Documents/SQLsafety/proj3/Towed_Vehicles.csv")
    how_many_car_makers(cursor)
    from_outof_state(cursor)
    most_cars_towed_date(cursor)
    conn.commit()
    conn.close()
main()


