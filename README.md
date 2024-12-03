# HTML, CSS, JavaScript, Node.js, and CGI Mini Projects

This repository contains multiple mini-projects completed using HTML, CSS, JavaScript, Node.js, and CGI. Each project is designed to practice core web development skills.

---

## Projects

### 1. **[format_validation_react.html](./format_validation_react.html)**

#### Assignment:
Using React.js, create an HTML form whose fields are validated during completion. The form contains the following fields:
- **Phone number**: Must start with "+370" followed by 8 digits.
- **Password**: Must contain at least one number, one uppercase letter, and one lowercase letter.
- **Years**: A number between 1900 and 2021.

Non-empty fields that do not conform to the format are colored red. After the field becomes valid, its original color should be restored. Fields use only the plain HTML element `<input type="text"/>`. Validation is implemented using React.js, without HTML5 validation attributes.

---

### 2. **[nodejs-serverside](./nodejs-serverside)**

#### Assignment:
Using Node.js, write a server-side application that:
- Sends a given HTML file (if it exists in the working directory) upon user request.
- Returns an HTTP 404 error if the file does not exist.

The application uses the **http**, **url**, **querystring**, and **fs** modules, with only asynchronous functions from the **fs** module.

---

### 3. **[filesearch](./filesearch)**

#### Assignment:
Create a web page with a text field and a button. When the user enters a file name (without an extension), JavaScript will search for files with the extensions `.html` and `.txt` in the same directory as the web page itself. 

- If a matching file is found (preferably `.html`), its content will be loaded into a `<div>` element.
- If no such file exists, the text input field will turn red.

The search is done asynchronously using AJAX. Both files are searched simultaneously (not sequentially), and the color of the input field will reset after the user starts editing again.

---

### 4. **[simple-webpage](./simple-webpage)**

#### Assignment:
Create a website with at least **two pages**:
1. **Description Page**: Contains a description of a topic (e.g., algorithm, database, conference) with relevant text and illustrations.
   - The page must use headings (up to level 3), paragraphs, and other common formatting tags.
   
2. **Form Submission Page**: Contains a data submission form with at least 5 different types of input elements (excluding buttons). 
   - Data input fields must be logically related to the selected topic.
   - The form must be linked to the description page with relative links.

The website should be styled with custom CSS to ensure a unified, aesthetic design that is user-friendly on different screen sizes.

---

### 5. **[cgi-apache-simple-webpage](./cgi-apache-simple-webpage)**

#### Assignment:
Create a CGI-based Perl program that:
- Takes form input, validates it, and returns an HTML response based on the selected theme (e.g., scientific data processing).
- The application must process the data (or simulate processing if complex) and return a web page with results.
- It should be secure, use tainted mode, and detect incomplete or invalid data.

The CGI program is accessible via `curl` from the command line. A short documentation in HTML format is provided on the website to describe the form fields and their expected inputs.

---
