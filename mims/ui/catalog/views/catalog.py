from flask import Blueprint, render_template, request

from mims.ui.catalog.forms import SearchForm
from odp.ui.base import cli

bp = Blueprint('catalog', __name__)


@bp.route('/')
def index():
    page = request.args.get('page', 1)
    text_q = request.args.get('q')

    api_filter = ''
    ui_filter = ''
    if text_q:
        api_filter += f'&text_q={text_q}'
        ui_filter += f'&q={text_q}'

    records = cli.get(f'/catalog/MIMS/records?page={page}{api_filter}')
    return render_template(
        'index.html',
        records=records,
        filter_=ui_filter,
        search_form=SearchForm(request.args),
    )


@bp.route('/<path:id>')
def view(id):
    record = cli.get(f'/catalog/MIMS/records/{id}')
    return render_template(
        'record.html',
        record=record,
    )
