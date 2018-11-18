from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from app.db import get_db



@app.route('/shorten_url', methods=['POST'])
# Returns the shortened URL - Stores submitted URL in DB, generating unique key, returns unique key on end of domain
def shorten_url():
    req_json = request.get_json()
    url = req_json['url']


# Gets original URL using unique code at end of shortened URL to search DB
def return_original_url(short_url):
    print('test')
    return