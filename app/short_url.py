from flask import (
    Blueprint, render_template, request, redirect
)
import random
import string
import validators
from . import db

bp = Blueprint('short_url', __name__)


@bp.route('/short_url', methods=['POST', 'GET'])
# Returns the shortened URL - Stores submitted URL in DB, generating unique key, returns unique key on end of domain
def shorten_url():
    if request.method == 'POST':
        req_json = request.get_json()
        url = req_json['url']
        if not url:
            error = 'Please enter a URL to shorten.'
            return render_template('/short_url.html', error=error)

        elif validators.url(url) is False:
            error = 'Please enter an valid URL.'
            return render_template('/short_url.html', error=error)

        # False here means URL given is in the database already,
        # and we can retrieve and return the shortened one that already exists

        if url.startswith('http://') is False and url.startswith('https://') is False:
            url = 'http://' + url

        if db.check_url_in_db(url) is False:
            short_url = db.get_short(url)
            return render_template('/short_url.html', short_url=short_url, url=url)

        else:
            short_url = generate_shortened_url()
            db.insert_urls(short_url, url)
            return render_template('/short_url.html', short_url=short_url, url=url)


@bp.route('/url/<short>', methods=['GET'])
def return_original_url(short):
    original_url = db.get_original(short)
    return redirect(original_url)


def generate_shortened_url():
    short_url = ''.join(random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits) for _ in range(8))
    return short_url
