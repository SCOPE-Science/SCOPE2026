# One oriented-root deletion: a crosspolytopal cap and three scales of geometric loss

## Finding
Let \(n\ge3\) and write \(H_n=\{x\in\mathbb R^n:\sum_{i=1}^n x_i=0\}\), equipped with the ambient Euclidean metric. Let
\[
P_n=\operatorname{conv}\{e_i-e_j:1\le i\ne j\le n\},\quad
v=e_1-e_2,\quad
Q_n=\operatorname{conv}\big(\operatorname{vert}(P_n)\setminus\{v\}\big).
\]
Here the opposite root \(-v\) remains in \(Q_n\). Put \(\phi(x)=x_1-x_2\). Then:

1. \(Q_n=P_n\cap\{\phi\le1\}\). Its newly exposed facet is the \((n-2)\)-crosspolytope
\[
F_n=\operatorname{conv}\{e_1-e_j,\ e_j-e_2:3\le j\le n\}.
\]
The closure of the deleted cap is exactly \(\operatorname{conv}(v,F_n)\); the base facet itself remains in \(Q_n\).
2. The directed Euclidean Hausdorff distance from \(P_n\) to \(Q_n\) and the distance of \(v\) to \(Q_n\) are both \(1/\sqrt2\). The deleted cap's \((n-1)\)-volume is
\[
\operatorname{Vol}_{n-1}(P_n\setminus Q_n)=\frac{2^{n-3}\sqrt n}{(n-1)!}.
\]
By the classical difference-body formula for a simplex,
\[
\frac{\operatorname{Vol}_{n-1}(P_n\setminus Q_n)}{\operatorname{Vol}_{n-1}(P_n)}
=\frac{2^{n-3}}{\binom{2n-2}{n-1}}
\sim\frac{\sqrt{\pi n}}{2^{n+1}}.
\]
3. Let \(U\) be uniform on the unit sphere in \(H_n\), and let \(\Lambda_n(U)=W_{P_n}(U)-W_{Q_n}(U)\) be the width loss. Then
\[
\Pr\{\Lambda_n(U)>0\}=\frac{2}{n(n-1)}.
\]
More precisely, if \(g_1,\ldots,g_n\) are independent standard normals, \(\bar g=n^{-1}\sum g_i\), \(s_g=(\sum(g_i-\bar g)^2)^{1/2}\), and \(g_{(1)}<\cdots<g_{(n)}\) are their ordered values, then for \(U=(g_i-\bar g)_{i=1}^n/s_g\),
\[
\Lambda_n(U)=\mathbf1_{\{\{\arg\max_i g_i,\arg\min_i g_i\}=\{1,2\}\}}
\frac{\min\{g_{(n)}-g_{(n-1)},\ g_{(2)}-g_{(1)}\}}{s_g}.
\]
Consequently, writing \(\mathrm{Exp}(2)\) for the exponential distribution of rate two,
\[
\sqrt{2n\log n}\;\Lambda_n(U)\ \big|\ \{\Lambda_n(U)>0\}
\ \Longrightarrow\ \mathrm{Exp}(2).
\]

## Assumptions and scope
The polytope uses the *complete-graph, oriented type-A root set* with all \(n(n-1)\) roots, but removes only one root, keeping its antipode. All Hausdorff distances and volumes are intrinsic to the Euclidean hyperplane \(H_n\). Width is \(W_K(u)=\max_{x\in K}\langle u,x\rangle-\min_{x\in K}\langle u,x\rangle\). A single randomly sampled direction is Haar-uniform on the unit sphere of \(H_n\). No result is asserted about deleting both orientations, which is a different operation.

## Proof
**Exact truncation.** For any surviving root \(r=e_i-e_j\), one has \(\phi(r)\le1\); only \(v\) has \(\phi(v)=2\). The roots with \(\phi=1\) are exactly the \(2(n-2)\) vertices defining \(F_n\). Intersections of the segment from \(v\) to a root \(r\) with \(\phi=1\) lie in \(Q_n\): if \(r\) is disjoint from indices \(1,2\), the intersection is \((v+r)/2\), the average of \(e_1-e_j\) and \(e_i-e_2\). If \(r=e_2-e_j\), it is \((2v+r)/3=\frac23(e_1-e_j)+\frac13(e_j-e_2)\); if \(r=e_i-e_1\), it is \((2v+r)/3=\frac13(e_1-e_i)+\frac23(e_i-e_2)\). If \(r=-v\), it is \(v/2\), the midpoint of \(e_1-e_3\) and \(e_3-e_2\). These exhaust the cases for \(\phi(r)<1\). Intersecting each segment \([v,r]\) with \(\{\phi\le1\}\) and taking convex hull proves \(P_n\cap\{\phi\le1\}=Q_n\), as claimed.

**Cap geometry, metric, and volume.** The center of \(F_n\) is \(v/2\), and its opposite vertex pairs are \(v/2\pm w_j\), \(w_j=(e_1+e_2)/2-e_j\), for \(3\le j\le n\). Their Gram matrix is \(I_{n-2}+\frac12J_{n-2}\), of determinant \(n/2\). Thus the intrinsic facet volume is \(2^{n-2}\sqrt{n/2}/(n-2)!\). Its affine supporting hyperplane \(\{\phi=1\}\) has unit normal \(v/\sqrt2\) in \(H_n\), so the height from \(v\) is \(1/\sqrt2\). The pyramid-volume formula yields the asserted cap volume. The foot of the perpendicular from \(v\) is \(v/2\in F_n\), giving \(\operatorname{dist}(v,Q_n)=1/\sqrt2\). Since distance to a convex set is convex, its maximum on \(P_n=\operatorname{conv}(Q_n\cup\{v\})\) equals the vertex distance, proving the Hausdorff claim. Write \(\Delta=\operatorname{conv}(e_1,\ldots,e_n)\). Then \(P_n=\Delta-\Delta\) and \(\operatorname{Vol}_{n-1}(\Delta)=\sqrt n/(n-1)!\); the Rogers–Shephard equality for a simplex says \(\operatorname{Vol}_{n-1}(\Delta-\Delta)=\binom{2n-2}{n-1}\operatorname{Vol}_{n-1}(\Delta)\). The ratio follows. Central binomial asymptotics give the stated limit.

**Random directions.** A direction with distinct coordinates exposes exactly \(e_a-e_b\) as maximizing root of \(P_n\), where \(a=\arg\max u_i\) and \(b=\arg\min u_i\). Since precisely \(v\) was removed, \(h_{P_n}(u)-h_{Q_n}(u)>0\) iff \((a,b)=(1,2)\), and the decrease is the minimum of the top and bottom coordinate gaps (changing just the maximizing or just the minimizing coordinate). The analogous loss in direction \(-u\) occurs iff \((a,b)=(2,1)\). These events are disjoint; exchangeability yields probability \(2/[n(n-1)]\) and the displayed exact finite-dimensional formula. The Gaussian-vector representation produces Haar-uniform directions in \(H_n\). For independent Gaussian samples, the two extreme-order spacings multiplied by \(\sqrt{2\log n}\) converge jointly to independent unit-rate exponentials (by the two-sided Gaussian extreme-value point-process limit). Also \(s_g/\sqrt n\to1\) in probability, including after conditioning on the two extreme *labels*: their random labels are independent of the ordered sample. The minimum of two independent unit-rate exponentials has rate two; Slutsky's theorem yields the displayed conditional weak limit.

## Verification
The accompanying standalone Python program independently constructs all roots for \(3\le n\le7\), evaluates the two convex-hull volumes in orthonormal coordinates with `scipy.spatial.ConvexHull`, checks the exact rational predicted ratios, checks the facet Gram determinants and the Hausdorff projection certificate, and verifies the extreme-label event formula for sampled distinct directions. The output ends with `ROOT_VERTEX_DELETION_EXACT_NUMERIC_PASS`. Finite checks support, but do not replace, the all-dimensional proof or the Gaussian weak-limit theorem.

## Relationship to prior work
D'Alì, Delucchi and Michałek establish the symmetric-edge/Kantorovich–Rubinstein framework, with results on graph constructions and lattice invariants (arXiv:1910.05193). Ohsugi and Tsuchiya study associated volume and generating-polynomial questions, especially graph suspensions (arXiv:2008.08621). The Rogers–Shephard simplex difference-body formula supplies the *known* denominator, not a new assertion. Awasthi, Kalantari and Zhang motivate vertex robustness as the distance to the hull of remaining vertices (arXiv:1802.01515). Related published work proves a crosspolytopal cap when deleting the highest root of the *positive*, not symmetric, type-A root polytope; its ambient vertex set and geometry differ. Another related result analyzes rare width loss after deleting **many matching-diagonal vertices** from a product of simplices, in a different dimension and vertex configuration. Neither of these statements formally yields the one-oriented-root truncation plus exact Gaussian-direction loss law proved here.

## Limitations
The theorem concerns complete type-A root sets with one oriented root removed. It does not assert analogous formulas for arbitrary graphs, both orientations removed, or nonuniform metrics. The asymptotic conditional distribution is weak convergence, not a finite-sample exponential identity. The difference-body volume input and standard Gaussian extreme-spacing limit are classical. The priority assessment remains provisional: relevant contemporary records were compared by their stated mathematical claims, but some entire published texts were not accessible for a complete line-by-line inspection. Independent mathematical validation has not been performed.

## References
1. A. D'Alì, E. Delucchi, M. Michałek, *Many Faces of Symmetric Edge Polytopes*, arXiv:1910.05193, initial preprint 11 October 2019.
2. H. Ohsugi, A. Tsuchiya, *Symmetric Edge Polytopes and Matching Generating Polynomials*, arXiv:2008.08621, initial preprint August 2020.
3. C. A. Rogers and G. C. Shephard, *The Difference Body of a Convex Body*, 1957/1958 classical simplex equality (volume-ratio reference; the theorem is used as prior work).
4. P. Awasthi, B. Kalantari, Y. Zhang, *Robust Vertex Enumeration for Convex Hulls in High Dimensions*, arXiv:1802.01515, initial preprint 5 February 2018.
5. Published research note, *Crosspolytopal highest-root deletion and a power-of-two volume loss*, published-finding corpus record `95c090fe6926` (positive-root variant).
6. Published research note, *Rare exponential directional loss despite constant Hausdorff distance in crown-graph root polytopes*, published-finding corpus record `771379f5fcb8` (different deletion and body).
