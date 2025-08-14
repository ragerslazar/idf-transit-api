from .routes.metros.MetroRoutes import metro_routes

def register_blueprints(app):
    app.register_blueprint(metro_routes, url_prefix="/api/v1/metro/")
