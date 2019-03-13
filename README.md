# Income_Prediction

### Adult income prediction analyses and modeling based on supervised learning algorithm (Python code)

#### Project In Briefs

The data set was extracted by Barry Becker from the 1994 Census database data and donored by both Ronny Kohavi and Barry Becker. The idea of this project was to predict whether individuals earn more than 50k in a year. I have employed and developed Python codes to analyse the datasets. The data was basically clean with no missing values, however there were some features with unknown values e.g. workclass, occupation and native-country. Since the features are catagorical variables I have dropped the rows with unknown values. 

All catagorical variables are converted to numerica values using OneHotEncoder for independent variables and LabelEncoder for the dependent variable. I have used Google collab and imported Python libraries such as pandas, scikit-learn, matplotlib, seaborn, numpy for the analyses. 


## Dataset Features 

age: continuous.

workclass: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.
fnlwgt: continuous.

education: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool.

education-num: continuous.

marital-status: Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.

occupation: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.

relationship: Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.

race: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.

sex: Female, Male.

capital-gain: continuous.

capital-loss: continuous.

hours-per-week: continuous.

native-country: United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands.
