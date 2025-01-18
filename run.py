from app import create_app

app = create_app()

if __name__ == "__main__":
    # app = app()
    app.run(debug=True)
