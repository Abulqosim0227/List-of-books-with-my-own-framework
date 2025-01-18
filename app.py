from Nimbus.app import Nimbusapp
from storage import BookStorage
from whitenoise import WhiteNoise
from auth import STATIC_TOKEN, TokenMidleware, login_required, on_exception

app = Nimbusapp()

book_storage = BookStorage()
book_storage.create(name="Atomic Habits", author="James Clear")
app.add_middleware(TokenMidleware)
app.add_exception_handler(on_exception)

static_dir = "static"
app.wsgi_app = WhiteNoise(app.wsgi_app, root=static_dir, prefix="static/")

@app.route("/", allowed_methods=["get"])
def home(request, response):
    books = book_storage.all()
    response.html = app.template("index.html", context={"books": books})

@app.route("/login", allowed_methods=["post"])
def login(req, resp):
    resp.json = {"token": STATIC_TOKEN}

@app.route("/books", allowed_methods=["post"])
@login_required
def create_book(req, resp):
    book = book_storage.create(**req.POST)
    resp.status_code = 201
    resp.json = book._asdict()

@app.route("/books/{id:d}", allowed_methods=["delete"])
@login_required
def delete_book(req, resp, id):
    book_storage.delete(id)
    resp.status_code = 204

if __name__ == "__main__":
    app.run()
