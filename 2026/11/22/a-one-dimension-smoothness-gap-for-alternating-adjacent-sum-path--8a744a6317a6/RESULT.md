# A one-dimension smoothness gap for alternating adjacent-sum path polytopes

## Finding
For each integer \(s\ge2\), dimension \(d\ge2\), and \(\varepsilon\in\{0,1\}\), consider the full-dimensional lattice polytope
\[
P_{d,s}^{(\varepsilon)}=\left\{x\in\mathbb R_{\ge0}^{d}: x_i+x_{i+1}\le s+\mathbf1_{i\equiv\varepsilon\pmod 2}\quad(1\le i<d)\right\}.
\]
Here \(\varepsilon=0\) means the *low-first* sequence \(s,s+1,s,s+1,\ldots\), and \(\varepsilon=1\) means the *high-first* sequence \(s+1,s,s+1,s,\ldots\). A lattice polytope is **smooth (Delzant)** when the primitive edge directions at every vertex form an integral basis; equivalently, its primitive incident facet normals form an integral basis.

**Theorem.** These path polytopes have sharp, orientation-dependent smoothness thresholds:
\[
\boxed{P_{d,s}^{(0)}\text{ is smooth}\ \Longleftrightarrow\ 2\le d\le2s+1,\qquad
P_{d,s}^{(1)}\text{ is smooth}\ \Longleftrightarrow\ 2\le d\le2s+2.}
\]
At the first nonsmooth dimension, the low-first polytope \(P_{2s+2,s}^{(0)}\) has **exactly one nonsimple vertex**, while the high-first polytope \(P_{2s+3,s}^{(1)}\) has **exactly two**. Each of these exceptional vertices is incident to exactly \(d+1\) facets; every other vertex at those respective dimensions is simple and smooth.

Write the length-\(2s+2\) vector
\[
q_s=(0,s,1,s-1,2,s-2,\ldots,s,0),\qquad
(q_s)_{2k+1}=k,\quad(q_s)_{2k+2}=s-k\quad(0\le k\le s).
\]
The unique nonsimple low-first vertex is \(q_s\). The two nonsimple high-first vertices are \((0,q_s)\) and \((s+1,q_s)\). All claims concern ordinary (noncyclic) path constraints.

## Assumptions and scope
The parameters \(d,s\) are integers, \(s\ge2\), \(d\ge2\). The orientation parameter is literal: the low-first polytope has capacity \(s\) on index-one edge, whereas the high-first polytope has capacity \(s+1\) there. There is no cyclic edge and no assertion for \(s=1\). Every coordinate is bounded by a positive-capacity incident edge. Small positive coordinates give a full-dimensional point.

Every displayed inequality is a genuine facet. For \(x_j=0\), choose all other coordinates sufficiently small and positive. For a given edge \(j\), set \(x_j=x_{j+1}=b_j/2\), with \(b_j\in\{s,s+1\}\), and all remaining coordinates sufficiently small and positive. The neighboring edge bound is at least \(s\), and \((s+1)/2<s\) for \(s>1\), so every other inequality is strict. Thus there are exactly \(2d-1\) facets, and their incidences can be read from the defining system without hidden redundancies.

## Proof
**1. Active-constraint components.** For a feasible point \(x\), let \(E(x)\) be the set of tight adjacent-sum edges and \(Z(x)=\{i:x_i=0\}\). The graph on \(\{1,\dots,d\}\) with edge set \(E(x)\) is a forest of consecutive paths, including isolated vertices. In a connected component of \(m\) vertices, the \(m-1\) tight edge equations are independent, leaving one free alternating-sign parameter. If this component contains at least one zero coordinate, that zero fixes the parameter uniquely; if it contains none, a small positive and negative alternating perturbation of the component preserves all tight equalities and every strict inequality. Hence \(x\) is a vertex if and only if **each tight-edge component contains a zero coordinate**.

Let \(z_C\) be the number of zero coordinates in a component \(C\). At a vertex, all \(z_C\ge1\), and the total number of incident facets is
\[
\sum_C (|C|-1+z_C)=d+\sum_C(z_C-1).
\]
Consequently a vertex is nonsimple precisely when some tight-edge component contains at least two zeros.

**2. Distance between zeros in a tight component.** Suppose \(x_a=0\) and every edge from index \(a\) up to an index \(b-1\) is tight. When edge \(a\) has high capacity \(s+1\), the next entries are \(x_{a+1}=s+1\) and, if the second edge is also tight, \(x_{a+2}=s-(s+1)=-1\), impossible. In particular, no second zero is reachable on a tight path starting at a high edge.

When edge \(a\) has low capacity \(s\), the forced coordinates are
\[
x_{a+2k}=k,\qquad x_{a+2k+1}=s-k\quad(0\le k\le s),
\]
for as long as the tight path remains feasible. Before \(a+2s+1\), all coordinates following the initial zero are strictly positive; the first second zero occurs exactly at \(a+2s+1\). Therefore **two zeros in a tight-edge component require at least \(2s+1\) intervening edges, with the first zero followed by a low-capacity edge**. This also establishes the converse construction via the displayed staircase.

**3. Sharp dimension cutoff.** In the low-first system, the earliest low edge is index \(a=1\). Thus two zeros in a tight component are impossible for \(d<2s+2\), but the length-\(2s+2\) staircase \(q_s\) is feasible and has every edge tight and its two endpoints zero. By Step 1 it is a nonsimple vertex in dimension \(2s+2\). In the high-first system, the earliest low edge is index \(a=2\). The corresponding minimum dimension is \(2s+3\), and both \((0,q_s)\) and \((s+1,q_s)\) are feasible vertices with two zero anchors in a common tight component.

For any higher dimension, append zero coordinates to an exceptional vertex. All new connecting inequalities are slack, and the new zero coordinates are isolated anchored components, so the original non-simplicity persists. Hence the two cutoffs are both necessary and sufficient for *simplicity*.

At the first cutoff in the low-first family, the only possible pair of zeros in a tight component has indices \(1\) and \(2s+2\). This forces every intervening edge tight and the complete vector to equal \(q_s\). In the high-first family, the unique possible pair has indices \(2\) and \(2s+3\), forcing the trailing coordinates to equal \(q_s\). The first coordinate must either be zero or be linked to the zero second coordinate by its tight high edge, hence equal \(s+1\). These are exactly the vertices listed in the theorem. Their tight-face counts are \(d+1\), while every other vertex at each first cutoff has precisely one zero per tight component and hence exactly \(d\) incident facets.

**4. Simplicity equals lattice smoothness here.** The matrix of all facet normals has rows \(\pm e_i\) and \(e_i+e_{i+1}\). Multiplying every other coordinate column by \(-1\) converts edge rows to signed differences \(\pm(e_i-e_{i+1})\) and retains signed unit rows. The transpose is a reduced signed vertex-edge incidence matrix of the graph made from the path by adding a root connected to every coordinate vertex. Such matrices are totally unimodular: each square minor is \(0\) or \(\pm1\), by the elementary expansion on a row/column with at most one nonzero; if none exists, summing the signed incidence rows shows the determinant vanishes. Consequently all vertices are integral and every nonsingular square basis of incident primitive facet normals has determinant \(\pm1\). At a simple vertex its exactly \(d\) incident normals provide such a basis, so the primitive edge directions are an integral basis. Conversely a smooth polytope is simple by definition. The simplicity thresholds from Step 3 are therefore exactly the claimed smoothness thresholds.

## Verification
The standalone dependency-free Python file `verify.py` independently enumerates every feasible integral point for \(s=2,3\) in all dimensions from two through the respective first nonsimple dimension, then uses exact rational Gaussian elimination on the actual active facet-normal matrix to recognize vertices and count incident facets. All 26 parameter-orientation-dimension cases passed, examining 68,589 feasible lattice points. It found exactly one first singular low-first vertex for each tested \(s\), and two first singular high-first vertices, matching the displayed vectors. It also checks the proposed staircase witnesses and their normal ranks for every \(2\le s\le20\). Run `python3 verify.py` and expect `CHECK_OK cases=26 feasible_points=68589 witnesses=57`.

The exhaustive finite checks do not establish the infinite-family result; Steps 1–4 do. No independent external audit is claimed.

## Relationship to prior work
Jiang, Wen and Zhong (2026, arXiv:2607.14887v1) introduce and analyze the **low-first** alternating adjacent-sum polytope using transfer matrices, Ehrhart theory and Gorenstein questions. Zhou (2026, arXiv:2611.15122v1, submitted November 11) studies the corresponding **high-first** inequality sequence and its lattice-point enumeration. Those results concern counting dilated lattice points and related arithmetic properties, rather than the first occurrence and multiplicity of nonsimple vertices. The distinction between first-edge orientations is essential: it shifts the threshold by exactly one dimension. Classical total unimodularity of bipartite graph incidence matrices and the smooth-vertex criterion are used as standard tools, not claimed as new.

A published classification of Gorenstein members of the low-first family uses facet lattice distances; it does not imply smoothness or nonsimplicity. Another published geometric result determines Euclidean enclosing-ball contact points and diametral pairs of the low-first family; enclosing-ball contacts are different from the full active-face incidence structure. No implication-equivalent smoothness cutoff was located in the targeted literature and mathematical-record searches. This negative search is not proof of historical uniqueness.

## Limitations
The result is for integer \(s\ge2\), noncyclic paths, and exactly two alternating capacities. The \(s=1\) systems can have redundant upper inequalities and require separate treatment; no conclusion about them is asserted. The theorem does not compute the full face lattice or the number of nonsimple vertices in every higher dimension, nor does it give information about normality, reflexivity or Gorenstein status. Historical priority is provisional, especially if a general weighted-path simple-polytope criterion subsumes the theorem under different terminology; the full latest versions of both motivating preprints were not inspected exhaustively.

## References
1. Xinru Jiang, Suzhen Wen, Yueming Zhong, *Alternating adjacent-sum polytopes: transfer matrices and Ehrhart series*, arXiv:2607.14887v1, submitted July 16, 2026. https://arxiv.org/abs/2607.14887
2. Yangbiao Zhou, *Ehrhart Series and Transfer Matrices for Period-Two Polytopes with Consecutive Inequalities*, arXiv:2611.15122v1, submitted November 11, 2026; revised November 13, 2026. https://arxiv.org/abs/2611.15122
3. Tadao Oda, *Convex Bodies and Algebraic Geometry*, Springer, 1988, for the classical smooth lattice-polytope criterion.
