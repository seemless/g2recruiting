__author__ = 'root'

from g2recruiting import app

@app.route('/test')
def test():
    return 'hi'

