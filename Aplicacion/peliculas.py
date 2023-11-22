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
        """SELECT f.title AS titulo, f.film_id FROM film f """
    ).fetchall()
    return render_template('peliculas/index.html', peliculas=peliculas)



@bp.route('/<int:id>/')
def detalle(id):
    db = get_db()
    pelicula = db.execute(
        """SELECT f.title AS titulo ,rating as clasificacion, 
            c.name AS categoria ,length as tiempo, l.name as idioma ,
              description as descripcion 
            FROM film f JOIN film_category fc ON f.film_id = fc.film_id  
            JOIN category c ON c.category_id = fc.category_id 
            join language l on l.language_id = f.language_id
            WHERE f.film_id = ?
        """, (id,)
    ).fetchone()

    actores = db.execute( """
                    select last_name as nombre , first_name as apellido , actor_id from actor
                        join film_actor USING(actor_id)
                        where film_id = ?
            
                         """, (id,)).fetchall()

    return render_template('peliculas/detalle.html', pelicula=pelicula, actores = actores)
