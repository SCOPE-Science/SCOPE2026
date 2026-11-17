# A sharp isoperimetric sign transition after deleting one edge of a complete bipartite root polytope

## Finding
Let \(\Delta_{r-1}=\operatorname{conv}(e_1,\ldots,e_r)\), and let \(P^0_{p,q}=\Delta_{p-1}\times\Delta_{q-1}\) with its intrinsic Euclidean product metric. Delete the corner \((e_p,f_q)\) and take the convex hull of the remaining vertices, denoted \(P_{p,q}\). In graph terminology this is the (sign-reversed but Euclidean-isometric) root polytope of the complete bipartite graph with a single missing edge.

**Theorem (exact area, volume, and the sharp sign transition).** For integers \(2\le p\le q\), put
\[
\begin{gathered}
d=p+q-2,\quad a=\sqrt{\frac{p-1}{p}},\quad b=\sqrt{\frac{q-1}{q}},\quad c=\sqrt{a^2+b^2},\\
A=(p-1)a,\quad B=(q-1)b,\quad H=pA+qB,\quad F=A+B-c,\\
\varepsilon=\binom{d}{p-1}^{-1},\qquad z=\frac{dF}{H}.
\end{gathered}
\]
The intrinsic Euclidean volume \(V\), boundary area \(S\), and scale-invariant isoperimetric quotient \(Q=S/V^{(d-1)/d}\) satisfy
\[
\begin{aligned}
V(P^0_{p,q})&=\frac{\sqrt{pq}}{(p-1)!(q-1)!},& S(P^0_{p,q})&=V(P^0_{p,q})H,\\
V(P_{p,q})&=V(P^0_{p,q})(1-\varepsilon),& S(P_{p,q})&=S(P^0_{p,q})(1-z\varepsilon),\\
\frac{Q(P_{p,q})}{Q(P^0_{p,q})}&=\frac{1-z\varepsilon}{(1-\varepsilon)^{(d-1)/d}}.
\end{aligned}
\]
**Four exceptional unordered size pairs.** More precisely,
\[
\boxed{\quad Q(P_{p,q})>Q(P^0_{p,q})\ \Longleftrightarrow\ p=2\ \text{and}\ 2\le q\le5.\quad}
\]
For every other pair \(2\le p\le q\), the strict inequality reverses. In particular one missing graph edge can either improve or worsen the Euclidean isoperimetric quotient, and no equality occurs. The phrase "four exceptional size pairs" counts \((2,2),(2,3),(2,4),(2,5)\), not symmetry-ordered alternatives.

For balanced parameters \(p=q=m\to\infty\),
\[
1-\frac{Q(P_{m,m})}{Q(P^0_{m,m})}\sim\binom{2m-2}{m-1}^{-1}\sim\frac{\sqrt{\pi(m-1)}}{4^{m-1}}.
\]
For fixed \(p\ge2\), as \(q\to\infty\),
\[
1-\frac{Q(P_{p,q})}{Q(P^0_{p,q})}\sim (p-1)!\biggl[(p-1)+(p-1)\sqrt{\frac{p-1}{p}}-\sqrt{2-\frac1p}\biggr]q^{-p}.
\]

## Assumptions and scope
The intrinsic affine span is defined by the two coordinate-sum-one equations; its dimension is \(d=p+q-2\). All areas are \((d-1)\)-dimensional Euclidean Hausdorff measures of the boundary, with ordinary Euclidean lengths and no lattice normalization. The standard simplex vertices have unit coordinate length in their separate factors. The result excludes a singleton factor: both \(p,q\ge2\). Symmetry allows \(p\le q\). Strict signs are over exact reals, not rounded numerical approximations.

## Proof
**1. An exact one-corner cut.** Since edges of a product of simplices incident to \((e_p,f_q)\) terminate at \((e_i,f_q)\) or \((e_p,f_j)\), the supporting hyperplane \(x_p+y_q=1\) contains all these neighbors and separates only the deleted vertex. Thus
\[
P_{p,q}=P^0_{p,q}\cap\{x_p+y_q\le1\}.
\]
The removed region is the closed \(d\)-simplex whose apex is \((e_p,f_q)\) and whose other vertices are those \(d\) neighbors. Their difference vectors have mutually orthogonal \(p-1\) and \(q-1\) blocks, with Gram matrices \(I_{p-1}+J_{p-1}\) and \(I_{q-1}+J_{q-1}\). The determinants are \(p\) and \(q\), hence the removed simplex has Euclidean volume \(\sqrt{pq}/d!\). The full product has volume \(\sqrt{pq}/((p-1)!(q-1)!)\). Their ratio is \(\varepsilon\).

**2. Surface area, including boundary-sized factors.** Every facet of the full product from an \(x_i=0\) equation has area \(\sqrt{(p-1)q}/((p-2)!(q-1)!)\), and there are \(p\) of them; the \(q\) other facets analogously have area \(\sqrt{p(q-1)}/((p-1)!(q-2)!)\). Summing gives \(S(P^0)=V(P^0)H\). Only \(p-1\) of the \(x\)-facets and \(q-1\) of the \(y\)-facets meet the removed vertex. Each loses an \((d-1)\)-simplex, of area respectively \(\sqrt{(p-1)q}/(d-1)!\) and \(\sqrt{p(q-1)}/(d-1)!\). The new facet is the base of the removed simplex, normal to the intrinsic gradient of \(x_p+y_q\), which has squared norm \((p-1)/p+(q-1)/q=c^2\). Its height from the apex is \(1/c\), so its \((d-1)\)-area is \(d\,(\sqrt{pq}/d!)c=\sqrt{pq}c/(d-1)!\). Hence
\[
S(P^0)-S(P)=\frac{\sqrt{pq}}{(d-1)!}\bigl((p-1)a+(q-1)b-c\bigr)=\frac{\sqrt{pq}}{(d-1)!}F,
\]
which is the asserted surface formula. The same derivation works when \(p=2\) or \(q=2\), including any original facet that disappears completely after clipping.

**3. Reduce the sign to a scalar inequality.** Set \(t=(d-1)/d\) and \(T=(1-(1-\varepsilon)^t)/\varepsilon\). As the factors are positive, the quotient is larger than one exactly when \(z<T\). Strict concavity of \((1-u)^t\) gives \(T>t\); also \(T<1\), because \((1-\varepsilon)^t>1-\varepsilon\). In particular, \(z\ge1\) implies strict improvement.

**4. All pairs with \(p\ge4\), and \(p=3,q\ge5\).** The inequality \(z\ge1\) is equivalent to \((q-2)A+(p-2)B\ge dc\). Since \(p\le q\), \(b\ge a\), and \(c\le\sqrt2 b\), while \(A\ge(p-1)ab\). Thus the left side minus the right is at least \(b L(p,q)\) with
\[
L(p,q)=(q-2)(p-1)a+(p-2)(q-1)-(p+q-2)\sqrt2.
\]
This expression grows strictly with \(q\), since its slope is \((p-1)a+p-2-\sqrt2>0\) for \(p\ge3\). For \(p\ge4\), at \(q=p\) it equals \((p-1)[(p-2)(1+a)-2\sqrt2]>0\). For \(p=3\), at \(q=5\) it equals \(6\sqrt{2/3}+4-6\sqrt2>0\). This proves \(z>1>T\) in those parameter ranges.

**5. Remaining infinite case \(p=2,q\ge7\).** Here \(d=q\), \(\varepsilon=1/q\), \(a=1/\sqrt2\), \(b=\sqrt{1-1/q}\), \(c=\sqrt{a^2+b^2}\), \(A=a\), \(B=(q-1)b\). Direct rearrangement gives
\[
H(z-t)=(q-2+2/q)a-b-q(c-b)=:N_q.
\]
Because \(c-b=1/[2(c+b)]\) decreases with \(q\), and at \(q=7\) one has \(c+b>25/12\), for all \(q\ge7\) we have \(c-b<6/25\). Using \(a>7/10\) and \(b<1\),
\[
N_q>\frac{23}{50}q-\frac{12}{5}+\frac{7}{5q}>1 \qquad(q\ge7).
\]
Also \(H=\sqrt2+q(q-1)b<q^2\), so \(z-t>q^{-2}=\varepsilon^2\). Taylor's formula with \(t=1-\varepsilon\) yields
\[
0<T-t\le\frac{\varepsilon^2}{2(1-\varepsilon)^\varepsilon}\le\varepsilon^2,
\]
using \((1-\varepsilon)^\varepsilon\ge1/2\) for \(0<\varepsilon\le1/2\). Therefore \(z>T\), giving strict improvement.

**6. The seven finite boundary cases.** Only \((2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4)\) remain. Their strict signs are certified by the standalone checker `checks/check_one_missing_edge.py`, which encloses all required square roots in rational intervals of width \(10^{-12}\), then proves the strict sign of
\[
(1-z\varepsilon)^d-(1-\varepsilon)^{d-1}
\]
with exact fraction arithmetic and outward interval propagation. The signs are positive in the first four pairs (worsening) and negative in the final three (improving). The enclosures are sufficiently narrow to exclude zero, and the script asserts and reproduces this fact. This closes the classification without reliance on a floating-point sign.

**7. Limiting regimes.** When \(p=q=m\), direct substitution gives \(z=2-(2+\sqrt2)/m\), \(t=(2m-3)/(2m-2)\), and \(\varepsilon=\binom{2m-2}{m-1}^{-1}\). Hence \(z-t\to1\), and the first-order expansion of the quotient gives the balanced asymptotic. At fixed \(p\) and \(q\to\infty\), write \(a=\sqrt{(p-1)/p}\) and expand \(z-t\) to first order:
\[
q(z-t)\longrightarrow (p-1)+(p-1)a-\sqrt{2-1/p}.
\]
Since \(\varepsilon\sim(p-1)!q^{-(p-1)}\), the exact identity \(Q(P)/Q(P^0)=(1-\varepsilon)^{1/d}[1-(z-1)\varepsilon/(1-\varepsilon)]\) gives the claimed fixed-part coefficient, including at \(p=2\): both the \((z-1)\varepsilon\) term and the \(\varepsilon/d\) term contribute, and the remaining errors are lower-order. The coefficient is positive for \(p\ge2\).

## Verification
The standalone Python 3 program `checks/check_one_missing_edge.py` uses NumPy/SciPy to construct the ambient vertices, orthonormally project to the affine difference space, and compare intrinsic `ConvexHull.volume` and `ConvexHull.area` with the independent formulas for 11 pairs, including all seven exceptional or boundary cases. It additionally performs exact rational interval enclosure of the seven nontrivial quotient-sign comparisons; output includes `ONE_DEFECT_ROOT_SURFACE_PASS cases=11` and `RATIONAL_BOUNDARY_PASS cases=7`. The numerical convex-hull calculations are independent finite-dimensional corroboration, whereas the general claims rely on the preceding symbolic proof. The script requires a working SciPy `ConvexHull` implementation and is not a formal proof assistant.

## Relationship to prior work
Almousa, Dochtermann, and Smith [1] study graph-root subpolytopes of products of simplices, their regular subdivisions, tropical types, and toric edge ideals. Their graph construction includes the present family, but their inspected article does not give a Euclidean boundary-area formula or classify the sign of its isoperimetric response to a missing graph edge. Korotov and Vatne [2] study dihedral-angle sums and facet counts of untruncated product polytopes, not the scale-invariant surface-area comparison after a corner is removed. Previously documented exact volume and rare width loss for the *crown graph* (a product with every diagonal edge deleted) concern a different deletion pattern and do not determine the current sharp one-edge quotient classification [3]. Standard elementary simplex-volume and Taylor formulas used above are not claimed as new. The contribution is the complete sign threshold, exact intrinsic metric profile, and two distinct asymptotic scales.

## Limitations
The shape, metric, and deletion are fixed: this is a single-edge deletion from a complete bipartite root polytope in its standard Euclidean realization, with both part sizes at least two. The result makes no claim about multiple deleted edges, nonsymmetric embeddings, or arbitrary bipartite graphs. The one-corner area formula follows classical geometry; the main nonroutine feature is its global strict comparison and four-exception classification. Bibliographic searches cannot exclude unindexed equivalent descriptions under product-polytope or elementary geometric terminology. Independent mathematical validation has not been performed.

## References
[1] A. Almousa, A. Dochtermann, B. Smith, *Root polytopes, tropical types, and toric edge ideals*, arXiv:2209.09851 (first public submission 2022-09-20), https://arxiv.org/abs/2209.09851; full text https://arxiv.org/html/2209.09851v3.

[2] S. Korotov, J. E. Vatne, *On dihedral angle sums and number of facets for product polytopes*, *Journal of Geometry* 115 (2024), article 34, https://doi.org/10.1007/s00022-024-00732-7 (published 2024-09-14).

[3] *Rare exponential directional loss despite constant Hausdorff distance in crown-graph root polytopes*, https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-rare-exponential-directional-loss-despite-constant-hausdorff-dis--771379f5fcb8/RESULT.md (related geometric result; different deletion pattern).
