const urlProfe = 'https://notes-deploy-api.herokuapp.com/teachers';

fetch(urlProfe, {
    'mode': 'cors',
    'headers': {
        'Access-Control-Allow-Origin': '*',
    }
});
.then(response => response.json() )
.then(data => {
    console.log(data)
})
.catch(err=>console.log(err))