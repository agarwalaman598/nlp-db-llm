async function ask() {
    const question = document.getElementById("q").value;

    document.getElementById("sql").innerText = "Generating SQL...";
    document.getElementById("table").innerHTML = "";

    const res = await fetch("http://127.0.0.1:5000/query", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({question})
    });

    const data = await res.json();

    document.getElementById("sql").innerText = data.sql || data.error;

    if(!data.result) return;

    const table = document.getElementById("table");
    const headers = Object.keys(data.result[0] || {});

    table.innerHTML += "<tr>" + headers.map(h=>`<th>${h}</th>`).join("") + "</tr>";

    data.result.forEach(row=>{
        table.innerHTML += "<tr>" + headers.map(h=>`<td>${row[h]}</td>`).join("") + "</tr>";
    });
}