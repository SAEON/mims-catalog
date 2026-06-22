from pathlib import Path

from flask import Blueprint, render_template

from odp.ui.base.forms import SearchForm

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
