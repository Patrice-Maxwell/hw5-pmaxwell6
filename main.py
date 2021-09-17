import flask


app = flask.Flask(__name__)
shows=["Doctor Who" , "Smallville" , "Arrowverse" , "A.O.S" , "HIMYM"]
cards=[
    "/static/DoctorWho.jpg",
    "/static/Smallville.png",
    "/static/Arrowverse.jpeg",
    "/static/AOShield.jpg",
    "/static/HIMYM.jpg",



]

@app.route("/")
def index():
    return  flask.render_template(
        "index.html", name= "Rice" , len = len(shows) , shows = shows , cards= cards,
    )
app.run(use_reloader = True , debug=True)
