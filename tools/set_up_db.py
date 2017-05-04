import ConfigParser
import psycopg2
import psycopg2.extras

config = ConfigParser.RawConfigParser()
config.read('../settings.cfg')

host = config.get('postgres', 'host')
port = config.get('postgres', 'port')
dbname = config.get('postgres', 'dbname')
user = config.get('postgres', 'user')
password = config.get('postgres', 'password')
conn_string = "host='"+host+"' port='"+port+"' dbname='"+dbname+"' user='"+user+"' password='"+password+"'"
# print the connection string we will use to connect
print "Connecting to database\n	->%s" % (conn_string)

conn = psycopg2.connect(conn_string)
cursor = conn.cursor('cursor_unique_name', cursor_factory=psycopg2.extras.DictCursor)
    
query = "CREATE TABLE IF NOT EXISTS dggrid ( \
        id BIGSERIAL PRIMARY KEY, \
        gid bigint UNIQUE, \
        geo geometry, \
        population int, \
        employment int \
    );"
print query
cursor.execute(query)