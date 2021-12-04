const authentication = [
                        {username: "user",
                         password: "cc74f5e2594f7103105b3fce80dc794f778837f7"},
                        {username: "Learning Connections",
                         password: "8acbac4983d82f62b41b6542013c73a52a4f6a32"       
                        }];
                        

const  env = require('dotenv').config();
const crypto = require('crypto');
var  hash;

const cors = require('cors');
const myExpress = require('express');
const app = myExpress();
const jwt = require('jsonwebtoken');
const { response } = require('express');
//
var token;


console.log(token);


const root =  function (req, res) {
   
    res.set({'Content-Type': 'text/html'});
    console.log('Sending index.html');
    res.sendFile('views/index.html',{root: __dirname},()=>{console.log('Error sending file')} );

};

const getToken = function(req, res){
    /* 
        l'utente invia tramite POST in formato x-www-form-urlencoded
        username, seed, userHash = sha(seed+sha(pwd))
        L'autenticatore possede username-> sha(pwd)
    */
    let username;
    let seed;
    let userHash;

    username = req.body.USERNAME;
    seed = req.body.SEED;
    userHash = req.body.HASH;

    hash= crypto.createHash('sha1');
    
    let authorized = false;
    let found = false;

    for (let auth of authentication) 
        if(auth.username === username) {
            var ourHash = auth.password;
            found = true;
        }
  

    if (found === true){
        console.log("trovato utente ");
        if(userHash === hash.update(seed+ourHash).digest('hex')){
            authorized = true;
            console.log("autorizzato !, signing with "+process.env.SECRET_KEY);

            token = jwt.sign({scope:"Learning Connections webinar",
                            exp: Math.floor(Date.now() / 1000) + (60 * 60)},
                            process.env.SECRET_KEY);
                            res.status(201);
                            res.send({TOKEN:token});
                            
            }
    }
    if (! authorized)  { 
            res.status(403);
            res.end();   
    }    
}


const retrieveData = function(req, res){
    const thisToken = req.query.token;
    
    try {
        console.log(jwt.verify(thisToken,process.env.SECRET_KEY));
        res.set({'Content-Type':'application/json'});
        res.write('[{"id":1, "name":"Private data 1"},{"id":2, "name":"Private data 2"}]');
        res.end();
  
    } catch (err) {
        console.log("non autorizzato");
        res.status(403).send("non autorizzato");
    }
    
          
};


app.use(cors());
app.use(myExpress.urlencoded({ extended: true }));

app.get('/',root);
app.get('/list',retrieveData);
app.post('/getToken', getToken);

app.listen(process.env.PORT,()=>{console.log("Server started, listening on port: "+process.env.PORT);});




