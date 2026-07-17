async function load(sort = "id") {

    const response = await fetch("/api/products?sort=" + sort);

    const products = await response.json();

    const table = document.getElementById("data");

    table.querySelectorAll("tr:not(:first-child)").forEach(r => r.remove());

    for (const p of products) {

        const row = document.createElement("tr");

        row.innerHTML = `
            <td>${p.id}</td>
            <td>${p.name}</td>
            <td>${p.price}</td>
        `;

        table.appendChild(row);
    }
}

document.addEventListener("DOMContentLoaded", () => {
    load();
});