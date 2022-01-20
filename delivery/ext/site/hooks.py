def init_app(app):
    
    @app.before_first_request
    def init_everything():
        print('Roda antes do primeiro request.')