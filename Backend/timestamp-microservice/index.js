var express = require('express');
var app = express();

// enable CORS (https://en.wikipedia.org/wiki/Cross-origin_resource_sharing)
// so that your API is remotely testable by FCC 
var cors = require('cors');
app.use(cors({optionsSuccessStatus: 200}));  // some legacy browsers choke on 204

// http://expressjs.com/en/starter/static-files.html
app.use(express.static('public'));

// http://expressjs.com/en/starter/basic-routing.html
app.get("/", function (req, res) {
  res.sendFile(__dirname + '/views/index.html');
});


// API endpoints
app.get("/api", function(req,res) {
  let date = new Date()

  return res.json({
    unix: date.getTime(),
    utc: date.toUTCString()
  })
})

app.get("/api/:date", function (req, res) {
  // Build Date object from params
  function getData(time) {
      dateObj = new Date(time)
      return !isNaN(dateObj)
  }

  // If it is valid get save it, else get unix
  let date = getData(req.params.date) ? new Date(req.params.date) : new Date(Math.floor(req.params.date))

  if (isNaN(Date.parse(date))) {
    return res.json({
      error: "Invalid Date"
    })
  } else {
    return res.json({
      unix: date.getTime(),
      utc: date.toUTCString()
    })
  }
});

// listen for requests :)
var listener = app.listen(3000, function () {
  console.log('Your app is listening on port ' + listener.address().port);
});
