document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('tree-form');
    const inputNode = document.getElementById('node-value');
    const btnDelete = document.getElementById('btn-delete');
    const btnClear = document.getElementById('btn-clear');
    const canvas = document.getElementById('tree-canvas');
    const ctx = canvas.getContext('2d');
    const messages = document.getElementById('messages');

    const NODE_RADIUS = 20;
    const LEVEL_HEIGHT = 70;

    // Configurar resolucion de canvas para pantallas retina
    function setupCanvas() {
        const dpr = window.devicePixelRatio || 1;
        const rect = canvas.parentElement.getBoundingClientRect();
        
        canvas.width = rect.width * dpr;
        canvas.height = 600 * dpr; // Altura fija logica
        
        ctx.scale(dpr, dpr);
        canvas.style.width = `${rect.width}px`;
        canvas.style.height = `600px`;
    }

    window.addEventListener('resize', () => {
        setupCanvas();
        fetchTree();
    });

    setupCanvas();

    function showMessage(msg, isError = false) {
        messages.textContent = msg;
        messages.style.color = isError ? '#ef4444' : '#34d399';
        setTimeout(() => {
            messages.textContent = '';
        }, 3000);
    }

    async function fetchTree() {
        try {
            const response = await fetch('/api/tree');
            const data = await response.json();
            drawTree(data.tree);
        } catch (error) {
            showMessage('Error al obtener el árbol', true);
        }
    }

    async function insertNode(value) {
        try {
            const response = await fetch('/api/tree/insert', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ value })
            });
            const data = await response.json();
            
            if (response.ok) {
                drawTree(data.tree);
                showMessage(data.message);
            } else {
                showMessage(data.error, true);
            }
        } catch (error) {
            showMessage('Error de conexión', true);
        }
    }

    async function deleteNode(value) {
        try {
            const response = await fetch('/api/tree/delete', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ value })
            });
            const data = await response.json();
            
            if (response.ok) {
                drawTree(data.tree);
                showMessage(data.message);
            } else {
                showMessage(data.error, true);
            }
        } catch (error) {
            showMessage('Error de conexión', true);
        }
    }

    async function clearTree() {
        try {
            const response = await fetch('/api/tree/clear', { method: 'POST' });
            const data = await response.json();
            drawTree(null);
            showMessage(data.message);
        } catch (error) {
            showMessage('Error al limpiar el árbol', true);
        }
    }

    // Dibujado en Canvas
    function drawTree(tree) {
        // Limpiar canvas (usando dimensiones lógicas)
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        if (!tree) return;

        const rootX = canvas.width / (2 * (window.devicePixelRatio || 1));
        const rootY = 50;

        // Primero calculamos las posiciones para poder dibujar las líneas por debajo
        const positions = [];
        calculatePositions(tree, rootX, rootY, canvas.width / (4 * (window.devicePixelRatio || 1)), positions);

        // Dibujar lineas
        drawLines(positions);
        
        // Dibujar nodos encima
        drawNodes(positions);
    }

    function calculatePositions(node, x, y, dx, positions) {
        if (!node) return;

        const currentPos = { ...node, x, y };
        positions.push(currentPos);

        if (node.left) {
            currentPos.leftPos = { x: x - dx, y: y + LEVEL_HEIGHT };
            calculatePositions(node.left, x - dx, y + LEVEL_HEIGHT, dx / 1.5, positions);
        }
        if (node.right) {
            currentPos.rightPos = { x: x + dx, y: y + LEVEL_HEIGHT };
            calculatePositions(node.right, x + dx, y + LEVEL_HEIGHT, dx / 1.5, positions);
        }
    }

    function drawLines(positions) {
        ctx.strokeStyle = '#475569';
        ctx.lineWidth = 2;

        positions.forEach(pos => {
            if (pos.leftPos) {
                ctx.beginPath();
                ctx.moveTo(pos.x, pos.y);
                ctx.lineTo(pos.leftPos.x, pos.leftPos.y);
                ctx.stroke();
            }
            if (pos.rightPos) {
                ctx.beginPath();
                ctx.moveTo(pos.x, pos.y);
                ctx.lineTo(pos.rightPos.x, pos.rightPos.y);
                ctx.stroke();
            }
        });
    }

    function drawNodes(positions) {
        positions.forEach(pos => {
            // Circulo del nodo
            ctx.beginPath();
            ctx.arc(pos.x, pos.y, NODE_RADIUS, 0, 2 * Math.PI);
            ctx.fillStyle = '#1e293b';
            ctx.fill();
            ctx.strokeStyle = '#3b82f6';
            ctx.lineWidth = 3;
            ctx.stroke();

            // Texto (Valor)
            ctx.fillStyle = '#f8fafc';
            ctx.font = 'bold 14px Inter';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillText(pos.key, pos.x, pos.y);

            // Factor de balance o altura (opcional visual)
            ctx.fillStyle = '#94a3b8';
            ctx.font = '10px Inter';
            ctx.fillText(`h:${pos.height}`, pos.x + NODE_RADIUS + 10, pos.y - 10);
        });
    }

    // Event Listeners
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const val = inputNode.value;
        if (val) {
            insertNode(val);
            inputNode.value = '';
            inputNode.focus();
        }
    });

    btnDelete.addEventListener('click', () => {
        const val = inputNode.value;
        if (val) {
            deleteNode(val);
            inputNode.value = '';
            inputNode.focus();
        }
    });

    btnClear.addEventListener('click', clearTree);

    // Carga inicial
    fetchTree();
});
