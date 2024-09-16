CREATE TABLE pedidos (
    id SERIAL PRIMARY KEY,
    cliente VARCHAR(100),
    prato VARCHAR(100),
    quantidade INT
);

CREATE TABLE

estoque (
    id SERIAL PRIMARY KEY,
    produto VARCHAR(100),
    quantidade INT
);