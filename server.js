var express = require('express');
let app = express();
let data = require('./technology.js')
console.log(data[0])
let router = express.Router();
app.get('/*',function(req,res){
  var item = data[Math.floor(Math.random()*data.length)];
  res.json({
    "quote":item.quote,
    "author":item.author
  })
})

app.listen('5000',function(err){
  if(err)
    console.log(err);
  else
    console.log("Traveling through port-> 5000")
})
