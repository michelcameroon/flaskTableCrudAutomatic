from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

#import fieldNamesInTable

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


@app.route('/')
def index():
    records = YourModel.query.all()
    return render_template('index.html', records=records)


@app.route('/new', methods=['GET', 'POST'])
def new_record():
    #namesNoId = fieldNamesInTable.namesNoId('your_database.db', 'YourModel')
    #print (namesNoId)

    if request.method == 'POST':
        # Create a new record object
        new_record = YourModel(
            firstName=request.form['firstName'],
            lastName=request.form['lastName'],
            # Other fields
        )

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
        # record.firstName = request.form['firstName']
        # record.lastName = request.form['lastName']
        # ...
        db.session.delete(record)
        db.session.commit()
        return redirect(url_for('index'))  # Redirect to index page or another suitable location

    return render_template('delete_record.html', record=record)



if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
