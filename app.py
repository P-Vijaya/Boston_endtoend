import pickle
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        try:
            crime_rate = float(request.form['CRIM'])
            land_zoned = float(request.form['ZN'])
            acres = float(request.form['INDUS'])
            river_bound = int(request.form['CHAS'])
            nitric_oxide_conc = float(request.form['NOX'])
            rooms_dwelling = float(request.form['RM'])
            home_before_1940 = float(request.form['AGE'])
            distance_to_centres = float(request.form['DIS'])
            radial_highways = int(request.form['RAD'])
            property_tax = float(request.form['TAX'])
            pupil_teacher_ratio = float(request.form['PTRATIO'])
            blacks_in_town = float(request.form['B'])
            lower_status = float(request.form['LSTAT'])
            filename = 'linear_regression.pickle'
            loaded_model = pickle.load(open(filename,'rb'))
            prediction = loaded_model.predict([[crime_rate,land_zoned,acres,river_bound,nitric_oxide_conc,
                                                rooms_dwelling,home_before_1940,distance_to_centres,
                                                radial_highways,property_tax,pupil_teacher_ratio,blacks_in_town,
                                                lower_status]])
            print("Prediction values is:", prediction)
            return render_template('results.html',prediction = prediction[0])
        except Exception as e:
            print("The exception is:",e)
            return "Something is wrong"
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run(port=2000,debug=True)
