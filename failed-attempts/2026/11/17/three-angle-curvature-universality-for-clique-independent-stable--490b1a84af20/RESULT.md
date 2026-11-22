# Three-angle curvature universality for clique–independent stable-set polytopes

## Finding
Let integers \(c\ge1\), \(m\ge2\) be given and write \(N=c+m\). The standard Euclidean stable-set polytope of the complete split graph \(G=K_c\vee\overline{K_m}\) is
\[
P_{c,m}=\left\{(x,y)\in\mathbb R^c\times\mathbb R^m:\ x_i\ge0,\ y_j\ge0,\ \sum_{i=1}^c x_i+y_j\le1\text{ for }1\le j\le m\right\}.
\]
It has \(c+2m\) facets and precisely three distinct exterior dihedral angles along its \((N-2)\)-faces:
\[
\frac\pi2,\qquad \alpha_c=\arccos\!\left(-\frac1{\sqrt{c+1}}\right),\qquad
\beta_c=\arccos\!\left(\frac c{c+1}\right).
\]
Their respective total \((N-2)\)-dimensional ridge measures, divided by \(\operatorname{Vol}_N(P_{c,m})N(N-1)\), are
\[
\frac{c^2+c+1}{2}+\sqrt{c+1},\qquad c\sqrt c,\qquad \frac{\sqrt{2c+1}}2.
\]
Thus these three normalized angular masses depend only on \(c\), irrespective of \(m\). Writing \(S(P)\) for ordinary Euclidean surface area and \(V_j(P)\) for intrinsic volumes in the Steiner convention below, we have
\[
\operatorname{Vol}_N(P_{c,m})=\frac{m!}{N!},\qquad
\frac{S(P_{c,m})}{\operatorname{Vol}_N(P_{c,m})}=N\bigl(c+1+\sqrt{c+1}\bigr),
\]
\[
\boxed{\frac{V_{N-2}(P_{c,m})}{\operatorname{Vol}_N(P_{c,m})}
=N(N-1)\left[\frac{c^2+c+1+2\sqrt{c+1}}8
+\frac{c\sqrt c}{2\pi}\alpha_c
+\frac{\sqrt{2c+1}}{4\pi}\beta_c\right].}
\]
The equalities apply to every integer pair in the indicated domain, including \(c=1\) and \(m=2\).

## Assumptions and scope
All coordinate axes are orthonormal in the canonical indicator-vector realization. The graph has a clique of size \(c\), an independent set of size \(m\), and every possible edge across these two parts. The standard stable-set polytope is the convex hull of indicators of independent vertex subsets. The same polytope is Stanley's chain polytope of a poset formed by a \(c\)-element chain placed below an \(m\)-element antichain.

The intrinsic-volume normalization is
\[
\operatorname{Vol}_N(P+t B_N)=\sum_{j=0}^N\kappa_j V_{N-j}(P)t^j,
\qquad \kappa_1=2,\quad\kappa_2=\pi,
\]
where \(B_N\) is the Euclidean unit ball. Consequently \(V_{N-1}(P)=S(P)/2\), and for a polytope of dimension at least three,
\[
V_{N-2}(P)=\frac1{2\pi}\sum_{R}\operatorname{Vol}_{N-2}(R)\,\phi_R,
\]
where \(R\) runs over ridges and \(\phi_R\) is the angle between the two outward unit facet normals at that ridge.

## Proof
**1. The polytope and all its facets.** An independent set is either a subset of the independent class or a singleton clique vertex. Convex combination therefore gives the displayed inequalities exactly: if \(s=\sum x_i<1\), subtract the mass \(x_i\) at clique singleton \(i\), and use the remaining mass \(1-s\) to realize the cube point \(y/(1-s)\). If \(s=1\), then \(y=0\). The irredundant facets are:

- \(A_i:\ x_i=0\) for \(1\le i\le c\);
- \(B_j:\ y_j=0\) for \(1\le j\le m\);
- \(C_j:\ s+y_j=1\) for \(1\le j\le m\).

All are genuine facets by choosing strict values for the other constraints. No further facets occur because these inequalities already cut out the convex hull. Their outward normals are \(-e_i\), \(-f_j\), and \(u+f_j\), respectively, with \(u=\sum_{i=1}^c e_i\).

**2. Every ridge and its intrinsic Euclidean measure.** Two distinct facets meet in a ridge except for the pairs \(B_j,C_j\), whose intersection has dimension \(c-1<N-2\) since \(m\ge2\). In the following table, \(A A\), \(A B\) and so on denote unordered pairs of those facet types, and each displayed relative measure is the measure of ONE ridge divided by \(\operatorname{Vol}_N(P_{c,m})N(N-1)\). The row counts are exact.

| Facet pair | Number of ridges | Relative measure of each ridge | Exterior angle |
|---|---:|---:|---|
| \(AA\) | \(\binom c2\) | \(1\) | \(\pi/2\) |
| \(AB\) | \(cm\) | \(1/m\) | \(\pi/2\) |
| \(AC\) | \(cm\) | \(\sqrt c/m\) | \(\alpha_c\) |
| \(BB\) | \(\binom m2\) | \(1/[m(m-1)]\) | \(\pi/2\) |
| \(BC\), different indices | \(m(m-1)\) | \(\sqrt{c+1}/[m(m-1)]\) | \(\pi/2\) |
| \(CC\) | \(\binom m2\) | \(\sqrt{2c+1}/[m(m-1)]\) | \(\beta_c\) |

Here is a direct verification of every measure. For \(q\ge0\), the Dirichlet simplex integral is
\[
\int_{\substack{x_i\ge0\\s\le1}}(1-s)^q\,dx_1\cdots dx_c=\frac{q!}{(c+q)!}.
\]
On a face with two coordinate-zero constraints, the free leaf variables form an orthogonal box of side \(1-s\); the integral with \(q=m,m-1,m-2\) gives the \(AA,AB,BB\) rows. For \(AC\), substitute \(y_j=1-s\) with \(x_i=0\); the Euclidean Jacobian equals \(\sqrt c\). For \(BC\) with different indices, the analogous Jacobian is \(\sqrt{c+1}\). For \(CC\), substitution \(y_j=y_k=1-s\) has Jacobian \(\sqrt{2c+1}\). The remaining variables are orthogonal cube fibers, so applying the same integral gives the last three entries. The positivity of the free-variable interiors establishes that each listed intersection really has dimension \(N-2\). In particular, there are no missing ridge types.

The outward-normal scalar products give \(0\) for all four right-angle rows, \(-1/\sqrt{c+1}\) for \(AC\), and \(c/(c+1)\) for \(CC\). Since \(c\ge1\), the three exterior angles are distinct, with \(\alpha_c>\pi/2>\beta_c\).

**3. Surface area and second Steiner coefficient.** The same integral gives \(\operatorname{Vol}_N(P_{c,m})=m!/N!\). Each \(A\)-facet has \((N-1)\)-measure \(m!/(N-1)!\); each \(B\)-facet has \((m-1)!/(N-1)!\); and each \(C\)-facet has \(\sqrt{c+1}(m-1)!/(N-1)!\). Summing these \(c+2m\) measures yields the claimed surface-to-volume ratio.

Summing the \(AA,AB,BB,BC\) rows in the ridge table gives the aggregate normalized right-angle ridge measure \((c^2+c+1)/2+\sqrt{c+1}\). Summing \(AC\) gives \(c\sqrt c\), and summing \(CC\) gives \(\sqrt{2c+1}/2\). Inserting these three sums and their corresponding angles into the polyhedral Steiner ridge formula yields the displayed expression for \(V_{N-2}\), proving the theorem.

## Verification
A standalone checker, `check_geometry.py`, independently enumerates every indicator vertex and the proposed bounding hyperplanes, projects each facet and pairwise facet intersection onto its affine span, and computes its intrinsic Euclidean measure using convex-hull volume. It recomputes the exterior-normal angles rather than reading the six-row table. Numerical checks cover \((c,m)=(1,2),(1,3),(2,2),(2,3),(3,2),(2,4),(4,2)\), including all exceptional small dimensions, and verify volume, total surface area, each ridge-type count and the second intrinsic volume. Running it requires NumPy and SciPy (versions described in `requirements.txt`). These finite calculations check the implementation and low-dimensional boundary cases; the unrestricted theorem is proved by the exact integral and normal calculations above.

## Relationship to prior work
Stable-set polytopes and their coordinate realizations are standard. Aliniaeifard, Benedetti, Bergeron, Li, and Saliola (arXiv:1804.00360, first submitted 2018-04-02) discuss their 1-skeleta and cite the facet characterization by maximal cliques for perfect graphs. Hu and Laurent (2019) likewise use that perfect-graph facet presentation. These facts support the object and facet setup, but no Euclidean ridge-area or second-intrinsic-volume formula is derived in the inspected relevant sections. Separate work on isotropic constants and vertex/volume covariances of complete-split stable-set polytopes addresses bulk moment geometry rather than outer-parallel-body curvature. The present contribution is the explicit ridge-angle/measure spectrum and the resulting second Steiner coefficient, not the defining inequalities, ordinary volume integral, or the general Steiner formula.

## Limitations
The theorem requires the canonical unweighted Euclidean coordinate realization and integers \(c\ge1,m\ge2\). It does not claim metric invariance under arbitrary affine transformations or equality of all higher Steiner coefficients. The full historical priority of the explicit curvature formula cannot be guaranteed from indexed-search coverage alone.

## References
1. F. Aliniaeifard, C. Benedetti, N. Bergeron, S. X. Li and F. Saliola, *Stable set polytopes and their 1-skeleta*, arXiv:1804.00360 (first version 2018-04-02). https://arxiv.org/abs/1804.00360
2. H. Hu and M. Laurent, *On the linear extension complexity of stable set polytopes for perfect graphs*, European Journal of Combinatorics **80** (2019), 247–260. https://doi.org/10.1016/j.ejc.2018.02.014
3. R. P. Stanley, *Two poset polytopes*, Discrete & Computational Geometry **1** (1986), 9–23. https://doi.org/10.1007/BF02187680
4. Classical Steiner formula and polyhedral ridge-angle expansion, in the normalization stated under “Assumptions and scope.”
