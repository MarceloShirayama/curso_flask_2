from flask import Blueprint, render_template


bp = Blueprint("site", __name__)

@bp.route("/")
def index():
    return render_template(
        "index.html",
        name="Marcelo Shirayama",
        company="CodeShow",
        texto1="Foods Delivery",
        texto2="Vários pratos a sua escolha:",
        comidas=["pizza", "lanche", "japonês"]
    )
