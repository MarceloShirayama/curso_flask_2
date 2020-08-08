from flask import Blueprint, render_template


nameby = "Marcelo Shirayama"
company = "CodeFoods"

bp = Blueprint("site", __name__)


@bp.route("/")
@bp.route("/home")
def index():
    return render_template(
        "index.html",
        name=nameby,
        site_name=company,
        site_subtitle="O melhor site de delivery",
    )


@bp.route("/sobre")
def about():
    return render_template(
        "about.html",
        name=nameby,
        site_name=company,
        site_subtitle="O melhor site de delivery de \
            comida vegan do mundo! da twitch! e do universo!!!",
    )


@bp.route("/restaurantes")
def restaurants():
    return render_template(
        "restaurants.html",
        name=nameby,
        site_name=company
    )
