# Exact width-variance rigidity and a logarithmic star limit for graphical discotopes

## Finding

Let \(G=([n],E)\) be any connected simple graph with \(n\ge3\), \(m=|E|\), and degrees \(d_v\). In the standard Euclidean space \(\mathbb R^n\), define its *graphical discotope*
\[
K_G=\sum_{\{i,j\}\in E}\{s e_i+t e_j:s^2+t^2\le1\}.
\]
For a Haar-uniform unit vector \(U\in S^{n-1}\), let \(W_G=h_{K_G}(U)+h_{K_G}(-U)\) be its directional width, and put
\[
q(G)=\sum_{v=1}^n\binom{d_v}{2},\qquad
\mu=\sqrt{\pi/2},\qquad
r_n=\sqrt2\,\frac{\Gamma((n+1)/2)}{\Gamma(n/2)}.
\]
For independent standard normals \(Z,Z'\), write
\[
f(s)=\mathbb E\sqrt{s^2+(Z')^2},\qquad
c_\mathrm D=\operatorname{Var}(f(Z))=0.20884335238\ldots>0.
\]
The exact first and second spherical moments, valid for every such graph, are
\[
\boxed{\mathbb E W_G=\frac{2\mu m}{r_n},\qquad
\mathbb E W_G^2=\frac4n\left[2m+\mu^2m(m-1)+2c_\mathrm D q(G)\right].}
\tag{1}
\]
In particular, at fixed order and edge count, the entire variance depends on the graph only through its incident-edge-pair count \(q(G)\), and increases strictly with that count.

For every tree on \(n\ge4\) vertices, the path \(P_n\) uniquely minimizes and the star \(S_n=K_{1,n-1}\) uniquely maximizes the width variance, up to graph isomorphism. Their exact separation is
\[
\boxed{\operatorname{Var}(W_{S_n})-\operatorname{Var}(W_{P_n})
=\frac{4c_\mathrm D(n-2)(n-3)}n.}
\tag{2}
\]
The two extremal families have different fluctuation scales:
\[
\boxed{W_{P_n}-\mathbb E W_{P_n}\ \xrightarrow{\mathrm d}\
N(0,8-3\pi+8c_\mathrm D),}\qquad 8-3\pi+8c_\mathrm D\approx0.24596886,
\tag{3}
\]
\[
\boxed{\frac{W_{S_n}}{\sqrt n}\ \xrightarrow{\mathrm d}\ 2f(|Z|),}\qquad
\frac{\operatorname{Var}(W_{S_n})}{n}\longrightarrow4c_\mathrm D.
\tag{4}
\]
The star limit has lower support endpoint \(w_0=2\sqrt{2/\pi}\). Its exact small-excess asymptotic is the non-power-law boundary singularity
\[
\boxed{\Pr\bigl(2f(|Z|)\le w_0+t\bigr)
\sim\frac{2^{3/4}}{\pi^{1/4}}
\sqrt{\frac{t}{\log(1/t)}}\qquad(t\downarrow0).}
\tag{5}
\]

## Assumptions and scope

All disks are filled radius-one Euclidean disks in the *coordinate* two-planes, not unit segments along graph incidence vectors. Every sum uses the original Euclidean coordinates; no quotient by the all-ones vector is taken. Graphs are finite, simple, connected, and unweighted; isolated vertices are excluded. The independent random direction is uniform on the ambient unit sphere, not sampled with graph-dependent weights. Formula (1) holds for all \(n\ge3\); the distinct tree extremizers require \(n\ge4\). The limits (3)–(5) are along the usual integer orders tending to infinity, with the standard unweighted path and star at each order. No finite-sample power law is inferred from (5).

## Proof

**Support function and radial reduction.** By support-function additivity and symmetry of each disk,
\[
W_G(u)=2\sum_{\{i,j\}\in E}\sqrt{u_i^2+u_j^2}\quad(\|u\|_2=1).
\tag{6}
\]
Let \(g_1,\ldots,g_n\) be independent standard normals, set \(R=(\sum_i g_i^2)^{1/2}\) and \(U=g/R\), and let \(X_{ij}=(g_i^2+g_j^2)^{1/2}\), \(S=\sum_{ij\in E}X_{ij}\). Then \(R\) and \(U\) are independent, \(R\) has mean \(r_n\) and squared mean \(\mathbb E R^2=n\), and \(W_G(U)=2S/R\). Since \(S=RW_G(U)/2\), homogeneity gives
\[
\mathbb EW_G=2\mathbb ES/r_n,\qquad \mathbb EW_G^2=4\mathbb ES^2/n.
\tag{7}
\]
Each \(X_{ij}\) is Rayleigh, so \(\mathbb EX_{ij}=\mu\) and \(\mathbb EX_{ij}^2=2\). Disjoint-edge summands are independent and have product mean \(\mu^2\). Distinct summands sharing exactly one endpoint, say \(X_{12}\) and \(X_{13}\), are conditionally independent given \(g_1\); therefore their covariance is exactly
\[
\operatorname{Cov}(X_{12},X_{13})
=\operatorname{Var}(\mathbb E[\sqrt{g_1^2+g_2^2}\mid g_1])=c_\mathrm D.
\]
Counting \(q(G)\) unordered incident-edge pairs and expanding \(S^2\) proves (1). The function \(f(|s|)\) is strictly increasing, so \(c_\mathrm D>0\). For an explicit integral useful in (5),
\[
f(s)=\sqrt{\frac2\pi}\int_0^\infty\sqrt{s^2+z^2}\,e^{-z^2/2}\,dz.
\tag{8}
\]

**Sharp tree extremizers.** A tree has \(m=n-1\). Writing \(a_v=d_v-1\ge0\), the degree-sum identity gives \(\sum_v a_v=n-2\), and
\[
q(T)=\frac12\sum_v(a_v^2+a_v).
\]
Since the \(a_v\) are nonnegative integers, \(\sum a_v^2\ge\sum a_v\), with equality exactly when every degree is at most two, forcing a path. Also \(\sum a_v^2\le(\sum a_v)^2\), with equality exactly when all excess degree is concentrated at one vertex, forcing a star. Thus \(n-2\le q(T)\le\binom{n-1}{2}\) with those unique equality cases. Inserting the difference into (1) proves (2).

**Path central limit.** For \(P_n\), let \(X_i=\sqrt{g_i^2+g_{i+1}^2}\), \(Q_n=\sum_{i=1}^n(g_i^2-1)\), and \(A_n=n^{-1/2}\sum_{i=1}^{n-1}(X_i-\mu)\), \(B_n=Q_n/\sqrt n\). The vector-valued summands involving \(X_i\) and \(g_i^2-1\) form a stationary one-dependent sequence with moments of every order. Blocking, or the standard one-dependent multivariate central limit theorem, yields a centered Gaussian joint limit with
\[
\lim\operatorname{Var}(A_n)=2-\mu^2+2c_\mathrm D,\quad
\lim\operatorname{Var}(B_n)=2,\quad
\lim\operatorname{Cov}(A_n,B_n)=\mu.
\tag{9}
\]
For the cross covariance, \(\operatorname{Cov}(X_{12},g_1^2+g_2^2-2)=\mathbb EX_{12}^3-2\mathbb EX_{12}=\mu\), using the Rayleigh moments; no other vertex contributes. Since \(R^2=n+\sqrt n B_n\), the first-order radial Taylor expansion gives
\[
W_{P_n}-\frac{2\mu(n-1)}{\sqrt n}=2A_n-\mu B_n+o_{\Pr}(1).
\tag{10}
\]
The gamma-ratio expansion shows \(2\mu(n-1)/r_n-2\mu(n-1)/\sqrt n=o(1)\), so the centering is the exact mean in (3). The variance of the Gaussian linear combination in (10) is \(8-3\pi+8c_\mathrm D\). It is strictly positive: Cauchy–Schwarz applied to \(f(g_1)\) and \(g_1^2-1\), together with \(\operatorname{Cov}(f(g_1),g_1^2)=\mu/2\), gives \(c_\mathrm D\ge\mu^2/8=\pi/16\); consequently the displayed variance is at least \(8-5\pi/2>0\).

**Star law and logarithmic edge.** Label the center of \(S_n\) by zero, the other coordinates by \(1,\ldots,n-1\), and write \(S=\sum_{j=1}^{n-1}\sqrt{g_0^2+g_j^2}\). Conditional on \(g_0\), the strong law gives \(S/(n-1)\to f(|g_0|)\) almost surely, and independently \(R/\sqrt n\to1\) in probability. The exact identity \(W=2S/R\) proves the distributional limit (4). Its variance limit follows directly from the finite formula (1), with \(q(S_n)=\binom{n-1}{2}\).

Put \(a=\sqrt{2/\pi}\). Subtracting \(f(0)=a\) in (8) and rationalizing the square root yields
\[
f(s)-a=a s^2\int_0^\infty
\frac{e^{-z^2/2}}{\sqrt{s^2+z^2}+z}\,dz
\sim\frac{a}{2}s^2\log(1/s)\quad(s\downarrow0).
\tag{11}
\]
The coefficient follows by splitting the integral into \((0,s)\), \((s,1)\) and \((1,\infty)\): only the middle interval contributes the divergent \(\tfrac12\log(1/s)\). In particular, setting \(x=s^2\),
\[
2(f(s)-a)\sim\frac1{\sqrt{2\pi}}x\log(1/x).
\]
The inverse relation for \(x\log(1/x)\) and \(\Pr(|Z|\le s)\sim a s\) then give (5), including its constant. This proves a logarithmic modification of the square-root lower edge, not merely an unquantified convergence statement.

## Verification

The accompanying `verify.py` runs using only the Python standard library. It numerically integrates (8) to determine \(c_\mathrm D\), compares the exact first two moments of twenty graphs (paths, stars, cycles, and complete graphs on four to eight vertices) against independently seeded uniform-sphere Monte Carlo samples, checks (2) for every order from four through twenty-nine, and exhaustively checks the degree-count extremal certificates for all 18,247 labeled trees on three to seven vertices through Prüfer sequences. On the packaged script the execution reports `DISCOTOPE_WIDTH_CHECK_PASS` with \(c_\mathrm D\approx0.20884354\) and the path variance approximately \(0.24597035\); its numerical quadrature tolerance explains the slight deviation from (8)'s higher-precision integral value. These are diagnostics; the exact identities, infinite graph classification, Gaussian limit and edge asymptotic are supplied by the proof, not inferred from finite tests.

## Relationship to prior work

Gesmundo and Meroni study the algebraic boundary and exposed-face structure of discotopes, while Mathis and Meroni analyze fiber convex bodies involving discotopes. These works supply the natural disk-sum class but do not evaluate its spherical width variance or the logarithmic star-law edge. The published *Degree-ellipsoid rigidity and complete contact graphs of bipartite graphical discotopes* concerns John–Löwner ellipsoids and contact loci of the same coordinate-plane disk sums, not the probability distribution of their support widths.

The published *Sharp width-variance extremizers among tree graphical zonotopes* establishes an analogous wedge-count identity for **line segments along incidence vectors**, not two-dimensional disks in coordinate planes. In that model the edge summands are absolute one-dimensional Gaussian projections and the star fluctuations are folded-normal, whereas here the summands are correlated Rayleigh norms and the star limit has the logarithmic boundary behavior (5). Neither geometric model is an affine equivalent of the other: the discotope has curved summands and different ambient support geometry. Consequently those prior theorems do not imply (1)–(5). They are close methodological antecedents, not claims of historically certified novelty.

## Limitations

The calculation assumes independent standard Gaussian coordinates and the uniform ambient Euclidean spherical direction, not anisotropic norms, non-unit disk radii, or a projected intrinsic sphere. The exact graph-invariant formula gives only the first two moments; the complete finite-width distribution of an arbitrary graph is not claimed. The path normal limit and star law do not establish a universal law for every tree sequence. The star lower-edge formula concerns the **limiting** width law, not a uniform finite-order small-deviation estimate. The quadrature and enumeration are finite corroboration, not independent verification or an infinite proof. Priority remains subject to unindexed results on general zonoid support-function correlations and disk-sum random widths.

## References

1. L. Mathis and C. Meroni, *Fiber Convex Bodies*, arXiv:2105.12406, first public submission 2021-05-26, https://arxiv.org/abs/2105.12406. Full open-access text at https://doi.org/10.1007/s00454-022-00451-3.
2. F. Gesmundo and C. Meroni, *The Geometry of Discotopes*, arXiv:2111.01241, first public submission 2021-11-01, https://arxiv.org/abs/2111.01241. In particular Sections 2–3 and 8.
3. *Degree-ellipsoid rigidity and complete contact graphs of bipartite graphical discotopes*, published 2026-10-18, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-degree-ellipsoid-rigidity-and-complete-contact-graphs-of-biparti--5cadf5d3fdbb.
4. *Sharp width-variance extremizers among tree graphical zonotopes*, published 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-width-variance-extremizers-among-tree-graphical-zonotopes--482983ab9269.
