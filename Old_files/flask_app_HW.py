from flask import Flask, jsonify
# from sqlalchemy import func, asc
# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import Session
# from sqlalchemy import create_engine




# engine = create_engine("sqlite:///hawaii.sqlite")

# Base = automap_base()
# Base.prepare(engine,reflect=True)
# Measurments = Base.classes.measurments
# Stations = Base.classes.stations

# session = Session(engine)

# measurments = Base.classes.measurments
# station = Base.classes.stations



app = Flask(__name__)

@app.route('/')
def hello_world():

    return hello_world



# @app.route('/api/v1.0/precipitation')
# def dates_prcp():
    
#     precip_measurments_2016 =session.query(Measurments.date,Measurments.prcp).\
#     filter(Measurments.date.between('2016-01-01','2016-12-31')).all()

#     dictionary_2016_PRCP = dict(precip_measurments_2016)


#     return jsonify(dictionary_2016_PRCP)



@app.route('/api/v1.0/stations')

def station():
    most_active_stations = session.query(Stations.station,func.count(Stations.station))\
    .order_by(func.count(Stations.station))\
    .join(Measurments)\
    .group_by(Stations.station).all()


    dictionary_Stations = dict(most_active_stations)
    
    return jsonify(dictionary_Stations)


@app.route('/api/v1.0/tobs')

def dates_tob():
    
    temp_measurments_2016 =session.query(Measurments.date,Measurments.tobs).\
    filter(Measurments.date.between('2016-01-01','2016-12-31')).all()

    dictionary_2016_Tobs = dict(temp_measurments_2016)




    return jsonify(dictionary_2016_Tobs)


@app.route('/api/v1.0/start/end')

def tmax_avg_tmin():
    cal_temp = session.query(func.avg(Measurments.tobs),func.min(Measurments.tobs),func.max(Measurments.tobs)).\
    filter(Measurments.date.between('2015-01-28', '2016-01-05')).all()


    temp_dict= {'avg': cal_temp[0][0],
             'min':cal_temp[0][1],
             'max':cal_temp[0][2]}


    return jsonify(temp_dict)


if __name__ == "__main__":
    app.run(debug=True)