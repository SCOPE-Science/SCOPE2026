# Exact two-type spectra over transitive tournaments in the directed-triangle-free homogeneous oriented graph

## Finding
Let \(\mathbb H\) be the countable homogeneous oriented graph with no directed three-cycle, and let \(A_n\) be an individually named, transitively oriented complete tournament on \(n\) vertices, where \(n\ge0\). Let \(u_n\) be the number of nonalgebraic complete one-types over \(A_n\). Let \(a_n\) be the number of complete ordered types of two distinct new vertices \((x,y)\) with \(x\to y\), and let \(b_n\) be the count with no edge between \(x\) and \(y\). The opposite orientation has the same count as \(a_n\). Then
\[
 u_n=(n+2)2^{n-1},\qquad a_n=\frac{n(n+9)4^n}{8}+3^n,\qquad b_n=(n+2)^2 4^{n-1}.
\]
The formulas also hold at \(n=0\), interpreted as rational powers whose products are integers. Thus the total number of ordered pair types is \(T_n=2a_n+b_n\). Under uniform sampling from these types, the adjacency fraction is
\[
 p_n=\frac{n(n+9)+8(3/4)^n}{2n^2+13n+4+8(3/4)^n}.
\]
It is strictly decreasing for every integer \(n\ge0\), from \(p_0=2/3\) to \(1/2\), and obeys \(p_n=1/2+5/(4n)+O(n^{-2})\) as \(n\to\infty\).

## Assumptions and scope
An *oriented graph* has no loops and at most one directed edge between any pair of distinct vertices. The forbidden configuration is the *cyclic* directed triangle, not a transitive triangle; missing edges are allowed. The class of all finite oriented graphs omitting a cyclic directed triangle has hereditary, joint embedding, and free amalgamation properties: freely combining two members along a common induced subgraph creates no new three-cycle spanning both new sides. Hence its Fraïssé limit \(\mathbb H\) exists and is homogeneous. Every complete type of finitely many distinct new points over a named finite base is represented uniquely by an admissible finite oriented extension. The base \(A_n=\{v_1,\ldots,v_n\}\) has edges \(v_i\to v_j\) exactly when \(i<j\). Pair types are ordered and injective, and both new points are distinct from the base. These type counts are combinatorial orbit counts, not probabilities of sampling random vertices from \(\mathbb H\).

## Proof
**Unary words.** For each new vertex \(x\), record a word \(w_x\) of length \(n\) in the three symbols \(-,0,+\), where the symbol at \(i\) means respectively \(v_i\to x\), no edge, or \(x\to v_i\). The only possible cyclic triangle containing \(x\) and two base vertices is \(x\to v_i\to v_j\to x\) for \(i<j\). Hence a word is valid precisely when no plus symbol precedes any minus symbol. Words with no minus number \(2^n\). For each last-minus position \(j\), the prefix of length \(j-1\) uses \(-,0\), and the suffix uses \(+,0\); there are \(2^{j-1}2^{n-j}=2^{n-1}\) words. Therefore \(u_n=2^n+n2^{n-1}\), including the empty word at \(n=0\).

**No edge.** If \(x\) and \(y\) are nonadjacent, no directed triangle can involve both. Thus their valid unary words are independent, and \(b_n=u_n^2\).

**Directed edge.** Suppose \(x\to y\). Besides the unary constraints, the triple \(x,y,v_i\) would be a directed cycle precisely when \(y\to v_i\to x\), namely when the pair of signs at position \(i\) is \((-,+)\). Thus one counts pairs of unary words avoiding this single forbidden simultaneous sign. Read signs from left to right while recording, for each word, whether a \(+\) has occurred. After a plus has occurred, a minus is forbidden in that coordinate. With states \((00),(10),(01),(11)\), the exact transition matrix (rows are old flags, columns new flags) is
\[
 M=\begin{pmatrix}4&2&1&1\\0&4&0&2\\0&0&3&2\\0&0&0&4\end{pmatrix}.
\]
For instance the \((00)\)-to-\((01)\) entry is one because when \(y\) first has a plus and \(x\) does not, \(x\) must have a zero, not a minus. The other entries follow directly by enumerating the allowed sign pairs. Consequently \(a_n=e_{00}^{\mathsf T}M^n\mathbf1\) for every \(n\ge0\). Inverting \(I-zM\), or solving the four triangular recurrences, gives
\[
 \sum_{n\ge0}a_n z^n=\frac{1-7z+17z^2-16z^3}{(1-3z)(1-4z)^3}.
\]
Extracting coefficients from this rational function yields \(a_n=3^n+\frac{n(n+9)}8 4^n\). The matrix calculation is an identity of formal power series, not a numerical interpolation. Exchanging \(x,y\) interchanges the two edge orientations and does not change the count.

**Strict decay.** Put \(q=3/4\) and \(R_n=b_n/a_n=(n+2)^2/[n(n+9)/2+4q^n]\). Since \(p_n=2/(2+R_n)\), it suffices to show \(R_{n+1}>R_n\). Cross-multiplication by positive denominators gives exactly
\[
 R_{n+1}>R_n\ \Longleftrightarrow\ \frac{5n^2-3n-40}{2}+(n^2+12n+24)q^n>0.
\]
For every integer \(n\ge4\) the polynomial term is positive. At \(n=0,1,2,3\), direct substitution gives strictly positive values. Hence \(p_n\) strictly decreases. Since \(R_n\to2\), one has \(p_n\to1/2\), and expansion of the explicit rational expression proves the stated \(5/(4n)\) leading correction.

## Verification
Run \(\texttt{python3 verifier.py}\) with Python 3 and no third-party packages. The checker independently enumerates all valid oriented diagrams over \(A_n\) for \(0\le n\le5\) (examining each triple for cyclic orientations), checks all three pair-relation channels, verifies the triangular-matrix count through \(n=100\), and compares exact rational fractions for strict decay through \(n=100\). Expected output is included in \(\texttt{verifier_output.txt}\). Finite checks corroborate, but do not replace, the symbolic matrix proof and sign argument.

## Relationship to prior work
Cherlin's classification of countable homogeneous directed graphs supplies the structural and Fraïssé context. Kühn–Osthus–Townsend–Zhao study finite oriented graphs omitting cyclic triangles and their global structural/enumerative behavior; the earliest verified public version of that initiating source is arXiv:1404.6178v1 (2014-04-24). Neither inspected material establishes the exact conditional pair-type enumerator over a pointwise-named transitive tournament, nor its strictly decreasing adjacency fraction. Fixed-chain type enumerators for the homogeneous partial order concern different extension constraints and do not imply the present formula. These are statement-implication comparisons, not a claim that keyword searches establish novelty.

## Limitations
The result applies to cyclic-triangle-free oriented graphs with missing edges, a pointwise-named *transitive complete tournament* base, and ordered pairs of distinct fresh points. It is not a result for transitive-triangle-free oriented graphs, arbitrary named bases, or larger arities. Fractions are over logical types, not random vertices. An older equivalent formula in the homogeneous-directed-graph literature may exist; the full text of Cherlin's later monograph was not accessible for a complete historical-priority check. Independent mathematical validation has not been performed.

## References
- Daniela Kühn, Deryk Osthus, Timothy Townsend, Yi Zhao, "On the structure of oriented graphs and digraphs with forbidden tournaments or cycles," arXiv:1404.6178v1, posted 2014-04-24. https://arxiv.org/abs/1404.6178
- Gregory Cherlin, "The Classification of Countable Homogeneous Directed Graphs and Countable Homogeneous n-Tournaments," *Memoirs of the American Mathematical Society* 131 (1998), no. 621. https://doi.org/10.1090/memo/0621
- Gregory Cherlin, "Infinite Homogeneous Directed Graphs," earlier manuscript, https://ow3.math.rutgers.edu/~cherlin/Paper/1992Digraph.pdf
