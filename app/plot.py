
import pandas as pd
import altair as alt
import geopandas as gpd


data = pd.read_csv("./data/cleaned_salaries.csv")

def plot_11(xmax):
    
    source = data[(data["Age"]>0) & (data["Salary_USD"]<=xmax[1])]
    
    chart = alt.Chart(source).mark_rect().encode(
        x = alt.X("Age:Q", bin=alt.Bin(maxbins=60), title=None),
        y = alt.Y("Salary_USD:Q", bin=alt.Bin(maxbins=40), 
                  title="Salary in USD", axis=alt.Axis(format='~s')),
        tooltip='count()',
        color=alt.Color('count()',scale=alt.Scale(scheme='greenblue'), legend=alt.Legend(title='Total Records')),
    ).properties(
        title = "Rect plot by Wenjia",
        width=350,
        height=120,
    )
    
    bar = alt.Chart(source).mark_bar().encode(
        x='Age:Q',
        y='count()',
    ).properties(
        width=350,
        height=50,
    )
    
    fchart = alt.vconcat(chart, bar, spacing=0)
    
    return fchart.to_dict()


def plot_12(value):
    boxplot_order = (data.groupby("Country")["Salary_USD"]
    .median().sort_values(ascending=False).index.tolist())

    chart = alt.Chart(data).mark_boxplot(clip=True).encode(
        x=alt.X("Country", sort=boxplot_order),
        y=alt.Y("Salary_USD", title="Salary in USD", 
                scale=alt.Scale(
                    domain=(value[0], value[1])
                    ),
                axis=alt.Axis(format='~s'))
    ).properties(
        title = "Box plot by Joshuia",
        width=400,
        height=160,
    ).configure_axis(
        labelFontSize=12
    )          
    
    return chart.to_dict()


def plot_21(value):
    
    education_order = ["Less than bachelor's degree", "Bachelor's degree", 
                       "Master's degree", "Doctoral degree"]

    country = data.query("Country == @value")
    for idx, i in enumerate(country["FormalEducation"]):
        if i in education_order[1:]:
            continue
        else:
            print("Change")
            country["FormalEducation"].iloc[idx] = "Less than bachelor's degree"

    chart = alt.Chart(country).mark_bar().encode(
            x=alt.X("Salary_USD", bin=alt.Bin(maxbins=20), title="Salary in USD"),
            y=alt.Y("count()", title="Counts"),
            color=alt.Color("FormalEducation", sort=education_order,
            title="Education level"),
            order=alt.Order('education_order:Q')
        ).configure_legend(
            orient='bottom'
        ).properties(
            title = "Hist plot by Joshuia",
            width=400,
            height=160,
        ).configure_axis(
            labelFontSize=12
        )          

    return chart.to_dict()


def plot_22():
    
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    world["name"] = world["name"].apply(lambda x:str.lower(" ".join(x.split(" ")[0:2])))

    source = data[["Country", "Salary_USD"]].groupby("Country").median().reset_index()
    source["Country"] = source["Country"].apply(lambda x:str.lower(x))
    source.rename({"Country":"name"}, axis=1, inplace=True)

    datamap = pd.merge(world, source, how='left')
    datamap['Salary_USD'] = datamap['Salary_USD'].fillna(0)


    chart = alt.Chart(datamap).mark_geoshape().encode( 
        color=alt.Color(field = "Salary_USD",type = "quantitative",
                        scale=alt.Scale(type = "sqrt"),
                        legend=alt.Legend(title="Salary in USD",labelFontSize = 10,symbolSize = 10,titleFontSize=10)),
        tooltip=['name:N', 'Salary_USD:Q']
    ).properties(
        title='Median Salary of The World',
        projection={"type":'mercator'},
        width=400,
        height=300,
    ).configure_axis(
            labelFontSize=12
    )    
    
    return chart.to_dict()