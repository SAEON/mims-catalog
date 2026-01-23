from pathlib import Path

from flask import Blueprint, render_template,request,jsonify

from odp.ui.base.forms import SearchForm
from odp.ui.base import api, cli

bp = Blueprint(
    'home', __name__,
    static_folder=Path(__file__).parent.parent / 'static',
    static_url_path='/static/mims',
)


@bp.route('/')
def index():
    return render_template(
        'home.html',
        search_form=SearchForm(),
    )