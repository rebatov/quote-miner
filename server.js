var express = require('express');
let app = express();
let data = require('./technology.js')
console.log(data[0])
var port=Number(process.env.PORT || 3000);
let router = express.Router();

app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});

app.get('/*',function(req,res){
  var item = data[Math.floor(Math.random()*data.length)];
  res.json({
    "quote":item.quote,
    "author":item.author
  })
})

app.listen(port,function(err){
  if(err)
    console.log(err);
  else
    console.log("Traveling through port-> "+port)
})
