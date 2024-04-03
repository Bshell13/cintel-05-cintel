# Continuous Intelligence and Live Data
### Brandon Shellenberger
### 4/2/2024

This is a PyShiny Express app used to show fake live data updating random temperatures to a DEQUE. The temperatures are graphed as a scatter plot with a regression line. The range of the temperatures are controled by the user with numeric inputs. Below are the important keys to setup and run the PyShiny app.

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
List of External Libraries

-  faicons
-  shiny
-  shinylive
-  shinyswatch

### Running Locally
Running the app locally for quick updates.
```shell
shiny run --reload --launch-browser dashboard/app.py
```

### After Making Changes, Export to Docs Folder
Export to docs folder and test GitHub Pages locally.
```shell
shiny static-assets remove
shinylive export dashboard docs
py -m http.server --directory docs --bind localhost 8008
```