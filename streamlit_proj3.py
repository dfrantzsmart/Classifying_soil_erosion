import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write('''# Welcome to the the soil erosion predictor!''')

st.write(
'''
Soil health is extremely important to sustain food production for a growing population. However, a decrease in production is expected. One of the major factors is soil erosion. In order to prevent futher erosion of prime farmland, farmers need to understand what factors are important in soil erosion. The following model provides an insight.


'''
)

@st.cache
def load_data(data):
	data = pd.read_csv(data)
	data.drop(['Unnamed: 0'], axis = 1, inplace=True)
	return data
data = load_data('df_streamlit.csv')

st.write(
'''
## Train a Random Forest Classifier
First, a model trained to predict whether soil erosion is tolerated or not tolerated. Slope, field operations, organic matter, rotation, soil class, and crop yield were identified to be the most impactful features.
'''
)
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

X = data[['Slope','scifo','sciom','rotation', 'soil_text','yield1']]
y = data['soil_erosion']

X_train, X_test, y_train, y_test = train_test_split(X, y)

rf = RandomForestClassifier()

rf.fit(X_train, y_train)
st.write('The R2 on test data for this model is {:.2f}.'.format(rf.score(X_test, y_test)))

st.write(
'''
## Now, we can make predictions with the trained model from user input
'''
)


rotation_data = [['corn, grain (CG)', 0], ['corn, grain, canola, winter wheat (CGCAWW)', 1],['corn, fallow, winter wheat CGFAWW)', 2], ['corn, grain, soy-beans (CGSB)', 3],
['sorghum, grain, cotton (SGCT)', 4], ['sorghum, cotton, cotton (SGCTCT)', 5],
['sorghum, fallow, winter wheat (SGFAWW)',6], ['sorghum, grain, soy-bean, winter wheat (SGSBWW)', 7],
['winter wheat(WW)', 8], ['winter wheat, cotton (WWCT)', 9], ['winter wheat, cotton, cotton (WWCTCT)', 10],
['winter wheat, fallow (WWFA)', 11],
['winter wheat, winter wheat, canola (WWWWCA)', 12],
['winter wheat, winter wheat, cotton (WWWWCT)', 13]]

rot_df = pd.DataFrame(rotation_data, columns = ['Name','ID'])
values = rot_df['Name'].tolist()
options = rot_df['ID'].tolist()
rot_dic = dict(zip(options,values))
rot_select = st.selectbox('What type of crop rotation does your farm employ?', options, format_func = lambda x: rot_dic[x])
st.write(rot_select)

soil_class = [['clay',0],['clay loam',1],['decomposed plant material',2],['loam',3],['loamy sand',4],['sand',5],['sandy loam',6],['silty clay',7],['silty clay loam',8],['silty loam',9]]
soil_df = pd.DataFrame(soil_class, columns = ['Name','ID'])
values = soil_df['Name'].tolist()
options = soil_df['ID'].tolist()
soil_dic = dict(zip(options,values))
soil_select = st.selectbox('What type is your soil classified as?', options, format_func = lambda x: soil_dic[x])
st.write(soil_select)

slope = st.slider('What is the slope of your field?', min_value=0, max_value=100)
field_operations = st.slider('Consider the relative amount of field operations. To estimate: If your farm employs field operations more than four times a year, pick a number close to 0.1. If your farm does not employ field operations that disturb the soil, pick a number close to 1. For a more accurate calculation, refer to Jim Sharkoff - Evaluation of Management Alternatives Using the Soil Conditioning Index.', min_value=0.1, max_value=1.0)
organic_matter = st.slider('Consider the relative amount of organic material removed. To estimate: If you farm removes a large amount of organic matter, pick a number closer to -0.7. If the amount of organic matter is sustained, pick a number around 0. If the amount of organic matter is added, pick a number around 5.5)', min_value=-0.7, max_value=5.5)
yield1 = st.number_input('Input crop yield per year in kg/m squared (1kg/m squared is equivalent to 11.02 US ton/hectare)')
input_data = pd.DataFrame({'Slope': [slope], 'scifo': [field_operations], 'sciom':[organic_matter], 'rotation':[rot_select],'soil_text':[soil_select], 'yield1':[yield1]})
output = rf.predict(input_data)[0]
return_statement = ['tolerated' if output == 1 else 'not tolerated']
if st.button('Predict soil tolerance'):
	st.write('The predicted amount of soil erosion is {}.'.format(return_statement[0]))
