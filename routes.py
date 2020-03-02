from config import app
from controller_functions import main, add_dojo, add_ninja

app.add_url_rule("/", view_func=main)
app.add_url_rule("/add_dojo", view_func=add_dojo, methods=["POST"])
app.add_url_rule("/add_ninja", view_func=add_ninja, methods=["POST"])