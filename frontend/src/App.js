// src/App.js
// React 应用的主组件，定义路由和页面结构。

import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import ProductList from './components/ProductList';
import Cart from './components/Cart';
import OrderHistory from './components/OrderHistory';

function App() {
  return (
    <Router>
      <div className="App">
        <Switch>
          <Route path="/" exact component={ProductList} />
          <Route path="/cart" component={Cart} />
          <Route path="/orders" component={OrderHistory} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
