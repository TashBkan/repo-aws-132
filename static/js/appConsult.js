function consult_user() {
    let id = document.getElementById("ident").value
    fetch('/consult_user', {
        'method': 'post',
        'headers': {'Content-Type': 'application/json'},
        'body': JSON.stringify(id)
    })
}