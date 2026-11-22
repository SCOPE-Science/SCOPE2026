# Universal modulo-eight signed-dimer rigidity for the Coxeter graph

## Finding

Let \(G\) be the Coxeter graph on 28 vertices and 42 edges, constructed below, and let \(\mathcal M\) be its 84 perfect matchings. For **every** subset \(S\subseteq E(G)\), define the unnormalized binary Walsh coefficient
\[
W(S)=\sum_{M\in\mathcal M}(-1)^{|S\cap M|}.
\]
Then
\[
\boxed{W(S)\equiv4\pmod8.}
\]
Consequently no character vanishes, the matching-incidence counting convolution on the Boolean group \(\mathbb F_2^{42}\) is invertible, and its exact \(\ell^2\) condition number is \(84/4=21\).

More precisely, after switching signs at vertices to make all 27 edges of a fixed spanning tree positive, the remaining 15 independent edge signs exhibit the following **complete absolute Fourier spectrum**:

| \(|W|\) | Number of reduced signings |
| ---: | ---: |
| 4 | 21000 |
| 12 | 9548 |
| 20 | 1890 |
| 28 | 300 |
| 36 | 28 |
| 84 | 2 |

Each reduced signing represents exactly \(2^{27}\) edge characters with the same absolute coefficient, so the table covers all \(2^{42}\) characters. In the stated tree gauge, the signed multiplicities at \(\pm4,\pm12,\pm20,\pm28,\pm36,\pm84\) are respectively \(10500,4774,945,150,14,1\) at **each** sign. The sharp smallest nonzero absolute coefficient is 4, attained 21,000 times in the reduced table.

## Assumptions and scope

Construct the Fano plane on \(\mathbb Z/7\mathbb Z\) with seven lines \(\{j,j+1,j+3\}\), arithmetic modulo seven. The 28 vertices of \(G\) are the three-element subsets of \(\mathbb Z/7\mathbb Z\) that are **not** those lines; two distinct vertices are adjacent exactly when they are disjoint as triples. This is the classical Coxeter graph, a connected cubic graph with 42 edges.

For an edge subset \(A\), let \(1_A\in\mathbb F_2^{42}\) be its binary incidence vector. Define \(k(x)\) to be 1 if \(x=1_M\) for a perfect matching \(M\) and 0 otherwise, and define convolution \((Tf)(x)=\sum_y k(y)f(x-y)\) over the finite Boolean group. The Walsh basis \(\chi_S(x)=(-1)^{\langle1_S,x\rangle}\) diagonalizes \(T\), with eigenvalues \(W(S)\). All results concern this specified finite graph and unnormalized integer transform; no infinite graph-family claim is made.

## Proof

**1. The requisite matching incidences.** Enumerate perfect matchings using the recurrence that chooses the least currently unmatched vertex and pairs it, in turn, with each available neighbour. It gives exactly 84 matchings. An independent vertex-deletion matching recurrence verifies the total and all required incidences: each edge lies in exactly 28 perfect matchings, and the number \(c_{ef}\) of perfect matchings containing two distinct edges \(e,f\) is always even. Across the 861 unordered edge pairs, the exact incidence histogram is

| \(c_{ef}\) | Number of pairs |
| ---: | ---: |
| 0 | 84 |
| 4 | 21 |
| 6 | 168 |
| 8 | 168 |
| 10 | 84 |
| 12 | 168 |
| 14 | 168 |

These are exact finite certificates: the independent recursive algorithms, explicit graph input, and complete pair comparisons are provided in `verify.py`. In particular the parity assertion covers **every** edge pair, rather than sampled pairs.

**2. Modulo-eight rigidity for all signings.** Set \(I_e(M)=1\) if \(e\in M\), zero otherwise, and expand
\[
(-1)^{|S\cap M|}=\prod_{e\in S}(1-2I_e(M)).
\]
Summing over matchings and retaining only terms of size at most two modulo eight gives
\[
W(S)\equiv84-2\sum_{e\in S}28
+4\sum_{\{e,f\}\subseteq S}c_{ef}\pmod8.
\]
Since 28 is a multiple of four and each \(c_{ef}\) is even, the last two terms are zero modulo eight. Hence \(W(S)\equiv84\equiv4\pmod8\) for all \(S\), proving nonvanishing without enumerating all \(2^{42}\) edge subsets.

**3. Exhaustion of the complete Fourier spectrum.** For a vertex subset \(U\), switch each incident edge sign once for each endpoint in \(U\). Because every perfect matching contains exactly one edge incident to each vertex, switching at \(U\) multiplies its signed sum by \((-1)^{|U|}\) and therefore preserves absolute value. Switching along a spanning tree uniquely gauges its 27 edge signs to positive, modulo the simultaneous switch at all 28 vertices; the 15 non-tree signs remain independent. This produces \(2^{15}=32768\) gauge classes, each with exactly \(2^{27}\) original sign assignments.

Identify each perfect matching with its 15-bit chord-incidence mask, form the integer multiplicity array on \(\mathbb F_2^{15}\), and apply the unnormalized Walsh–Hadamard transform. The resulting 32,768 exact coefficients give the signed and absolute tables above. Each coefficient is also verified by a separate direct 84-term signed summation, independently of the transform recurrence. The complete spectrum then follows from the gauge argument, with no missed frequencies. It contains coefficients of absolute magnitude 4 and 84; the latter is achieved by the trivial signing. As \(T\) is real self-adjoint and unitarily diagonalized by Walsh characters, its \(\ell^2\) condition number is exactly \(84/4=21\) and its rank is \(2^{42}\).

## Verification

Run `python verify.py` with Python 3.9 or later; only its standard library is used. The program constructs the graph from the seven Fano lines; recursively lists every matching with uniqueness checks; independently counts remaining-vertex matchings to obtain single-edge and pairwise frequencies; compares all 861 pair counts by both methods; fixes an explicit breadth-first spanning-tree gauge; checks every transformed value against a direct signed sum; verifies the full histogram, Plancherel identity, nonvanishing and congruence; and asserts the stated rank and extremal magnitudes. It prints `PASS` after every assertion. The finite algorithm is exhaustive on the specified graph, not a proof for different graphs.

## Relationship to prior work

Biggs introduced and studied the Coxeter graph's exceptional geometry and proved that it has 84 perfect matchings; these facts supply context and are not claimed as new. Dejter gives a Fano-geometric treatment of the graph. Later work on graph matching polynomials concerns unsigned enumerators. Their matching totals and graph constructions do not imply the present signed congruence, its six-level absolute spectrum, or its Boolean convolution condition number. The new content is the complete cancellation-free Fourier classification, with a two-incidence arithmetic explanation.

## Limitations

The theorem is restricted to the Coxeter graph and the ordinary, equally weighted perfect-matching incidence measure. The result is not a classification of weighted complex dimer partition functions, of arbitrary cubic graphs, or of all spectral projection norms. Priority against unindexed prior signed enumerations cannot be guaranteed, and independent mathematical review has not been performed.

## References

1. N. L. Biggs, *Three Remarkable Graphs*, Canadian Journal of Mathematics **25** (1973), 397–411. DOI: https://doi.org/10.4153/CJM-1973-040-1.
2. I. J. Dejter, *From the Coxeter graph to the Klein graph*, arXiv:1002.1960, first public preprint version 2010-02-09. https://arxiv.org/abs/1002.1960.
3. *Matching Polynomials of Symmetric, Semisymmetric, Double Group Graphs and a Graph Formed by Three Mutual-Coupled Networks*, Symmetry **17** (2025), article 133. DOI: https://doi.org/10.3390/sym17010133.
