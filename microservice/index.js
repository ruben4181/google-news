const express = require("express");
const app = express();
const port = 1217;

app.get("/news-beans", (req, res)=>{
  let response = require("./scrapping_data/bean_news.json");
  res.json(response);
});

app.get("/news-musa", (req, res)=>{
  let response = require("./scrapping_data/musa_news.json");
  res.json(response);
});

app.get("/news-cassava", (req, res)=>{
  let response = require("./scrapping_data/cassava_news.json");
  res.json(response);
});

app.listen(port, ()=>{
  console.log("Server listening at port", port);
})
