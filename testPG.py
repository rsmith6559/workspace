#!/usr/bin/python3

import pgdb

query = "select count(*) from evt where townid = ( select id from locality where state = %(state)s and name = %(name)s )"

params = dict( name="Chemistry", state="nc" )

con =  pgdb.connect( database='mrs', host='localhost' )

cur = con.cursor()
print( cur.execute( query, params ).fetchone()[ 0 ] )
print( cur.rowcount )
print( cur.colnames )

cur.close()
