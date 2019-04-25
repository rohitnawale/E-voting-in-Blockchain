import cx_Oracle as cx

con=cx.connect('teb222','qwerty','TEB222')
cursor_c_party_info = con.cursor()

stmt1="create table c_party_info (party_id number(3), party_name varchar(20),votes number(10))"
cursor_c_party_info.execute(stmt1)
con.commit()


print('hi')