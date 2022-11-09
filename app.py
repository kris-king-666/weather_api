from flask import Flask, render_template, flash
import requests
from forms import SearchForm
from resources import resources

app = Flask(__name__)

app.config['SECRET_KEY'] = resources['SECRET_KEY']


def get_weather(city):
    url = 'http://api.weatherapi.com/v1/current.json'
    api_key = resources['API_KEY']
    # q = 'X'
    params = {'key': api_key, 'q': city}
    response = requests.get(url=url, params=params)
    return response.json()


@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    showdata = False
    form = SearchForm()
    if form.validate_on_submit():
        city = form.search.data
        data = get_weather(city)
        if list(data.keys())[0] == 'error':
            flash('That city name is not recognised')
            form.search.data = ''
        else:
            showdata = True
            form.search.data = ''
            # return redirect(request.url)
            return render_template('index.html', data=data, form=form, showdata=showdata)
    return render_template('index.html', form=form, showdata=showdata)


if __name__ == '__main__':
    app.run(debug=True)
