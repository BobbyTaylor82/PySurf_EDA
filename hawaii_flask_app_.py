import numpy as np
import pandas as pd

from sqlalchemy import func
from sqlalchemy import asc
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify


engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()
Base.prepare(engine,reflect=True)
Measurments = Base.classes.measurments
Stations = Base.classes.stations

session = Session(engine)


app = Flask(__name__)


@app.route('/api/v1.0/precipitation')

def dates_prcp():

    # This function returns the json list of prcp dates and measurements between 12/2016 and 01/16
    
    precip_measurments_2016 =session.query(Measurments.date,Measurments.prcp).\
    filter(Measurments.date.between('2016-01-01','2016-12-31')).all()

    dictionary_2016_PRCP_results = dict(precip_measurments_2016)


    return jsonify(dictionary_2016_PRCP_results)



@app.route('/api/v1.0/stations')

def station():

    # This function returns a list of the most active stations by number of observations 


    most_active_stations = session.query(Stations.station,func.count(Stations.station))\
    .order_by(func.count(Stations.station))\
    .join(Measurments)\
    .group_by(Stations.station).all()


    dictionary_Stations = dict(most_active_stations)
    
    return jsonify(dictionary_Stations)



@app.route('/api/v1.0/tobs')

def dates_tob():

    # This function returns the json list of tobs dates and measurements between 12/2016 and 01/16
    
    temp_measurments_2016 =session.query(Measurments.date,Measurments.tobs).\
    filter(Measurments.date.between('2016-01-01','2016-12-31')).all()

    dictionary_2016_Tobs = dict(temp_measurments_2016)


    return jsonify(dictionary_2016_Tobs)




@app.route('/api/v1.0/start')

def tmax_avg_tmin0():

    # The function will output the tavg,tmin,and tmax for dates greater than or equal to input date.

    cal_temp0 = session.query(func.avg(Measurments.tobs),func.min(Measurments.tobs),func.max(Measurments.tobs)).\
    filter(Measurments.date >= start_date).all()

    temp_dict0= {'avg': cal_temp0[0][0],
                'min':cal_temp0[0][1],
                'max':cal_temp0[0][2]}

    
    return jsonify(temp_dict0)





@app.route('/api/v1.0/start/end')

def tmax_avg_tmin():

    # This function  will return the tavg,tmin, and tmax for dates between input dates.

    cal_temp = session.query(func.avg(Measurments.tobs),func.min(Measurments.tobs),func.max(Measurments.tobs)).\
    filter(Measurments.date.between('2015-01-28', '2016-01-05')).all()

    temp_dict= {'avg': cal_temp[0][0],
                'min':cal_temp[0][1],
                'max':cal_temp[0][2]}

    return jsonify(temp_dict)



if __name__ == '__main__':
    app.run(debug=True)