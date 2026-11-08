# Strictly negative rim-leaf correlations in wheel spanning trees, with a distance-two maximum

## Finding

Let \(W_{m+1}=K_1\vee C_m\) be the unweighted wheel with hub \(h\) and \(m\ge3\) labeled rim vertices \(v_0,\ldots,v_{m-1}\). Choose uniformly from its spanning trees, and write \(I_i=\mathbf 1\{\deg_T(v_i)=1\}\). For distinct rim vertices at cyclic distance \(d=\min\{|i-j|,m-|i-j|\}\), \(1\le d\le\lfloor m/2\rfloor\), set \(K_m(d)=\operatorname{Cov}(I_i,I_j)\).

Write \(F_0=0,F_1=1,F_{k+2}=F_{k+1}+F_k\) and \(L_0=2,L_1=1,L_{k+2}=L_{k+1}+L_k\), and set \(Z_m=L_{2m}-2\). The exact one- and two-point probabilities are
\[
\Pr(I_i=1)=\frac{3F_{2m-2}}{Z_m},\qquad
\Pr(I_i=I_j=1)=\begin{cases}
\dfrac{4F_{2m-4}}{Z_m},&d=1,\\[4pt]
\dfrac{9F_{2d-2}F_{2m-2d-2}}{Z_m},&2\le d\le\lfloor m/2\rfloor.
\end{cases}
\]
Consequently \(K_m(d)<0\) for every permitted \(m,d\). More sharply, for every \(m\ge4\),
\[
K_m(2)<K_m(1)<0,
\]
and, for \(2\le d<\lfloor m/2\rfloor\),
\[
K_m(d)<K_m(d+1)<0.
\]
Thus *distance two*, not adjacency, gives the strongest negative rim-leaf correlation. With \(t=(3-\sqrt5)/2\), for each fixed \(d\) as \(m\to\infty\),
\[
\lim_{m\to\infty}K_m(1)=-\frac{t^2(9-4\sqrt5)}5,
\qquad
\lim_{m\to\infty}K_m(d)=-\frac{9t^{2d}}5\quad(d\ge2).
\]
In particular, negative correlations at fixed distances at least two have an exactly geometric limiting profile.

## Assumptions and scope

The wheel is simple, connected, unweighted, and has at least three rim vertices. All spanning trees have equal probability. The random variables refer to *degree-one vertices of the selected tree*, not occupied edges or leaves of a random rooted forest. Cyclic distance is taken along the rim, and only distinct rim vertices are considered. Fibonacci and Lucas indices are nonnegative integers as defined above. The limiting assertions take \(m\to\infty\) with \(d\) fixed, not with distance proportional to \(m\).

## Proof

**1. Leaf-grafting identities.** For a connected simple graph \(G\) and vertex \(v\) with \(G-v\) connected, every spanning tree in which \(v\) is a leaf is uniquely obtained by taking a spanning tree of \(G-v\) and adding one of the \(\deg_G(v)\) edges incident to \(v\). Therefore the number of such trees is \(\deg_G(v)\tau(G-v)\), where \(\tau\) is the spanning-tree count. For distinct vertices \(v,w\) with \(G-\{v,w\}\) connected, the corresponding simultaneous-leaf count is \(\deg_G(v)\deg_G(w)\tau(G-\{v,w\})\) if \(v,w\) are nonadjacent. If they are adjacent, the edge \(vw\) cannot be used when both are leaves, because it would isolate the two-vertex component. Hence the simultaneous-leaf count becomes \((\deg_G(v)-1)(\deg_G(w)-1)\tau(G-\{v,w\})\). These are bijective counts, with no independence assumptions.

**2. Deleted-wheel spanning-tree counts.** For the fan consisting of a hub adjacent to every vertex of a path of length \(k-1\), the matrix-tree cofactor is tridiagonal, with determinant \(F_{2k}\). For \(k=1,2\) the values are \(1,3\), and expansion gives the recursion \(D_k=3D_{k-1}-D_{k-2}\), also obeyed by \(F_{2k}\); this proves the formula for all \(k\ge1\). For a wheel, deleting the hub yields the cofactor \(3I-A(C_m)\), whose circulant eigenvalues give
\[
\tau(W_{m+1})=\prod_{j=0}^{m-1}\bigl(3-2\cos(2\pi j/m)\bigr)=L_{2m}-2=Z_m.
\]
To see the final equality directly, each factor equals \(t^{-1}(1-te^{2\pi i j/m})(1-te^{-2\pi i j/m})\), where \(t+t^{-1}=3\); multiplying the roots-of-unity factors gives \(t^{-m}(1-t^m)^2=t^{-m}+t^m-2=L_{2m}-2\).
Deleting one rim vertex leaves a fan on \(m-1\) path vertices, with \(F_{2m-2}\) spanning trees. Deleting two adjacent rim vertices leaves a fan on \(m-2\) path vertices, with \(F_{2m-4}\) spanning trees. Deleting two nonadjacent rim vertices at distance \(d\ge2\) leaves two fans meeting only at the hub, whose path orders are \(d-1\) and \(m-d-1\). The spanning-tree number is their product \(F_{2d-2}F_{2m-2d-2}\). Every rim vertex has degree three, so the preceding leaf-grafting identities prove the displayed probabilities exactly, including the triangle-rim boundary \(m=3\).

**3. Strict negative sign at every separation.** Put \(t=(3-\sqrt5)/2\in(0,1)\). Binet's formulas yield
\[
F_{2k}=\frac{t^{-k}-t^k}{\sqrt5},\quad Z_m=t^{-m}(1-t^m)^2,\quad
p_m:=\Pr(I_i=1)=\frac{3t}{\sqrt5}\frac{1-t^{2m-2}}{(1-t^m)^2}.
\]
For adjacent vertices the ratio of the joint probability \(q_m(1)\) to \(p_m^2\) equals
\[
\frac{q_m(1)}{p_m^2}=\frac{4\sqrt5}{9}
\frac{(1-t^{2m-4})(1-t^m)^2}{(1-t^{2m-2})^2}<1.
\]
Indeed, \(4\sqrt5/9<1\), \(1-t^{2m-4}<1-t^{2m-2}\), and \((1-t^m)^2<1-t^{2m-2}\) for all \(m\ge3\). Thus \(K_m(1)<0\).

For \(d\ge2\), set \(x=t^{d-1}\), \(y=t^{m-d-1}\), \(z=xy=t^{m-2}\). The ratio of joint probability \(q_m(d)\) to \(p_m^2\) is
\[
\frac{q_m(d)}{p_m^2}
=\frac{(1-x^2)(1-y^2)(1-t^m)^2}{(1-t^{2m-2})^2}.
\]
The elementary identity \((1-xy)^2-(1-x^2)(1-y^2)=(x-y)^2\ge0\) gives \((1-x^2)(1-y^2)\le(1-z)^2\). Since \(t^m=t^2z\), \(0<z<1\), one has \((1-z)(1-t^2z)<1-t^2z^2=1-t^{2m-2}\). It follows strictly that \(q_m(d)<p_m^2\), and hence \(K_m(d)<0\).

**4. Distance-two extremality and ordering.** The numerators of the adjacent and distance-two joint probabilities satisfy
\[
4F_{2m-4}>9F_{2m-6}\qquad(m\ge4),
\]
because for \(k=m-3\ge1\), \(F_{2k+2}/F_{2k}=t^{-1}(1-t^{2k+2})/(1-t^{2k})>t^{-1}=(3+\sqrt5)/2>9/4\). Thus \(q_m(2)<q_m(1)\), and subtraction of the common \(p_m^2\) proves \(K_m(2)<K_m(1)\).

For \(2\le d\le\lfloor m/2\rfloor\), the product numerator obeys
\[
5F_{2d-2}F_{2m-2d-2}=t^{-(m-2)}+t^{m-2}-t^{-(m-2d)}-t^{m-2d}.
\]
The function \(a\mapsto t^{-a}+t^a\) is strictly increasing for \(a\ge0\); hence this product strictly increases as \(d\) increases toward \(\lfloor m/2\rfloor\). The subtraction of \(p_m^2\) again preserves the ordering. Every pair of possible distances is covered by these comparisons.

**5. Infinite-wheel limit.** With \(d\) fixed, \(t^m\to0\), so \(p_m\to3t/\sqrt5\). For \(d=1\), \(q_m(1)\to4t^2/\sqrt5\), giving \(-t^2(9-4\sqrt5)/5\). For each \(d\ge2\), \(q_m(d)\to(9t^2/5)(1-t^{2d-2})\), giving \(-9t^{2d}/5\). This proves all limits.

## Verification

The accompanying `check_wheel_leaves.py` is standalone Python using integer arithmetic and `fractions.Fraction`. It independently enumerates all edge subsets of the appropriate size and all acyclic spanning trees for \(m=3,4,5,6,7,8\), counts rim-leaf events at every distinct distance, and compares them with the closed formulas. It additionally checks every claimed sign and ordering in integer arithmetic for \(3\le m\le100\). An extracted copy of the embedded checker completed **2,718 assertions**. Enumeration on these finite ranges supports the analysis but does not substitute for the all-size proof in the preceding section. To reproduce, run `python3 check_wheel_leaves.py`.

## Relationship to prior work

Classical identities for the number of spanning trees of fans and wheels are explicitly reported in C. Merino, *The Number of Quasi-Trees in Fans and Wheels* (2023), Theorem 1; these identities are used, not claimed as new. Miezaki and Tamura (2025) count conditioned two-component forests on wheels, including specified vertex separation, but these events differ from simultaneous degree-one events in a uniformly sampled spanning tree. Tamura and Tanaka (2026) study rooted-forest counts and root configurations, not the present leaf-covariance sign profile. General uniform-spanning-tree edge negative association does not entail negative association of nonmonotone leaf indicators. The claimed contribution is precisely the two-point degree-one distribution and its strict, distance-two-extremal correlation law, rather than the underlying classical counting formulas.

## Limitations

The theorem does not extend by its proof to arbitrary graphs, weighted wheels, the hub leaf indicator, or simultaneous events involving more than two rim vertices. No convergence rate uniform in the separation \(d\) is claimed. The historical comparison is limited to the primary sources and records specified below; related unpublished derivations may exist.

## References

1. Criel Merino, *The Number of Quasi-Trees in Fans and Wheels*, Electronic Journal of Combinatorics **30** (2023), #P1.46, published 2023-03-10. https://doi.org/10.37236/11097
2. Tsuyoshi Miezaki and Shunya Tamura, *Fibonacci and Lucas numbers arising from two-component spanning forests of wheel graphs*, arXiv:2512.18214 (first posted 2025-12-20). https://arxiv.org/abs/2512.18214
3. Shunya Tamura and Yuuho Tanaka, *Rooted spanning forests in wheel graphs: Fibonacci-Lucas formulas and extremal root configurations*, arXiv:2609.29486 (first posted 2026-09-04). https://arxiv.org/abs/2609.29486
4. David J. Aldous, *The Random Walk Construction of Uniform Spanning Trees and Uniform Labelled Trees*, SIAM J. Discrete Math. **3** (1990), 450–465. https://doi.org/10.1137/0403039
5. Geoffrey R. Grimmett and Stephan N. Winkler, *Negative association in uniform forests and connected graphs*, arXiv:math/0302185 (2003). https://arxiv.org/abs/math/0302185
