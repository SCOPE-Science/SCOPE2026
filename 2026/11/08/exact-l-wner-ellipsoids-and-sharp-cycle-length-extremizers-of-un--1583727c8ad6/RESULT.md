# Exact Löwner ellipsoids and sharp cycle-length extremizers of unicyclic graphical zonotopes

## Finding
Let \(G\) be a connected simple unicyclic graph with \(n\ge 3\) vertices and unique cycle of length \(3\le k\le n\). Put \(d=n-1\), \(b=n-k\), \(q_k=\lfloor k^2/4\rfloor\), and define the centered Euclidean graphical zonotope
\[
Z_G=\sum_{uv\in E(G)}[-(e_u-e_v)/2,(e_u-e_v)/2]
\subset H_n:=\{x\in\mathbb R^n:\sum_vx_v=0\}.
\]
Define two positive edge weights
\[
w_{\mathrm{bridge}}=\frac d4,\qquad
w_{\mathrm{cycle}}=\frac{d q_k}{k(k-1)},
\]
and let \(M_G=\sum_{uv\in E(G)}w_{uv}(e_u-e_v)(e_u-e_v)^{\mathsf T}\) be their weighted Laplacian. Then the **unique minimum-volume containing Euclidean ellipsoid** of \(Z_G\), in its intrinsic \(d\)-dimensional metric, is
\[
\boxed{\mathcal E_G=\{x\in H_n:x^{\mathsf T}M_G^+x\le1\}},
\]
where \(M_G^+\) is the Moore–Penrose inverse. Its Euclidean volume is
\[
\boxed{\operatorname{Vol}_d(\mathcal E_G)=\kappa_d\sqrt{nk}
\left(\frac d4\right)^{b/2}
\left(\frac{d q_k}{k(k-1)}\right)^{(k-1)/2}},
\]
with \(\kappa_d=\pi^{d/2}/\Gamma(1+d/2)\). In particular the volume depends on \(G\) only through \(n\) and \(k\), regardless of the placement of its bridges.

Orient the cycle cyclically; assign independent signs \(\sigma_e\in\{\pm1\}\) to its edges and to every bridge. The graphical-zonotope vertex defined by \(\sigma\) contacts \(\partial\mathcal E_G\) **if and only if** the number of positive cycle signs is \(\lfloor k/2\rfloor\) or \(\lceil k/2\rceil\). Bridge signs are unrestricted. Consequently the exact number of tangent vertices is
\[
\boxed{N_{\mathrm{contact}}=2^{n-k}\begin{cases}
\binom{k}{k/2},&k\text{ even},\\
2\binom{k}{(k-1)/2},&k\text{ odd}.
\end{cases}}
\]
There are \(2^{n-k}(2^k-2)\) vertices altogether. Every vertex contacts the ellipsoid exactly when \(k=3\); if \(k\ge4\), some vertices lie strictly inside it.

At fixed \(n\), the ellipsoid volume is **strictly increasing with the cycle length \(k\)**. Thus the minimum occurs exactly for unicyclic graphs whose cycle is a triangle, and the maximum occurs uniquely (up to graph isomorphism) for the cycle graph \(C_n\). For \(k=3\), the attachments are arbitrary and all attain the same minimum.

## Assumptions and scope
All edges are distinct and unweighted. The graph is connected and has exactly one cycle, hence \(|E(G)|=n\). The realization is the canonical incidence-vector realization in \(H_n\) with its inherited Euclidean inner product; the ellipsoid statement is not about an arbitrary affine embedding. The term 'minimum-volume containing ellipsoid' means a full-dimensional ellipsoid in \(H_n\) enclosing every point of \(Z_G\). The graph orientation affects neither the zonotope nor the result.

## Proof
**1. One-circuit quotient.** Direct the \(k\) cycle edges consistently and orient all bridges arbitrarily. Let \(B\) be the \(n\times n\) vertex-edge incidence matrix. Connectivity and unicyclicity imply \(\operatorname{rank}B=n-1\), and the nullspace of \(B\) consists of the vector equal to \(1\) on the cycle edges and \(0\) on the bridges. Its orthogonal complement is
\[
W=\mathbb R^b\oplus H_k,
\qquad H_k=\{y\in\mathbb R^k:\sum_i y_i=0\}.
\]
The restriction \(T=B|_W:W\to H_n\) is a linear isomorphism. With \(P_k=I_k-\mathbf1\mathbf1^{\mathsf T}/k\), the zonotope is the image under \(T\) of the orthogonal Cartesian product
\[
K=[-1/2,1/2]^b\times P_k([-1/2,1/2]^k).
\]
The second factor has vertices indexed by all mixed-sign vectors \(\sigma\in\{\pm1\}^k\), excluding the two constant vectors. The first factor contributes every bridge sign independently. Indeed, any mixed cycle sign pattern can be strictly realized by a zero-sum linear functional of that sign pattern, whereas constant signs project to the interior point \(0\).

**2. Exact optimal ellipsoid in quotient coordinates.** Set \(q_k=\lfloor k^2/4\rfloor\). For \(\sigma\in\{\pm1\}^k\) with \(j\) positive signs,
\[
\left\|\tfrac12P_k\sigma\right\|^2
=\frac{j(k-j)}k\le\frac{q_k}k,
\]
with equality exactly for balanced counts \(j\in\{\lfloor k/2\rfloor,\lceil k/2\rceil\}\). Every bridge vector in \([-1/2,1/2]^b\) has squared norm at most \(b/4\). Therefore the ellipsoid
\[
\mathcal F=\left\{(u,v)\in W:
\frac{\|u\|^2}{d/4}
+\frac{\|v\|^2}{d q_k/[k(k-1)]}\le1\right\}
\]
contains \(K\): the two summands are at most \(b/d\) and \((k-1)/d\), respectively.

To certify **global** volume minimality, rather than merely symmetry-constrained minimality, choose each bridge sign uniformly and independently, and choose the cycle sign uniformly among the balanced mixed patterns. Let \(X\) be the resulting vertex of \(K\). Opposite signs and coordinate permutations imply \(\mathbb E X=0\). The bridge covariance is \(I_b/4\). The cycle covariance, by permutation invariance on the irreducible zero-sum coordinate space and the constant squared norm \(q_k/k\), is
\[
\operatorname{Cov}(X_{\mathrm{cycle}})=
\frac{q_k}{k(k-1)}P_k.
\]
Thus \(\operatorname{Cov}(X)\) restricted to \(W\) is exactly \(1/d\) times the positive definite shape operator of \(\mathcal F\). After normalizing by that operator, the contact distribution is supported on the unit sphere, has mean zero and covariance \(I_d/d\).

For any competing ellipsoid \(\{y:(y-c)^{\mathsf T}A^{-1}(y-c)\le1\}\) containing the normalized body, expectation over these contacts gives
\[
\frac1d\operatorname{tr}(A^{-1})+c^{\mathsf T}A^{-1}c\le1.
\]
The arithmetic–geometric mean inequality gives \(\det A\ge1\). Equality forces \(c=0\) and \(A=I_d\). Hence the unit ball is the unique minimizing ellipsoid in normalized coordinates; equivalently \(\mathcal F\) is the unique Löwner ellipsoid of \(K\). By affine invariance, \(T\mathcal F\) is the unique Löwner ellipsoid of \(Z_G\).

**3. Weighted-Laplacian shape, vertex contacts, and volume.** The image shape operator is \(TST^{\mathsf T}\), with scalar blocks \(S_b=(d/4)I_b\) and \(S_k=dq_kP_k/[k(k-1)]\). Since \(BP_k=B\) on cycle-edge columns, this image shape is exactly \(M_G\). The quadratic ellipsoid equation with \(M_G^+\) follows. Equality in the containing inequality holds precisely when all bridge coordinates have magnitude \(1/2\) and the cycle sign pattern is balanced. Distinct mixed cycle patterns and bridge signs give distinct vertices, proving both contact and total vertex counts.

For the volume, \(\det(T^{\mathsf T}T)=\operatorname{pdet}(BB^{\mathsf T})=n\tau(G)=nk\): the matrix-tree theorem and the fact that a unicyclic graph has exactly \(k\) spanning trees prove the last equality. Hence the Jacobian of \(T\) is \(\sqrt{nk}\). The determinant of \(S\) on \(W\) is \((d/4)^b(dq_k/[k(k-1)])^{k-1}\). Multiplying the unit-ball volume by the Jacobian and the square root of this determinant yields the displayed formula.

**4. Strict cycle-length ordering.** For fixed \(n\), factor the volume as
\[
\kappa_d\sqrt n\left(\frac d4\right)^{d/2}F(k),
\qquad F(k)=\sqrt k\left(\frac{4\lfloor k^2/4\rfloor}{k(k-1)}\right)^{(k-1)/2}.
\]
For odd \(k\), direct cancellation gives \(F(k+1)/F(k)=(k+1)/k>1\). For even \(k=2m\), \(m\ge2\), direct cancellation gives
\[
\frac{F(2m+1)^2}{F(2m)^2}
=\frac{2m+1}{2m-1}
\left(1-\frac1{m(2m+1)}\right)^{2m}>1.
\]
The strict inequality follows from Bernoulli's inequality: the power is strictly greater than \(1-2/(2m+1)=(2m-1)/(2m+1)\). Therefore \(F(k)\) increases strictly with \(k\), as claimed.

## Verification
The accompanying standalone `check_unicyclic_ellipsoid.py` uses exact rational matrices and checks 51 labeled connected unicyclic graph instances with \(3\le n\le8\). For every instance it independently enumerates edge-sign images, verifies enclosure and the balanced-sign contact criterion, checks the full isotropic contact covariance certificate and the weighted matrix-tree cofactor identity. It also checks strict volume ordering for integer \(k\) from 3 through 40. Run with `python check_unicyclic_ellipsoid.py` after installing the dependency listed in `requirements.txt`. The observed success marker is `UNICYCLIC_GRAPHICAL_ZONOTOPE_LOEWNER_CHECKS_PASSED 51 3468 6696`. Finite checks are not a substitute for the general proof above.

## Relationship to prior work
Padrol, Pilaud and Poullot characterize deformation cones of graphical zonotopes and describe the acyclic-orientation vertex correspondence and standard graphical examples, but do not determine minimum-volume enclosing ellipsoids. Deza and Pournin treat efficient zonotope vertex enumeration rather than this metric invariant. Gassmann and Althoff study zonotope–ellipsoid conversion, identify the exact invertible-generator (parallelotope) case, and give approximation schemes for redundant generators. The present one-circuit incidence family has exactly one generator dependence and a complete exact solution. The established complete-bipartite graphical-zonotope ellipsoid formula covers the special case \(C_4=K_{2,2}\) but neither arbitrary unicyclic graphs nor the cycle-length volume ordering. Standard uniqueness, isotropic contact criteria, and the matrix-tree theorem are proof tools and are not new claims.

## Limitations
The statement is confined to connected unweighted unicyclic graphs. Weighted cycles with nonuniform edge magnitudes, multiple independent graph cycles, disconnected graphs, and alternative Euclidean embeddings are not covered. The proof provides an analytical certificate, not an independent external audit. Historical priority is provisional: a specialized ellipsoid theorem under matroid or experimental-design terminology could yield an equivalent formulation that was not located in the inspected literature.

## References
1. A. Deza and L. Pournin, *A Linear Optimization Oracle for Zonotope Computation*, arXiv:1912.02439 (first posted 2019-12-05), https://arxiv.org/abs/1912.02439.
2. V. Gassmann and M. Althoff, *Scalable Zonotope-Ellipsoid Conversions using the Euclidean Zonotope Norm*, Proceedings of ACC 2020, DOI:10.23919/ACC45564.2020.9147938, https://doi.org/10.23919/ACC45564.2020.9147938.
3. A. Padrol, V. Pilaud, and G. Poullot, *Deformed Graphical Zonotopes*, arXiv:2111.12422 (first posted 2021-11-24), https://arxiv.org/abs/2111.12422.
4. Classical minimum-enclosing-ellipsoid (isotropic-contact) characterization and the matrix-tree theorem, as standard background results.
5. *Exact Löwner ellipsoid and contact vertices of complete-bipartite graphical zonotopes*, publicly indexed mathematical research record (2026-10-11); summary inspected, primary full text not accessible.
