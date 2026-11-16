# Exact cubic-harmonic spectrum and a rigidity obstruction for three unequal antipodal cap pairs

## Finding
Let \(\sigma\) be probability area measure on the unit sphere \(S^2\). For any three independent thresholds \(2^{-1/2}\le c_1,c_2,c_3<1\), define the interior-disjoint antipodal cap-pair observation region
\[
\Omega_{\boldsymbol c}=\{x\in S^2:|x_1|\ge c_1\text{ or }|x_2|\ge c_2\text{ or }|x_3|\ge c_3\}.
\]
On the seven-dimensional complex space \(\mathcal H_3\) of *pure degree-three* spherical harmonics, let \(T_{\boldsymbol c}=P_3\mathbf1_{\Omega_{\boldsymbol c}}P_3\) be the spatial-concentration operator. Its complete spectrum is one explicit scalar and the eigenvalues of three explicit real symmetric two-by-two matrices, specified below. In particular, all seven eigenvalues are strictly between zero and one, and **no admissible choice of the three independent cap widths makes \(T_{\boldsymbol c}\) a scalar multiple of the identity.** Thus independently tuning all six polar-cap apertures in opposite pairs cannot produce a tight spatial sampling form for cubic spherical harmonics.

Define the following elementary polynomials of \(c\):
\[
\begin{aligned}
A(c)&=\frac1{105}-\frac{c^3}{24}+\frac{c^5}{20}-\frac{c^7}{56},\\
B_a(c)&=\frac47-3c^3+6c^5-\frac{25c^7}{7},\\
B_t(c)&=\frac47-\frac{17c}{16}+\frac{29c^3}{16}-\frac{39c^5}{16}+\frac{125c^7}{112},\\
C_a(c)&=4A(c),\\
C_t(c)&=\frac4{105}-\frac c{16}+\frac{7c^3}{48}-\frac{19c^5}{80}+\frac{13c^7}{112},\\
H(c)&=-\frac{c(1-c^2)^2(5c^2+1)}{16}.
\end{aligned}
\]
For each cyclic triple \((i,j,k)\) of \((1,2,3)\), define
\[
\begin{aligned}
\alpha&=105\sum_{h=1}^3 A(c_h),\\
u_i&=\frac74\bigl(B_a(c_i)+B_t(c_j)+B_t(c_k)\bigr),\\
w_i&=\frac{105}{4}\bigl(C_a(c_i)+C_t(c_j)+C_t(c_k)\bigr),\\
v_i&=\frac{\sqrt{735}}4\bigl(H(c_j)-H(c_k)\bigr).
\end{aligned}
\]
Then the entire seven-element eigenvalue multiset (including accidental coincidences) is
\[
\boxed{\left\{\alpha\right\}\ \cup\ \bigcup_{i=1}^3
\left\{\frac{u_i+w_i+\sqrt{(u_i-w_i)^2+4v_i^2}}2,\ 
\frac{u_i+w_i-\sqrt{(u_i-w_i)^2+4v_i^2}}2\right\}.}
\]
Consequently, for every nonzero \(f\in\mathcal H_3\), its observed-energy fraction lies sharply between the least and greatest values in this explicit multiset. The optimizer spaces are exactly the corresponding eigenspaces of the displayed blocks, including their direct sums at eigenvalue coincidences. The operator trace is \(7\sum_{i=1}^3(1-c_i)\).

## Assumptions and scope
All norms and inner products use \(d\sigma=dA/(4\pi)\). The three pairs each have equal positive and negative cap thresholds, but the thresholds for different coordinate axes are independent. At the endpoint \(2^{-1/2}\), two caps may touch along boundaries of zero measure. Each \(c_i<1\) guarantees the observed region contains open sets. Spherical harmonics are restrictions of homogeneous harmonic cubics, not the sum of degrees zero through three. The exact spectral formulas also describe coincidence multiplicities; no general simplicity is asserted.

## Proof
**1. Orthogonal harmonic basis and parity sectors.** Set \(r^2=x_1^2+x_2^2+x_3^2\). The following homogeneous cubics are harmonic under the Euclidean Laplacian:
\[
q_0=x_1x_2x_3,\quad b_i=x_i(5x_i^2-3r^2),\quad d_i=x_i(x_j^2-x_k^2),
\]
where \((i,j,k)\) runs cyclically. Their full-sphere squared norms are \(1/105\), \(4/7\), and \(4/105\), respectively. All seven are pairwise orthogonal on the sphere, so the normalized vectors
\[
\sqrt{105}q_0,\qquad \frac{\sqrt7}{2}b_i,\qquad \frac{\sqrt{105}}2d_i
\]
form an orthonormal basis of \(\mathcal H_3\). Every cap-pair mask remains invariant under independent coordinate sign changes. Thus \(q_0\) has its own one-dimensional parity sector, while \((b_i,d_i)\) form one two-dimensional parity sector for each coordinate index \(i\). All cross-sector Gram entries vanish *for arbitrary unequal thresholds*, not just equal ones.

**2. Exact one-cap moments.** In the cap \(|x_i|\ge c\), use \(x_i=t\), \(x_j=\sqrt{1-t^2}\cos\phi\), \(x_k=\sqrt{1-t^2}\sin\phi\). Normalized integration over both signs gives \(\int_c^1\langle\cdot\rangle_\phi\,dt\). The relevant circular averages are
\[
\begin{aligned}
\langle q_0^2\rangle&=\frac{t^2(1-t^2)^2}{8},\\
\langle b_i^2\rangle_{\text{axis }i}&=t^2(5t^2-3)^2,\\
\langle b_i^2\rangle_{\text{axis }j}&=\frac{(1-t^2)(125t^4-70t^2+17)}{16},\\
\langle d_i^2\rangle_{\text{axis }i}&=\frac{t^2(1-t^2)^2}{2},\\
\langle d_i^2\rangle_{\text{axis }j}&=\frac{(1-t^2)(13t^4-6t^2+1)}{16},\\
\langle b_i d_i\rangle_{\text{axis }j}&=-\frac{(1-t^2)(35t^4-10t^2-1)}{16}.
\end{aligned}
\]
For the last mixed moment the cap on axis \(k\) has the opposite sign, and the cap on axis \(i\) gives zero. These circular averages follow term-by-term from
\[
\langle\cos^{2a}\phi\sin^{2b}\phi\rangle_\phi=\frac{(2a)!(2b)!}{4^{a+b}a!b!(a+b)!},
\]
while averages containing an odd power vanish. Integrating the six rows from \(c\) to \(1\) gives exactly the polynomial functions \(A,B_a,B_t,C_a,C_t,H\) stated above. Normalizing by the squared norms produces the one-by-one block \(\alpha\) and the three matrices
\[
M_i=\begin{pmatrix}u_i&v_i\\v_i&w_i\end{pmatrix}.
\]
Their characteristic equations give the displayed seven eigenvalues with no numerical approximation. Their trace sums to \(7\sigma(\Omega_{\boldsymbol c})=7\sum_i(1-c_i)\), also following from the spherical-harmonic addition theorem.

**3. Rigidity of failure of tightness.** Direct differentiation gives
\[
H'(c)=\frac{(1-c^2)(35c^4-10c^2-1)}{16}>0
\quad(2^{-1/2}\le c<1),
\]
since, for \(s=c^2\in[1/2,1)\), the polynomial \(35s^2-10s-1\) is increasing and at least \(11/4\). If \(T_{\boldsymbol c}\) were scalar, the off-diagonal entry \(v_i\) of every block would vanish, giving \(H(c_1)=H(c_2)=H(c_3)\). Strict monotonicity forces \(c_1=c_2=c_3=c\).

For equal \(c\), the \(q_0\)-sector eigenvalue and the \(b_i\)-sector eigenvalue have difference
\[
\lambda_{q_0}(c)-\lambda_b(c)=\frac{7c(1-c^2)}{32}(15c^4-48c^2+17)<0.
\]
Indeed \(15s^2-48s+17\) is negative at \(s=1/2\) and strictly decreasing for \(s\in[1/2,1]\). Therefore the equal-aperture operator is not scalar either, proving the obstruction in the whole three-parameter domain. All concentration eigenvalues are strictly positive because a nonzero real-analytic spherical harmonic cannot vanish on a nonempty open observed cap; they are strictly below one because the unobserved region also contains an open set when each \(c_i\ge2^{-1/2}\).

## Verification
Run `python verify_unequal.py` with the `requirements.txt` dependencies from this package. The checker constructs all seven harmonic polynomials and evaluates all 28 distinct full-sphere and three-cap Gram pairings by exact rational polar-coordinate integration. It reproduces every block entry and trace identity, verifies the mixed-moment derivative and the equal-radius polynomial gap, and independently computes the full normalized seven-by-seven Gram matrices by Gauss–Legendre and angular quadrature for four unequal-threshold triples. The largest observed entrywise difference was \(1.45\times10^{-15}\). The exact algebraic identities support all admissible real thresholds; finite quadrature is only a cross-check. No external proof assistant or independent audit is claimed.

## Relationship to prior work
Roddy and McEwen (arXiv:2302.06006v1, first public 2023-02-12) develop Slepian wavelets on partially observed manifolds; their general concentration framework motivates exact spatial masks but does not state this three-parameter harmonic spectrum or prove the obstruction to tightness. Simons, Dahlen and Wieczorek (arXiv:math/0408424) formulated the general spherical Slepian matrix eigenproblem, not these explicit anisotropic eigenvalues.

Closer exact harmonic results already identify the three symmetry sectors for **equal** coordinate-axis cap apertures in all dimensions, and give an exact mode transition in dimension three. That equal-radius theorem includes the specialization \(c_1=c_2=c_3\) of the present formulas; the equal-radius spectral result and its transition are not asserted as new. A separate, later-degree exact treatment gives four sectors for degree-four harmonics on the same six equal caps, and a tetrahedrally centered degree-three cap theorem addresses a different region. None of these statements determines the off-diagonal mixing terms for unequal apertures, their exact three-parameter eigenvalues, or the proof that isotropy cannot be restored by independently tuning the three cap widths. The polynomial expressions are elementary but the simultaneous scalar-rigidity assertion requires the signed-coordinate pairing and strict-moment injectivity, not a substitution in the symmetric spectra.

## Limitations
The mask consists of three antipodal pairs with individually variable but pairwise symmetric apertures; the threshold lower bound prevents overlap. Arbitrarily oriented, differently weighted, overlapping or non-antipodal caps are not covered. This theorem supplies exact spectral evaluation and an impossibility result, not the globally smallest attainable condition number among unequal masks. The earlier general equal-cap harmonic decomposition greatly simplifies this calculation, and specialist unpublished or unindexed equivalent computations remain a historical priority risk. No independent mathematical audit has yet occurred.

## References
1. P. J. Roddy and J. D. McEwen, *Slepian Scale-Discretised Wavelets on Manifolds*, arXiv:2302.06006v1 (first submitted 2023-02-12), https://arxiv.org/html/2302.06006v2.
2. F. J. Simons, F. A. Dahlen and M. A. Wieczorek, *Spatiospectral concentration on a sphere*, arXiv:math/0408424v1 (2004-08-31), https://arxiv.org/abs/math/0408424.
3. V. Michel, A. Plattner and K. Seibert, *A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator*, arXiv:2103.14650v1 (2021-03-26), https://arxiv.org/abs/2103.14650.
