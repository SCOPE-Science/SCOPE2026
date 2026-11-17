# Complete hyperoctahedral character of the four-robust clique complex of the Boolean four-cube

## Finding
Let \(Q_4\) be the graph on the sixteen binary four-vectors, with edges joining vectors differing in one coordinate, and let \(X=\mathsf{Cliq}_4(Q_4)\) be the simplicial complex of vertex subsets containing **no independent four-set**. Under the full graph automorphism group \(B_4=(C_2)^4\rtimes\mathfrak S_4\), the complete character of the rational fifth reduced homology representation \(\widetilde H_5(X;\mathbb Q)\) is given by the twenty class values in Table 1 below. Here a positive (respectively negative) coordinate cycle means an orbit of coordinates on which the accumulated bit-flip parity is even (respectively odd); both cycle lists are partitions with total size four.

The underlying nonequivariant homotopy type is \(X\simeq\bigvee^{529}S^5\), consistent with the previously published Alexander-dual total four-cut homology rank. The genuinely additional information is the **full group character** and its decomposition on the translation subgroup \(T=(C_2)^4\). The traces on a pure translation \(b\in T\) of Hamming weight \(0,1,2,3,4\) are respectively
\[
529,\quad -35,\quad 5,\quad 1,\quad 9.
\]
For each linear character \(\lambda_a(b)=(-1)^{a\cdot b}\), the multiplicity depends only on the Hamming weight of \(a\):
\[
\begin{array}{c|ccccc}\mathrm{wt}(a)&0&1&2&3&4\\\hline
\operatorname{mult}(\lambda_a)&27&28&33&37&44.
\end{array}
\]
Consequently, the translation quotient has \(27\) independent rational degree-five homology classes, the quotient by coordinate permutations has \(24\), and the quotient by **all** \(384\) automorphisms has **none**. All these quotient statements concern rational homology of geometric realizations, not integral quotient torsion.

**Table 1: Rational fifth-homology character of the full signed-coordinate group.** A dash denotes an empty list.

| Positive cycles | Negative cycles | Class size | Trace |
|---|---|---:|---:|
| – | 1,1,1,1 | 1 | 9 |
| – | 2,1,1 | 12 | 1 |
| – | 2,2 | 12 | 1 |
| – | 3,1 | 32 | 0 |
| – | 4 | 48 | 1 |
| 1 | 1,1,1 | 4 | 1 |
| 1 | 2,1 | 24 | 1 |
| 1 | 3 | 32 | −2 |
| 1,1 | 1,1 | 6 | 5 |
| 1,1 | 2 | 12 | −3 |
| 1,1,1 | 1 | 4 | −35 |
| 1,1,1,1 | – | 1 | 529 |
| 2 | 1,1 | 12 | 7 |
| 2 | 2 | 24 | −1 |
| 2,1 | 1 | 24 | −21 |
| 2,1,1 | – | 12 | 11 |
| 2,2 | – | 12 | −19 |
| 3 | 1 | 32 | −2 |
| 3,1 | – | 32 | 4 |
| 4 | – | 48 | 1 |

## Assumptions and scope
The graph is the ordinary unweighted Boolean four-cube, **not** the nonperiodic rectangular four-by-four grid (which has only twenty-four edges rather than thirty-two). Use binary vertex labels \(0,\ldots,15\); the neighbors of \(u\) are \(u\oplus 2^i\) for \(i\in\{0,1,2,3\}\). An independent four-set has no internal graph edge. The simplices of \(X\) are exactly the masks whose induced independence number is at most three. The full automorphism group acts by
\[
g_{\sigma,b}(u)=b\oplus\sum_{i=0}^3 u_i2^{\sigma(i)},
\qquad \sigma\in\mathfrak S_4,\ b\in\{0,1\}^4.
\]
The indicated transformations comprise the entire graph automorphism group: an automorphism can send the zero vertex to any of sixteen vertices, and can permute its four neighbors in any of twenty-four ways; graph distances and unique coordinate intervals then determine every remaining image. Thus the action has precisely \(16\cdot24=384\) elements. The complex has sixteen vertices and dimension five; only this single fixed graph and threshold are classified. The representation is over \(\mathbb Q\), not a specified integral module decomposition.

## Proof
**1. Exact finite simplicial model.** There are exactly \(228\) independent four-sets in \(Q_4\). A subset is a simplex of \(X\) if and only if none of these \(228\) sets is contained in it. Exhaustive enumeration of all \(2^{16}\) masks yields the augmented face-number sequence (by cardinality zero through six)
\[
(1,16,120,560,1592,2592,1984),
\]
and no faces of larger cardinality. In particular \(X\) has \(6,864\) nonempty simplices. As an independently computed membership test, for every subset \(S\) compute the exact induced independence number using
\[
\alpha(S)=\max\bigl\{\alpha(S\setminus\{v\}),\,1+\alpha(S\setminus N[v])\bigr\}
\]
with \(\alpha(\varnothing)=0\); both methods give precisely the same face set, not just the same face count.

**2. Integral homotopy concentration.** On the **nonempty** face poset of \(X\), perform the deterministic sequential-element matching: for \(v=0,\ldots,15\), pair each still-unmatched face \(F\) not containing \(v\) with \(F\cup\{v\}\) if both are still available, then remove the pair. The process produces \(3,167\) pairs and leaves exactly one critical vertex and \(529\) critical five-simplices. The complete reversed-matching Hasse graph has \(6,864\) vertices and \(33,152\) edges; its topological sorting visits all \(6,864\) vertices, proving acyclicity. Thus discrete Morse theory yields a CW model with only one zero-cell and \(529\) five-cells. All attaching maps land in its one-point four-skeleton, so \(X\simeq\bigvee^{529}S^5\), with torsion-free integral fifth homology and no other reduced integral homology. This construction independently corroborates, but does not assert novelty for, the already known Alexander-dual sphere count.

**3. Exact equivariant Lefschetz count.** Fix \(g=g_{\sigma,b}\). Let \(O_1,\ldots,O_t\) be its orbits on the sixteen cube vertices. An invariant face is a union \(F_J=\bigcup_{j\in J}O_j\), and it is present precisely if \(\alpha(F_J)\le3\). The signed oriented-chain contribution of any invariant face with \(|J|\) orbits is \((-1)^{|J|-1}\): the permutation sign on a union of orbits cancels the parity of its total vertex count. Including the empty face as the augmented degree-minus-one chain, and using the established concentration in odd degree five, the Hopf trace identity becomes the exact formula
\[
\boxed{\quad
\chi_5(g)=\sum_{\substack{J\subseteq\{1,\ldots,t\}\\\alpha(F_J)\le3}}(-1)^{|J|}.\quad}
\]
Every one of the \(384\) group elements is explicitly enumerated by its coordinate permutation and translation. Applying the displayed sum and grouping by signed coordinate cycle type yields Table 1; the twenty class sizes sum to \(384\), and the trace is constant within every class. As an independent combinatorial Alexander-dual check, for every element the sum over invariant faces of \(\Delta_4^t(Q_4)\) gives the **same** character. This is valid because every signed-coordinate automorphism induces an even permutation of the sixteen graph vertices and the two complexes are combinatorial Alexander duals.

**4. Translation Fourier decomposition and quotient ranks.** Restricting Table 1 to pure translations gives the five Hamming-weight traces above. Orthogonality of the sixteen sign characters of \(T\) gives the exact multiplicity
\[
m(a)=\frac1{16}\sum_{b\in T}(-1)^{a\cdot b}\chi_5(g_{\mathrm{id},b}).
\]
Evaluating this sum gives the multiplicity sequence \(27,28,33,37,44\), with dimension check \(27+4(28)+6(33)+4(37)+44=529\). Averaging the full character over the group gives \(0\) invariant dimensions, while averaging over \(T\) and \(\mathfrak S_4\) gives \(27\) and \(24\), respectively. For a finite simplicial group action, rational homology of the orbit space equals the invariant rational homology after barycentric subdivision, so these averages yield the stated quotient conclusions.

## Verification
The included `verify.py` uses only the Python standard library. Running it alongside `certificate.json` rebuilds the graph and all faces from two independent exact definitions, reconstructs the sequential matching, checks **all** \(33,152\) Hasse covers for gradient acyclicity, computes the \(384\) Lefschetz sums by two dual methods, checks the twenty conjugacy-class constants, and independently performs translation Fourier inversion. It compares all intermediate counts and the matched-pair SHA-256 digest to `certificate.json`, terminating with `VERIFY_OK`. The file `VERIFIER_OUTPUT.txt` records the actual result. The computation is exhaustive for this finite graph, not evidence of an analogous general statement for arbitrary hypercube dimension.

## Relationship to prior work
Filakovský [1] defines robust clique complexes and classifies planar square sequences principally at thresholds two and three (and arbitrary thresholds under edge-only attachment). Its original full-text definitions and main results do not establish the Boolean four-cube character. Carnero Bravo [2] studies bounded independence complexes, dual total cut complexes, and Cartesian products, but treats the relevant general Cartesian-product calculation only at threshold two and explicitly asks for higher thresholds. An earlier exact calculation [3] establishes the **total four-cut complex** of \(Q_4\) to be a wedge of \(529\) eight-spheres; by Alexander duality this supplies the corresponding rational Betti number, so the sphere multiplicity is credited and not presented as independently new. That study does **not** provide an equivariant character. Another prior calculation [4] determines the complete twenty-class character at total-cut threshold **three**, with rank \(129\), rather than the rank-\(529\) threshold-four character here. The present contribution is the complete threshold-four rational \(B_4\)-character, the new weight-dependent translation multiplicities, and the three subgroup-quotient homology ranks.

## Limitations
Only the rational character of the canonical signed-coordinate action and the integral nonequivariant homotopy are determined. No integral \(B_4\)-lattice decomposition, integral torsion for symmetry quotients, canonical equivariant sphere basis, or uniform formula for higher-dimensional cubes is established. Exhaustive finite verification is not independent mathematical auditing, and an unindexed equivalent treatment cannot be excluded absolutely.

## References
1. M. Filakovský, *The Topology of k-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365 (first posted 2026-02-11), https://arxiv.org/html/2602.11365.
2. A. Carnero Bravo, *Total cut complexes and their duals*, arXiv:2602.21427 (first posted 2026-02-24), https://arxiv.org/html/2602.21427v3, especially Section 5.4 and Question 53.
3. *Higher total-cut complexes of the Boolean four-cube*, 2026 mathematical result, https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-higher-total-cut-complexes-of-the-boolean-four-cube--2216882e6bb9/RESULT.md.
4. *The total 3-cut complex of the 4-cube: a 129-sphere wedge and its hyperoctahedral character*, 2026 mathematical result, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-the-total-3-cut-complex-of-the-4-cube-a-129-sphere-wedge-and-its--ccb644c2e2a2/RESULT.md.
5. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics **134** (1998), 90–145.
