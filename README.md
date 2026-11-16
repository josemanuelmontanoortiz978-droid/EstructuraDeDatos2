# 🌳 Estructura de Datos 2


* **Lenguaje / Entorno:** Python ( Google Colab )
* **Enfoque:** Implementación manual de nodos, punteros/referencias y contratos mediante interfaces abstractas.

---

## 🗂️ Módulos y Estructuras Implementadas

| Carpeta / Archivo | Estructura / Módulo | Descripción Técnica | Estado |
| :--- | :--- | :--- | :---: |
| `InterfazArbolBinario/` | Contrato base (TDA) | Define la interfaz abstracta y operaciones estándar que implementan los distintos árboles binarios. | ✅ Completado |
| `ÁrbolBinaroADT/` | Árbol Binario de Búsqueda (ABB) | Implementación de nodos, inserción, búsqueda, recorridos y operaciones base del TDA. | ✅ Completado |
| `Árbol_AVL/` | Árbol AVL (Autobalanceado) | Cálculo de factor de equilibrio y rotaciones simples/dobles para mantener altura logarítmica $O(\log n)$. | ✅ Completado |
| `ÁrbolBinarioDeExpresiones/` | Árbol de Expresiones | Construcción y evaluación sintáctica de expresiones matemáticas mediante recorridos del árbol. | ✅ Completado |
| `ÁrbolBinarioAVLyEliminar.ipynb` | Cuaderno de Pruebas (Colab) | Pruebas interactivas de inserción, balanceo AVL y casos de eliminación de nodos. | ✅ Completado |
| `Grafos/` *(Próximamente)* | Grafos (Dirigidos y No Dirigidos) | Representación mediante Lista/Matriz de Adyacencia, recorridos (**BFS**, **DFS**), detección de ciclos y algoritmos de caminos mínimos / expansión mínima. | ⏳ En desarrollo |

---

## 📁 Estructura del Proyecto

```text
Árbol_Binario_De_Expresiones/
├── InterfazArbolBinario/            # Interfaz base para los árboles binarios
├── ÁrbolBinaroADT/                  # Implementación del TDA Árbol Binario
├── Árbol_AVL/                       # Implementación con rotaciones y autobalanceo
├── ÁrbolBinarioDeExpresiones/       # Aplicación para evaluación de expresiones
├── ÁrbolBinarioAVLyEliminar.ipynb   # Notebook de pruebas y eliminación en AVL
├── Grafos/                          # [Reservado] Próxima estructura de datos
└── README.md
