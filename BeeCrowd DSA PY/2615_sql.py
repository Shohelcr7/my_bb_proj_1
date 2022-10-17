
CREATE TABLE customer(
id int,
name varchar(32),
street varchar(64),
city varchar(28),
PRIMARY KEY(id )
);
 
INSERT INTO customer (id, name, street,city)
VALUES (1, 'Giovanna Goncalves Oliveira','Rua Mato Grosso','Canoas'),
(2,'Kauã Azevedo Ribeiro','Travessa Ibiá','Uberlândia'),
(3,'Rebeca Barbosa Santos','Rua Observatório Meteorológico','Salvador'),
(4,'Sarah Carvalho Correia','Rua Antônio Carlos da Silva','Uberlândia'),
(5,'João Almeida Lima','Rua Rio Taiuva','Ponta Grossa'),
(6,'Diogo Melo Dias','Rua Duzentos e Cinqüenta','Várzea Grande'); 

select distinct city from customer;