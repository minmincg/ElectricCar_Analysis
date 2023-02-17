import pandas as pd
import hvplot.pandas
import geopandas as gpd
import scipy

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

def regression():
    
    return