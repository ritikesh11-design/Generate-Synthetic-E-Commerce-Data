SELECT c.name AS customer_name,
       p.name AS product_name,
       oi.quantity,
       p.price,
       py.amount AS total_amount,
       py.payment_date
FROM customers c
JOIN orders o ON c.id = o.customer_id
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON p.id = oi.product_id
JOIN payments py ON py.order_id = o.id;
