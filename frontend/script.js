async function enviarEmocao(emocao) {
    try {
        const response = await fetch('http://127.0.0.1:5000/frase', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ emocao })
        });

        if (!response.ok) {
            throw new Error("Erro ao obter a frase.");
        }

        const data = await response.json();
        const fraseAleatoria = data.frase[Math.floor(Math.random() * data.frase.length)];
        const fraseElement = document.getElementById('frase');

        
        fraseElement.textContent = `"${fraseAleatoria}"`;
    } catch (error) {
        console.error('Erro:', error);
        document.getElementById('frase').textContent = "Erro na conexão com o servidor.";
    }
}