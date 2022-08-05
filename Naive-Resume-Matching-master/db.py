import streamlit as st
import sqlite3

conn = sqlite3.connect('data.db', check_same_thread=False)
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(id INTEGER PRIMARY KEY AUTOINCREMENT,email TEXT UNIQUE,password TEXT)')
    
	
#email,password,	

#=========================================================================================	
# Security
#passlib,hashlib,bcrypt,scrypt
import hashlib


def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()


def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False


def add_userdata(email,password):
    #J'utilise try et except pour chancger le message d'erreur de la base de donnée
    try:
        c.execute('INSERT INTO userstable(email,password) VALUES (?,?)',(email,password))
        conn.commit()
    except:
        st.error("Cet email est déjà utilisé")
        st.stop()
	

def login_user(email,password):
	c.execute('SELECT * FROM userstable WHERE email =? AND password = ?',(email,password))
	data = c.fetchall()
	return data

def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data
##################################"""""


def delete_user(id):
	c.execute('DELETE FROM Audit WHERE id="{}"'.format(id))
	conn.commit()