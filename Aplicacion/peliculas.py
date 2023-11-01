from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from Aplicacion.db import get_db

bp = Blueprint('peliculas', __name__,url_prefix="/peliculas/")

@bp.route('/')
def index():
    db = get_db()
    peliculas = db.execute(
        """SELECT f.title AS titulo FROM film f """
    ).fetchall()
    return render_template('peliculas/index.html', peliculas=peliculas)



@bp.route('/<int:id>/')
def detalle(id):
    db = get_db()
    pelicula = db.execute(
        """SELECT f.title AS titulo ,rating as clasificacion FROM film f 
            WHERE f.film_id = ?
        """, (id,)
    ).fetchone()
    return render_template('peliculas/detalle.html', pelicula=pelicula)
