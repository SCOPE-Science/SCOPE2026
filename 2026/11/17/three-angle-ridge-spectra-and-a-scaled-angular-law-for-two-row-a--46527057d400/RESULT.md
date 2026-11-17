# Three-angle ridge spectra and a scaled angular law for two-row assignment polytopes

## Finding
For each integer \(n\ge3\), let
\[
P_n=\operatorname{conv}\{(e_i,e_j)\in\mathbb R^n\times\mathbb R^n:1\le i,j\le n,\ i\ne j\}.
\]
This is the full-cardinality \(2\)-assignment polytope of a two-by-\(n\) complete bipartite graph, equivalently the crown-graph root polytope after a sign change in one coordinate block. Equip its affine hull with the inherited standard Euclidean (Frobenius) metric. Its dimension is \(2n-2\). The interior *ridge angle* is the angle inside \(P_n\) between its two incident facet hyperplanes. Every ridge is counted once, without weighting by ridge area.

For \(n\ge4\), the complete angle multiset is

| Angle | Exact number of ridges |
|---|---:|
| \(\arccos(1/(n-1))\) | \(n(n-1)\) |
| \(\pi/2\) | \(n^2\) |
| \(\arccos(-1/(\sqrt2(n-1)))\) | \(2n(n-1)\) |

Thus \(P_n\) has exactly \(4n^2-3n\) ridges for \(n\ge4\). At the exceptional smallest dimension, \(P_3\) has exactly eighteen ridges: six of angle \(\pi/2\) and twelve of angle \(\arccos(-1/(2\sqrt2))\). In particular there are no acute ridges when \(n=3\), but there are \(n(n-1)\) acute ridges for each \(n\ge4\).

If \(\Theta_n\) denotes the interior angle of a uniformly selected ridge of \(P_n\), then for \(n\ge4\)
\[
\boxed{\mathbb E\Theta_n=\frac\pi2+\frac{n-1}{4n-3}
\left(2\arcsin\frac1{\sqrt2(n-1)}-\arcsin\frac1{n-1}\right)>\frac\pi2.}
\]
For \(n=3\), \(\mathbb E\Theta_3=\pi/2+(2/3)\arcsin(1/(2\sqrt2))>\pi/2\). Although every ridge angle tends to \(\pi/2\), the rescaled signed angle \(Z_n=n(\Theta_n-\pi/2)\) converges in distribution to the nondegenerate three-point law
\[
\boxed{\Pr\{Z=-1\}=\tfrac14,\quad\Pr\{Z=0\}=\tfrac14,\quad
\Pr\{Z=1/\sqrt2\}=\tfrac12.}
\]
Its scaled mean satisfies
\[
\boxed{\lim_{n\to\infty}n\left(\mathbb E\Theta_n-\pi/2\right)=\frac{\sqrt2-1}{4}>0.}
\]

## Assumptions and scope
The standard basis is \(e_1,\ldots,e_n\). The ambient realization is not changed by an arbitrary affine transformation: Euclidean angles are not affine invariants. Its affine hull is
\[
H_n=\{(x,y)\in\mathbb R^{2n}:\sum_i x_i=\sum_i y_i=1\},
\]
whose tangent space is \(L_n=\{(v,w):\sum_i v_i=\sum_i w_i=0\}\). The known description of this \(2\)-assignment polytope, specialized to two rows, is
\[
P_n=\{(x,y)\in H_n:x_i\ge0,\ y_i\ge0,\ x_i+y_i\le1\text{ for }1\le i\le n\}.
\]
Its three kinds of facets are labeled \(A_i=\{x_i=0\}\), \(B_i=\{y_i=0\}\), and \(C_i=\{x_i+y_i=1\}\). This halfspace representation and its combinatorial assignment interpretation are previously known and are not claimed as new; the present claim concerns *all* codimension-two incidences, their intrinsic dihedral angles, and their asymptotic law.

## Proof
**1. Known halfspace representation and genuine facets.** Every vertex \((e_i,e_j)\), \(i\ne j\), satisfies the inequalities in the statement. Conversely, a pair of marginal vectors \((x,y)\) with these inequalities admits a nonnegative transportation table of total mass one with diagonal cells forbidden, by the bipartite Hall condition: the only nontrivial neighborhood constraints come from singleton row sets and have the form \(x_i\le1-y_i\); all row sets with two or more indices see every column when \(n\ge3\). Such a table expresses \((x,y)\) as a convex combination of the stated vertices. The point \(x_i=y_i=1/n\) strictly satisfies all \(3n\) inequalities, so \(\dim P_n=2n-2\). To see that each inequality is genuinely a facet, for \(A_i\) set \(x_i=0\), let the remaining entries of \(x\) equal \(1/(n-1)\), and set all entries of \(y\) to \(1/n\). Every other inequality is strict. The \(B_i\) case is symmetric. For \(C_i\), set \(x_i=y_i=1/2\), and let \(x_j=y_j=1/[2(n-1)]\) for \(j\ne i\). This lies in the relative interior of \(C_i\). Consequently there are exactly \(3n\) facets.

**2. Classification of all facet-pair intersections.** In a polytope a codimension-two face has exactly two incident facets, since its two-dimensional normal cone has exactly two extreme rays. It is therefore enough to identify those pairs of facet hyperplanes whose intersection with \(P_n\) has dimension \(2n-4\). The following explicit points have *precisely the indicated two tight inequalities* and all others strict, so each proves a ridge.

For \(n\ge4\):

- For \(A_i\cap A_j\), \(i\ne j\), set \(x_i=x_j=0\), all other \(x\)-coordinates to \(1/(n-2)\), and all \(y\)-coordinates to \(1/n\); for \(B_i\cap B_j\) exchange \(x,y\).
- For \(A_i\cap B_j\), any \(i,j\), set \(x_i=y_j=0\), all remaining entries of each row to \(1/(n-1)\).
- For \(A_i\cap C_j\), \(i\ne j\), set \(x_i=0\), \(x_j=y_j=1/2\), every other \(x_k=1/[2(n-2)]\), and \(y_k=1/[2(n-1)]\) for all \(k\ne j\). The \(B_i\cap C_j\) case is symmetric.

All denominators and strictness conditions above are valid for the specified dimensions. For \(n=3\), the last bullet still works; \(A_i\cap B_j\) is a ridge if \(i\ne j\). Its strict witness may be chosen with the third index \(k\ne i,j\), putting \(x_i=y_j=0\), \(x_j=y_i=3/4\), and \(x_k=y_k=1/4\). Every nonlisted constraint is strict.

The remaining pairs have too small an intersection: \(A_i\cap C_i\) forces \(y_i=1\) and \(y_j=0\) for \(j\ne i\), leaving dimension at most \(n-2\), strictly below \(2n-4\). By symmetry, the same holds for \(B_i\cap C_i\). Two distinct cap facets \(C_i\cap C_j\) force all other column sums to vanish; the intersection is the segment parameterized by \(x_i=y_j=t\), \(x_j=y_i=1-t\) and all other entries zero, hence dimension one. When \(n=3\), each \(A_i\cap A_j\) (and analogously each \(B_i\cap B_j\)) forces the remaining coordinate of the respective row to equal one, leaving only one free coordinate in the other row; each \(A_i\cap B_i\) forces the remaining two column caps to be tight, again yielding a line segment. These intersections have dimension one rather than the required two. No other facet-pair type exists.

For \(n\ge4\) the surviving pair counts are: same-row zero-coordinate facets, \(2\binom n2=n(n-1)\); arbitrary opposite-row zero-coordinate facets, \(n^2\); and differently indexed zero-coordinate/cap facets, \(2n(n-1)\). Summation gives \(4n^2-3n\). For \(n=3\), only \(n(n-1)=6\) opposite-row distinct-index pairs and \(2n(n-1)=12\) zero-coordinate/cap pairs survive, totaling eighteen.

**3. Intrinsic Euclidean angles.** Put \(u_i=e_i-\mathbf1/n\) in the zero-sum subspace of \(\mathbb R^n\). Then
\[
u_i\cdot u_j=\delta_{ij}-1/n,\qquad\|u_i\|^2=(n-1)/n.
\]
Projected outward facet normals in \(L_n\) are
\[
N_{A_i}=(-u_i,0),\qquad N_{B_i}=(0,-u_i),\qquad N_{C_i}=(u_i,u_i).
\]
For any ridge incident to facets \(F,G\), its *interior* angle is \(\arccos[-\langle N_F,N_G\rangle/(\|N_F\|\|N_G\|)]\). For two \(A\)-facets or two \(B\)-facets at different indices, the outward-normal cosine equals \(-1/(n-1)\), giving interior angle \(\arccos[1/(n-1)]\). An \(A\)-normal and a \(B\)-normal are orthogonal, giving \(\pi/2\). For \(A_i\) or \(B_i\) against \(C_j\) with \(i\ne j\), the outward-normal cosine is \(+1/[\sqrt2(n-1)]\), giving the stated obtuse interior angle. This exhausts every ridge by Step 2.

**4. Positive mean bias and scaled law.** Write \(s=1/(n-1)\), \(a=\arcsin(s)\), and \(b=\arcsin(s/\sqrt2)\). Relative to \(\pi/2\), the acute angle contributes \(-a\), and the obtuse angle contributes \(+b\). For \(n\ge4\), the total signed excess is \(n(n-1)(2b-a)\), divided by \(4n^2-3n=n(4n-3)\), yielding the displayed exact mean. The identity
\[
\sin\bigl(2\arcsin(s/\sqrt2)\bigr)=s\sqrt{2-s^2}>s
\]
and the fact that \(0<2\arcsin(s/\sqrt2)<\pi/2\) for \(0<s\le1/3\) imply \(2b>a\). The \(n=3\) mean follows directly from the two surviving angle classes.

For \(n\ge4\), the probabilities of the acute, right, and obtuse classes are respectively \((n-1)/(4n-3)\), \(n/(4n-3)\), and \(2(n-1)/(4n-3)\). Their limits are \(1/4,1/4,1/2\). Moreover,
\[
-n\arcsin(1/(n-1))\to-1,\quad 0\to0,\quad
n\arcsin(1/[\sqrt2(n-1)])\to1/\sqrt2.
\]
Since the laws have only three atoms, these convergences prove weak convergence to the displayed three-point distribution; bounded support after rescaling also proves convergence of the first moment. The limiting mean is \((-1)/4+(1/\sqrt2)/2=(\sqrt2-1)/4\).

## Verification
The standalone script `checks/verify_angles.py` runs under Python 3 with no third-party dependencies. It constructs *every* vertex and *every* facet pair for all \(3\le n\le8\), computes each intersection's affine dimension by exact rational Gaussian elimination, checks the three counts and exceptional dimension-three cases, and calculates the exact squared facet-normal cosine and its sign. It reports `TWO_ROW_FIXED_RANK_RIDGE_EXACT_PASS` after six successful test dimensions. The computations are finite corroboration and do not replace the all-integer geometric proof above.

## Relationship to prior work
Gill and Linusson's *The \(k\)-assignment polytope* supplies the complete-bipartite fixed-cardinality assignment inequality description and affine dimensions; Torres's 2023 paper develops fixed-size matching polytopes for arbitrary bipartite graphs. Their facet and dimension results are starting points, not new results here [1,2]. Existing results for the *same* crown-graph root polytope determine volume, Hausdorff distance, and Gaussian width loss, but not these dihedral angles [3]. Existing general rectangular assignment-polytope work determines intrinsic inradii and their center sets, which likewise do not determine pairwise facet incidences or normal products [4]. Korotov and Vatne calculate angle sums for Cartesian products [5]; the present polytope has the extra \(n\) cap facets \(C_i\) and is a proper nonproduct subpolytope of \(\Delta_{n-1}\times\Delta_{n-1}\), so their product theorem does not yield its spectrum. The universal all-dimensional ridge-angle distribution and its signed scaled limit, rather than the classical polytope description, constitute the claims advanced here.

## Limitations
The results apply to the indicated standard Euclidean realization and to a *uniformly chosen ridge*, not to ridge-area-weighted angular means or arbitrary affine transforms. They do not give higher-codimension angle spectra, a general formula for all \(k\)-assignment polytopes, or independent mathematical certification. Although checked primary literature and related mathematical records do not cover the asserted ridge-angle spectrum, an unindexed equivalent result remains possible under the terminology of crown-graph root polytopes or matching-polytopal geometry.

## References
[1] Jonna Gill and Svante Linusson, *The \(k\)-assignment polytope*, Discrete Optimization 6 (2009), 148–161, DOI: https://doi.org/10.1016/j.disopt.2008.10.003. Author postprint: https://liu.diva-portal.org/smash/get/diva2:210918/FULLTEXT01.pdf.

[2] Juan Camilo Torres, *Normality of \(k\)-Matching Polytopes of Bipartite Graphs*, arXiv:2306.11910v1 (first posted 2023-06-20), https://arxiv.org/abs/2306.11910.

[3] *Rare exponential directional loss despite constant Hausdorff distance in crown-graph root polytopes*, published mathematical result (2026), https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-rare-exponential-directional-loss-despite-constant-hausdorff-dis--771379f5fcb8/RESULT.md.

[4] *Aspect-ratio phase transitions for the inballs of rectangular \(k\)-assignment polytopes*, published mathematical result (2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-aspect-ratio-phase-transitions-for-the-inballs-of-rectangular-k--ea0b015088bd/RESULT.md.

[5] Sergey Korotov and Jon Eivind Vatne, *On dihedral angle sums and number of facets for product polytopes*, Journal of Geometry (first published 2024-09-14), DOI: https://doi.org/10.1007/s00022-024-00732-7.
