from database.models.produto import Produto, db

def configura_tudo(app):
    db.connect()
    db.create_tables([Produto])
    app.teardown_appcontext(close_db)


def close_db(exception):
    if not db.is_closed():
        db.close()