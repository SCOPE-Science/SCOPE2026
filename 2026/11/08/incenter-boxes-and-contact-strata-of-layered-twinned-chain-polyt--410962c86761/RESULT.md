# Incenter boxes and contact strata of layered twinned chain polytopes

## Finding

Let \(P=A_{m_1}\oplus\cdots\oplus A_{m_k}\) be an ordinal sum of \(k\ge1\) nonempty antichains, with integers \(m_i\ge1\). Let \(d=\sum_i m_i\), and let \(C(P)\subset\mathbb R^d\) be Stanley's chain polytope in canonical indicator coordinates. Define the centrally symmetric twinned chain polytope
\[
K_P=\operatorname{conv}\bigl(C(P)\cup(-C(P))\bigr).
\]
Write \(S=\{i:m_i=1\}\), \(W=\{i:m_i\ge2\}\), \(s=|S|\), \(w=|W|\), and \(H=s+2w\). Then the maximum radius of a Euclidean ball contained in \(K_P\), in the displayed ambient Euclidean metric, is
\[
\rho(K_P)=H^{-1/2}.
\]
If \(w=0\), the origin is the unique incenter. If \(w\ge1\), set
\[
\tau_H=1-\sqrt{1-H^{-1}}.
\]
**Every** center of a ball of radius \(\rho(K_P)\) in \(K_P\) has coordinates
\[
c_{ij}=\begin{cases}0&i\in S,\\t_i&i\in W,\end{cases}
\qquad -\tau_H\le t_i\le\tau_H\quad(i\in W).
\]
Conversely, every such point is an optimal center. Thus the incenter locus is an orthogonal box of affine dimension \(w\), whose Euclidean edge lengths are \(2\tau_H\sqrt{m_i}\) for \(i\in W\). In particular, the inradius and the coordinate half-width are independent of the actual values of \(m_i\) once each size is classified as one or at least two.

The number of distinct facets tangent to the centered maximal ball is
\[
F_0=2^s\prod_{i\in W}m_i(m_i-1).
\]
For a general optimal center \(c\), let \(B(c)=\{i\in W:|t_i|=\tau_H\}\). The number of facets tangent to its maximal ball is exactly
\[
F(c)=F_0+2^s\sum_{i\in B(c)}m_i
\prod_{j\in W\setminus\{i\}}m_j(m_j-1).
\]
Hence the relative interior of the incenter box has precisely \(F_0\) contacts; a boundary point has additional contacts indexed by its active box coordinates. Empty products equal one.

## Assumptions and scope

The chain polytope is \(C(P)=\operatorname{conv}\{\mathbf1_A:A\text{ is an antichain of }P\}\). All comparisons, ball radii, normals, and center dimensions use the ordinary Euclidean inner product on \(\mathbb R^d\), not a lattice-equivalent but metrically different realization. The result covers positive integer layer sizes and all \(k\ge1\), including the all-singleton case and the one-layer case. It concerns only the symmetric pair \(C(P),C(P)\), not arbitrary distinct twinned posets.

## Proof

**Step 1: the exact polar decomposition.** All antichains of \(P\) are subsets of a single layer, and each subset of each layer is an antichain. Because \(K_P\) is the convex hull of the signed antichain indicators, its polar is a Cartesian product
\[
K_P^\circ=Q_{m_1}\times\cdots\times Q_{m_k},\qquad
Q_m=\left\{z\in\mathbb R^m:
\sum_{j:z_j>0}z_j\le1,\ \sum_{j:z_j<0}(-z_j)\le1\right\}.
\]
Equivalently, \(Q_m\) is defined by \(-1\le\sum_{j\in A}z_j\le1\) for every subset \(A\subseteq[m]\). On any coordinate orthant it is the Cartesian product of a positive and a negative simplex. Its **entire vertex set** is \(\{\pm e_j:1\le j\le m\}\cup\{e_i-e_j:i\ne j\}\) if \(m\ge2\), and \(\{-1,1\}\) if \(m=1\). Indeed, the simplex decomposition shows every possible global vertex is in this list; each listed point is itself a global vertex, as witnessed by the tight subset-sum inequalities fixing all coordinates. In particular, vertex squared norms are one or two, and the squared norm of a farthest vertex of \(Q_m\) is one for \(m=1\), and two for \(m\ge2\).

**Step 2: the optimal radius and the farthest facet normals.** As \(K_P\) is centrally symmetric, any ball \(B(c,r)\subseteq K_P\) has its reflected ball \(B(-c,r)\subseteq K_P\); convexity then gives \(B(0,r)\subseteq K_P\). The largest centered ball is determined by \(v\cdot x\le1\) for vertices \(v\) of \(K_P^\circ\). Hence its radius is \(\rho=1/\max\|v\|_2=1/\sqrt H\). A vertex with norm \(\sqrt H\) selects \(\pm1\) in every singleton layer and \(e_a-e_b\), \(a\ne b\), in every wide layer. Since polar vertices correspond one-to-one to facets of \(K_P\), the count of these farthest facets is \(F_0\).

**Step 3: all possible optimal centers.** For any farthest polar vertex \(v\), the two opposite inequalities \(v\cdot c+\rho\|v\|\le1\) and \(-v\cdot c+\rho\|v\|\le1\) force \(v\cdot c=0\). Differences of farthest vertices differing in one singleton sign force the corresponding center coordinate to vanish. Differences of farthest vertices obtained by changing an ordered pair \((a,b)\) in a wide layer force all center coordinates in that layer to be equal. (For a two-element layer, the two vectors \(e_a-e_b\) and \(e_b-e_a\) already force equality.) Conversely, blockwise-constant centers with zeros in singleton layers annihilate all farthest vertices.

**Step 4: the sharp box constraints.** Write such a center using \(t_i\) for \(i\in W\). A polar vertex may select a unit vector \(\pm e_j\) instead of a difference vector in a subset \(J\subseteq W\) of the wide layers. Its squared norm is \(H-|J|\), and the maximum dot product over sign choices is \(\sum_{i\in J}|t_i|\). Thus this center is feasible for the ball of radius \(H^{-1/2}\) if and only if
\[
\sum_{i\in J}|t_i|\le f(|J|),\qquad
f(j)=1-\sqrt{1-j/H}\quad(J\subseteq W).
\]
The singleton-set inequalities are exactly \(|t_i|\le\tau_H=f(1)\). Conversely, \(f\) is strictly convex on \([0,w]\) with \(f(0)=0\); therefore \(f(j)\ge j f(1)\), strictly for \(j\ge2\). The singleton bounds consequently imply every remaining inequality. This proves precisely the displayed incenter box, including its Euclidean side lengths and affine dimension.

**Step 5: all tangent facets at every optimal center.** At any such center the polar vertices using only difference vectors in the wide layers have \(v\cdot c+\rho\|v\|=1\), yielding \(F_0\) contacts. A vertex using unit vectors in precisely one wide layer \(i\) is tangent exactly when \(|t_i|=\tau_H\), and the sign of its single nonzero coordinate agrees with the sign of \(t_i\). There are \(m_i\) such unit choices. Vertices using units in two or more wide layers cannot be tangent, because \(f(j)>j f(1)\) for \(j\ge2\). Multiplying the independent choices in all other layers gives exactly the stated contact-count formula.

## Verification

The accompanying `verification.py` enumerates all vertices of the polar factors, checks maximum squared norm, computes the exact rational rank of all farthest facet normals, and verifies every incenter-box corner and its tangent-facet count at 62-digit decimal precision. It uses only the Python standard library. An additional independent numerical linear-program calculation directly maximized the Euclidean Chebyshev radius for thirteen small profiles and agreed with the formula. These finite calculations do not prove the general theorem; Steps 1–5 do.

Reproduce the finite enumerations with `python verification.py`. No data files or external downloads are required.

## Relationship to prior work

Tsuchiya's 2015 preprint (published in 2018) introduced the relevant twinned-chain-polytope framework and already gives its complete facet and dual-vertex descriptions. The **central-radius formula** is a direct metric consequence of those established descriptions and is not asserted here as an independent priority claim. Freij-Hollanti and Lundström (first posted December 21, 2023) study ordinal sums of posets and chain polytopes through their face vectors, rather than their incenter loci. The new claim assessed here is the **full optimal-center box with exact edge lengths and contact-stratified facet count for all layered symmetric twinned chain polytopes**. Other published results on enriched or signed chain polytopes concern different constructions; an equivalent geometric analysis under anti-blocking or norm-optimization terminology remains possible.

## Limitations

This is a classification for the canonical Euclidean embedding of symmetric twinned chain polytopes from ordinal sums of antichains. It makes no claim for arbitrary signed pairs of posets, non-Euclidean norms, or general metric realizations. The original facet classification is prior work; no priority is claimed for rederiving it. The historical-priority comparison is necessarily provisional. The finite program is corroboration and not an infinite certificate.

## References

1. R. P. Stanley, *Two poset polytopes*, Discrete & Computational Geometry 1 (1986), 9–23. DOI: 10.1007/BF02187680.
2. A. Tsuchiya, *Volume, facets and dual polytopes of twinned chain polytopes*, arXiv:1512.08332 (first posted December 28, 2015), especially Theorem 2.2 and Corollary 2.4. https://arxiv.org/abs/1512.08332
3. R. Freij-Hollanti and T. Lundström, *f-vector inequalities for order and chain polytopes*, arXiv:2312.13890 (first posted December 21, 2023), especially Section 4 on ordinal sums. https://arxiv.org/abs/2312.13890
4. A. Mori, K. Mori and H. Ohsugi, *Facet numbers of non-centrally symmetric reflexive polytopes arising from posets*, arXiv:2511.22981 (2025), an independent recent facet-count study. https://arxiv.org/abs/2511.22981
