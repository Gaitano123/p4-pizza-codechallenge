from .pizza.api import app,db

if __name__ =="__main__":
    app.run(debug=True, port=5555)