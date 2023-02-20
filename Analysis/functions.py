import pandas as pd
import hvplot.pandas
import matplotlib.pyplot as plt
import geopandas as gpd
import scipy.stats as st

def heatmap(df,state_column_name,outputcolumn,cmap="plasma"):
    """ df:The DataFrame where data will be pulled from
    state_column_name:The name of the column where full uppercase state names are
    outputcolumn:The target column including the data for heatmap
    cmap(optional):See https://matplotlib.org/stable/tutorials/colors/colormaps.html for different options """
    #File obtained from https://public.opendatasoft.com/explore/dataset/us-state-boundaries/table/
    states = gpd.read_file(open("../Input/us-state-boundaries.geojson"))
    exclude=['Commonwealth of the Northern Mariana Islands',
         'Puerto Rico','Guam','American Samoa','United States Virgin Islands']
    states=states.loc[states["name"].isin(exclude)==False]
    merge_with=df[[state_column_name,outputcolumn]]
    states=pd.merge(states,merge_with,how="inner",left_on="name", right_on=state_column_name)
    map1=states.hvplot.polygons(geo=True,
                                tiles=True,
                                title=outputcolumn,
                                hover_cols=["State"],
                                color=outputcolumn,
                                cmap=cmap,
                                cnorm="log",
                                xlim=(-180, -60),
                                ylim=(0, 72),
                                height=600,
                                width=800
                               )
    return map1


def regression(df,col1,col2):
    
    model = st.linregress(df[col1], df[col2])
    r_squared = model.rvalue**2
    print(f"The correlation between {col1} and {col2} is {model.rvalue:.2f} with a p-value of {model.pvalue:.2f}")
    y_values = df[col1]*model[0]+model[1]
    plt.figure(figsize=(10, 7))
    plt.scatter(df[col1],df[col2])
    plt.plot(df[col1],y_values,color="red")
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.show()
    print(f"The r-squared value of the linear regression model is {r_squared:.2f}")
    
    return