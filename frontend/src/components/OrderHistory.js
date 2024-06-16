// OrderHistory.js
// 显示订单历史的组件。

import React, { useState, useEffect } from 'react';
import axios from 'axios';

function OrderHistory() {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    axios.get('/api/orders/')
      .then(response => {
        setOrders(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the orders!', error);
      });
  }, []);

  return (
    <div>
      <h1>Order History</h1>
      <ul>
        {orders.map(order => (
          <li key={order.id}>
            Order #{order.id} - ${order.total_price}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default OrderHistory;
