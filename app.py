from flask import Flask, render_template, request
from world import getCountryData, getCountryNames, filterCountriesByVariable

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    countries = getCountryNames()
    countryData = None
    
    if request.method == 'POST':
        country = request.form.get('country')
        if country:
            countryData = getCountryData(country)   
    
    return render_template('index.html', countries = countries, countryData = countryData)


@app.route('/page2', methods=['GET', 'POST'])
def page2():
    filteredCountries = None
    error_message = None
    
    if request.method == 'POST':
        variable = request.form.get('variable')
        min_value = request.form.get('min_value')
        max_value = request.form.get('max_value')
        
        if variable and min_value and max_value:
            try:
                min_val = float(min_value)
                max_val = float(max_value)
                
                if min_val > max_val:
                    error_message = "Error: El valor mínim no pot ser major que el valor màxim."
                else:
                    filteredCountries = filterCountriesByVariable(variable, min_val, max_val)
            except ValueError:
                error_message = "Error: Els valors han de ser numèrics."
    
    return render_template('page2.html', filteredCountries = filteredCountries, error_message = error_message)


app.run(debug=True)

