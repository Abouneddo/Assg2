import plotly.figure_factory as ff
import pandas as pd
import plotly.express as px
import streamlit as st
import chart_studio.plotly as py
import plotly.graph_objects as go

st.title ("Karim's APP")
st.header("this is the markdown")
st.markdown("this is the header: Graphical Representation")
st.subheader("this is the subheader: Scatter-Bar-BoxPlot,...")
# st.caption("this is the caption")
st.code("Year=2022")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

st.write("This is the python logo")
st.image("C:\\Users\\rawad\\OneDrive\\Desktop\\plogo.png")


st.button('Click me')
st.slider('Pick a number')
st.multiselect('Charts',['Bar','Pie','Line', 'Scatter'])

df = pd.read_csv("C:\\Users\\rawad\Downloads\\Top250.csv")
print(df)

# st.title('Uber pickups in NYC')

# LINE
fig = px.line(df, x = 'Restaurant', y = 'Sales', title='Sales Per Restaurant (Line)')
fig.show()

# SCATTER
fig2 = px.scatter(df, x = 'Restaurant', y = 'Sales', title='Sales Per Restaurant (Scatter)')
fig2.show()

# SCATTER
fig3 = px.scatter(df, x = 'Rank', y = 'Restaurant', title='Restaurant Per Rank (Scatter)')
fig3.show()

# SCATTER
fig4 = px.scatter(df, x = 'Segment_Category', y = 'Restaurant', title='Restaurant Per Segment Category (Scatter)')
fig4.show()

#px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
#           size="pop", color="continent", hover_name="country",
#           log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])

# BAR
fig5 = px.bar(df, x = 'Segment_Category', y = 'Restaurant', title='Restaurant Per Segment Category (Bar)')
fig5.show()

# HISTOGRAM
fig6 = px.histogram(df, x = 'Restaurant', y = 'Sales', title='Sales Per Restaurant (Histogram)')
fig6.show()

# HISTOGRAM
fig7 = px.histogram(df, x = 'Segment_Category', y = 'Units', title='Units Per Segment Category (Histogram)')
fig7.show()

# BOX PLOT
fig8 = px.box(df, x = 'Segment_Category', y = 'YOY_Units', title='YOY Units per Segment Category (Box Plot)')
fig8.show()

# PIE
random_x = [11293, 4085, 3266]
names = ["Taco Bell", "Applebee's", "IHOP"]
fig10 = px.pie(df, values=random_x, names=names)
fig10.show()

# Interactive Multidimensional Visualization, in one line of Python
fig9 = px.scatter_matrix(df, dimensions=["YOY_Sales", "Units", "YOY_Units", "Sales"], color="Segment_Category")
fig9.show()

# SCATTER
df5 = px.data.gapminder()
fig11 = px.scatter(df, x="Restaurant", y="Units", animation_frame="Sales")
# fig11 = px.scatter(df, x = 'YOY_Sales', y = 'YOY_Units', title='YOY_Units Per YOY_Sales (Scatter)')
fig11.show()