// curl https://example.com/user/image?imgUrl=http://myimage.com/me.jpg

const express = require("express");
const axios = require("axios");
const app = express();
const port = 3000;

app.get('/user/image/', async function (req, res) {
    const imgUrl = req.query.imgUrl;
    const imageReq = await axios.get(imgUrl);
    //user.updateProfileImage(imageReq.data);
    res.send(imageReq.data);
});

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
  })