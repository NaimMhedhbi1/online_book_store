from shop import app,db #improt app and df from shop 
if __name__ =="__main__":
    app.app_context().push() 
    db.create_all()
    app.run(debug=True)
#In a working environment, avoid running the development server or turning on the built-in debugger. Any Python code may be executed from the browser using the debugger. It has a pin protection, but you shouldn't rely on that to keep it secure.
#In essence, it prevents you from running code when the file is imported as a module but permits it when the file runs as a script.
#Simply import the db object from an interactive Python shell and use the SQLAlchemy.create all() method to build the basic database, creating the tables and database
#Throughout a request, CLI command, or other action, the application context keeps track of the application-level data.
#Upon processing a request, Flask automatically pushes an application context.