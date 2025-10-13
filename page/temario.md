
# Temario

Lista de temas para IOI/ICPC

> Existen otros temarios. Por ejemplo:
>
> - [Temario oficial de IOI]( https://ioinformatics.org/page/syllabus/12 )
> - <https://youkn0wwho.academy/topic-list>
>
> Podes contribuir a este temario sugiriendo cambios en <https://github.com/SebastianMestre/comp-prog-argentina/blob/trunk/raw/temario.tsv>



<details>
 <summary>Razonamiento formal</summary>
 <ul>
  <li>Modelado y formalización de problemas</li>
  <li>Razonamiento ecuacional sobre programas</li>
  <li>Razonamiento axiomático sobre programas (lógica de Hoare)</li>
 </ul>
</details>

<details>
 <summary>Técnicas de resolución</summary>
 <ul>
  <li>Generalización y reducción</li>
  <li>Invariantes</li>
  <li>Monotonía</li>
  <li>Análisis de elementos especiales (e.g. analizar máximos y mínimos)</li>
  <li>Coloreos (e.g. cubrir un tablero de ajedrez sin esquinas con piezas de dominó)</li>
  <li>Principio del palomar (e.g. mayor hueco de menor a mayor en O(N))</li>
  <li>Inversión del problema ("mirar para atras", e.g. perros de OIA 2019)</li>
  <li>Separación en componentes independientes</li>
 </ul>
</details>

<details>
 <summary>Grafos</summary>
<h3>Basico</h3>
 <ul>
  <li>Nociones elementales y definiciones de teoria de grafos</li>
 </ul>
<h3>Caminos especiales</h3>
 <ul>
  <li>Circuito euleriano, teorema de existencia <=>, algoritmos para construirlo</li>
  <li>Circuito hamiltoniano, teoremas de Ore / Dirac</li>
 </ul>
<h3>Representaciones</h3>
 <ul>
  <li>Matriz de Adyacencia</li>
  <li>Matriz de Incidencia</li>
  <li>Listas de Adyacencia</li>
  <li>Lista de incidencia</li>
  <li>Grafo Implícito</li>
 </ul>
<h3>BFS</h3>
 <ul>
  <li>Algoritmo basico.</li>
  <li>BFS con cola de dos puntas [Aristas 0 y 1]</li>
  <li>BFS con K+1 bolsas [aristas 0..K]</li>
 </ul>
<h3>DFS</h3>
 <ul>
  <li>Implementacion con stack</li>
  <li>Implementacion recursiva</li>
  <li>Clasificacion de aristas en grafo no-dirigido ({tree,back}-edges)</li>
  <li>Clasificacion de aristas en grafo dirigido ({tree,back,forward,cross}-edges)</li>
  <li>Ordenamiento Topologico</li>
  <li>Clausura transitiva</li>
  <li>Componentes Fuertemente Conexas</li>
  <li>Deteccion de puntos de articulacion y puentes</li>
  <li>Componentes Biconexas</li>
  <li>Block-cut tree</li>
 </ul>
<h3>Caminos minimos</h3>
 <ul>
  <li>Dijkstra en N^2</li>
  <li>Dijkstra en (N + M) log N</li>
  <li>Distancia Min-Max (Prim)</li>
  <li>Bellman-Ford y su implementacion tipica.</li>
  <li>Bellman-Ford como programacion dinamica.</li>
  <li>Bellman-Ford para contar caminos entre pares de nodos.</li>
  <li>Bellman-Ford, deteccion y tratamiento de ciclos negativos</li>
  <li>Floyd-Warshall Vision como programacion dinamica.</li>
  <li>Floyd-Warshall y su implementacion tipica.</li>
  <li>Floyd-Warshall, para contar caminos entre pares de nodos.</li>
  <li>Floyd-Warshall como producto de matrices de adyacencia / Potencias de la matriz de adyacencia.</li>
  <li>Floyd-Warshall, eteccion y tratamiento de ciclos negativos</li>
  <li>Reconstruir caminos</li>
  <li>Reconstruir caminos</li>
 </ul>
<h3>Arbol recubridor minimo</h3>
 <ul>
  <li>Kruskal</li>
  <li>Relación del Minimum Spanning Tree con la distancia Min-Max.</li>
  <li>Aplicación a calcular la distancia min-max todos contra todos en N^2</li>
  <li>Solución alternativa para el mismo problema: hacerlo en el mismo Kruskal que calcula el MST</li>
 </ul>
<h3>Flujo y derivados</h3>
 <ul>
  <li>Algoritmo de Khun -- Matching Maximo Bipartito O(VE)</li>
  <li>Modelado de problemas con flujo maximo</li>
  <li>Modelado de problemas con corte minimo, dualidad con flujo maximo</li>
  <li>Algoritmo de Edmonds-Karp</li>
  <li>Algoritmo de Dinitz</li>
  <li>Algoritmos de Preflow-Push</li>
  <li>Manejo de la red residual de un grafo.</li>
  <li>Teoremas de König, Hall y Menger.</li>
  <li>Mínimo Cubrimiento por Caminos. Mínima Partición en Caminos. Teorema de Dilworth</li>
  <li>Min-cost max-flow</li>
  <li>min vertex cover / max independent set en grafo bipartito</li>
 </ul>
<h3>Árboles</h3>
 <ul>
  <li>Detección, recorrido.</li>
  <li>Representación de arbol con raiz: Padre de cada nodo</li>
  <li>Representación de arbol con raiz: Lista de adyacencia del dirigido "bajando desde la raíz".</li>
  <li>Radio, centro y diámetro de un árbol en tiempo lineal.</li>
 </ul>
<h3>Grafos planares</h3>
 <ul>
  <li>Fórmula de Euler</li>
  <li>Los grafos planares son ralos</li>
  <li>Max-clique en grafo planar</li>
  <li>Grafo dual</li>
  <li>Construir Grafo dual de un grafo planar (dado el embedding)</li>
 </ul>
</details>

<details>
 <summary>Complejidad computacional</summary>
 <ul>
  <li>Entendimiento de la notacion asintotica (La O grande de "O(N)")</li>
  <li>Analisis amortizado de complejidad</li>
  <li>Nocion de P, NP, NP completo, algoritmo polinomial, etc</li>
  <li>Problemas NP completos conocidos (Camino hamiltoniano, TSP, Maximum independent set, Minimum dominating set, subset sum, etc.)</li>
  <li>Problemas que no se sabe que sean P ni NP completo (Factorización entera, logaritmo discreto, isomorfismo de grafos)</li>
 </ul>
</details>

<details>
 <summary>Ordenamiento</summary>
 <ul>
  <li>Busqueda lineal</li>
  <li>Busqueda binaria (con LA RECETA)</li>
  <li>Counting Sort</li>
  <li>MergeSort</li>
  <li>QuickSort</li>
  <li>Mediana (o elemento iesimo) en tiempo lineal esperado (n\_th element)</li>
  <li>HeapSort</li>
  <li>BubbleSort</li>
  <li>InsertionSort</li>
  <li>RadixSort</li>
 </ul>
</details>

<details>
 <summary>Estructuras de datos</summary>
<h3>Básicas</h3>
 <ul>
  <li>Arreglos</li>
  <li>Listas enlazadas</li>
  <li>Colas</li>
  <li>Pilas</li>
 </ul>
<h3>C++</h3>
 <ul>
  <li>STL (set, multiset, map, multimap, vector, queue, stack, deque, priority\_queue, list, etc)</li>
  <li>Policy based data structures de GCC (en especial indexed\_set)</li>
 </ul>
<h3>Árboles</h3>
 <ul>
  <li>Árboles con raíz generales</li>
  <li>Árbol binario de búsqueda (ABB)</li>
  <li>ABB balanceado (por ej, Treap)</li>
  <li>Heap (para priority queue), heapsort, heapify en O(N)</li>
  <li>Tries</li>
 </ul>
<h3>Consultas sobre arreglos</h3>
 <ul>
  <li>Tablas Aditivas (prefix sums)</li>
  <li>Binary Index Tree (Fenwick Tree)</li>
  <li>Union Find (Implementacion con listas y con arbol)</li>
  <li>RMQ (Segment tree sobre arreglo)</li>
  <li>Sliding Windows, Sliding-RMQ (para en O(N) calcular el RMQ de subarreglos de un tamaño K dado)</li>
  <li>RMQ/Fenwick 2D</li>
 </ul>
<h3>Consultas sobre árboles</h3>
 <ul>
  <li>Binary lifting en árbol con raíz</li>
  <li>LCA en O(lg n) mediante Euler Tour + RMQ</li>
  <li>LCA en O(lg n) mediante binary lifting</li>
  <li>Distancias en un arbol en O(log N) con LCA</li>
  <li>Heavy Light Decomposition</li>
 </ul>
<h3>Varias</h3>
 <ul>
  <li>Tabla hash</li>
  <li>Estructuras de datos persistentes (con path copying)</li>
  <li>Estructuras de datos para arboles dinamicos (link-cut trees)</li>
  <li>Principio small-to-large</li>
 </ul>
</details>

<details>
 <summary>Algoritmos con sqrt()</summary>
 <ul>
  <li>sqrt-decomposition: Separar la secuencia del input en bloques de sqrt(N)</li>
  <li>Algoritmo de MO: separar queries por posicion inicial en bloques de sqrt(N)</li>
  <li>Combinar dos algoritmos O(nk) y O(n^2/k)</li>
  <li>Agrupar updates en bloques de sqrt(U), hacer queries iterando por las updates dentro de cada bloque</li>
  <li>Hay <= sqrt(N) elementos que aparecen >= sqrt(N) veces</li>
  <li>Si una suma es igual a N, hay <= sqrt(N) valores distintos</li>
 </ul>
</details>

<details>
 <summary>Strings</summary>
 <ul>
  <li>Algoritmo KMP, y que significa su tablita.</li>
  <li>Z-Array</li>
  <li>Rabin-Karp, y uso del concepto de hash en general.</li>
  <li>xor-hashing y sum-hashing con una tabla de números aleatorios</li>
  <li>Suffix Array (Algoritmo de Larsson y Sadakane), LCP</li>
  <li>Matching con automatas deterministas y no deterministas (dado un automata ya hecho)</li>
  <li>Suffix Tree</li>
  <li>Suffix Automaton</li>
  <li>Automata de Aho-Corasick (version multicadena de KMP)</li>
  <li>Algoritmo de Manacher (tabla de radio de palindromos)</li>
  <li>Factorización de Lyndon (Mínima factorización en rotaciones mínimas)</li>
 </ul>
</details>

<details>
 <summary>Programacion Dinámica</summary>
 <ul>
  <li>Recursion (en matematica, en programacion, recursion mutua)</li>
  <li>Maxima subsecuencia creciente (En O(n^2), y su variante en O(n lg n))</li>
  <li>Cálculo del triangulo de pascal</li>
  <li>Longest common subsequence</li>
  <li>Edit distance mínima (La común, y permitiendo swaps adyacentes)</li>
  <li>Producto de matrices con costo minimo</li>
  <li>"En una matriz yendo de una esquina a la otra solo bajando y para la derecha, maximizar la suma de las casillas visitadas."</li>
  <li>Knapsack (Problema de la mochila), Subset Sum</li>
  <li>Dar vuelto usando una cantidad minima de monedas</li>
  <li>Optimal Binary Search Tree en O(n^3) y O(n^2) (Knuth optimization)</li>
  <li>Divide and conquer optimization</li>
  <li>Dada una string par de {,(,[,],),} dar la minima cantidad de cambios necesarios para que sea valida.</li>
  <li>Dinámicas con máscaras de bits: TSP y muchas otras.</li>
  <li>Dinámicas con "frente": Poner fichitas / tubitos en un tablero, y muchas otras</li>
 </ul>
</details>

<details>
 <summary>Matemática</summary>
<h3>Analisis numérico</h3>
 <ul>
  <li>Punto flotante: Conocerlos, saber que existe el error, cuentitas basicas, uso de EPSILON en los if</li>
  <li>Operaciones aritmeticas con enteros de longitud arbitraria</li>
 </ul>
<h3>Álgebra</h3>
 <ul>
  <li>Potenciacion logaritmica (binary lifting)</li>
  <li>Sumas de progresiones aritmeticas y geometricas con binary lifting</li>
  <li>Recurrencias lineales</li>
  <li>Sistemas de ecuaciones lineales (algoritmo de Gauss)</li>
  <li>Calculo de determinantes, matriz inversa (algoritmo de Gauss)</li>
  <li>Funciones generatrices</li>
 </ul>
<h3>Combinatoria y Probabilidad</h3>
 <ul>
  <li>Relacion entre combinatoria y probabilidad</li>
  <li>Principios de la suma y del producto</li>
  <li>Coeficientes binomiales / triangulo de Pascal</li>
  <li>Bolitas y palitos</li>
  <li>Inclusion-exclusion</li>
  <li>Linealidad de la esperanza / técnica "contribution to the sum"</li>
  <li>Distribución de la suma de dos variables aleatorias (convolucion)</li>
  <li>Convolucion rápida usando FFT</li>
  <li>Números de Catalan</li>
  <li>Cadenas de Markov</li>
  <li>Young Tableaux</li>
 </ul>
<h3>Teoría de números</h3>
 <ul>
  <li>Teorema fundamental de la aritmetica</li>
  <li>Aritmetica modular</li>
  <li>MCD (Algoritmo de euclides)</li>
  <li>Inverso Modular (Con euclides extendido o con pequeño teorema de Fermat)</li>
  <li>Teorema Chino del Resto</li>
  <li>Producto de matrices</li>
  <li>Chequeo de primalidad raiz(N)</li>
  <li>Criba de Eratostenes</li>
  <li>Chequeo de primalidad eficiente probabilistico (Miller-Rabin)</li>
  <li>Orden de un elemento en (N_p,*), raices primitivas</li>
  <li>Funcion phi de Euler</li>
  <li>Funciones multiplicativas, función de Mobius</li>
 </ul>
</details>

<details>
 <summary>Geometria</summary>
 <ul>
  <li>Vectores (Suma, Resta)</li>
  <li>Producto escalar</li>
  <li>Norma, distancia euclidea (pitagoras)</li>
  <li>Producto vectorial</li>
  <li>Area de triangulos / paralelogramos, detección de sentido de giro</li>
  <li>Area de poligonos</li>
  <li>Representaciones de recta, segmento, etc estilo lineal (vectores / puntos + direccion)</li>
  <li>Chequear si un punto esta en un poligono / en un segmento / en una recta / en un plano</li>
  <li>Chequear si esta en poligono convexo en lg N</li>
  <li>Chequear si está en un poligono no convexo en O(N)</li>
  <li>Teorema de Pick</li>
  <li>Compresion de coordenadas</li>
  <li>Par de puntos mas cercano en O(n lg n)</li>
  <li>Capsula convexa en O(n lg n)</li>
  <li>Par de puntos mas lejano en O(n lg n), O(n) dada ya la capsula convexa</li>
  <li>Rotating calipers</li>
  <li>Interseccion de dos segmentos</li>
  <li>Distancia entre dos segmentos</li>
  <li>Sweep Line (Es MUY importante la idea de sweep line / sweep circle / sweep sarasa)</li>
  <li>Dualidad punto / linea</li>
  <li>Interseccion circulo - circulo y circulo - recta</li>
  <li>Suma de Minkowski, aplicación a distancia entre polígonos convexos</li>
  <li>Convex Hull Trick</li>
  <li>Clasificar/contar puntos dominados/dominantes</li>
 </ul>
</details>

<details>
 <summary>Divide and conquer</summary>
 <ul>
  <li>Elemento mayoria en n lg n usando *solamente* comparaciones por igualdad entre elementos.</li>
  <li>Par de puntos mas cercano en O(n lg n)</li>
  <li>Strassen</li>
  <li>Karatsuba</li>
 </ul>
</details>

<details>
 <summary>Greedies</summary>
 <ul>
  <li>Dar vuelto usando una cantidad minima de monedas</li>
  <li>Ordenamiento de trabajos con distintos tiempos de ejecución para minimizar el tiempo de finalización promedio.</li>
  <li>Optimo cubrimiento de intervalo por subintervalos.</li>
  <li>Codigos de Huffman</li>
  <li>Maxima subsecuencia creciente (resolviendo "mínima partición en subsecuencias no crecientes" + Dilworth)</li>
 </ul>
</details>

<details>
 <summary>Backtracking</summary>
 <ul>
  <li>Fuerza Bruta</li>
  <li>Fuerza Bruta sobre permutaciones (next_permutation)</li>
  <li>Backtracking con cantidad de pasos fija (for if for if for if)</li>
  <li>Backtracking con cantidad de pasos variable (recursiva)</li>
  <li>Backtracking sobre permutaciones (recursiva)</li>
  <li>Backtracking sobre subconjuntos (recursiva)</li>
  <li>Optimización "Branch & Bound"</li>
  <li>Problema de las N reinas</li>
  <li>Cubrir un tablero con fichitas. (e.g. Codeforces 143E)</li>
  <li>Sudoku</li>
 </ul>
</details>

<details>
 <summary>Teoría de juegos</summary>
 <ul>
  <li>Propiedad Universal de las posiciones P/G</li>
  <li>Cálculo con DP de posiciones ganadoras y perdedoras.</li>
  <li>Algoritmo minimax para juegos de suma cero de informacion perfecta.</li>
  <li>Idea de la criba para llenar tablitas como la anterior.</li>
  <li>Variante de la DP donde el que gana trata de ganar rápido y el que pierde de perder lento.</li>
  <li>Juegos combinatorios imparciales: Sumar de juegos.</li>
  <li>Nim. Misére Nim.</li>
  <li>Grundy Numbers, cálculo de los grundy numbers en tiempo lineal en el grafo, con DP. Grundy Number de una suma de juegos.</li>
 </ul>
</details>

<details>
 <summary>Teoría de lenguajes</summary>
 <ul>
  <li>Gramatica BNF</li>
  <li>Autómatas Finitos</li>
  <li>Expresiones Regulares</li>
  <li>Parsing Recursivo Descendente predictivo (con "prediccion artesanal")</li>
  <li>Gramaticas libres de contexto</li>
 </ul>
</details>

<details>
 <summary>Interactivos</summary>
 <ul>
  <li>Problemas estilo "descubrir el secreto"</li>
  <li>Problemas estilo "queries online"</li>
  <li>Problemas estilo "juego contra el juez"</li>
  <li>Heuristica de repartir parejo</li>
  <li>Teoria de la informacion, bits, entropia</li>
 </ul>
</details>

<details>
 <summary>Permutaciones</summary>
 <ul>
  <li>Composicion</li>
  <li>Representacion de cosas como permutaciones (e.g. Rubik, o cualquier grupo)</li>
  <li>Transposiciones (swaps)</li>
  <li>Inversiones</li>
  <li>Contar inversiones en O(N log N) (con mergesort o con Fenwick tree)</li>
  <li>Ciclos</li>
  <li>Paridad (Mediante inversiones y mediante ciclos)</li>
 </ul>
</details>

<details>
 <summary>Truquitos</summary>
<h3>Estructuras de datos</h3>
 <ul>
  <li>Sumas de prefijos de cadenas de paréntesis balanceadas</li>
 </ul>
<h3>Grafos</h3>
 <ul>
  <li>Al Reconstruir caminos, dar vuelta origen y destino (y trasponer el grafo si es dirigido) así al recorrer los padres queda el camino al derecho.</li>
 </ul>
<h3>Matemática</h3>
 <ul>
  <li>Gauss rápido para matrices banda: Bidiagonales, Tridiagonales, Adyacencias en una grilla rectangular.</li>
 </ul>
</details>
