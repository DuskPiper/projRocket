from rocket.server import app

if __name__ == '__main__':
    # app.run()
    app.run(host='0.0.0.0', port=50011, threaded=True)
