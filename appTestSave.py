from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
db = SQLAlchemy(app)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
db = SQLAlchemy(app)

import fieldNamesInTable

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
db = SQLAlchemy(app)

app.app_context().push()






class YourModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Other columns (e.g., name, email)
    # ...
    firstName = db.Column(db.String(20))
    lastName = db.Column(db.String(20))
    
    def __repr__(self):
        return f'<YourModel {self.id}>'

    def __init__(self, firstName, lastName):
        self.firstName=firstName
        self.lastName=lastName

def get_table_name():
    return YourModel.__tablename__  # Returns 'users' by default

table1 = get_table_name()

print ('table1=')
print (table1)

@app.route('/')
def index():
    
    records = YourModel.query.all()
    return render_template('index.html', records=records)


@app.route('/new', methods=['GET', 'POST'])
def new_record():
    namesNoId = fieldNamesInTable.namesNoId('your_database.db', 'your_model')
    print ('namesNoId=')
    print (namesNoId)

    if request.method == 'POST':
        # Create a new record object
        data1 = ''
        for name in namesNoId:
            print ('name=') 
            print (name) 
            data1 = data1 + name + '=request.form[\'' + name + '\'],' + '\n'

        print ('data1=')
        print (data1)
        data = 'YourModel(\n'
        data = data + data1 + '\n'
        data =data + ')'
        
        print ('data=')
        print (data)

        '''
        new_record = YourModel(
            firstName=request.form['firstName'],
            lastName=request.form['lastName'],
            # Other fields

        )
        '''
        #new_record = data
        #new_record = YourModel( data1 )
        #data1 = "firstName=request.form['firstName']"
        #new_record = YourModel( data1 )
        names11 = []
        
        firstName=request.form['firstName']
        lastName=request.form['lastName']

        names11.append(firstName)
        names11.append(lastName)
        
        #new_record = YourModel( firstName )
        #new_record = YourModel( firstName )
        #new_record = YourModel( firstName )
        #new_record = YourModel(firstName=request.form['firstName])
        #new_record = YourModel(firstName=request.form['firstName'], lastName=request.form['lastName'])
        #new_record = YourModel(firstName, lastName) 	# ok

        print ('names11=')                        
        print (names11)                        


        name110 = ''

        for name11 in names11:
            name110 = ',' + name11
            '''
            if name110 == '':
                name110 = name11
            else:
                name110 = ',' + name11
            '''
        print ('name110=')                        
        print (name110)                        
        a = 'asd'
        b = 'fgh'
        name110 = 'a, b'


        #new_record = YourModel(name110)
        #new_record = YourModel('a', 'b')
        #new_record = YourModel(a, b)
        #names11 = ['firstName', 'lastName']
        data = {nameNoId: request.form[nameNoId] for nameNoId in namesNoId}

        new_record = YourModel(**data)
        #new_record = YourModel(name111: request.form[name111] for name111 in names111)
	
        #new_record = YourModel(names11)	# not working it must be 2 varaibles
        #new_record = YourModel(name110)	#not working

     

        #new_record = data1
        print ('new_record=')
        print (new_record)
        db.session.add(new_record)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('new_record.html')






@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_record(id):
    record = YourModel.query.get(id)

    if not record:
        return "Record not found", 404

    if request.method == 'POST':
        # Update record attributes based on form data
        record.firstName = request.form['firstName']
        record.lastName = request.form['lastName']
        # ...

        db.session.commit()
        return redirect(url_for('index'))  # Redirect to index page or another suitable location

    return render_template('update_record.html', record=record)


@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_record(id):
    record = YourModel.query.get(id)

    if not record:
        return "Record not found", 404

    if request.method == 'POST':
        # Update record attributes based on form data
        record.firstName = request.form['firstName']
        record.lastName = request.form['lastName']
        # ...
        db.session.delete(record)
        db.session.commit()
        return redirect(url_for('index'))  # Redirect to index page or another suitable location

    return render_template('delete_record.html', record=record)



if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
