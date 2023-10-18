from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from Aplicacion.db import get_db

bp = Blueprint('language', __name__,url_prefix="/lenguaje/")

@bp.route('/')
def index():
    db = get_db()
    language = db.execute(
        """SELECT name  FROM language """
    ).fetchall()
    return render_template('language/index.html', language= language)
