const mongoose = require('mongoose')
const Schema = mongoose.Schema

const urlSchema = new Schema({
    original_url: String,
    short_url: String
})

const UrlModel = mongoose.model("Url", urlSchema)
module.exports = UrlModel