
function AddTown() {
    let Town = document.getElementById('town').value
    let Date = document.getElementById('visit_date').value
    fetch('/add', {
        method: 'post',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'town': Town,
                             'visit_date': Date})
    })
}
async function DeleteAll(){
    await fetch('/delete')
    location.reload()
}
