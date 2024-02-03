const mongoose = require('mongoose')
const { Schema } = mongoose

const logSchema = new Schema({
    username: {type: String},
    count: {type: Number},
    _id: {type: mongoose.Schema.Types.ObjectId},
    log: [{
      description: {type: String},
      duration: {type: Number},
      date: {type: Date}
    }]
    
})

const Log = mongoose.model("Log", logSchema)
module.exports = Log