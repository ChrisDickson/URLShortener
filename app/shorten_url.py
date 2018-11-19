from flask import (
    Blueprint, flash, render_template, request, redirect
)
import random
import string
import re
from app.db import get_db

bp = Blueprint('shorten_url', __name__, url_prefix='/shorten_url')


@bp.route('/', methods=['POST'])
# Returns the shortened URL - Stores submitted URL in DB, generating unique key, returns unique key on end of domain
def shorten_url():
    if request.method == 'POST':
        shortened_url = ''

        req_json = request.get_json()
        url = req_json['url']

        db = get_db()

        if not url:
            error = 'Please enter a URL to shorten.'

        elif url.startswith('https://') or url.startswith('http://') is False:
            url = 'http://'+url

        elif re.match('(https|http)(\:\/\/www)(\.)(.+)(\.)(\w{2,3})(.+)', url) is False:
            error = 'Please enter an valid URL.'
            
        elif db.execute(
            'SELECT id FROM urls WHERE url = ?', (url,)
        ).fetchone() is not None:
            shortened_url = db.execute(
                'SELECT short FROM urls WHERE url = ?', (url,)
            )
            return render_template('/short_url')

        if error is None:
            db.execute('INSERT INTO urls (url, shortened_url) VALUES ? ?',
                (url, generate_shortened_url())
            )
            db.commit()
            return render_template('/short_url', shortened_url, url)

        flash(error)

    return render_template('short_url')


@bp.route('/<short_url>')
def return_original_url(short_url):
    db = get_db()

    original_url = db.execute(
        'SELECT url FROM urls WHERE short = ?', (short_url,)
    )

    return redirect(original_url)


def generate_shortened_url():
    shortened_url = ''.join(random.choice(string.ascii_uppercase, string.ascii_lowercase, string.digits) for _ in range(8))

    return shortened_url
