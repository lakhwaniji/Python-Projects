from flask import Flask,render_template
import get_info
app=Flask(__name__)
@app.route("/")
def home():
    var=get_info.getfilename()
    var=var.to_html()
    return render_template("Home.html",data=var)
@app.route("/api/v1/<station>/<date>")
def about(station,date):
    station=station.zfill(6)
    temp=get_info.acessfile(station,date)
    return {
        "Station":station,
        "Date":date,
        "Temperature":temp
    }
@app.route("/api/v1/station/<station_name>")
def station_data(station_name):
    station_name=station_name.zfill(6)
    data=get_info.station(station_name)
    return data

@app.route("/api/v1/yearly/<station_name>/<year>")
def year_data(station_name,year):
    station_name=station_name.zfill(6)
    data=get_info.getyear(station_name,year)
    return data
if(__name__=="__main__"):
    app.run(debug=True)