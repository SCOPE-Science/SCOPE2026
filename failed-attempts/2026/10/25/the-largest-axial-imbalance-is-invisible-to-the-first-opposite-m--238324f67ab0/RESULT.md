# The largest axial imbalance is invisible to the first opposite mixed volume of a cross-polytope

## Finding
Let \(d\ge2\) and let \(K=\operatorname{conv}\{a_i e_i,-b_i e_i:1\le i\le d\}\subset\mathbb R^d\), with \(a_i,b_i>0\). Put \(t_i=\min(a_i,b_i)/\max(a_i,b_i)\), and relabel coordinates so \(0<t_1\le\cdots\le t_d\le1\). Normalize the first opposite-body mixed volume by
\[
R_d(K)=\frac{V(K[d-1],-K)}{\operatorname{vol}_d(K)},\qquad
\operatorname{vol}_d(K+sL)=\operatorname{vol}_d(K)+dsV(K[d-1],L)+O(s^2).
\]
Then, for all such positive arm lengths,
\[
\boxed{R_d(K)=\sum_{j=1}^{d-2}\frac1{\prod_{i=1}^j(1+t_i)}+\frac2{\prod_{i=1}^{d-1}(1+t_i)}}.
\]
The empty sum for \(d=2\) is zero. In particular, this entire mixed-volume ratio is independent of the *largest* normalized arm ratio \(t_d\), although all remaining ratios matter. As a symmetric subfamily, when every \(t_i=t\),
\[
R_d(t)=1+(1-t)\sum_{j=1}^{d-1}(1+t)^{-j}.
\]
For any positive arm ratios, \(1\le R_d(K)<d\), with equality \(R_d(K)=1\) if and only if all \(t_i=1\). The upper value \(d\) is sharp as \(t_1,\dots,t_{d-1}\to0^+\), even if \(t_d\) stays fixed. For fixed sorted parameters, the formula strictly decreases with each \(t_1,\dots,t_{d-1}\) and does not change with \(t_d\), as long as the sorting constraints remain satisfied.

## Assumptions and scope
Here \(V(K[d-1],L)\) is the standard mixed volume, not an unnormalized coefficient of the Minkowski polynomial. The polytope need not have a common length along any axis; each positive and negative arm is independently prescribed. Reflection signs and independent invertible diagonal scalings do not change the normalized ratio, permitting the arm presentation \(K=\operatorname{conv}\{e_i,-t_i e_i\}\). All ratios must be positive; the asserted upper endpoint \(d\) is limiting, not attained in this positive-parameter family.

## Proof
Invertible linear maps scale mixed volumes and volume by the same determinant, so normalize each axis to positive arm length one and negative arm length \(t_i\). In each orthant, \(K\) is the simplex with the origin and one selected axial vertex per coordinate. Summing the \(2^d\) disjoint-interior orthant simplices gives
\[
d!\operatorname{vol}_d(K)=\prod_{i=1}^{d}(1+t_i).
\]
Every facet is indexed by the subset \(S\subseteq\{1,\ldots,d\}\) of its negative axial vertices, and lies in the plane \(u_S\cdot x=1\), where \((u_S)_i=-1/t_i\) for \(i\in S\), and \((u_S)_i=1\) otherwise. Its base-height cone volume is \(\prod_{i\in S}t_i/d!\); equivalently its \((d-1)\)-area divided by \(\|u_S\|\) equals \(\prod_{i\in S}t_i/(d-1)!\).

The facet measure formula \(dV(K[d-1],L)=\sum_F\operatorname{area}_{d-1}(F)h_L(\nu_F)\), with unit outer normals \(\nu_F\), yields
\[
d!V(K[d-1],-K)=\sum_{S\subseteq[d]}\Bigl(\prod_{i\in S}t_i\Bigr)h_{-K}(u_S).
\]
Since \(t_i\le1\), for nonempty \(S\) the support is \(h_{-K}(u_S)=\max_{i\in S}t_i^{-1}\); for \(S=\varnothing\), it is \(\max_i t_i=t_d\). Sort the \(t_i\) ascending. Partition nonempty subsets by their least index \(j\); ties cause no problem because any tied value gives the same support. Their weighted contribution is \(\prod_{k=j+1}^d(1+t_k)\). Therefore
\[
d!V(K[d-1],-K)=t_d+\sum_{j=1}^d\prod_{k=j+1}^d(1+t_k).
\]
The term for \(j=d\) is one; combine it with \(t_d\), and cancel the common factor \(1+t_d\). Dividing by the preceding volume formula gives exactly the displayed sum of reciprocal prefix products. All coefficients in this expression are positive; monotonicity and independence follow immediately. At \(t_i=1\) its value is one, and if any parameter is smaller than one, the first deficient ratio among the smallest \(d-1\) strictly increases the expression (unless only \(t_d<1\), which is impossible by sorting). The limit \(d\) follows by letting the first \(d-1\) parameters approach zero. For equal parameters, sum the geometric series, yielding the stated one-parameter identity. QED.

## Verification
The included standalone Python standard-library program `verify.py` tests the facet-support sum against the closed form using exact fractions across 7,001 parameter vectors in dimensions two through six, checks exact sharp inequalities, and independently checks the planar formula against convex-hull Minkowski addition and the shoelace area formula for 3,025 integer-ratio pairs. Run it with `python verify.py`. Its finite tests support the algebra but the preceding facet proof establishes all dimensions and positive real parameters.

## Relationship to prior work
The October 2026 resolution of the higher-order Godbersen inequality establishes the universal upper bound and rigid simplicial equality, rather than an explicit sorted-arm formula for this asymmetric cross-polytope family [1]. Earlier work establishes Godbersen inequalities for locally anti-blocking bodies, which include this family and supply important surrounding methods [2,3]. The formula above instead computes the actual first mixed volume and exposes the independence of one entire arm-ratio parameter. A prior equivalent specialization may exist in the aligned-simplex literature; that priority question is not settled by the accessible primary abstracts.

## Limitations
This evaluates \(V(K[d-1],-K)\) only. It does not calculate the full \(d+1\)-term opposite-body mixed-volume profile, imply a new universal Godbersen bound, or resolve historical priority relative to inaccessible full texts. The ratio invisibility applies only within the stated axis-arm family and to the largest ratio after sorting.

## References
[1] F. Fryš, J. Kotrbatý, M. A. Mouamine, S. Wang, *Higher-order Godbersen inequality and a characterization of simplices via the face lattice*, arXiv:2610.06806 (first public 2026-10-05).

[2] S. Artstein-Avidan, S. Sadovsky, R. Sanyal, *Geometric inequalities for anti-blocking bodies*, arXiv:2008.10394 (2020), *Communications in Contemporary Mathematics* 25 (2023), 2150113.

[3] S. Sadovsky, *Godbersen's conjecture for locally anti-blocking bodies*, arXiv:2312.03473 (2023), *Advances in Geometry* 25 (2025), 307–315.
