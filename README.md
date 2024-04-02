# Continuous Intelligence and Live Data
This is Module 5 and it talks about using live data such as data lakehouses, data piplines, continuous intellegence, and much more.

### Virtual Environment
This code opens a virtual environment for the project.
``` shell
py -m venv .venv
.venv/Scripts/activate
```

### External Libraries
Installing any external libraries (not apart of the standard libraries), if there are any.
``` shell
py -m pip install "libraries to install"
py -m pip freeze > requirements.txt
```
#### List of External Libraries
-  faicons
-  shiny
-  shinylive

### Running Locally
```shell
shiny run --reload --launch-browser dashboard/app.py
```

### After Making Changes, Export to Docs Folder
Export to docs folder and test GitHub Pages locally

```shell
shiny static-assets remove
shinylive export dashboard docs
py -m http.server --directory docs --bind localhost 8008
```