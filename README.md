<p align="center">
<h1 align="center">2020 Emerging Technologies Project  </h1>


## Description
 <p align="left">
Here is my  documentation for the final year project for the module Emerging Technologies.The objective of the project is to create a web service that uses machine learning from the computer langauge python to create predictions based on a dataset named "powerproduction" provided by our college online portal.
</p>

| Header | Description |
| --- | --- |
| `Author` | Tomas O'Malley (G00361128)@gmit.ie |
| `Course` | Software Development GA_KSOAG_H08 Y4  |
| `Module` | Emerging  Technologies  |
| `Program` | Wind Turbine Prediction Model  |
| `Language` | Python |
| `Weighting` | 50% |
| `Due Date ` | 08/01/2021 |
| `Year of Study` | 4 |



## Module Enviroment


| Number | Software |
| --- | --- |
| 1 | Windows 10|
| 2 | Anaconda|
| 3 | Python|
| 4 | Docker|
| 5 | Jupyter|
| 6 | Git|
| 7 | Cmder |
| 8 | Flask |
| 9 | Bootstrap |



## Deployment
- To run my program(s) you must carefully follow the instructions provided in the links below to successfully run .
 1. git clone https://github.com/OmalleyTomas98/EmergingTechnologiesFinalYearProject.git
 2. cd EmergingTechnologiesFinalYearProject


 # Running Wind Turbine Metric Flask App.
docker run -d -p 5000:5000 windturbine-app
 # Execution on Linux Platform
 ```bash
 export FLASK_APP=webService.py
 python3 -m flask run
 ```

 # Execution on  Windows Platform
 ```bash
 set FLASK_APP=webService.py
 python -m flask run
 ```
 # Docker  Execution 
docker build -t windturbine-app .
docker run -d -p 5000:5000 windturbine-appdocker run -d -p 5000:5000 windturbine-app



## Application Modules  Breakdown
  - modelTrainerOverview.ipynb : Jupyter notebook that trains a model using the data set. In the notebook I
 explain the  model and  an analysis of its accuracy.
  - powerproduction.csv : csv with 500 speed , power datasets from moodle portal.
  - webService.py : . Python script that runs a web service based on the model provided
  - Dockerfile : builds and runs the web service "webService.py" in a container.
  - powerProduction.h5 : saved data model in h5 file  from modelTrainerOverview.ipynb , An H5 file is a data file saved in the Hierarchical Data Format (HDF). It contains multidimensional arrays of scientific data. 
  - index.html : html file qith python script for displaying user input for application using flask
  - README : The current document report you are reading covering the nature of the Program to the core fundamentals/technologies used to resolve the problem sheet  -"specsheet.pdf" issues.


- Underneath is a list of all the software needed and installed to develop my program  for the Module : Emerging Technologies

* [Windows 10  Installation   ](https://www.microsoft.com/en-gb/software-download/windows10)
  - Windows 10 is the Operating System used to Develope my Programs.
* [Anaconda Installation   ](https://www.anaconda.com/)
  - Anaconda is a package tool that install Python(3.8) used largely by Data Scientists.

* [Docker Installation](https://www.docker.com/?utm_source=google&utm_medium=cpc&utm_campaign=dockerhomepage&utm_content=nemea&utm_term=dockerhomepage&utm_budget=growth&gclid=Cj0KCQiA8dH-BRD_ARIsAC24umarjP9XjIo_qI0gCJSfvesHjGmRdcFrk3JSXOKtQsHPbueLkN-IHmEaAphBEALw_wcB)
  - Docker is a set of platform as a service products that use OS-level virtualization to deliver software . Needed o. windows for Unix packages emulation.

* [Jupyter Installation ](https://jupyter.org/)

  - Jupyter Software support interactive data science and scientific computing across all programming languages.
* [Git  Installation ](https://git-scm.com/downloads)
  - Git is a distributed version-control system for tracking changes in any set of file.Used to maintain and update files in my Taskbook.
* [Cmdr  Installation  ](https://cmder.net/)
  - Cmder  is a command  Line Interface emualtor used on windows to emulate the UNIX shell.
/github.com/OmalleyTomas98/EmergingTechnologiesTasks/blob/main/TASK3/standardDeviation.ipynb)


* [Flask Installation ](https://pypi.org/project/Flask/)
  - Flask is a micro web framework written in Python


* [Bootstrap Installation ](https://getbootstrap.com/docs/4.0/getting-started/download/)
  - Bootstrap is a free and open-source CSS framework directed at responsive, mobile-first front-end web
