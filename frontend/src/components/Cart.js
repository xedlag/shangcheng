// Cart.js
// 显示购物车内容的组件。

import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Cart() {
  const [cartItems, setCartItems] = useState([]);

  useEffect(() => {
    axios.get('/api/cart-items/')
      .then(response => {
        setCartItems(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the cart items!', error);
      });
  }, []);

  return (
    <div>
      <h1>Shopping Cart</h1>
      <ul>
        {cartItems.map(item => (
          <li key={item.id}>
            {item.product.name} - ${item.product.price} x {item.quantity}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Cart;
