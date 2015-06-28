from scrumble import app
import os
from flask.ext.session import Session

if __name__ == "__main__":
    app.SECRET_KEY = "supersecret"
    app.config['SESSION_TYPE'] = 'filesystem'
    
    sess = Session()
    sess.init_app(app)
    
    port = int(os.environ.get("PORT", 5000))
    # Cache template for fast loading
    app.jinja_env.cache = {}
    app.run(host='0.0.0.0', port=port, debug=True)
