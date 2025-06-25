#importing important libraries
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pymysql

#giving title
st.title("Titanic")

#connecting python with mysql
mydb = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'Sanjana@2003'
)
mycursor = mydb.cursor()

mycursor.execute("use titanic2")
st.markdown('<h1 style = "color:blue;"> Titanic Dataset </h1>',unsafe_allow_html = True)
mycursor.execute("select * from titanic2")
data = mycursor.fetchall()
df = pd.DataFrame(data,columns = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Embarked'])
st.dataframe(df)

        
#query1
st.markdown('<h1 style = "color:purple;"> Distribution of Survived and Sex </h1>',unsafe_allow_html=True)
mycursor.execute("select survived,count(sex) as count_sex,sex from titanic2 group by sex,survived")
data1 = mycursor.fetchall()
df1 = pd.DataFrame(data1,columns=['Survived','count_sex','Sex'])

df1['Survived_Sex'] = df1['Survived'].astype(str) + "_" + df1['Sex']
fig1 = px.pie(
        df1,
        names='Survived_Sex',
        values = "count_sex",
        hole = 0.4,
        labels = ['Survived_Sex']
            )
st.plotly_chart(fig1)

#query 2
st.markdown('<h1 style = "color:green;">Gender By Embarked </h1>',unsafe_allow_html = True)
mycursor.execute("select embarked,count(sex) as count_sex,sex from titanic2 group by sex,embarked")
data2 = mycursor.fetchall()
df2 = pd.DataFrame(data2,columns = ['Embarked','count_sex','Sex'])
df2['Embarked_sex'] = df2['Embarked'] + '_' +df2['Sex']
fig2 = px.bar(
        df2,
        x = 'Embarked_sex',
        y = 'count_sex',
        text = 'Embarked_sex',
        labels = {'Embarked':'Embarked_sex','Count Sex':'count_sex'}
)
fig2.update_traces(texttemplate ='%{text:.2s}', textposition = 'outside',marker_color='purple')
st.plotly_chart(fig2)



#query 3
st.markdown('<h1 style = "color:red;">Age By Survived </h1>',unsafe_allow_html = True)
mycursor.execute('select Age,Survived from titanic2')
data3 = mycursor.fetchall()
df3 = pd.DataFrame(data3,columns = ['Age','Survived'])
fig3 = px.histogram(df3,x = 'Age',nbins=100,color = 'Survived',color_discrete_sequence= ['red','green'])
st.plotly_chart(fig3)

#query 4
st.markdown('<h1 stype = "color:black;">Pie Chart For Sibsp Wise Surivied </h1>',unsafe_allow_html = True)
mycursor.execute("select count(sibsp) as count_sibsp,sibsp,survived from titanic2 group by sibsp,survived order by survived")
data4 = mycursor.fetchall()
df4 = pd.DataFrame(data4,columns = ['Count_sibsp','Sibsp','Survived'])

df4['SibspSurvived'] = df4['Sibsp'].astype(str) +"_"+df4['Survived'].astype(str)

fig4 = px.pie(
    df4,
    names = 'SibspSurvived',
    values = 'Count_sibsp',
    labels = 'SibspSurvived'
)
st.plotly_chart(fig4)

#query5
st.markdown('<h1 style = "color:orange;"> Embarked and Survived Wise Parch </h1>',unsafe_allow_html = True)
mycursor.execute("select embarked,survived,count(parch) as total_parch from titanic2 group by embarked,survived order by total_parch")
data5 = mycursor.fetchall()
df5 = pd.DataFrame(data5,columns = ['Embarked','Survived','Total_parch'])

df5['ES'] = df5['Embarked'] + '_' + df5['Survived'].astype(str)
fig5 = px.bar(
    df5,
    x = 'ES',
    y = 'Total_parch',
    text = 'ES'
)
fig5.update_traces(texttemplate ='%{text:.2s}', textposition = 'outside',marker_color='magenta')
st.plotly_chart(fig5)



