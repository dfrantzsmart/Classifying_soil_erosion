# Classifying soil erosion
## Identifying areas susceptible to soil erosion - Project 3 at Metis

### The goal of this project is to identify features in an area of land that significantly impacts soil erosion. The model created in this project uses six features: organic matter, field operations, slope, crop rotation, soil texture, and yield in a random forest model. The prediction accuracy is 95%.

Data obtained from
Tatarko, John; Ascough II, James C.; Nelson, Richard. (2015). Soil erosion and organic matter for central Great Plains cropping systems under residue removal. Ag Data
Commons. https://doi.org/10.15482/USDA.ADC/1167058.

Contents:

1. [PART 1 Cleaning and EDA](https://github.com/chennat811/Classifying_soil_erosion/blob/master/Project_3_PART1_Cleaning_and_EDA.ipynb)

2. [PART 2 Feature and Model Selection](https://github.com/chennat811/Classifying_soil_erosion/blob/master/Project_3_PART2_feature_and_model_selection.ipynb)

3. [PART 3 Final Model Tuning](https://github.com/chennat811/Classifying_soil_erosion/blob/master/Project_3_PART3_Final_Model.ipynb)

4. [Streamlit App Code](https://github.com/chennat811/Classifying_soil_erosion/blob/master/streamlit_proj3.py)

5. [Presentation](https://github.com/chennat811/Classifying_soil_erosion/blob/master/project3_wo_demo.pptx)

6. [Cleaned data](https://github.com/chennat811/Classifying_soil_erosion/blob/master/cleaned_df.csv)

### Background
According the Sheffield's Grantham Center, 33% of the world's adequate or high-quality food producing land has been lost. Most of these lands have been affected by erosion. It is projected that erosion will continue to occur at a faster rate than soil can be regenerated. Erosion is a serious problem because the lost of fertile farmland means a reduction in food production.

Soil erosion occurs when the topsoil of fertile farmland is lost by wind, water, or tillage. Erosion can also cause the pollution of waterways because chemical inputs (fertilizers and pesticides) are washed into the rivers and lakes. Erosion can also cause the loss of flood control because eroded soils cannot hold water.

There are many practices and factors that can affect soil health. Farmers need to increase soil health regenerating practices and reduce soil eroding practices for sustainable food production. This project provides an insight on which features are most impactful in soil erosion.

### Tools Used
Pandas, SQL, Matplotlib, Seaborn, SKlearn, Streamlit

### Impacts
The streamlit app can be deployed for farmers to use. It only needs the farmers to input six pieces of information to get a prediction accuracy of 95%. This can be used to evaluate the farmland. It could also be used to explore what features should be changed in the field to improve soil health.
