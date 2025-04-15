![Screenshot (166)](https://github.com/user-attachments/assets/f03f1fb6-fb2d-454b-bd22-b8a6a01de7d1)
This data science project series walks through step by step process of how to build a real estate price prediction website. We will first build a model using sklearn and linear regression using Dhaka home rent dataset from kaggle.com. Second step would be to write a python flask server that uses the saved model to serve http requests. Third component is the website built in html, css and javascript that allows user to enter home square ft area, bedrooms etc and it will call python flask server to retrieve the predicted price.

During model building I covered almost all data science concepts such as:

- Data load and cleaning
- Outlier detection and removal
- Feature engineering
- Dimensionality reduction
- Gridsearchcv for hyperparameter tunning
- K fold cross validation etc.

Here is the folder structure:

- client : This contains ui website code
- server: Python flask server
- model: Contains datafile and python notebook for model building and generated models and artifacts

Technology and tools wise this project covers:

1. Python
2. Numpy and Pandas for data cleaning
3. Matplotlib for data visualization
4. Sklearn for model building
5. Jupyter notebook, visual studio code and pycharm as IDE
6. Python flask for http server
7. HTML/CSS/Javascript for UI
