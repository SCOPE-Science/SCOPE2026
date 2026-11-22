# Parity-sharp near-Nyquist recovery of exact three-sphere harmonics on one torus knot

## Finding
For every integer \(\ell\ge1\), let \(\mathcal H_\ell(S^3)\) be the complex exact-degree-\(\ell\) spherical-harmonic space on the unit three-sphere. Its dimension is \((\ell+1)^2\). Fix \(0<s<1\) outside the finite zero set described below and sample on one closed primitive Hopf-torus trajectory
\[
\gamma_{p,q,s}(t)=\big(\sqrt{s}\,e^{ipt},\sqrt{1-s}\,e^{iqt}\big),\qquad t_j=2\pi j/M,\quad 0\le j<M.
\]
Among **all** primitive integer windings \((p,q)\) and all positive integers \(M\), the sharp minimum number of equally spaced samples needed for injectivity on \(\mathcal H_\ell(S^3)\) is
\[
\boxed{M_\ell=\begin{cases}(\ell+1)^2,&\ell\text{ even},\\(\ell+1)^2+1,&\ell\text{ odd}.\end{cases}}
\]
For even \(\ell\), the sharp count is attained by
\[
(p,q)=\big(\ell/2,\ell/2+1\big).
\]
For odd \(\ell\), it is attained by
\[
(p,q)=(1,\ell+1).
\]
At the optimal counts, the sampling image equals the full \(\mathbb C^{M_\ell}\) for even degree and precisely the zero-mean hyperplane \(\{(v_j):\sum_jv_j=0\}\) for odd degree. The explicit inversion is a single discrete Fourier transform followed by division by the separated radial coefficients. Every degree can use the same fixed torus parameter \(s=e^{-1}\), because it is transcendental.

## Assumptions and scope
The complex sphere is \(S^3=\{(z_1,z_2)\in\mathbb C^2:|z_1|^2+|z_2|^2=1\}\). Harmonics are restrictions of complex homogeneous **real-four-dimensional** harmonic polynomials, not holomorphic polynomials alone. For fixed \(\ell\), the finite exceptional set \(Z_\ell\subset(0,1)\) is the set of zeros of all nonzero rational polynomials \(Q_{\ell,m,n}\) in the proof. All asserted sharp counts hold whenever \(s\notin Z_\ell\). The universal choice \(s=e^{-1}\) avoids \(Z_\ell\) for every \(\ell\). The construction uses equispaced points on one periodic trajectory; no claim is made about shortest path length, optimal conditioning, arbitrary nonuniform points, or simultaneous recovery of multiple degrees.

## Proof
**1. Exact angular basis and nonvanishing.** The allowed torus weights in degree \(\ell\) are
\[
D_\ell=\{(m,n)\in\mathbb Z^2:|m|+|n|\le\ell,\ \ell-|m|-|n|\in2\mathbb Z_{\ge0}\}.
\]
Write \(\alpha=|m|\), \(\beta=|n|\), \(h=(\ell-\alpha-\beta)/2\). Put \(c_0=1\) and
\[
c_{a+1}=-c_a\frac{(h-a)(h-a+\beta)}{(a+1)(a+1+\alpha)},\qquad0\le a<h,
\]
\[
Q_{\ell,m,n}(s)=\sum_{a=0}^h c_a s^a(1-s)^{h-a}.
\]
The corresponding homogeneous polynomial is
\[
H_{m,n}=z_1^{m_+}\bar z_1^{m_-}z_2^{n_+}\bar z_2^{n_-}
\sum_{a=0}^{h}c_a|z_1|^{2a}|z_2|^{2(h-a)}.
\]
The Laplacian \(4(\partial_{z_1}\partial_{\bar z_1}+\partial_{z_2}\partial_{\bar z_2})\) annihilates this polynomial: the coefficient indexed by \(a\) is \(c_{a+1}(a+1)(a+1+\alpha)+c_a(h-a)(h-a+\beta)=0\). Distinct pairs give independent torus characters. Under the substitution
\[
U=m+n=-\ell+2i,\quad V=m-n=-\ell+2j,\qquad0\le i,j\le\ell,
\]
we obtain a bijection from the \((\ell+1)\times(\ell+1)\) integer square onto \(D_\ell\). As \(\dim\mathcal H_\ell(S^3)=(\ell+1)^2\), these harmonics form a basis. On the torus their values are
\[
H_{m,n}(\gamma_{p,q,s}(t))=s^{\alpha/2}(1-s)^{\beta/2}Q_{\ell,m,n}(s)e^{i(pm+qn)t}.
\]
Every radial polynomial is nonzero with rational coefficients, since \(Q_{\ell,m,n}(0)=1\); hence its zeros are algebraic and finite. The global fixed choice \(s=e^{-1}\) is transcendental and avoids all those zeros.

**2. Fourier-residue criterion.** For \(L=\ell+1\), the projected integer frequency corresponding to the pair \((i,j)\in\{0,\ldots,L-1\}^2\) is
\[
k_{i,j}=-\ell p+(p+q)i+(p-q)j.
\]
At equispaced nodes, two basis columns are identical up to their nonzero radial scalars if and only if their frequencies are congruent modulo \(M\); columns with different residues are orthogonal. Therefore
\[
\operatorname{rank}E_{\ell,M,p,q,s}=\#\{k_{i,j}\bmod M:0\le i,j<L\}.
\]
If the residues are distinct, the coefficient of \(H_{m,n}\) in an expansion \(f=\sum a_{m,n}H_{m,n}\) is recovered as
\[
a_{m,n}=\frac{1}{M\,s^{\alpha/2}(1-s)^{\beta/2}Q_{\ell,m,n}(s)}
\sum_{j=0}^{M-1} f(\gamma_{p,q,s}(2\pi j/M))e^{-2\pi i(pm+qn)j/M}.
\]

**3. Even degrees: exact Nyquist sampling.** When \(\ell\) is even, \(L\) is odd. Choose \(p=(L-1)/2\), \(q=(L+1)/2\); these are consecutive integers and thus primitive. Then
\[
k_{i,j}=-\ell p+Li-j.
\]
For successive \(i\), the \(L\) values indexed by \(j\) form consecutive, nonoverlapping integer blocks. Together they form an interval of \(L^2\) consecutive integers. Modulo \(M=L^2\) every residue appears exactly once. Thus evaluation is invertible onto \(\mathbb C^{L^2}\). No system of fewer than \(L^2\) scalar samples can be injective on a space of dimension \(L^2\).

**4. Odd degrees: an exact one-site parity obstruction.** Suppose \(\ell\) is odd and \(M=L^2\). The set \(D_\ell\) consists of \(L^2\) nonzero weights arranged in pairs \((m,n),(-m,-n)\). If an \(M\)-point cyclic sampling rule were injective, these weights would map bijectively to all residues modulo the even number \(M\). But neither self-inverse residue \(0\) nor \(M/2\) can be attained under an injective map, since the two opposite nonzero weights would then collide. Contradiction. The dimension bound excludes all smaller \(M\), proving \(M\ge L^2+1\).

For sufficiency, \(L\) is even; take \(p=1\), \(q=L\), \(M=L^2+1\). A collision would give
\[
(L+1)A-(L-1)B=rM,\qquad |A|,|B|\le L-1,
\]
where \(A,B\) are differences of indices. Since the left-hand magnitude is at most \(2L(L-1)<2M\), only \(r=0,\pm1\) are possible. When \(r=0\), \(\gcd(L-1,L+1)=1\) and the index bounds force \(A=B=0\). For \(r=1\) and \(L\ge4\), reduction modulo odd \(L-1\) gives \(A\equiv1\pmod{L-1}\), hence \(A=1\) or \(A=2-L\); substitution gives respectively \(B=-L\) and \(B=-(2L+1)\), both out of bounds. The case \(r=-1\) follows by sign symmetry. For \(L=2\), the four frequencies are \(-2,-1,1,2\), distinct modulo five. Thus there are precisely \(L^2\) distinct residues modulo \(M=L^2+1\). Since \(D_\ell\) is sign-symmetric without zero and \(M\) is odd, the missing residue must be \(0\): any other missing residue would require its distinct negative also to be missing. Hence the sample image is exactly the zero-mean hyperplane, completing the proof.

## Verification
The standalone Python 3 standard-library program `check.py` reconstructs the complete harmonic index square and proves its bounded residue properties by exact integer arithmetic through degree 199; independently it builds full finite-field Fourier sampling matrices at carefully chosen rational nonnodal radii and verifies their ranks for degrees 1 through 8. It checks each harmonic recurrence with rational arithmetic. Successful replay prints `TORUS_KNOT_INTERPOLATION_OK 199 exact residue classifications 8 independent finite-field evaluation matrix ranks`. These finite checks corroborate the analytic proof; they are not an infinite-degree certificate.

## Relationship to prior work
Optimal-dimensional sampling of spin-weighted functions on \(S^2\) by Elahi, Khalid, Kennedy and McEwen (2018), and near-optimal randomized spherical-harmonic recovery by Zandieh, Han and Avron (2022), motivate the exact acquisition-count question but concern different manifolds and sampling architectures. Nasdala and Potts (2021) give the general Fourier-separation criterion for reconstructing rank-one lattices: the congruence principle is classical, whereas the exact checkerboard harmonic weight set, sharp parity lower bound, and explicit one-trajectory count on \(S^3\) are the evaluated result. Mildenberger and Quellmalz (2023) develop torus Fourier representations for manifolds, not the present sharp cyclic one-curve interpolation theorem.

Two closely related published calculations are *Exact-degree spherical sampling on a doubly wound Clifford circle* (2026), concerning a **fixed** \((1,2)\) equal-radius curve and its generally noninjective full harmonic trace, and *Parity-sharp rectangular Hopf-grid interpolation of exact spherical harmonics* (2026), concerning **two-dimensional product grids** on a nonnodal torus. Their harmonic basis information is standard and is used here; neither stated theorem provides the sharp minimal count over all single primitive winding trajectories or the one-extra-site odd-degree construction. An implicit version in general rank-one lattice sampling theory cannot be excluded by the bounded literature inspection.

## Limitations
The statement is an exact algebraic rank/reconstruction theorem, not an assertion of uniformly bounded condition numbers. Radial amplitude factors can be small, particularly for high degrees, and the curve windings depend on degree. The exceptional radii are given by zero sets and are not individually classified. The sharpness is among equispaced samples along one closed integer-winding Hopf-torus trajectory, not among all possible sample configurations or paths. A single torus does not recover arbitrary mixed-degree bands because low-degree combinations can vanish identically upon restriction. Historical priority remains subject to unindexed or inaccessible equivalent results, and no independent mathematical audit has been performed.

## References
1. U. Elahi, Z. Khalid, R. A. Kennedy and J. D. McEwen, *An Optimal-Dimensionality Sampling for Spin-s Functions on the Sphere*, arXiv:1809.01321v1, first public 2018-09-05. https://arxiv.org/html/1809.01321v1
2. C. Gross, M. A. Iwen, L. Kämmerer and T. Volkmer, *A Deterministic Algorithm for Constructing Multiple Rank-1 Lattices of Near-Optimal Size*, arXiv:2003.09753v1, first public 2020-03-21. https://arxiv.org/abs/2003.09753
3. R. Nasdala and D. Potts, *Efficient multivariate approximation on the cube*, Numerische Mathematik 147 (2021), published online 2021-01-22. https://doi.org/10.1007/s00211-021-01177-9
4. A. Zandieh, I. Han and H. Avron, *Near Optimal Reconstruction of Spherical Harmonic Expansions*, arXiv:2202.12995v1, first public 2022-02-25. https://arxiv.org/html/2202.12995v1
5. S. Mildenberger and M. Quellmalz, *A double Fourier sphere method for d-dimensional manifolds*, arXiv:2301.06540v1, first public 2023-01-16. https://arxiv.org/abs/2301.06540
6. *Exact-degree spherical sampling on a doubly wound Clifford circle*, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-degree-spherical-sampling-on-a-doubly-wound-clifford-circl--de4a312a107d
7. *Parity-sharp rectangular Hopf-grid interpolation of exact spherical harmonics*, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-parity-sharp-rectangular-hopf-grid-interpolation-of-exact-spheri--78e042407020
