#this is a work in progress that will grab unique column values to allow for dropdown menus instead of text boxes in the search form

import sqlite3

def queryDropdowns():
    db = sqlite3.connect("cities.db")
    curs = db.cursor()
    curs.execute("SELECT DISTINCT cylinders FROM vehicles")
    cylinders = curs.fetchall()
    curs.execute("SELECT DISTINCT fuel FROM vehicles")
    fuel = curs.fetchall()
    curs.execute("SELECT DISTINCT title_status FROM vehicles")
    titleStatus = curs.fetchall()
    curs.execute("SELECT DISTINCT drive FROM vehicles")
    drive = curs.fetchall()
    curs.execute("SELECT DISTINCT type FROM vehicles")
    vehicleType = curs.fetchall()
    curs.execute("SELECT DISTINCT paint_color FROM vehicles")
    paintColor = curs.fetchall()
    curs.execute("SELECT DISTINCT year FROM vehicles")
    year = curs.fetchall()
    curs.execute("SELECT DISTINCT manufacturer FROM vehicles")
    manufacturer = curs.fetchall()
    curs.execute("SELECT DISTINCT condition FROM vehicles")
    condition = curs.fetchall()

queryDropdowns()