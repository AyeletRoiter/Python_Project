
## B\&B – A Web Platform for Finding and Managing Zimmers

**B\&B** is a web application built with Flask that provides an easy and efficient way for users to find available zimmers (B\&B-style lodgings) across Israel, and for property owners to manage their listings.

### Key Features

* Search and filter zimmers by name, region, or price range
* View detailed information for each listing, including images, pricing, location, and amenities (e.g., pool, jacuzzi)
* Add new zimmer listings through a dedicated submission form
* Secure login system for property owners
* Account management dashboard displaying the owner’s zimmers
* Edit or delete zimmer listings from the account panel
* Responsive and modern front-end design using Bootstrap and HTML templates

### Technologies Used

* **Backend**: Python, Flask
* **Frontend**: HTML, CSS, Bootstrap
* **Templating**: Jinja2
* **Additional Components**: Modular Python files for database operations (e.g., `Add_Zimmer`, `Delete_Zimmer`, `Login`, etc.)

### Getting Started

1. Ensure Python 3.9 or higher is installed.
2. (Optional) Install required dependencies using a `requirements.txt` file, if available.
3. Run the server with:

   ```bash
   python server.py
   ```
4. Open your browser and navigate to `http://localhost:2024`
