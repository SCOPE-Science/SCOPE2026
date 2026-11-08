# The shattered-support complexes of the Schläfli graph under open and closed neighborhoods

## Finding
Let \(G\) be the Schläfli graph on the \(27\) lines of a smooth cubic surface, with adjacency meaning the lines are *skew*. For \(m\in\{\mathrm{open},\mathrm{closed}\}\), let \(\mathcal C_m\) contain the \(27\) corresponding vertex neighborhoods, and let \(\Phi_m(z)=\sum_{k\ge0}s_k(m)z^k\) count the \(k\)-vertex supports shattered by that neighborhood class.

The *complete* polynomials are
\[
\Phi_{\mathrm{open}}(z)=1+27z+351z^2+2880z^3+1080z^4,
\qquad
\Phi_{\mathrm{closed}}(z)=1+27z+351z^2+720z^3+1080z^4.
\]
In particular, both VC dimensions are \(4\). More precisely, for any subset \(S\subseteq V(G)\):

- If \(|S|\le2\), it is shattered by both classes.
- If \(|S|=3\), it is shattered by the open-neighborhood class precisely when \(G[S]\) contains an edge; it is shattered by the closed-neighborhood class precisely when \(G[S]\) is a triangle.
- If \(|S|=4\), it is shattered by either class precisely when \(G[S]\cong K_4\).
- If \(|S|\ge5\), it is shattered by neither class.

Thus the two shattering complexes have **identical top-dimensional faces** (the \(1080\) four-cliques), but differ on precisely \(2160\) triangular-size faces: every one-edge and two-edge triple is shattered only in the open model. The \(45\) independent triples are shattered by neither model.

## Assumptions and scope
The graph is the standard \(27\)-vertex Schläfli graph, uniquely specified by strongly regular parameters \((27,16,10,8)\). One combinatorial realization has vertices \(a_i,b_i\) for \(i\in\{0,1,2,3,4,5\}\) and \(c_{ij}\) for \(0\le i<j\le5\), with the following complete adjacency rules for distinct vertices:

1. Two vertices of type \(a\), or two of type \(b\), are adjacent.
2. \(a_i\) is adjacent to \(b_j\) if and only if \(i=j\).
3. A vertex \(a_i\) or \(b_i\) is adjacent to \(c_{jk}\) if and only if \(i\notin\{j,k\}\).
4. \(c_{ij}\) and \(c_{k\ell}\) are adjacent if and only if \(\{i,j\}\cap\{k,\ell\}\ne\varnothing\).

A neighborhood concept has value \(1\) at a queried vertex exactly when it is adjacent to the chosen center; in the closed model, equality with the center also yields \(1\). Shattering requires all \(2^{|S|}\) Boolean restrictions, including the all-zero restriction. Every center ranges over all \(27\) vertices, not a chosen subset.

## Proof
There are \(6+6+\binom62=27\) vertices. For a second construction, represent the vertices by the divisor vectors \(E_i\), \(Q_i=2H-\sum_{j\ne i}E_j\), and \(L_{ij}=H-E_i-E_j\) in the blow-up model of a cubic surface. For two distinct \((-1)\)-curves represented as \(dH-\sum_i m_iE_i\), their intersection is \(dd'-\sum_i m_im'_i\). Declare them adjacent when this intersection is zero. Substitution gives exactly the four adjacency rules above. Directly counting common neighbors establishes the parameter tuple \((27,16,10,8)\); the executable proof checks both independent constructions entry-by-entry and every degree and pairwise common-neighbor count.

Fix an unordered \(k\)-set \(S=(v_0,\ldots,v_{k-1})\) listed in the vertex order \(a_0,\ldots,a_5,c_{01},\ldots,c_{45},b_0,\ldots,b_5\). Encode the restriction of the neighborhood of center \(u\) to \(S\) as the integer
\[
T_m(u,S)=\sum_{j=0}^{k-1}2^j\mathbf 1\{v_j\in N_m(u)\}.
\]
Then \(S\) is shattered if and only if \(\#\{T_m(u,S):u\in V(G)\}=2^k\). This equality is a finite decidable predicate, not a statistical test. The accompanying complete executable enumeration visits **all** \(\binom{27}{k}\) supports for each \(0\le k\le4\), evaluates all \(27\) possible centers for each support, and independently forms trace tuples from the second graph construction. The two trace sets agree for every support.

The enumeration yields the following exhaustive table for triples, classified by number of edges of the induced graph:

| Induced edges on three vertices | Total supports | Open shattered | Closed shattered |
|:--:|--:|--:|--:|
| \(0\) | 45 | 0 | 0 |
| \(1\) | 1080 | 1080 | 0 |
| \(2\) | 1080 | 1080 | 0 |
| \(3\) | 720 | 720 | 720 |

For quadruples, the independent induced-edge histogram at edge counts \(0,1,2,3,4,5,6\) is respectively \(0,0,2160,6480,4590,3240,1080\). In **both** models every quadruple with fewer than six edges fails a shattering trace, and all \(1080\) six-edge quadruples realize all \(16\) traces. A supplementary certificate partitions those \(1080\) quadruples into exactly \(12\) orbits under the natural \(S_6\)-action, of sizes \(15,60,180,120,60,180,30,120,60,180,60,15\), with orbit total \(1080\). The checker independently tests that every proposed permutation preserves the graph.

All \(351\) unordered vertex pairs and all \(27\) singletons realize the full trace set in both models. No \(k\)-set with \(k\ge5\) can be shattered, since the entire concept family has at most \(27<2^5\) distinct concepts. Combining these facts proves both support characterizations, coefficient formulas, and the VC-dimension assertions.

## Verification
Run `python3 verify_schlafli.py` with standard-library Python 3. Expected first line:

`SCHLAEFLI_SHATTER_PASS 27 vertices 351 pairs 2925 triples 17550 quadruples 12 S6 top orbits`

The verifier checks the two non-equivalent descriptions of the Schläfli graph, strongly regular parameters, all support/center traces for sizes \(0\) through \(4\), both structural criteria on *every* support, all coefficient and induced-edge totals, the complete \(S_6\) orbit partition of four-cliques, and \(16\) explicit trace witnesses for a sample four-clique. Enumeration is exhaustive over a finite graph; no randomization, external service, or computation over an unbounded range is involved.

## Relationship to prior work
Coudert, Csikós, Ducoffe, and Viennot (2024) define graph VC dimension through closed neighborhoods and develop an efficient general algorithm, whereas this result gives the exact *entire shattering complex* for the Schläfli graph, for both open and closed conventions. Pham, Senger, Tait, and Nguyen Thu-Huyen (2023) study VC lower bounds for pseudorandom graph adjacency concept classes; their asymptotic conditions do not imply this finite classification. Standard Schläfli-graph references give the strongly regular parameters, maximal cliques, and \(45\) independent triples, but do not determine which supports realize every neighborhood trace. The ordinary Lovász neighborhood complex of a graph (faces merely sharing one common neighbor) is mathematically different from its VC-shattering complex (faces realizing **all** Boolean traces); results about one do not imply this classification of the other.

## Limitations
The statement concerns one canonical finite graph, not all strongly regular graphs or all configurations of lines. It depends on the open/closed conventions specified above. The proof is a transparent, exhaustive finite certificate rather than a uniform symbolic classification for a graph family; in particular the triple and quadruple assertions require the enclosed independent exact enumerations. The historical originality comparison is bounded by accessible literature and does not prove global priority.

## References
1. D. Coudert, M. Csikós, G. Ducoffe, L. Viennot, *Practical Computation of Graph VC-Dimension*, arXiv:2405.07588 (first submitted 2024-05-13); DOI:10.4230/LIPIcs.SEA.2024.8.
2. T. Pham, S. Senger, M. Tait, N. Thu-Huyen, *VC-dimension and pseudo-random graphs*, arXiv:2303.07878 (2023-03-14).
3. A. E. Brouwer, *Schläfli graph*, https://jaanos.github.io/tables/graphs/Schlaefli.html (classical graph construction and clique data).
4. M. Anthony, G. Brightwell, C. Cooper, *The Vapnik-Chervonenkis dimension of a random graph*, Discrete Mathematics 138 (1995), 43–56; DOI:10.1016/0012-365X(94)00187-N.
