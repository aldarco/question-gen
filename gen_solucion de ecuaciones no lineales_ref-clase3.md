### **Problema 1 (Teórico - Conceptual)**  
**Tema:** Métodos Abiertos vs. Métodos de Intervalo  

**Pregunta:**  
Compara los métodos abiertos (como Newton-Raphson) con los métodos de intervalo (como bisección o falsa posición) en términos de:  
1. **Garantía de convergencia** (¿Qué método asegura encontrar una raíz y bajo qué condiciones?).  
2. **Velocidad de convergencia** (¿Cuál converge más rápido y por qué?).  
3. **Requerimientos de información sobre la función** (¿Qué datos adicionales necesita cada método?).  

**Instrucciones:**  
- Explica claramente las ventajas y desventajas de cada enfoque.  
- Justifica tus respuestas con los conceptos vistos en clase (e.g., convergencia lineal vs. cuadrática, necesidad de derivadas, etc.).  

---

### **Problema 2 (Aplicativo - Numérico)**  
**Tema:** Método de Newton-Raphson  

**Pregunta:**  
Dada la función no lineal \( f(x) = e^{-x} - x \):  
1. **Demuestra** que tiene una raíz real en el intervalo \([0, 1]\).  
2. **Aplica el método de Newton-Raphson** para aproximar dicha raíz con una tolerancia de \( 0.001 \). Usa \( x_0 = 1 \) como valor inicial.  
3. **Calcula** el error relativo porcentual en cada iteración y verifica la convergencia cuadrática.  

**Datos adicionales:**  
- La derivada de \( f(x) \) es \( f'(x) = -e^{-x} - 1 \).  
- La raíz exacta, redondeada a 5 decimales, es \( 0.56714 \).  

**Instrucciones:**  
- Muestra al menos 3 iteraciones completas (tabla con \( x_k \), \( f(x_k) \), \( f'(x_k) \), \( x_{k+1} \), y error).  
- Explica por qué el método converge cuadráticamente en este caso.  

---

### **Notas para el profesor:**  
- **Problema 1** evalúa comprensión conceptual y capacidad de contrastar métodos.  
- **Problema 2** valora aplicación práctica, manejo de fórmulas y análisis de error.  
- Ambos problemas integran los temas clave de la clase: convergencia, estabilidad y requerimientos de los métodos numéricos.