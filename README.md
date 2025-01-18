
```markdown
# List of Books with My Own Framework

This project demonstrates a book management application built using **Nimbus**, a web framework I created. The app allows users to manage a list of books with features such as adding, viewing, and deleting books. The project also includes token-based authentication and static file handling using WhiteNoise.

## Features

- **Book Management**: Add, view, and delete books.
- **Authentication**: Token-based authentication for protected routes.
- **Static File Handling**: Serve static files efficiently using WhiteNoise.
- **Custom Framework**: Built with Nimbus, a custom web framework.

## Installation

To get started with this project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/Abulqosim0227/List-of-books-with-my-own-framework.git
    cd List-of-books-with-my-own-framework
    ```

2. Set up a virtual environment and install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. Set up environment variables:
    - `STATIC_TOKEN`: A static token used for authentication.
    ```bash
    export STATIC_TOKEN="your_static_token"
    ```

4. Run the application:
    ```bash
    python app.py
    ```

    The application will be available at `http://localhost:8000`.

## Routes

- **GET `/`**: Displays the list of books.
- **POST `/login`**: Provides a static token for authentication.
- **POST `/books`**: Create a new book (requires authentication).
- **DELETE `/books/{id}`**: Delete a book by its ID.

## Example Usage

1. **Login and get a token**:
    - Make a `POST` request to `/login` to receive a static token.

2. **Create a new book**:
    - Make a `POST` request to `/books` with the following JSON body:
    ```json
    {
        "name": "Atomic Habits",
        "author": "James Clear"
    }
    ```

    Example `curl` command:
    ```bash
    curl -X POST http://localhost:8000/books -H "Authorization: Bearer your_static_token" -d '{"name": "Atomic Habits", "author": "James Clear"}'
    ```

3. **Delete a book**:
    - Make a `DELETE` request to `/books/{id}`, replacing `{id}` with the book's ID.

## Dependencies

- **Nimbus**: The web framework used for building this application.
- **WhiteNoise**: Serves static files in production.
- **WebOb**: Provides request and response objects.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, feel free to open an issue on GitHub or contact me directly.

- **Author**: [Abulqosim Rafiqov](https://github.com/Abulqosim0227)
```

