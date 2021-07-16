const express = require("express");
const app = express();
var cors = require('cors');
const port = 1217;
const axios = require("axios");
const API_KEY = "$2b$10$X0kbxQICfdAyqkQCj6Lv3ugD2uvhllWkbr8mywZyx5s5llC9nbxCy";

app.use(cors());

app.get("/update-news-beans", (req, res)=>{
  let config = {
    url : "https://api.jsonbin.io/v3/b",
    method : "post",
    data : require("./scrapping_data/bean_news.json"),
    headers : {
      "Content-Type" : "application/json",
      "X-Master-Key" : API_KEY,
      "X-Bin-Private" : false,
      "X-Bin-Name" : "beans.json"
    }
  }
  axios(config).then((resp)=>{
    res.json(resp.data);
  }).catch((err)=>{
    res.status(500);
    res.json(err);
  });
});

app.get("/update-news-musa", (req, res)=>{
  let config = {
    url : "https://api.jsonbin.io/v3/b",
    method : "post",
    data : require("./scrapping_data/musa_news.json"),
    headers : {
      "Content-Type" : "application/json",
      "X-Master-Key" : API_KEY,
      "X-Bin-Private" : false,
      "X-Bin-Name" : "musa.json"
    }
  }
  axios(config).then((resp)=>{
    res.json(resp.data);
  }).catch((err)=>{
    res.status(500);
    res.json(err);
  });
});

app.get("/update-news-cassava", (req, res)=>{
  let config = {
    url : "https://api.jsonbin.io/v3/b",
    method : "post",
    data : require("./scrapping_data/cassava_news.json"),
    headers : {
      "Content-Type" : "application/json",
      "X-Master-Key" : API_KEY,
      "X-Bin-Private" : false,
      "X-Bin-Name" : "cassava.json"
    }
  }
  axios(config).then((resp)=>{
    res.json(resp.data);
  }).catch((err)=>{
    res.status(500);
    res.json(err);
  });
});

app.get("/news-beans", (req, res)=>{
  let config = {
    url : "https://api.jsonbin.io/v3/b/60e0b73755b7245a20d4ba71/latest",
    method : "get",
    headers : {
      "X-Master-key" : "$2b$10$X0kbxQICfdAyqkQCj6Lv3ugD2uvhllWkbr8mywZyx5s5llC9nbxCy"
    }
  }
  axios(config).then((resp)=>{
    res.json(resp.data);
  }).catch((err)=>{
    res.status(200);
    res.json(err);
  })
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
