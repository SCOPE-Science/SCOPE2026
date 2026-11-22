# Nine vertices are the first tie-robust failure of greedy three-chord D-optimal cycle augmentation

## Finding

Fix the unit-conductance cycle \(C_n\) with labeled vertices \(0,1,\ldots,n-1\), and admit only nonedges as new unit-conductance chords. From the empty augmentation, choose three chords one after another, maximizing the number of spanning trees at each intermediate step; all maximizers are allowed as tie choices. For each \(5\le n\le8\), **every** resulting greedy triple is globally three-chord optimal. For \(n=9\), **every** greedy triple is suboptimal: all \(18\) distinct greedy triples have exactly \(235\) spanning trees, while exactly three triples attain the global optimum \(240\). Thus nine vertices form the first tie-robust greedy failure among cycles admitting three distinct chords.

In the labeling above, the three global optima are

\[
\begin{aligned}
&\{\{0,4\},\{1,6\},\{3,7\}\},\
&\{\{0,5\},\{2,6\},\{3,8\}\},\
&\{\{1,5\},\{2,7\},\{4,8\}\}.
\end{aligned}
\]

The optimality gap is \(5\) trees, or \(1/48\) of the global maximum. It cannot be fixed by choosing different greedy ties.

## Assumptions and scope

The base graph is a simple undirected cycle with \(n\) vertices and all edge conductances one. The permitted chord set is exactly

\[
E_n=\{\{a,b\}:0\le a<b<n,\ b-a\ge2,\ (a,b)\ne(0,n-1)\}.
\]

Each chord may be used at most once. Let \(\tau_n(S)\) denote the number of spanning trees of \(C_n+S\). A greedy prefix \(S\) is extended only by edges \(e\in E_n\setminus S\) maximizing \(\tau_n(S\cup\{e\})\) for that particular prefix. We retain **every** tied maximizer at every stage. All claims involve exactly three added edges and integer orders \(5\le n\le9\); we make no assertion about other budgets, arbitrary base graphs, or larger cycles.

## Proof

For any chord set \(S\subseteq E_n\), Kirchhoff's matrix-tree theorem gives

\[
\tau_n(S)=\det L_{n,S}^{(n-1)},
\]

where \(L_{n,S}^{(n-1)}\) is the matrix obtained by deleting the last row and column from the integer Laplacian of \(C_n+S\). Thus every comparison can be decided exactly by integer arithmetic.

The attached `verify.py` implements an exhaustive, finite proof. It constructs \(E_n\) from the displayed inequalities, enumerates every \(S\subseteq E_n\) of cardinality \(0,1,2,3\), and calculates each \(\tau_n(S)\) as an exact determinant using fraction-free Bareiss elimination. It independently calculates the same integers by the matrix determinant lemma on the cycle. Specifically, if \(S=\{e_1,\ldots,e_k\}\), orient each chord \(e_i=(a_i,b_i)\) and set

\[
r_n(u,v)=|u-v|\bigl(n-|u-v|\bigr),
\]

\[
Z_{ij}=r_n(a_i,b_j)+r_n(b_i,a_j)-r_n(a_i,a_j)-r_n(b_i,b_j).
\]

The cycle resistance identity \(R_{uv}=r_n(u,v)/n\), together with polarization of the cycle pseudoinverse, yields

\[
\tau_n(S)=\frac{n\det\bigl(2nI_k+Z\bigr)}{(2n)^k}.
\]

For \(k=0\), this equals \(n\). All divisions in the program are asserted exact. This second identity is used as an independent crosscheck, not as a substitute for the matrix-tree cofactor.

To determine the greedy output set, the program starts with the singleton collection containing the empty prefix, then for **each** prefix takes all distinct best one-edge extensions; it unions these extensions and repeats for stages two and three. It separately calculates the maximum over **all** triples and its entire equality set. The following output is certified exhaustively:

| \(n\) | Global three-chord maximum | Number of global triples | Greedy stage counts \(\tau_1,\tau_2,\tau_3\) | Number of greedy triples | Greedy/global intersection |
|---|---:|---:|---|---:|---:|
| 5 | 45 | 5 | 11, 24, 45 | 5 | 5 |
| 6 | 81 | 1 | 15, 36, 81 | 1 | 1 |
| 7 | 117 | 7 | 19, 51, 117 | 7 | 7 |
| 8 | 168 | 12 | 24, 72, 168 | 4 | 4 |
| 9 | 240 | 3 | 29, 93, 235 | 18 | 0 |

The complete candidate family for each fixed size is finite and the program covers every member. Its equality-set comparisons show that all greedy outputs at \(n\le8\) reach the optimum and none at \(n=9\) do. Because \(C_4\) has only two nonedges, there is no earlier cycle on which three distinct chords can be added. This proves minimality and the asserted complete tie cases.

## Verification

Run `python3 verify.py` under Python 3.8 or later; only the standard library is needed. The verifier compares \(5,281\) graph configurations with both exact integer determinant methods. It enumerates all \(\binom{|E_n|}{3}\) triples at each size, verifies all three greedy stages under arbitrary ties, checks the exact maxima, and prints the three nine-cycle optimal triples. Numerical approximation and floating point are not used. The executable and the mathematical text are in the same reproducible package.

## Relationship to prior work

Khosoussi, Sukhatme, Huang and Dissanayake (arXiv:1604.01116, first public April 5, 2016), Sections 3 and 4, establish spanning-tree connectivity as a monotone submodular objective and give a general greedy edge-addition approximation algorithm; their guarantees do not assert exact greedy optimality or this first cycle cutoff. Llagostera, López and Comas (arXiv:2005.02848, 2020), Sections 2.2 and 2.3, analyze two- and three-chord Hamiltonian network reliability and compute small exact optimal designs. In particular, their work provides stronger context for optimal three-chord graph structure, but the inspected material does not give the **all-greedy-ties 235-versus-240 obstruction or smallest-order comparison**. The scope here is the greedy algorithm's optimality, not rediscovery of the globally most reliable graph.

## Limitations

This is a finite, exhaustively verified first-obstruction result, not a uniform theorem for larger cycles or a worst-case approximation ratio. The determinant method and the algorithmic question are established; the original element is the complete small-size exact boundary and tie-robust failure. Unindexed work or uninspected portions of specialized reliability-design papers could contain equivalent finite comparisons; independent scholarly review is needed before claiming publication priority. The \(5\)-tree gap is small in numerical terms and is relevant chiefly as a decisive structural failure of exact greedy optimality.

## References

- K. Khosoussi, G. S. Sukhatme, S. Huang, G. Dissanayake, *Maximizing the Weighted Number of Spanning Trees: Near-\(t\)-Optimal Graphs*, arXiv:1604.01116 (first public April 5, 2016), https://arxiv.org/abs/1604.01116 .
- P. Llagostera, N. López, C. Comas, *Network reliability in hamiltonian graphs*, arXiv:2005.02848 (first public May 6, 2020), https://arxiv.org/abs/2005.02848 ; *Discrete Optimization* **41** (2021), 100645.
- S. Li, J. Du, X. Tian, *Maximizing the Number of Spanning Trees in a Connected Graph*, arXiv:1804.02785 (2018), https://arxiv.org/abs/1804.02785 .
