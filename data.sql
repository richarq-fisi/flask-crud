CREATE DATABASE flask_crud;
USE flask_crud;

CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    correo VARCHAR(255) NOT NULL,
    telefono INT
);

INSERT INTO clientes (nombre, correo, telefono)
VALUES 
('Juan Guzman', 'juan.guzman@gmail.com', 123456789),
('María Alvarado', 'maria.alvarado@gmail.com', 234567890),
('Carlos Mendoza', 'carlos.mendoza@gmail.com', 345678901),
('Ana Gómez', 'ana.gomez@gmail.com', 456789012);

SELECT * FROM clientes