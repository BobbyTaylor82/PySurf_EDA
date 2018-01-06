<h3>Project Title: PySurf_EDA</h3>

![png](pic/surfs-up.jpeg)

<b>Project Objective:</b> In this project, the goal was to understand basic sqlalchemy and how it can be used to query db's using python. After all the queries were performed, a Flask api was built using all the information collected during the analysis.

Tools Used: 
<ul>
<li>DB Browser for Sqlite </li>
<li>Jupyter notebook</li>
<li> Tableau</li>
</ul>

libraries used:
<ul>
<li>sqlalchemy </li>
<li>pandas </li>
<li>numpy </li>
<li>seaborn </li>
<li>matplotlib</li>
</ul>


<h3><u>Instructions</u></h3>


## Section 1 - Data Engineering

The climate data for Hawaii is provided through two CSV files. Start by using Python and Pandas to inspect the content of these files and clean the data.

* Create a Jupyter Notebook file called `data_engineering.ipynb` and use this to complete all of your Data Engineering tasks.

* Use Pandas to read in the measurement and station CSV files as DataFrames.

* Inspect the data for NaNs and missing values. You must decide what to do with this data.

* Save your cleaned CSV files with the prefix `clean_`.

---

## Section 2 - Database Engineering

Use SQLAlchemy to model your table schemas and create a sqlite database for your tables. You will need one table for measurements and one for stations.

* Create a Jupyter Notebook called `database_engineering.ipynb` and use this to complete all of your Database Engineering work.

* Use Pandas to read your cleaned measurements and stations CSV data.

* Use the `engine` and connection string to create a database called `hawaii.sqlite`.

* Use `declarative_base` and create ORM classes for each table.

  * You will need a class for `Measurement` and for `Station`.

  * Make sure to define your primary keys.

* Once you have your ORM classes defined, create the tables in the database using `create_all`.

---

## Section 3 - Climate Analysis and Exploration

You are now ready to use Python and SQLAlchemy to do basic climate analysis and data exploration on your new weather station tables. All of the following analysis should be completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

* Create a Jupyter Notebook file called `climate_analysis.ipynb` and use it to complete your climate analysis and data exporation.

* Choose a start date and end date for your trip. Make sure that your vacation range is approximately 3-15 days total.

* Use SQLAlchemy `create_engine` to connect to your sqlite database.

* Use SQLAlchemy `automap_base()` to reflect your tables into classes and save a reference to those classes called `Station` and `Measurement`.

## Precipitation Analysis

* Design a query to retrieve the last 12 months of precipitation data.

* Select only the `date` and `prcp` values.

* Load the query results into a Pandas DataFrame and set the index to the date column.

* Plot the results using the DataFrame `plot` method.


* Use Pandas to print the summary statistics for the precipitation data.

### Station Analysis

* Design a query to calculate the total number of stations.

* Design a query to find the most active stations.

  * List the stations and observation counts in descending order

  * Which station has the highest number of observations?

* Design a query to retrieve the last 12 months of temperature observation data (tobs).

  * Filter by the station with the highest number of observations.

  * Plot the results as a histogram with `bins=12`.

## Temperature Analysis

* Write a function called `calc_temps` that will accept a start date and end date in the format `%Y-%m-%d` and return the minimum, average, and maximum temperatures for that range of dates.

* Use the `calc_temps` function to calculate the min, avg, and max temperatures for your trip using the matching dates from the previous year (i.e. use "2017-01-01" if your trip start date was "2018-01-01")

* Plot the min, avg, and max temperature from your previous query as a bar chart.

  * Use the average temperature as the bar height.

  * Use the peak-to-peak (tmax-tmin) value as the y error bar (yerr).


## Section 4 - Climate App

Now that you have completed your initial analysis, design a Flask api based on the queries that you have just developed.

* Use FLASK to create your routes.

## Section 5 - Routes

* `/api/v1.0/precipitation`

  * Query for the dates and temperature observations from the last year.

  * Convert the query results to a Dictionary using `date` as the key and `tobs` as the value.

  * Return the json representation of your dictionary.

* `/api/v1.0/stations`

  * Return a json list of stations from the dataset.

* `/api/v1.0/tobs`

  * Return a json list of Temperature Observations (tobs) for the previous year

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Return a json list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

  * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.

## Analysis and Plots

## <u> Step 3 - Climate Analysis and Exploration </u>


# <u>Vacation Analysis</u>

### Observed Temperature and Precipation for 10-01-2016 to 10-10-2016


```python

    I have decided to go on a 10 day vacation !!!

```


### Plot for  Observed Temperature and Precipation between 10-01-2016 to 10-10-2016


```python
plt.style.use('classic')

fig,(ax1,ax2) = plt.subplots(2,1,sharex=True)
df_temp_weather_for_vacation.Vacation_TOBS.plot(ax=ax1,figsize=(18,8),ls='--',lw=10,color='r',legend=True,title='Vacation Observed Temperature',ylim=(60,100))
df_temp_weather_for_vacation.Vacation_PRCP.plot(ax=ax2,figsize=(18,8),ls='--',lw=10,legend=True,title='Vacation Observed Precipation',ylim=(0,10));

fig.suptitle('Observed Temperature and Precipation for 10-01-2016 to 10-10-2016',size=20);
```


![png](pic/output_12_0.png)


# <u>Precipitation Analysis</ul>

## Plot Hawaii Rainfall for 2016


```python
plt.style.use('dark_background')

df_greater_1_inch.precipitation.plot(c='b',figsize=(18,8),ls=':',lw=(5),marker='^',grid=True,label='precip > 1 inch ',markerfacecolor='yellow',ms=15,markeredgecolor='yellow')
df_at_1_inch.precipitation.plot(c='b',figsize=(18,8),ls=':',lw=(5),marker='^',label='precip = 1 inch',markerfacecolor='white',ms=15,markeredgecolor='yellow')
df_less_1_inch.precipitation.plot(c='b',figsize=(18,8),ls='--',lw=(5),marker='^',grid=True,label='precip < 1 inch ', markerfacecolor='red',ms=15,markeredgecolor='white',alpha=.5)

plt.xlabel('Dates',fontsize=(18))
plt.ylabel('Percipitation (inches)',fontsize=(18));
plt.title('2016 Observed Rainfall in Hawaii',fontsize=(25));
plt.legend(fontsize='x-large')
plt.ylim(0,8)
plt.grid(color='white', linestyle='--', linewidth=2,alpha=.1)
plt.tight_layout()


```


![png](pic/output_20_0.png)


## Summary for Hawaii Rainfall for 2016


```python
df_precip_measurments_2016.describe().T
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>precipitation</th>
      <td>2069.0</td>
      <td>0.179845</td>
      <td>0.506363</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.02</td>
      <td>0.15</td>
      <td>9.64</td>
    </tr>
  </tbody>
</table>
</div>



# <u>Station Analysis</u>

### Design a query to calculate the total number of stations


```python
print('There are {} weather stations in hawaii'.format(session.query(Stations.station).count()))
```

    There are 9 weather stations in hawaii


###  Design a query to find the most active stations




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Station_id</th>
      <th>Activity Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>USC00518838</td>
      <td>342</td>
    </tr>
    <tr>
      <th>1</th>
      <td>USC00517948</td>
      <td>683</td>
    </tr>
    <tr>
      <th>2</th>
      <td>USC00511918</td>
      <td>1932</td>
    </tr>
    <tr>
      <th>3</th>
      <td>USC00514830</td>
      <td>1937</td>
    </tr>
    <tr>
      <th>4</th>
      <td>USC00516128</td>
      <td>2484</td>
    </tr>
    <tr>
      <th>5</th>
      <td>USC00519523</td>
      <td>2572</td>
    </tr>
    <tr>
      <th>6</th>
      <td>USC00519397</td>
      <td>2685</td>
    </tr>
    <tr>
      <th>7</th>
      <td>USC00513117</td>
      <td>2696</td>
    </tr>
    <tr>
      <th>8</th>
      <td>USC00519281</td>
      <td>2772</td>
    </tr>
  </tbody>
</table>
</div>



##  *USC00519281 is the most active station*

### <u>Plot Most Active Stations Dataframe</u>


```python
plt.style.use('dark_background')
plt.figure(figsize=(18,8))
sns.barplot(x='Station_id',y='Activity Count',data=df_station_activity,palette='bwr')
plt.xlabel('Stations',fontsize=(20))
plt.ylabel('Activity Count',fontsize=(20));
plt.title('Most Active Stations',fontsize=(25));
plt.legend(fontsize='x-large')
plt.tight_layout()
```


![png](pic/output_31_0.png)


![](pic/map.png)


### Plot for 2016 Observed Temperatures in Hawaii


```python
plt.style.use('classic')



df_temp_2016_hawaii.plot(c='gray',marker='v',legend=True, ms=2,markerfacecolor='blue',figsize=(18,8));

plt.xlabel('Dates',fontsize=(18))


plt.ylabel('Temp (°F)',fontsize=(18));
plt.title('2016 Observed Temperatures in Hawaii',fontsize=(25));
plt.legend(['Temp (°F)'],fontsize='x-large')
plt.ylim(50,90);
plt.tight_layout();


```


![png](pic/output_39_0.png)



```python
df_temp_2016_hawaii.var()
```




    Temp    19.968016
    dtype: float64




```python
df_temp_2016_hawaii.describe()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Temp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>2069.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>74.085549</td>
    </tr>
    <tr>
      <th>std</th>
      <td>4.468559</td>
    </tr>
    <tr>
      <th>min</th>
      <td>56.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>71.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>75.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>77.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>84.000000</td>
    </tr>
  </tbody>
</table>
</div>



### In 2015, the average temperature in Hawaii was 74.1 °F with variation of +/- 19.9 °F. This sounds like perfect weather to me. 


```python
print(emoji.emojize('Hawaii gets two :thumbsup: :thumbsup:\
and two raised :raised_hand: :raised_hand:.', use_aliases=True))
```

    Hawaii gets two 👍 👍and two raised ✋ ✋.

### Plot 2016 Hawaii Temperature Observations for Station USC00519281


![png](pic/output_50_0.png)


# <u>Temperature Analysis</u>




### Plot for tavg,tmin,and tmax for dates greater than or equal to input date


![png](pic/output_61_0.png)


### This query will return tavg,tmin, and tmax for dates between input dates.


```python

    """


### Plot for tavg,tmin, and tmax for dates between input dates


```python
plt.style.use('dark_background')
plt.figure(figsize=(3,5))
sns.barplot(y='Values',data=df_Temp_Analysis,ci=tmax-tmin,errwidth=3,errcolor='yellow', color='blue')
plt.ylabel('Avg Temp (°F)',fontsize=(18));

```


![png](pic/output_69_0.png)



