const mongoose = require('mongoose')
const { Schema } = mongoose

const exerciseSchema = new Schema({
    username: {type: String},
    description: {type: String},
    duration: {type: Number},
    date: {type: Date},
})

const Exercise = mongoose.model("Exercise", exerciseSchema)
module.exports = Exercise