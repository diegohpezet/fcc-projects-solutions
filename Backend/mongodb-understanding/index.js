require("dotenv").config()
const express = require('express')
const app = express()
const path = require('path')
const port = process.env.PORT || 3000

// App settings
app.use('/public', express.static(`${process.cwd()}/public`))

// Set up mongoose
const mongoose = require('mongoose')
mongoose.connect(process.env.URI)

// Get model for URLs
const UrlModel = require("./models/Url")

app.get('/', async (req,res) => {
    const urls = await UrlModel.find()
    res.send(urls)
})

app.listen(port, () => {
    console.log(`App running on port ${port}`)
})
