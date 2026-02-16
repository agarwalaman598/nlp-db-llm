async function ask() {
    const q = document.getElementById("q").value;

    document.getElementById("sql").innerText = "Processing...";
    document.getElementById("table").innerHTML = "";

    const res = await fetch("http://127.0.0.1:5000/query", {
        method:"POST",
        headers:{ "Content-Type":"application/json"},
        body:JSON.stringify({question:q})
    });

    const data = await res.json();

    document.getElementById("sql").innerText = data.error || data.sql;

    if(!data.result || data.result.length===0) return;

    const headers = Object.keys(data.result[0]);
    const table = document.getElementById("table");

    table.innerHTML = "<tr>"+headers.map(h=>`<th>${h}</th>`).join("")+"</tr>";

    data.result.forEach(r=>{
        table.innerHTML += "<tr>"+headers.map(h=>`<td>${r[h]}</td>`).join("")+"</tr>";
    });
}

document.getElementById("q").addEventListener("keydown", function(e){
    if(e.key === "Enter"){
        e.preventDefault();
        ask();
    }
});