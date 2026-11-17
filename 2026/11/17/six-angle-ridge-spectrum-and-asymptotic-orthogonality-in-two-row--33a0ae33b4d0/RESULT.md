# Six-angle ridge spectrum and asymptotic orthogonality in two-row generalized Pitman–Stanley polytopes

## Finding

For every integer \(m\ge2\), the standard Euclidean two-row generalized Pitman–Stanley polytope \(P_m\) defined below has dimension \(2m\), exactly \(3m+1\) facets, and exactly
\[
R_m=\frac{9m^2-m+2}{2}
\]
codimension-two faces (ridges). For each ridge, write \(c\) for the cosine of the angle between its two *outward* Euclidean unit facet normals. The interior dihedral angle is \(\pi-\arccos(c)\). The **complete multiset of normal cosines**, counting each geometric ridge once, is:

| Normal cosine \(c\) | Number of ridges |
|---|---:|
| \(-1/\sqrt2\) | \(3\) |
| \(-1/2\) | \(2m-1\) |
| \(-1/(2\sqrt2)\) | \(2m-4\) |
| \(0\) | \((9m^2-13m+8)/2\) |
| \(1/2\) | \(m-1\) |
| \(1/\sqrt2\) | \(m\) |

There are exactly \(6m-3\) nonright ridges. Thus, for a uniformly counted ridge, its interior dihedral angle converges in probability to a right angle, with an explicit sharp decay rate:
\[
\Pr(\theta_m=\pi/2)
=\frac{9m^2-13m+8}{9m^2-m+2}
=1-\frac{4}{3m}+O(m^{-2}).
\]
At \(m=2\), the class \(-1/(2\sqrt2)\) has zero multiplicity; from \(m=3\) onward all six classes occur. Facet/ridge numbers are combinatorial; the six cosine levels and the rate are Euclidean metric statements in the specified coordinate realization.

## Assumptions and scope

For \(m\ge2\), use the unscaled ambient Euclidean metric of \(\mathbb R^{2m}\), and define
\[
\begin{split}
P_m=\{(u_1,\ldots,u_m,v_1,\ldots,v_m):{}&u_j,v_j\ge0,\\
&u_1\le1,\quad u_1+v_1\le2,\\
&u_j\ge u_{j+1},\\
&u_j+v_j\ge u_{j+1}+v_{j+1}\ \ (1\le j<m)\}.
\end{split}
\]
This is precisely the \(n=2\), \(\mathbf a=(1,1)\), \(\mathbf b=(0,0)\) specialization of the \(m\)-column generalized Pitman–Stanley polytope in Dugan–Hegarty–Morales–Raymond, with their \(x_{1j}=u_j\), \(x_{2j}=v_j\). Only facet pairs meeting in dimension \(2m-2\) contribute a dihedral angle; nonadjacent pairs do not.

## Proof

**1. Irredundant facets.** Introduce \(s_j=u_j+v_j\). In \((u,s)\)-coordinates the inequalities describe two decreasing chains and the cross-comparisons:
\[
0\le u_m\le\cdots\le u_1\le1,\quad
u_j\le s_j\ (1\le j\le m),\quad
s_m\le\cdots\le s_1\le2.
\]
The inequality \(s_m\ge0\) is implied. This marked two-chain order system admits points with all displayed comparisons strict, so \(P_m\) has dimension \(2m\). Its cover comparisons give the following \(3m+1\) facets; \(e_{u_j},e_{v_j}\) denote standard orthonormal coordinate vectors:

| Facet | Tight equation | Outward normal \(n\) | Count |
|---|---|---|---:|
| \(A\) | \(u_m=0\) | \(-e_{u_m}\) | \(1\) |
| \(B_j\) | \(v_j=0\) | \(-e_{v_j}\) | \(m\) |
| \(C_j\) | \(u_j=u_{j+1}\) | \(-e_{u_j}+e_{u_{j+1}}\) | \(m-1\) |
| \(D_j\) | \(u_j+v_j=u_{j+1}+v_{j+1}\) | \(-e_{u_j}-e_{v_j}+e_{u_{j+1}}+e_{v_{j+1}}\) | \(m-1\) |
| \(E\) | \(u_1=1\) | \(e_{u_1}\) | \(1\) |
| \(F\) | \(u_1+v_1=2\) | \(e_{u_1}+e_{v_1}\) | \(1\) |

Each cover relation can be set to equality while every other listed relation remains strict: merge just its two endpoints in the two-chain order diagram and choose strictly increasing levels for the remaining nodes between the fixed marks \(0<1<2\). Thus each inequality defines a facet and the list is exhaustive.

**2. Which two facets meet in a ridge.** Exactly \(2m-1\) unordered facet pairs do **not** meet in a ridge:
\[
\{B_j,C_j\},\quad\{B_{j+1},D_j\}\ (1\le j<m),
\qquad \{B_1,F\}.
\]
For the first family, \(v_j=0\) and \(u_j=u_{j+1}\) imply \(v_{j+1}=0\) and \(D_j\) is also tight. For the second, \(v_{j+1}=0\) and \(s_j=s_{j+1}\) force \(v_j=0\) and \(C_j\) also tight. The last pair is disjoint since \(v_1=0\) and \(s_1=2\) contradict \(u_1\le1\).

For completeness, the converse uses the *two-relation contraction lemma* for this marked order diagram: contracting any two cover links not listed above introduces neither an additional forced comparison equality nor an identification of nodes across distinct fixed marks. This follows by examining the two local squares \(u_{j+1}\le u_j\le s_j\) and \(u_{j+1}\le s_{j+1}\le s_j\), including the cap \(u_1\le1<2\) and \(u_1\le s_1\le2\); all longer alternate routes contain one of these local squares. The quotient is an acyclic strict-order diagram compatible with its marks. Assigning heights strictly between the marks realizes exactly the two selected equalities with all other inequalities strict. The two selected outward normals are nonparallel, so this intersection has codimension exactly two. Therefore every pair outside the list is a ridge. In particular,
\[
R_m=\binom{3m+1}{2}-(2m-1)=\frac{9m^2-m+2}{2}.
\]

**3. Metric angles and multiplicities.** Compute normalized scalar products \(c=\langle n_G,n_H\rangle/(\|n_G\|\,\|n_H\|)\) for all admissible pairs. The normal lengths for \(A,B_j,E\), \(C_j,F\), and \(D_j\) respectively are \(1,\sqrt2,2\). Only neighboring positions can contribute nonzero scalar products. The complete nonzero tally is:

- \(c=-1/\sqrt2\): \(\{A,C_{m-1}\}\), \(\{C_1,E\}\), \(\{D_1,F\}\), three pairs.
- \(c=-1/2\): \(\{A,D_{m-1}\}\), neighboring \(C\)-pairs (\(m-2\)), neighboring \(D\)-pairs (\(m-2\)), \(\{C_1,F\}\), and \(\{D_1,E\}\); total \(2m-1\).
- \(c=-1/(2\sqrt2)\): neighboring \(C,D\)-pairs with different indices; \(2m-4\).
- \(c=1/2\): \(\{B_j,D_j\}\) for \(1\le j<m\); \(m-1\).
- \(c=1/\sqrt2\): \(\{C_j,D_j\}\) for \(1\le j<m\), and \(\{E,F\}\); \(m\).

All other ridge-normal pairs have scalar product zero. Subtracting the \(6m-3\) nonzero occurrences from \(R_m\) gives \((9m^2-13m+8)/2\) right-angle ridges. Direct division and expansion give the probability formula. This proves the result for every integer \(m\ge2\).

## Verification

The standalone `verify.py` reconstructs all inequalities and facet-normal vectors directly. It checks the exact six-class normal-cosine multiplicities in dimensions corresponding to \(2\le m\le32\). Using a separate slack-maximizing linear program for each facet pair, it checks the predicted ridge/nonridge pattern for \(2\le m\le8\); for \(m=2,3\) it enumerates all vertices with exact rational linear algebra and verifies each pair's intersection affine dimension, rather than inferring adjacency from the normal vectors. The expected completion marker is `TWO_ROW_PS_RIDGE_ANGLE_PASS angle_counts_m=2..32 strict_LP_m=2..8 exact_vertices_m=2,3`. These tests are finite reproducibility checks, not a replacement for the general marked-order proof.

## Relationship to prior work

Dugan, Hegarty, Morales, and Raymond defined this generalized Pitman–Stanley family and studied flow equivalence, vertices, and face numbers [1,2]. Their face enumeration contains some combinatorial information that can determine ridge totals, so neither the family nor combinatorial face-count methods are presented as new. The specific outward-normal cosine multiset, its exact six classes, and its asymptotic concentration at a right angle use the standard Euclidean realization and do not appear in the inspected source's geometric statements. Results on Euclidean inballs and bulk random points of the same generalized Pitman–Stanley family answer different metric questions [3,4]. Distinguish this **multichain flow polytope** from generalized **parking-function polytopes**, which have a different facet system. General marked-order-polytope principles motivate the facet/ridge proof but do not by themselves state the six multiplicities.

## Limitations

The theorem concerns the exact all-ones two-row family with \(m\) columns and the original coordinate Euclidean metric; it is not asserted for other row numbers, data vectors, or arbitrary affine images. The geometric angle spectrum cannot be transported from an integrally equivalent flow-polytope realization without changing the metric. Existing face-count results can imply the unweighted ridge count. Literature priority for the Euclidean six-class statement is provisional: unindexed specializations or metric observations could have escaped the examined literature. There is no independent mathematical audit.

## References

1. W. T. Dugan, M. Hegarty, A. H. Morales, A. Raymond, *Generalized Pitman–Stanley polytope: vertices and faces*, arXiv:2307.09925, first submitted July 19, 2023. https://arxiv.org/abs/2307.09925 ; full HTML https://arxiv.org/html/2307.09925v2
2. W. T. Dugan et al., *Generalized Pitman–Stanley flow polytopes*, Séminaire Lotharingien de Combinatoire 89B (2023), FPSAC Proceedings, article 80. https://www.mat.univie.ac.at/~slc/wpapers/FPSAC2023/80.pdf
3. *The generalized Pitman–Stanley staircase has dimension-free Euclidean inradius*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-generalized-pitman-stanley-staircase-has-dimension-free-eucl--90db80da3ebc
4. *Brownian-excursion transverse geometry of two-row Pitman–Stanley polytopes*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-brownian-excursion-transverse-geometry-of-two-row-pitman-stanley--bae9faf5cc83
