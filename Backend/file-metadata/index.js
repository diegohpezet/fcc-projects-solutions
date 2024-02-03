const express = require('express');
const cors = require('cors');
require('dotenv').config()
const multer = require('multer')
// const bodyParser = require('body-parser')

var app = express();

app.use(cors());
app.use('/public', express.static(process.cwd() + '/public'));

app.get('/', function (req, res) {
  res.sendFile(process.cwd() + '/views/index.html');
});

app.post('/api/fileanalyse', multer().single('upfile'), (req,res) => {
  const file = req.file
  res.json({
    name: file.originalname,
    type: file.mimetype,
    size: file.size
  })
})


const port = process.env.PORT || 3000;
app.listen(port, function () {
  console.log('Your app is listening on port ' + port)
});
