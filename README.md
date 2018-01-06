<h3>Project Title: PySurf_EDA</h3>

![png](pic/surfs-up.jpeg)

<b>Project Objective:</b> In this project, the goal was to understand basic sqlalchemy and how it can be used to query db's using python. After all the queries were performed, a Flask api was built using all the information collected during the analysis.

Tools Used: 
<ul>
<li>DB Browser for Sqlite </li>
<li>Jupyter notebook</li>
<li> Tableau</li>
<li> Excel </li>
</ul>

libraries used:
<ul>
<li>sqlalchemy </li>
<li>pandas </li>
<li>numpy </li>
<li>seaborn </li>
<li>matplotlib</li>
</ul>

## Analysis and Plots

<h2><u>Vacation Analysis</u></h2>

### Observed Temperature and Precipation for 10-01-2016 to 10-10-2016


```python

    I have decided to go on a 10 day vacation !!! 

```

![png](pic/output_12_0.png)


## <u>Precipitation Analysis</ul>

## Plot Hawaii Precipation for 2016





![png](pic/output_20_0.png)


## <u>Station Analysis</u>

### Design a query to calculate the total number of stations


```python
There are 9 weather stations in hawaii.
```

### <u>Plot Most Active Stations Dataframe</u>

![png](pic/output_31_0.png)


![](pic/map.png)

```python
USC00519281 is the most active station
```

## <u>Temperature Analysis</u>
### Plot for 2016 Observed Temperatures in Hawaii


![png](pic/output_39_0.png)


### In 2016, the average temperature in Hawaii was 74.1 °F with variation of +/- 19.9 °F. This sounds like perfect weather to me. 

```python
Hawaii gets two 👍 👍and two raised ✋ ✋.
```

    

### Plot 2016 Hawaii Temperature Observations for Station USC00519281


![png](pic/output_50_0.png)




### Plot for tavg,tmin,and tmax for dates greater than or equal to input date


![png](pic/output_61_0.png)


### Plot for tavg,tmin, and tmax for dates between input dates


![png](pic/output_69_0.png)

<h3><u>Conclusion</u></h3>
<p>While performing an eda for the hawaii sqlite database, I noticed a few different observations. The findings are below:. </p>
<h4><u>Findings</u></h4>
<ul>
<li>In 2016, the average temperature in Hawaii was 74.1 °F with variation of +/- 19.9 °F.</li> 
<p><li> All the stations, in this datebase where located in Oʻahu. There seems to be a positive relationship between the number of observations and location. The stations with the most obseravations where located along the coastline.</li><br>
<li>USC00519281 is the most active station in O'ahu located in Mililani Town.</li>
</ul>

