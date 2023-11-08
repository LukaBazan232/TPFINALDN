from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from Aplicacion.db import get_db

bp = Blueprint('actor', __name__,url_prefix="/actor/")

@bp.route('/')
def index():
    db = get_db()
    actores = db.execute(
        """ SELECT first_name as nombre , last_name as apellido FROM film f
             join film_actor fa on f.film_id = fa.film_id 
             join actor a on fa.actor_id = a.actor_id"""
    ).fetchall()
    return render_template('actor/index.html', actores = actores)