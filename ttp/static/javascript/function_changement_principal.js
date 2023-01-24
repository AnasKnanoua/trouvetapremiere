
function changement_principal(){   
    alert(1) 
    var lieu = document.getElementById("choix_lieu").value       

    var choix_dep = document.getElementById("choix_dep").value    
    var choix_ville = document.getElementById("choix_ville").value    
    var choix_fil = document.getElementById("choix_fil").value      
    alert(2)

    alert("here")
    let formData = new FormData();
    alert(3)
    formData.append('lieu', document.querySelector("#choix_lieu").value);
    formData.append('choix_dep', document.querySelector("#choix_dep").value);
    formData.append('choix_ville', document.querySelector("#choix_ville").value);
    formData.append('choix_fil', document.querySelector("#choix_fil").value);

    const request = new Request('{% url "compute" %}', {method: 'POST', body: formData});

    fetch(request)
        .then(response => response.json())
        .then(result => {
            document.getElementById("affiche").innerHTML = "hey"
            document.getElementById("affiche").innerHTML += result["operation_result"];
})
    

    
}