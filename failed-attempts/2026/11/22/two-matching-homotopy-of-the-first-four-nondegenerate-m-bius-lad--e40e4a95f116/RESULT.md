# Two-matching homotopy of the first four nondegenerate Möbius ladders

## Finding
For \(n\in\{3,4,5,6\}\), let \(M_{2n}\) be the Möbius ladder of order \(2n\). Its two-matching complex, defined precisely below, has the following **integral homotopy types**:
\[
\begin{aligned}
\mathcal M_2(M_6)&\simeq S^3,\\
\mathcal M_2(M_8)&\simeq S^5,\\
\mathcal M_2(M_{10})&\simeq S^7,\\
\mathcal M_2(M_{12})&\simeq\bigvee^3 S^8.
\end{aligned}
\]
The last example has three spheres rather than the single sphere appearing in each of the other three cases. The eight-vertex Wagner graph \(M_8\) gives one five-sphere, whereas the eight-vertex cubic graph \(Q_3\) has three five-spheres in its two-matching complex, a previously documented comparison.

## Assumptions and scope
All graphs are finite, simple and undirected. For \(n\ge3\), set \(V(M_{2n})=\{0,1,\dots,2n-1\}\) and take the \(2n\) edges \(\{i,i+1\bmod 2n\}\), plus the \(n\) distinct antipodal edges \(\{i,i+n\}\), \(0\le i<n\). Thus \(|E|=3n\). The simplicial complex \(\mathcal M_2(G)\) has a vertex for every edge of \(G\); a subset \(F\subseteq E(G)\) is a simplex exactly when \(\deg_F(v)\le2\) for every \(v\in V(G)\). This is **not** the ordinary matching complex, the vertex two-independence complex, or the subcomplex of matchings extendible to perfect matchings.

## Proof
**1. Exhaustive finite domain.** Put the \(3n\) distinct edges into lexicographic order \(e_0,\ldots,e_{3n-1}\). Encode a face \(F\) by \(b(F)=\sum_{e_i\in F}2^i\). Enumerate every integer mask from \(0\) through \(2^{3n}-1\), retaining it exactly when all vertex degrees are at most two. The standalone verifier supplies the whole enumeration and tests the condition directly. There are no unexamined masks. The empty face is retained for reduced chain bookkeeping.

**2. Acyclic face-poset matchings.** For \(i=0,\ldots,3n-1\) in order, and for every admissible mask \(b\) in increasing integer order, match \(b\) to \(b+2^i\) when the bit is unset and both faces are still unmatched. Run an entirely separate reverse edge-order matching. For each complete matching, form all codimension-one face-poset covers. Direct each unmatched cover downward by dimension and reverse each matched cover. Exhaustive Kahn topological sorting visits every face in each directed graph; hence each matching is acyclic, not merely pairwise disjoint. This is a finite, executable proof of acyclicity.

The forward matching data are:

| \(n\) | Augmented faces | Face-poset covers | Matching pairs | Unmatched positive-dimensional simplices |
|---|---:|---:|---:|---|
| 3 | 265 | 936 | 132 | one 3-simplex |
| 4 | 1697 | 7976 | 848 | one 5-simplex |
| 5 | 10897 | 64040 | 5446 | two 6-simplices and three 7-simplices |
| 6 | 69941 | 493212 | 34968 | one 7-simplex and four 8-simplices |

The empty simplex is paired with a vertex; equivalently, the resulting augmented Morse complex has a canonical basepoint together with the listed positive-dimensional critical cells. For \(n=3\) and \(n=4\), the discrete-Morse CW model therefore consists of a basepoint and a single positive-dimensional cell; this proves the first two spheres.

**3. Integral attaching degrees.** Orient every face by increasing edge indices. The simplicial boundary is \(\partial[e_{i_1},\ldots,e_{i_k}]=\sum_{j=1}^k(-1)^{j-1}[e_{i_1},\ldots,\widehat{e_{i_j}},\ldots,e_{i_k}]\). For each paired lower cell \(a\) and upper cell \(u\), eliminate the signed unit incidence \(\langle\partial u,a\rangle=\pm1\), substituting the other facets of \(u\) recursively. The verified acyclic gradient order ensures termination and yields the exact *integer*, not just mod-two, critical differential. With rows indexed by critical higher cells, the forward Morse matrices are
\[
D_{7\to6}=\begin{pmatrix}1&0\\0&1\\-1&1\end{pmatrix},\qquad
D_{8\to7}=\begin{pmatrix}-1\\1\\-1\\1\end{pmatrix}.
\]
The first has a unit \(2\times2\) minor and rank two. The second has a unit entry and rank one. Therefore unimodular integral cellular basis changes eliminate all six-dimensional cells and two seven-dimensional cells for \(n=5\), leaving one seven-sphere; for \(n=6\), they eliminate the sole seven-dimensional cell and one eight-dimensional cell, leaving three eight-spheres. Since the attaching maps have domain \(S^d\) and target a wedge of \(d\)-spheres with \(d\ge6\), they are classified by their integral degree vectors; the unit-incidence cellular cancellations are actual homotopy cancellations, not merely homology calculations.

**4. Independent checks.** Reversing the edge-toggle order produces another acyclic matching. For \(n=5\), its signed matrix is \(\begin{pmatrix}-1\\-1\end{pmatrix}\); for \(n=6\), it is \(\begin{pmatrix}1\\-1\\-1\\-1\end{pmatrix}\). Both have the same primitive rank as their forward counterparts. A separate Gaussian elimination on the unreduced simplicial boundary matrices over \(\mathbb F_2\) gives reduced Betti ranks one in degree 3, one in degree 5, one in degree 7 and three in degree 8, respectively, with no other nonzero reduced ranks. The integral homotopy conclusions rest on the preceding primitive integer Morse reductions.

## Verification
Run `python3 verify_mobius_two_matching.py` using Python 3 standard library. All lines of its deterministic output must equal `expected_verification.txt`. For each of the four sizes the program enumerates **all** edge subsets; verifies degree constraints, all directed Hasse covers and acyclicity for both matchings; computes the exact signed Morse boundary; asserts primitive matrices; and independently computes mod-two simplicial homology. The script and its expected output are embedded in the same package as this proof. A finite complete graph calculation is used only to prove these four stated finite cases; it does not extrapolate to an infinite classification.

## Relationship to prior work
Agarwal and Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs* (first public version 2026-08-31; arXiv:2608.30601), study the **vertex independence complexes** and **perfect-matching extendability complexes** of these same graph families. Their Main Theorems 1 and 2 and Section 6 do not determine \(\mathcal M_2\), which admits nonmatching edge sets with two incident edges at a vertex. Vega's *2-Matching Complexes* (arXiv:1909.10406) develops the bounded-incidence construction for other graph families. The published cubical-graph computation \(\mathcal M_2(Q_3)\simeq\bigvee^3S^5\) is a useful same-size cubic-graph comparator, not a Möbius-ladder result. For these triangle-free ladders there is also an equivalent formulation as the three-clique-free vertex-subset complex of the line graph; no directly covering publication was identified in the checked sources.

## Limitations
Only the four graphs of orders 6, 8, 10 and 12 are treated. No claim of periodicity, a general recurrence, a classification of every cubic graph, equivariant homotopy, or any result for \(n\ge7\) is made. Priority is subject to possible unindexed equivalent results and incomplete access to some general historical papers. Independent mathematical audit has not been performed.

## References
1. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601 (first public 2026-08-31), https://arxiv.org/abs/2608.30601 .
2. J. Vega, *2-Matching Complexes*, arXiv:1909.10406 (2019), https://arxiv.org/abs/1909.10406 .
3. M. L. Wachs, *Topology of matching, chessboard, and general bounded degree graph complexes*, *Algebra Universalis* 49 (2003), 345–385, https://doi.org/10.1007/s00012-003-1825-1 .
4. *Three five-spheres in the two-matching complex of the cubical graph*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-three-five-spheres-in-the-two-matching-complex-of-the-cubical-gr--0c97a14379cb .
