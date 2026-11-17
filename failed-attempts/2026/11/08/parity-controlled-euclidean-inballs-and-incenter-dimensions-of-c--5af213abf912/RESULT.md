# Parity-controlled Euclidean inballs and incenter dimensions of complete-bipartite symmetric edge polytopes

## Finding
For integers \(2\le p\le q\), put \(N=p+q\), \(H=\{z\in\mathbb R^N:\sum_i z_i=0\}\), and form the canonical symmetric edge polytope
\[
P_{p,q}=\operatorname{conv}\{\pm(e_i-e_{p+j}):1\le i\le p,\ 1\le j\le q\}\subset H.
\]
All balls and distances are Euclidean **within** \(H\), not in the ambient \(\mathbb R^N\). Write \(\varepsilon_q=q\bmod2\) and \(R_{p,q}=\sqrt{q-\varepsilon_q/N}\). The exact maximum inscribed ball radius is
\[
\boxed{r_{p,q}=R_{p,q}^{-1}.}
\]
The origin is a center of a maximum ball. Its full set of alternative centers has affine dimension
\[
\boxed{
\dim\mathcal I_{p,q}=\begin{cases}
p-\varepsilon_q,&p<q,\\
1,&p=q\text{ even},\\
0,&p=q\text{ odd}.
\end{cases}}
\]
The origin-centered maximal ball is tangent to precisely
\[
\boxed{F_{p,q}=\begin{cases}
\binom{q}{q/2},&p<q,\ q\text{ even},\\
2\binom{q}{(q-1)/2},&p<q,\ q\text{ odd},\\
2\binom{q}{q/2},&p=q\text{ even},\\
4\binom{q}{(q-1)/2},&p=q\text{ odd}
\end{cases}}
\]
facets. **All** centers, including their boundaries, are given by the finite, explicitly stated inequalities below. The facet-distance multiset is also determined by the sign sums of the two color classes.

For instance, \(P_{2,4}\) has inradius \(1/2\), six origin-tangent facets, and a two-dimensional incenter locus, whereas \(P_{3,3}\) has inradius \(\sqrt{6/17}\), twelve origin-tangent facets, and a unique incenter. Although every \(P_{m,m}\) is centrally symmetric, its incenter is unique for odd \(m\), but forms a nontrivial **line segment** for even \(m\).

## Assumptions and scope
The graph is connected, so the signed edge vectors span \(H\); central symmetry then makes the origin an interior point of \(P_{p,q}\). The two color classes are \(A=\{1,\ldots,p\}\) and \(B=\{p+1,\ldots,p+q\}\); the metric is inherited from the signed-incidence realization. Fix \(p,q\) throughout a finite-dimensional claim. A facet-label sign vector on \(B\) is \(\eta\in\{\pm1\}^q\), with \(S_\eta=\sum_j\eta_j\); on \(A\) it is \(\xi\in\{\pm1\}^p\), with \(S_\xi=\sum_i\xi_i\). Let \(\mathbf1\) be the length-\(N\) all-one vector. Define
\[
 u_\eta=(0_A,\eta_B)-\frac{S_\eta}{N}\mathbf1,
 \qquad v_\xi=(\xi_A,0_B)-\frac{S_\xi}{N}\mathbf1.
\]
These lie in \(H\). Each distinct such vector is the outward normal of a facet with right side \(1\), and the two all-constant-sign normals are duplicated across the classes. This is the complete facet-label family of Higashitani--Jochemko--Michałek, Proposition 3.4 (2018 preprint/2019 journal article); the metric consequences below are separate deductions.

The complete center set for maximal-radius balls is the following **finite polytope in \(H\)**:
\[
\begin{split}
\mathcal I_{p,q}=\{z\in H:\;&\sum_{j=1}^{q}\eta_jz_{p+j}
+r_{p,q}\sqrt{q-S_\eta^2/N}\le1\quad(\forall\eta\in\{\pm1\}^q),\\
&\sum_{i=1}^{p}\xi_i z_i
+r_{p,q}\sqrt{p-S_\xi^2/N}\le1\quad(\forall\xi\in\{\pm1\}^p)\}.
\end{split}
\]
This exact description includes centers on all lower-dimensional faces; the tangent-facet count in the Finding is specifically for center \(0\).

## Proof
**1. Facets.** The polar polytope in \(H\) is
\[
Q_{p,q}=\{u\in H:|u_i-u_{p+j}|\le1\text{ for all }i,j\}.
\]
At a vertex of \(Q_{p,q}\), the graph of pairs with equality must be connected and spanning, since otherwise the coordinates could be perturbed by a nonconstant componentwise shift without violating any constraint. If both color classes have nonconstant coordinate values, all equality edges of difference \(+1\) join \(A\)-maxima to \(B\)-minima, and all equality edges of difference \(-1\) join \(A\)-minima to \(B\)-maxima. The two equality graphs are disjoint, so they cannot span a connected graph. Consequently a vertex must be constant on one color class. On the other class, every coordinate must be at difference exactly \(1\) or \(-1\), or else that coordinate lacks an equality edge. Conversely, each such sign potential has connected spanning equality edges, and hence is a vertex. Therefore the listed \(u_\eta,v_\xi\) are **all** polar vertices, hence the complete family of facet normals of \(P_{p,q}\). In particular there are \(2^p+2^q-2\) facets, consistent with the earlier facet classification.

**2. Facet distances and sharp radius.** Orthogonal centering gives
\[
\|u_\eta\|^2=q-\frac{S_\eta^2}{N},\qquad
\|v_\xi\|^2=p-\frac{S_\xi^2}{N}.
\]
A corresponding support hyperplane has distance \(1/\|u\|\) from \(0\). Across sign words of length \(s\), the smallest possible \(|S|\) is \(s\bmod2\); thus the maximum squared facet-normal norm for the \(B\)-family is \(q-\varepsilon_q/N\). For \(p<q\) this strictly exceeds the maximum for the \(A\)-family. For \(p=q\) the maxima coincide. Hence the largest polar-vertex norm is \(R_{p,q}\), and a ball of radius \(1/R_{p,q}\) centered at \(0\) lies in every facet halfspace. Conversely, if a radius-\(r\) ball centered at any \(z\in H\) lies in \(P_{p,q}\), its clearance from every opposite facet pair \(\pm u\) implies \(r\|u\|+|\langle u,z\rangle|\le1\). Taking a maximum-norm \(u\) proves \(r\le1/R_{p,q}\). This proves the exact global inradius.

The squared inverse distances of **all facets**, counted with multiplicity, are \(q-(q-2j)^2/N\) for \(0\le j\le q\), each with multiplicity \(\binom qj\), together with \(p-(p-2i)^2/N\) for \(0\le i\le p\), each with multiplicity \(\binom pi\); delete the two duplicate constant-sign normals. Sign balances \(S=0\) (even) or \(|S|=1\) (odd), with the extra class contribution when \(p=q\), yield the displayed tangent-facet counts.

**3. All centers and their affine dimensions.** A center \(z\) at maximal radius must be orthogonal to every maximum-norm facet normal. For \(p<q\) and even \(q\), the balanced sign vectors on \(B\) span the zero-sum subspace of \(\mathbb R^q\), since switching a plus and minus sign produces every coordinate difference. Consequently \(z_B\) must have all coordinates equal, while \(z_A\) is otherwise free subject to \(\sum_i z_i=0\). The resulting linear space has dimension \(p\). If \(p<q\) and \(q\) is odd, the sign vectors with sum \(1\) instead span all of \(\mathbb R^q\): their differences span its zero-sum part, and a single vector has nonzero sum. Thus \(z_B=0\) and \(\sum_{i\in A}z_i=0\), a space of dimension \(p-1\).

If \(p=q\) is even, the two balanced sign-vector families force both color classes to have constant coordinates. The zero-sum condition leaves the line \(z=(t\mathbf1_p,-t\mathbf1_p)\). If \(p=q\) is odd, the maximum-norm families span all coordinate directions under the zero-sum restriction, leaving only \(z=0\).

All nonmaximum-norm facets have **strict positive clearance** at the origin for a radius-\(r_{p,q}\) ball. There are only finitely many of them. Hence a sufficiently small relative neighborhood of zero inside each just-described tangent-orthogonal linear space remains feasible; that space is exactly the affine hull of the full incenter set. The explicit clearance inequalities stated under Assumptions and scope give the entire incenter set, rather than merely its affine hull.

For \(p=q=m\) even, substitute \(z=(t\mathbf1_m,-t\mathbf1_m)\). The inequalities indexed by nonzero sign sums \(S\in\{\pm2,\pm4,\ldots,\pm m\}\) become
\[
|t|\le g_m(|S|):=\frac{1-\sqrt{1-S^2/(2m^2)}}{|S|}
=\frac{|S|}{2m^2(1+\sqrt{1-S^2/(2m^2)})}.
\]
The right side strictly increases with \(|S|\); \(|S|=2\) is binding. Hence **the complete segment** is
\[
\boxed{\mathcal I_{m,m}=\{(t\mathbf1_m,-t\mathbf1_m):
 |t|\le\tfrac12(1-\sqrt{1-2/m^2})\}\quad(m\text{ even}).}
\]
This proves the claimed strict nonuniqueness and completes the classification.

## Verification
Run `python verify.py` with NumPy and SciPy. The standalone script constructs both the signed-edge convex hull and the independent sign-normal families, deduplicates facet normals, checks supporting-plane sharpness, maximizes radius over unrestricted centers by linear programming, and computes the rank of maximum-norm facet normals. For small dimensions it separately enumerates facets from SciPy's Euclidean ConvexHull and checks the full facet-distance multiset. It tests 17 distinct parameter pairs with \(2\le p\le q\), verifies nonzero feasible shifts in every predicted incenter direction, and checks the endpoints and strict sharpness of balanced-even incenter segments for sizes \(2,4,6\). Its reported marker is `BICLIQUE_INBALL_FACETS_CENTERS_CHECKS_PASSED 17`.

The analytical proof establishes the theorem for all integers in the stated domain. Finite numerical checks are corroboration and are not a substitute for that proof.

## Relationship to prior work
Higashitani, Jochemko, and Michałek (arXiv:1807.07678v1, Proposition 3.4) already classify **all facets** of the complete-bipartite symmetric edge polytope. This classification is the essential known combinatorial input, and is not claimed new. Their stated goals concern facet labels, lattice points, and Ehrhart \(h^*\)-polynomials; they do not state the intrinsic Euclidean inradius, contact-facet count, or full incenter-locus phase diagram. The present results are quantitative Euclidean deductions and must not be construed as independent facet discovery.

D'Alì, Delucchi, and Michałek (arXiv:1910.05193v1; 2022 journal publication) connect symmetric edge polytopes, metric Lipschitz polytopes, and adjacency polytopes, and study face and Ehrhart invariants. Their related results do not directly yield the radius and center dimensions given here. A public 2026 note on **star** symmetric-edge polytopes has the analogous parity law for \(K_{1,q}\); it covers the excluded one-vertex color-class case, not genuine bicliques \(p,q\ge2\). The present classification includes a higher-dimensional incenter family of dimension \(p\) for unequal parts and even \(q\), and a balanced-part uniqueness transition, neither of which follows by an isometric reduction to a star.

## Limitations
The formulas require unweighted complete bipartite graphs and their standard signed-incidence Euclidean embedding; unimodular changes of coordinates need not preserve them. The result does not establish inradii for general bipartite graphs or other metric realizations. A prior equivalent observation under Lipschitz-polytope or optimal transport terminology is a residual historical-priority possibility. The relation between known facet enumeration and the new metric deductions should be taken into account when evaluating scope and novelty; independent assessment has not been performed.

## References
1. A. Higashitani, K. Jochemko, and M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678v1, public 2018-07-20; *Mathematika* **65** (2019), 763–784, DOI:10.1112/S0025579319000147. Especially Theorem 3.1 and Proposition 3.4.
2. A. D'Alì, E. Delucchi, and M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193v1, public 2019-10-11; *Electronic Journal of Combinatorics* **29** (2022), P3.24, DOI:10.37236/10387.
3. *Star symmetric-edge polytopes have a parity jump in their full incenter locus*, public research record (2026), specifically the \(K_{1,q}\) result and its incenter segment.
