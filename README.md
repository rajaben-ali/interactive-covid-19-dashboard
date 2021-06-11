# interactive-covid-19-dashboard

[![SWH](https://archive.softwareheritage.org/badge/swh:1:dir:898f46bbc89e269fefa6e99fbb72a53a5ad4a471/)](https://archive.softwareheritage.org/swh:1:dir:898f46bbc89e269fefa6e99fbb72a53a5ad4a471;origin=https://github.com/rajaben-ali/interactive-covid-19-dashboard.git;visit=swh:1:snp:70ee5afa30ac8bd3171b4f82e7cadb3530eb5920;anchor=swh:1:rev:9df31fd3baefc9c04ce8594ee547064504ec1d2d)

## **About this project**

The "interactive covid-19 dashboard" project is based on the dataset provided by [Johns Hopkins University](https://github.com/CSSEGISandData/COVID-19). The dashboard allows users to visualize the number of Covid-19 cases or deaths per country as a function of time.

## **Tools**

### Programming
Python

### Data extraction and manipulation
Pandas
### Visualization
Matplotlib for visualization. Interactive graphics library can be either Plotly or Bokeh

### Dashboard systems
Streamlit

# Setup configurations
Create a python virtual environment wit the method of your choice then install the requirements packages as follow:
```
pip install -r requirements.txt
```

To add a new python package to this project, make sure you have the virtual environment activated
DO NOT DO "pip freeze > requirements.txt", add the new packages manually to the requirements.txt file as follow:
```
pip install new_package==1.2.3
echo "new_package==1.2.3" >> requirements.txt
git add requirements.txt
git commit -m "Add library: 'new_package==1.2.3'
git push
```

# Run the Streamlit application - Dashboard application for covid data
Run the following line and go to the suggested URL.
```
streamlit run app.py
```
