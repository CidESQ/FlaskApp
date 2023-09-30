CREATE DATABASE flaskcontacts CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE flaskcontacts; 

CREATE TABLE IF NOT EXISTS contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fullname VARCHAR(255),
    phone VARCHAR(255),
    email VARCHAR(255)
);