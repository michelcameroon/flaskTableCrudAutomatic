from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import insert,update

#import models  # Import from models.py

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
db = SQLAlchemy(app)

#from .models import YourModel  # Import from models.py


import fieldNamesInTable


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
    namesNoId = fieldNamesInTable.namesNoId('your_database.db', 'your_model')
    
    records = YourModel.query.all()
    return render_template('index.html', records=records, namesNoId=namesNoId)


@app.route('/new', methods=['GET', 'POST'])
def new_record():
    namesNoId = fieldNamesInTable.namesNoId('your_database.db', 'your_model')
    if request.method == 'POST':

        # Create a new record object
        '''
        new_record = YourModel(
            firstName=request.form['firstName'],
            lastName=request.form['lastName'],
            # Other fields

        )
        '''

        data = {nameNoId: request.form[nameNoId] for nameNoId in namesNoId}

        new_record = YourModel(**data)
        print ('new_record=')
        print (new_record)
        db.session.add(new_record)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('new_record.html', namesNoId=namesNoId)






@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_record(id):

    record = YourModel.query.get(id)
    
    namesNoId = fieldNamesInTable.namesNoId('your_database.db', 'your_model')

    if not record:
        return "Record not found", 404

    if request.method == 'POST':

        
        keyValues = request.form
        '''
        print ('keyValues=')
        print (keyValues)
        for key, value in keyValue.items():
            print (key)
            print (value)
        '''
     
        
        update_stmt = update(YourModel).where (YourModel.id == id)

        
        
        for key, value in keyValues.items():
        
            if hasattr(YourModel, key):
                update_stmt = update_stmt.values(**{key: value})
        
        result = db.session.execute(update_stmt)
        db.session.commit()
        return redirect(url_for('index'))  # Redirect to index page or another suitable location

    return render_template('update_record.html', record=record, namesNoId=namesNoId)






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
