DROP TABLE books;
DROP TABLE authors;


CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    author_id INT REFERENCES authors(id), 
    publisher VARCHAR(255),
    publication_date VARCHAR(255)
);
