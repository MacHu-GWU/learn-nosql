##encoding=utf8

from __future__ import print_function
import bottle

@bottle.route("/")
def home_page():
    mythings = ["apple", "orange", "banana", "peach"]
    return bottle.template("hello_world", username="Andrew", things=mythings)

@bottle.route("/testpage")
def test_page():
    return "this is a test page"

bottle.debug(True)
bottle.run(host="localhost", port=8080)