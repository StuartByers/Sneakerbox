DROP TABLE IF EXISTS cal_sneakers;
DROP TABLE IF EXISTS brands;

CREATE TABLE brands (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE cal_sneakers (
  id SERIAL PRIMARY KEY,
  model VARCHAR(255),
  date VARCHAR(255),
  image_url VARCHAR(2048),
  brand_id INT NOT NULL REFERENCES brands(id)
);

INSERT INTO brands (name) VALUES ('Nike');

INSERT INTO brands (name) VALUES ('Adidas');

INSERT INTO brands (name) VALUES ('Jordan Brand');

INSERT INTO brands (name) VALUES ('Yeezy');

INSERT INTO brands (name) VALUES ('New Balance');