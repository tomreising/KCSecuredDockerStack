"""Module for Base Flask App Code"""
import os
from flask import Flask, request, redirect, make_response
from site_pages import (
	login_home,
    login_success
	)
from tokecloak.authenticator import KCAuth

KC_CLIENTID = os.getenv("KC_CLIENTID") if os.getenv("KC_CLIENTID") is not None else "pyauth"
KC_CLIENTREALM = os.getenv("KC_CLIENTREALM") if \
    os.getenv("KC_CLIENTREALM") is not None else "fullstack"
KC_CLIENTSECRET = os.getenv("KC_CLIENTSECRET") if \
    os.getenv("KC_CLIENTSECRET") is not None else "Etpm55fqWJldG07p9h7PGNww54P7oRy6"
KC_DOMAIN = os.getenv("KC_DOMAIN") if \
    os.getenv("KC_DOMAIN") is not None else "http://keycloak.fullstack.com"
AUTH_DOMAIN = os.getenv("AUTH_DOMAIN") if \
    os.getenv("KC_DOMAIN") is not None else "fullstack.com"
# Flask constructor
app = Flask(__name__)
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET"])
def ghp():
    """
    Handle initial calls to root. Returns login page.
    """
    return login_home.gen_login("/login")

@app.route('/auth')
def check_creds():
    """
    Authentication end point checks cookies for token and
    validates token if it exists otherwise redirect to root
    sign in page
    """
    token = request.cookies.get('token')
    if token is None:
        return redirect("/", code=302)
    if token is not None:
        kc_auth = KCAuth(
		KC_DOMAIN, KC_CLIENTREALM,
		KC_CLIENTID, KC_CLIENTSECRET
		)
        resp = kc_auth.token_introspect(token)
        if resp['active'] is False:
            return redirect("/", code=302)
        if resp['active'] is True:
            return "Valid Token", 200
    return redirect("/", code=302)

@app.route('/login', methods =["POST"])
def gfg():
    """
    end point hit upon sign in submit. Retrieves user token
    and redirects if invalid entry.
    """
	# getting input with name = fname in HTML form
    user = request.form.get("username")
	# getting input with name = lname in HTML form
    password = request.form.get("password")
    kc_auth = KCAuth(
		KC_DOMAIN, KC_CLIENTREALM,
		KC_CLIENTID, KC_CLIENTSECRET
		)
    token = kc_auth.get_token_basic(user,password)
    resp = kc_auth.token_introspect(token)
    if resp['active'] is False:
        return redirect("/", code=302)
    response = make_response(login_success.gen_success(), 200)
    response.set_cookie('token', token, domain = AUTH_DOMAIN, path="/")
    return response

if __name__=='__main__':
    app.run(port=5000, host="0.0.0.0", debug=False)
