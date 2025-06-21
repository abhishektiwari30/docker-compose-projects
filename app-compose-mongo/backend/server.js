const express = require('express');
const mongoose = require('mongoose');
const app = express();

app.use(express.json());

mongoose.connect(process.env.MONGO_URL, { useNewUrlParser: true, useUnifiedTopology: true });

const Data = mongoose.model('Data', { message: String });

app.get('/data', async (req, res) => {
  const data = await Data.find();
  res.json(data);
});

app.post('/data', async (req, res) => {
  const newData = new Data({ message: req.body.message });
  await newData.save();
  res.json(newData);
});

const redis = require('redis');
const redisClient = redis.createClient({
 url: 'redis://redis:6379'
});

redisClient.connect()
 .then(() => console.log("Connected to Redis"))
 .catch(console.error);

app.listen(3000, () => console.log("App running on port 3000"));
