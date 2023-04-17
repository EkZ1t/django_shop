async function sendPostRequest(url, data){
    return await fetch(
        url,  {
            method: 'POST',
            headers: {
                'Content-Type': 'application.json'
            },
            body: JSON.stringify(data)
        }
    )
    .then(response => response.json())
    .catch((error) => {console.error(error)})
}

sendPostRequest(
    'http://127.0.0.1:8000/auth/users/activation/',

{
    uid: "NQ", 
    token: 'bmni1a-9dd6bac13c78732a4b1be6a77ef1d9ee'

}
)