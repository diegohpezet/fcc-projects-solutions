const express = require('express')
const app = express()
const cors = require('cors')
require('dotenv').config()

// App config
app.use(cors())
app.use(express.static('public'))
app.use(express.json());
app.use(express.urlencoded( {extended: true} ));

// Set up mongoose
const mongoose = require("mongoose");
mongoose.connect(process.env.URI);

// Models
const User = require("./models/User");
const Exercise = require("./models/Exercise")

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/views/index.html')
});

app.route('/api/users')
  .get((req, res) => {
    User.find().exec().then(data => {
      res.json(data)
    })
  })
  .post((req, res) => {
    const thisUser = new User({
      username: req.body.username
    })
    thisUser.save()
    res.json({
      _id: thisUser._id,
      username: thisUser.username
    })
  })

app.post('/api/users/:_id/exercises', async (req,res) => {
  // Get user data
  const myUser = await User.findById(req.params._id)
  if (!myUser){
    res.send("User not found.")
  }

  // Buid Exercise object
  const thisExercise = new Exercise({
    user_id: myUser._id,
    username: myUser.username,
    description: req.body.description,
    duration: req.body.duration,
    date: req.body.date ? req.body.date : new Date()
  }) 
  const exercise = await thisExercise.save()
      
  res.json({
    _id: myUser._id,
    username: myUser.username,
    description: exercise.description,
    duration: exercise.duration,
    date: new Date(exercise.date).toDateString()
  })
})


app.get('/api/users/:_id/logs', async (req, res) => {
  const {from, to, limit} = req.query
  const id = req.params._id
  const user = await User.findById(id)
  if (!user) {
    res.send("Could not find user")
    return;
  }
  let dateObj = {}
  if (from) {
    dateObj["$gte"] = new Date(from)
  }
  if (to) {
    dateObj["$lte"] = new Date(to)
  }
  let filter = {
    username: user.username
  }
  if (from || to) {
    filter.date = dateObj
  }

  const exercises = await Exercise.find(filter).limit(+limit ?? 500)
  const log = exercises.map(e => ({
    description: e.description,
    duration: e.duration,
    date: new Date(e.date).toDateString()
  }))
  res.json({
    username: user.username,
    count: exercises.length,
    _id: user._id,
    log
  })
})


app.get('/api/reset', (req, res) => {
  User.deleteMany({}).exec()
  Exercise.deleteMany({}).exec()
})

const listener = app.listen(process.env.PORT || 3000, () => {
  console.log('Your app is listening on port ' + listener.address().port)
})
