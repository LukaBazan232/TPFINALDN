from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from Aplicacion.db import get_db

bp = Blueprint('peliculas', __name__)

@bp.route('/')
def index():
    db = get_db()
    peliculas = db.execute(
        """SELECT f.title AS titulo FROM film f """
    ).fetchall()
    return render_template('peliculas/index.html', peliculas=peliculas)