# Surface-area condensation and a Poisson-edge constant for complete-split graphical zonotopes

## Finding
For integers \(p\ge3\) and \(q\ge2\), let \(G_{p,q}=K_p\vee\overline{K_q}\) be the graph with a \(p\)-vertex clique, \(q\) mutually nonadjacent peripheral vertices, and every clique–periphery edge. Its canonical graphical zonotope is
\[
Z_{p,q}=\sum_{\{u,v\}\in E(G_{p,q})}[e_u,e_v]\subset\mathbb R^{p+q},
\]
with ordinary intrinsic Euclidean measure in its \((p+q-1)\)-dimensional affine hull. Write \(\mathcal S_{p,q}\) for its Euclidean boundary area. Every facet belongs to exactly one of these two classes:

1. There are exactly \(2q\) *peripheral-singleton* facets (the normal cuts with a single peripheral vertex on one side). Each has area
\[
L_{p,q}=(p+q-1)^{p-1/2}p^{q-2}.
\]
2. There are \((2^p-2)2^q\) *split-clique* facets. For each \(1\le k\le p-1\) and \(0\le t\le q\), precisely \(\binom pk\binom qt\) directed-cut facets have area
\[
B_{p,q}(k,t)=(k+t)^{k-1/2}(p-k+q-t)^{p-k-1/2}k^{t-1}(p-k)^{q-t-1}.
\]
The apparent negative exponents at a one-vertex side are harmless because the corresponding base is \(1\).

Consequently
\[
\begin{aligned}
\mathcal S_{p,q}={}&2qL_{p,q}
+\sum_{k=1}^{p-1}\binom pk\sum_{t=0}^{q}\binom qt B_{p,q}(k,t),\\
\operatorname{Vol}_{p+q-1}(Z_{p,q})={}&(p+q)^{p-1/2}p^{q-1}.
\end{aligned}
\]

For each *fixed* integer \(p\ge3\), define the positive coefficient
\[
A_p=\frac{p^2}{2}\sum_{k=1}^{p-1}\frac{\binom pk}{k(p-k)}
\left(\frac{k}{p}\right)^{k-1/2}
\left(\frac{p-k}{p}\right)^{p-k-1/2}.
\]
As \(q\to\infty\), the union of only \(2q\) peripheral-singleton facets carries the fraction
\[
\boxed{\frac{2qL_{p,q}}{\mathcal S_{p,q}}=1-A_pq^{-3/2}+O_p(q^{-5/2}).}
\]
Their proportion among all facets is exactly \(2q/[(2^p-2)2^q+2q]\to0\). Yet the area share tends to \(1\). The coefficient is genuinely clique-size dependent: \(A_3=3\sqrt2\) and \(A_4=3\sqrt3+3/2\).

The family of leading coefficients itself has the non-elementary large-clique limit
\[
\boxed{\lim_{p\to\infty}\frac{A_p}{p^{3/2}}
=C_*:=\sum_{j=1}^{\infty}\frac{e^{-j}j^{j-3/2}}{j!}\approx0.6186033.}
\]
This last limit concerns the coefficients from the *fixed-\(p\), large-\(q\)* expansion; it does **not** assert uniformity when both parameters tend to infinity together.

## Assumptions and scope
All edges are unweighted, and every generator is the unit-coefficient segment \([e_u,e_v]\), whose Euclidean length is \(\sqrt2\). Affine hull, dimensions, surface area, volume, and facet measures use the inherited Euclidean metric, **not** coordinate or lattice volume. A cut indexed by \(S\) and the complementary cut indexed by \(V\setminus S\) yield two distinct opposite facets and are both counted. A singleton graph has spanning-tree count \(1\).

## Proof
**Facets and their Euclidean measures.** For a connected graph \(G\) on \(n\) vertices, a nonempty proper cut \(S\sqcup T=V\) exposes a facet of its graphical zonotope precisely when both induced graphs \(G[S]\) and \(G[T]\) are connected. Fix a supporting normal constant on each side with distinct constants between the sides. Every crossing edge segment is thereby fixed at one endpoint, and the free generators lie entirely within the two induced subgraphs. Thus the face, up to translation, is an orthogonal Cartesian product of their graphical zonotopes. For a connected graph on \(s\) vertices, the Euclidean volume of its graphical zonotope is \(\sqrt{s}\,\tau(G)\), where \(\tau(G)\) counts spanning trees: expanding the zonotope volume by bases of its edge generators, each spanning-tree basis has Gram determinant \(s\). Therefore the cut-facet area is
\[
\sqrt{|S||T|}\,\tau(G[S])\tau(G[T]).
\]
For \(G_{p,q}\), any induced set containing a clique vertex is connected, while an induced set containing no clique vertex is connected only when it is a singleton. Hence the claimed exhaustive two-class classification and multiplicities.

**Tree factors.** The complete split graph with \(a\ge1\) clique vertices and \(b\ge0\) peripheral vertices has
\[
\tau(K_a\vee\overline{K_b})=(a+b)^{a-1}a^{b-1},
\]
including the singleton cases by direct interpretation. For \(b\ge1\), one proof uses its Laplacian eigenvalues: \(a+b\) repeated \(a\) times, \(a\) repeated \(b-1\) times, and one zero; the matrix-tree theorem divides their product by \(a+b\). For \(b=0\), Cayley's formula gives \(a^{a-2}\), and a one-vertex graph has tree count \(1\). Substitution into the cut-facet product gives \(L_{p,q}\) and \(B_{p,q}(k,t)\); applying the same volume identity to the whole graph gives the stated total volume.

**Fixed-clique asymptotics.** Put \(S_{\mathrm{sp}}=\mathcal S_{p,q}-2qL_{p,q}\). For each \(1\le k\le p-1\), let \(T_{q,k}\sim\operatorname{Bin}(q,k/p)\). Binomial reweighting yields the *exact* identity
\[
S_{\mathrm{sp}}=p^q\sum_{k=1}^{p-1}\frac{\binom pk}{k(p-k)}\,
\mathbb E\big[(k+T_{q,k})^{k-1/2}(p-k+q-T_{q,k})^{p-k-1/2}\big].
\]
When \(p\) is fixed, \(k/p\) lies strictly inside \((0,1)\). Taylor expansion about the binomial mean on a fixed interior neighborhood, together with its exponentially small complement and the binomial variance \(O(q)\), proves
\[
\mathbb E[\cdots]=q^{p-1}\left[\left(\frac{k}{p}\right)^{k-1/2}
\left(\frac{p-k}{p}\right)^{p-k-1/2}+O_p(q^{-1})\right].
\]
Therefore \(S_{\mathrm{sp}}=2A_p p^{q-2}q^{p-1}(1+O_p(q^{-1}))\). Meanwhile \(2qL_{p,q}=2p^{q-2}q^{p+1/2}(1+O_p(q^{-1}))\), so
\[
\frac{S_{\mathrm{sp}}}{2qL_{p,q}}=A_pq^{-3/2}+O_p(q^{-5/2}).
\]
Finally \((1+r)^{-1}=1-r+O(r^2)\) with \(r=O_p(q^{-3/2})\), proving the asserted area share. The exact facet-count fraction follows from the cut classification.

**Large-clique coefficient.** Write
\[
b_{p,k}=\binom pk\left(\frac{k}{p}\right)^k\left(1-\frac{k}{p}\right)^{p-k},
\qquad
\frac{A_p}{p^{3/2}}=\frac12\sum_{k=1}^{p-1}\frac{b_{p,k}}{[k(1-k/p)]^{3/2}}.
\]
For fixed \(k\), \(b_{p,k}\to e^{-k}k^k/k!\) as \(p\to\infty\). Stirling's elementary binomial-mass bound gives \(b_{p,k}\le C\sqrt{p/[k(p-k)]}\). For \(k\le p/2\), the summand is at most \(C'/k^2\), uniformly in \(p\). The full sum is symmetric under \(k\mapsto p-k\); hence both endpoint ranges converge by dominated convergence, and the central part has vanishing tails. The resulting endpoint series is precisely \(C_*\), and comparison with \(\sum k^{-2}\) proves absolute convergence. Elementary direct substitution gives the two stated small-clique coefficients.

## Verification
A separate reproducible checker (`verify_split.py`) enumerates every connected directed cut for small parameters and independently constructs its exposed Euclidean zonotope face as a convex hull of endpoint sums; SVD supplies intrinsic orthonormal coordinates and a convex hull supplies the face's ordinary Euclidean measure. It checks all \(28\) facets for \((p,q)=(3,2)\) and all \(54\) facets for \((3,3)\), including totals and class assignments, and also tests the \((2,2)\), \((2,3)\) and \((2,4)\) boundary cases as cross-checks. These finite checks corroborate, but do not substitute for, the all-parameter proof. The script also tests the coefficient formula and representative large-\(q\) numerical trends. Run `python verify_split.py` after installing `numpy` and `scipy` as specified in `requirements.txt`.

## Relationship to prior work
Dukes (first publicly posted 14 June 2020), in work on sandpiles of complete split graphs, gave the spanning-tree formula by a Prüfer-code argument; this is explicitly used as an ingredient, not claimed as new. Padrol, Pilaud and Poullot (first publicly posted 2021) study the graphical-zonotope normal fan and deformation cone and supply known face combinatorics, not Euclidean facet areas. The general spanning-tree zonotope volume identity is classical. A related two-hub complete-bipartite calculation exhibits the same \(q^{-3/2}\) concentration *exponent*; it involves a different graph and does not give the varying \(A_p\), its \(p\ge3\) exact area spectrum, or its large-\(p\) Poisson-edge constant. The new contribution is the complete metric calculation and the two asymptotic layers for complete split graphs.

## Limitations
Historical priority has been checked against accessible literature and mathematical research records but cannot exclude unindexed or inaccessible equivalent sources. No claim is made for weighted edges, simultaneous \(p,q\to\infty\), other multipartite block profiles, or an independent external mathematical audit. The exact facet-volume identity is a known principle; the asserted new content lies in this family's complete formula, concentration law, and coefficient limit. Numerical facet checks are only finite corroboration.

## References
- M. Dukes, *The sandpile model on the complete split graph, Motzkin words, and tiered parking functions*, arXiv:2006.08006, version 1 posted 2020-06-14; Proposition 3.8 and Corollary 3.9. https://arxiv.org/html/2006.08006v2
- A. Padrol, V. Pilaud, G. Poullot, *Deformed graphical zonotopes*, arXiv:2111.12422, 2021; Proposition 1.4 and associated normal-fan discussion. https://link.springer.com/article/10.1007/s00454-023-00586-x
- R. P. Stanley, *Enumerative Combinatorics*, volume 1, second edition, graphical zonotopes, spanning trees and standard zonotope volume theory (background only).
