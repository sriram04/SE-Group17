import React from "react";
import { createRoot } from "react-dom/client";
import { Provider } from "react-redux";
import store from "./store";
import "./index.css";

import App from "./App";
import * as serviceWorker from "./serviceWorker";
// import express from 'express'
import { BrowserRouter } from "react-router-dom";

// const app = express();
// app.use(express.static("")); //here is important thing - no static directory, because all static :)

// app.get("/*", function(req, res) {
//   res.sendFile("index.html");
// });

const container = document.getElementById("root");
const root = createRoot(container);

root.render(
  <Provider store={store}>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </Provider>
);

// If you want your app to work offline and load faster, you can chađinge
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
