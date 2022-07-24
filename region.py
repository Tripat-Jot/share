from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, String, MetaData 

app = Flask(__name__)

user = 'root'
password = ''
host = 'localhost'
port = 3306
database = 'railtel_switch'

url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, database )
db = create_engine(url)

meta = MetaData(db) 
create_table = Table( 'rt_regions', meta, 
                    Column('region_id', String),
                    Column('region_code', String),
                    Column('region_name', String)
                    )


@app.route('/')
@app.route('/region',methods=['GET','POST'])
def region():
    conn = db.connect()
    result = conn.execute(create_table.select ())
    for r in result: 
        print (r[0],r[1],r[2])
    # return str(result)
    return render_template("layout.html",result=result)
    
if __name__ == '__main__':
    app.run(port=5000,debug=True)