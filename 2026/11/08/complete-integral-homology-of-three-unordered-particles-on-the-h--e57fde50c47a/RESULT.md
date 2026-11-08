# Complete integral homology of three unordered particles on the Heawood graph

## Finding
Let \(H\) be the Heawood graph, presented as the incidence graph of the Fano plane. Its points are \(p_i\), its lines are \(\ell_j\), where \(i,j\in\mathbb Z/7\mathbb Z\), and incidence is defined by \(i-j\in\{0,1,3\}\). Let \(B_3(H)\) be the topological space of unordered configurations of three pairwise distinct points of the geometric realization of \(H\). Then
\[
H_k(B_3(H);\mathbb Z)\cong
\begin{cases}
\mathbb Z,&k=0,3,\\
\mathbb Z^8\oplus\mathbb Z/2,&k=1,\\
\mathbb Z^{43},&k=2,\\
0,&k\ge4.
\end{cases}
\]
The new component of this classification is the exact integral degree-two group, **including the absence of torsion of every order**. The integral degree-one and degree-three results and the mod-two/mod-three Betti numbers were already available; they are reproduced here for context, not offered as separate discoveries.

## Assumptions and scope
The graph has fourteen vertices, twenty-one edges and degree three at every vertex. A graph means its one-dimensional topological realization, including edge interiors. Configurations are *unordered* and have no collisions. Integral coefficients are used throughout; the answer is not merely a field-homology computation. The standard full-vertex reduced Świątkowski complex computes the integral singular homology of this configuration space by the comparison and reduced-complex theorems of An, Drummond-Cole and Knudsen [3]. The primary early source motivating graph configuration spaces is Ghrist's public preprint of 5 May 1999 [1].

For each vertex \(v\), order its three incident edges as \(e_{v,0},e_{v,1},e_{v,2}\). The local reduced chain generators of homological degree one are the differences \(h_{v,1}-h_{v,0}\) and \(h_{v,2}-h_{v,0}\). Polynomial variables for graph edges have homological degree zero and weight one. Each local difference has weight one and homological degree one. Their differential is
\[
\partial(h_{v,a}-h_{v,0})=e_{v,a}-e_{v,0}\qquad(a=1,2).
\]
The global differential is the graded Leibniz differential; the indicated vertex order fixes the Koszul signs. We retain exactly weight three. The complex vanishes above homological degree three.

## Proof
**Step 1: exhaustive finite integral model.** Choose \(q\) distinct graph vertices, choose one of their two local differences at each, and multiply by a monomial of edge variables of total weight \(3-q\), for \(0\le q\le3\). This gives free integral chain groups in dimensions zero through three of respective ranks
\[
(1771,6468,7644,2912).
\]
These ranks are computed directly by the formulas \(\binom{23}{3}\), \(14\cdot2\binom{22}{2}\), \(\binom{14}{2}\cdot4\cdot21\), and \(\binom{14}{3}\cdot8\). Every signed boundary entry is generated from the displayed local differential; the verifier checks \(\partial_1\partial_2=0\) and \(\partial_2\partial_3=0\) over **the integers**, not just modulo a prime.

**Step 2: exact integer diagonal invariants.** The verification program performs invertible elementary integer row and column operations. It repeatedly chooses entries equal to \(1\) or \(-1\), eliminates the corresponding row and column by an exact Schur complement, and continues to exhaustion. Such eliminations are unimodular and contribute Smith invariants equal to one. On the three full boundary matrices the result is:
\[
\begin{aligned}
\partial_1&:\quad 1^{1770}\quad\text{and zeros},\\
\partial_2&:\quad 1^{4689},\ 2\quad\text{and zeros},\\
\partial_3&:\quad 1^{2911}\quad\text{and zeros}.
\end{aligned}
\]
For \(\partial_2\), the residual after the 4,689 unit eliminations has nonzero rank exactly one. The program verifies this exactly by cross-multiplying every pair of columns against a fixed pivot entry. The gcd of **all** its integer coefficients is exactly two, so its sole nonzero Smith invariant is two, not just an observed finite-field rank. For \(\partial_3\), unit elimination leaves the zero matrix; its result is reproduced under two different pivot orderings. All remaining steps consist of integer arithmetic and exact assertions, not numerical tolerance or probabilistic tests.

**Step 3: read homology, including integral torsion.** The boundary ranks over \(\mathbb Q\) are \((1770,4690,2911)\). Thus the integral free ranks are \((1,8,43,1)\) in degrees zero through three. Since \(\partial_1\) has only unit nonzero Smith factors and \(\partial_1\partial_2=0\), the unique degree-one torsion factor is the factor two of \(\partial_2\). Since the cokernel of \(\partial_3\) is torsion-free (all its nonzero Smith factors are one), its subgroup \(\ker\partial_2/\operatorname{im}\partial_3\) is also torsion-free: it is a subgroup of that cokernel. Thus \(H_2\) is exactly \(\mathbb Z^{43}\). The degree-three kernel has rank one and no incoming boundary, hence is \(\mathbb Z\). There are no chains above dimension three.

## Verification
A complete self-contained Python 3 verifier is included at `artifacts/verify_integral.py`, with its actual stdout at `artifacts/verification_output.txt`. Execute `python3 artifacts/verify_integral.py` from the package root; no third-party Python dependency is required. It reconstructs every face-module basis element and signed differential, checks all integer chain identities, and calculates all three integral Smith diagonal invariants. Its final stdout line is `ALL_CHECKS_PASS`.

The finite model has 1,771, 6,468, 7,644 and 2,912 basis elements in degrees zero through three. The residual Smith calculation for degree two has 24 nonzero rows and 305 nonzero columns. Both independent pivot orders in degree three terminate with 2,911 unit invariants. The results also imply the previously published mod-two Betti vector \((1,9,44,1)\) and mod-three vector \((1,8,43,1)\) by the universal coefficient theorem.

## Relationship to prior work
Ghrist [1] introduced the graph-configuration-space perspective and proves broad structural results, not these integral groups. Ko and Park [2] determine first homology of graph braid groups; the \(\mathbb Z^8\oplus\mathbb Z/2\) entry is known rather than a new result. An, Drummond-Cole and Knudsen [3] give the reduced Świątkowski model used for the calculation. Maciążek and Sawicki [4] show structural generation of second homology for graphs of maximum degree three, but do not determine all integral relations or torsion for the Heawood graph.

A previous exact report [5] already proves \(H_3\cong\mathbb Z\) and the mod-two and mod-three Betti vectors for **this same three-particle Heawood object**. Its full result explicitly leaves the integral groups in degrees one and two undetermined. Those field Betti numbers, even combined with known \(H_1\), do not rule out torsion of prime order at least five or its higher prime powers in \(H_2\). The new exact \(\partial_3\) Smith computation resolves the remaining question.

An's subsequent work [6] computes torsion for complete bipartite graph families, particularly \(K_{a,b}\), not the cubic Fano incidence graph; its listed specialized conclusions do not entail the present integral degree-two classification. Planar-graph-only theorems do not apply, because \(H\) is nonplanar.

## Limitations
This is a result for exactly three unordered points on one specified fourteen-vertex graph. It does not determine the fundamental group, cohomology ring, symmetry action, configurations of other particle numbers, or corresponding groups for arbitrary incidence graphs. The claim of previously unreported integral degree-two homology is supported by explicit source comparisons and record searches, not a proof of global publication priority. Independent mathematical audit has not been performed.

## References
1. R. Ghrist, *Configuration spaces and braid groups on graphs in robotics*, arXiv:math/9905023, first public 1999-05-05, https://arxiv.org/abs/math/9905023.
2. K. H. Ko and H. W. Park, *Characteristics of graph braid groups*, arXiv:1101.2648, first public 2011-01-13, https://arxiv.org/abs/1101.2648.
3. B. H. An, G. C. Drummond-Cole and B. Knudsen, *Subdivisional spaces and graph braid groups*, arXiv:1708.02351, first public 2017-08-08, https://arxiv.org/abs/1708.02351.
4. T. Maciążek and A. Sawicki, *Non-abelian Quantum Statistics on Graphs*, arXiv:1806.02846, first public 2018-06-07, https://arxiv.org/abs/1806.02846.
5. *Three-particle homology of the Heawood graph*, previously published exact computation, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-three-particle-homology-of-the-heawood-graph--7524bced20b8/RESULT.md.
6. B. H. An, *Torsion of every finite order in the homology of graph braid groups*, arXiv:2610.04305, first public 2026-10-03, https://arxiv.org/abs/2610.04305.
