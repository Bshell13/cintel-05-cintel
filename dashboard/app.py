from datetime import datetime
import random
from shiny import reactive, render
from shiny.express import ui
from faicons import icon_svg


# --------------------------------------------
# SET UP THE REACIVE CONTENT
# --------------------------------------------

# --------------------------------------------
# PLANNING: We want to get a fake temperature and 
# Time stamp every N seconds. 
# For now, we'll avoid storage and just 
# Try to get the fake live data working and sketch our app. 
# We can do all that with one reactive calc.
# Use constants for update interval so it's easy to modify.
# ---------------------------------------------------------

# --------------------------------------------
# First, set a constant UPDATE INTERVAL for all live data
# Constants are usually defined in uppercase letters
# Use a type hint to make it clear that it's an integer (: int)
# --------------------------------------------
UPDATE_INTERVAL_SECS: int = 1
# --------------------------------------------

# Initialize a REACTIVE CALC that our display components can call
# to get the latest data and display it.
# The calculation is invalidated every UPDATE_INTERVAL_SECS
# to trigger updates.

# It returns everything needed to display the data.
# Very easy to expand or modify.
# (I originally looked at REACTIVE POLL, but this seems to work better.)
# --------------------------------------------

@reactive.calc()
def reactive_calc_combined():

    # Invalidate this calculation every UPDATE_INTERVAL_SECS to trigger updates
    reactive.invalidate_later(UPDATE_INTERVAL_SECS)

    # Data generation logic. Get random between -18 and -16 C, rounded to 1 decimal place
    temp = round(random.uniform(-18, -16), 1)

    # Get a timestamp for "now" and use string format strftime() method to format it
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    latest_dictionary_entry = {"temp": temp, "timestamp": timestamp}

    # Return everything we need
    return latest_dictionary_entry