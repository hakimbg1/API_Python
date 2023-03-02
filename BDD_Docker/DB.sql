CREATE DATABASE mydatabase;

USE mydatabase;

CREATE TABLE foods (
    ID INT PRIMARY KEY,
    Nom VARCHAR(255) ,
    typefood VARCHAR(255),
    adress VARCHAR(255),
    note INT
); ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Chargement des données

INSERT INTO foods (ID ,Nom, typefood, adress, note) VALUES
(1,'Poulet rôti', 'Plat principal', '12 Rue de la Paix, Paris', 4),
(2,'Salade César', 'Entrée', '25 High Street, Londres', 3),
(3, 'Pizza Margherita', 'Plat principal', '10 Via della Repubblica, Rome', 5),
(4, 'Moules marinières', 'Plat principal', '38 Rue du Vieux Port, Marseille', 4),
(5, 'Tarte aux pommes', 'Dessert', '8 Rue de la Liberté, Lyon', 4),