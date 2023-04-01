INSERT INTO custormers (id, name , city, country)
VALUES(105 , 'arash', 'mashhad', 'iran')

INSERT INTO products(id, name, price, count)
VALUES(1002, 'iphone', 100000000, 100)
 
SELECT * 
FROM products
WHERE name = 'arash'

DELETE FROM custormers
WHERE name = 'arash'

UPDATE products
SET price = price * 0.80