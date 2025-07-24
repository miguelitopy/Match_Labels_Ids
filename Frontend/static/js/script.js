document.addEventListener("DOMContentLoaded", function () {
    async function fetchData() {
        try {
            const statusResponse = await fetch('/api/get-comparison-results');
            const statusData = await statusResponse.json();

            const statusBox = document.getElementById('status-box');
            const statusText = document.getElementById('status-text');

            // Atualiza status (OK ou NG)
            if (statusData.status === "OK") {
                statusBox.className = 'status-box match';
                statusText.textContent = 'OK';
            } else {
                statusBox.className = 'status-box mismatch';
                statusText.textContent = 'NG';
            }

            // Busca os resultados completos
            const resultsResponse = await fetch('/api/getall');
            const resultsData = await resultsResponse.json();

            atualizarTabela(resultsData.results);
            atualizarHistorico(resultsData.results);
            verificarErros(resultsData.results);
        } catch (error) {
            console.error('Erro ao buscar dados:', error);
        }
    }

    function atualizarTabela(results) {
        const tableBody = document.getElementById('data-table');
        tableBody.innerHTML = ''; // Limpa os dados antigos

        results.forEach(result => {
            const row = document.createElement('tr');
            row.innerHTML = `<td>${result[0]}</td><td>${result[1]}</td><td>${result[2]}</td>`;
            tableBody.appendChild(row);
        });
    }

    function atualizarHistorico(results) {
        const queueItems = document.getElementById('queue-items');
        queueItems.innerHTML = ''; // Limpa os blocos antigos

        results.slice(0, 4).forEach(result => {
            const block = document.createElement('div');
            block.className = 'queue-item';
            block.innerHTML = `<div><strong>WIP:</strong> ${result[0]}</div>
                               <div><strong>SET ID:</strong> ${result[1]}</div>`;
            queueItems.appendChild(block);
        });
    }

    function verificarErros(results) {
        if (results.length === 0) return;

        const ultimoResultado = results[results.length - 1];
        const scanner1Erro = ultimoResultado.includes("ERRO_SCANNER1");
        const scanner2Erro = ultimoResultado.includes("ERRO_SCANNER2");

        if (scanner1Erro) {
            exibirPopup("Leitura não realizada no scanner inicial. Ler manualmente!", "scanner1-popup");
        } else {
            esconderPopup("scanner1-popup");
        }

        if (scanner2Erro) {
            exibirPopup("Falha no Scanner 2!", "scanner2-popup");
        } else {
            esconderPopup("scanner2-popup");
        }
    }

    function exibirPopup(mensagem, id) {
        let popup = document.getElementById(id);
        if (!popup) {
            popup = document.createElement("div");
            popup.id = id;
            popup.className = "popup";
            popup.innerHTML = `<p>${mensagem}</p>`;
            document.body.appendChild(popup);
        }
        popup.style.display = "block";
    }

    function esconderPopup(id) {
        let popup = document.getElementById(id);
        if (popup) popup.style.display = "none";
    }

    // Atualiza os dados a cada 2 segundos
    setInterval(fetchData, 2000);

    // Carrega os dados ao iniciar
    fetchData();
});
