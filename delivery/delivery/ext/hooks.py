
def init_app(app):

    @app.before_first_request
    def init_everything():
        """Roda sempre que for feito o primeiro request"""
        print("Primeiro request!")


    @app.before_request
    def before_request():
        """Roda sempre antes de um request"""
        print("request ...")        
    

    @app.after_request
    def after_request(response):
        """Roda sempre depois de um request"""
        print("request efetuado!")
        return response
