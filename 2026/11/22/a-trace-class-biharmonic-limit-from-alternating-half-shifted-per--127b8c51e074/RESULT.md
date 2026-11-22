# A trace-class biharmonic limit from alternating half-shifted periodic spline projections

## Finding

For every integer \(N\ge3\), let \(\mathbb T=\mathbb R/\mathbb Z\), let \(S_N\subset L^2(\mathbb T)\) be the \(N\)-dimensional space of continuous periodic functions affine on the uniform cells \([j/N,(j+1)/N]\), and let \(\widetilde S_N\) have knots shifted by exactly \(1/(2N)\). Let \(P_N\) and \(Q_N\) be their respective orthogonal \(L^2\) projections and define the positive finite-rank contraction
\[
T_N=P_NQ_NP_N.
\]
On \(S_N\), its \(N\) eigenvalues, with multiplicities, are **exactly**
\[
\mu_{k,N}=\left[\frac{|\cos(\pi k/N)|(11+\cos(2\pi k/N))}{4(2+\cos(2\pi k/N))}\right]^2,
\qquad k=0,\ldots,N-1.
\]
For even \(N\), the Nyquist mode \(k=N/2\) is itself a zero eigenvalue in \(S_N\); all vectors orthogonal to \(S_N\) are also annihilated. Here \(\mu_{0,N}=1\), all other eigenvalues are below one, and the eigenspace at one consists exactly of constants. If \(E\) is projection onto the constants, then
\[
\|T_N-E\|=\mu_{1,N}=1-\frac{\pi^4}{12N^4}+O(N^{-6}).
\]

**Critical operator limit.** For every fixed \(\tau>0\), the positive finite-rank operators
\[
T_N^{\lfloor \tau N^4\rfloor}\quad\longrightarrow\quad
\exp\!\left(-\frac{\tau}{192}\frac{d^4}{dx^4}\right)
\]
**in trace norm** on \(L^2(\mathbb T)\). The right-hand side is the periodic fourth-order heat semigroup, defined on Fourier modes by
\[
\exp\!\left(-\frac{\tau}{192}\frac{d^4}{dx^4}\right)e^{2\pi i kx}
=e^{-\tau\pi^4 k^4/12}e^{2\pi i kx}.
\]
Consequently the complete heat trace emerges from these two alternating finite-element projections:
\[
\lim_{N\to\infty}\operatorname{Tr}\bigl(T_N^{\lfloor\tau N^4\rfloor}\bigr)
=\sum_{k\in\mathbb Z} e^{-\tau\pi^4 k^4/12}.
\]
More generally, if positive integers \(m_N\) satisfy \(m_N/N^4\to0\), then \(T_N^{m_N}\to I\) strongly; if \(m_N/N^4\to\tau\in(0,\infty)\), the same trace-norm limit holds with parameter \(\tau\); and if \(m_N/N^4\to\infty\), then \(T_N^{m_N}\to E\) in trace norm. In the subcritical case, no trace-norm convergence to \(I\) is asserted (the identity is not trace class).

## Assumptions and scope

The measure on the unit circle is normalized Lebesgue measure. The spaces consist of complex or real continuous, periodic piecewise-affine functions with the stated knots; the projections are genuine orthogonal projections for the continuous \(L^2\) inner product, **not** nodal interpolation, discrete sample least squares, or positivity-preserving conditional expectations. The two knot grids are separated by half a cell. Integer powers are taken on all of \(L^2(\mathbb T)\). The trace-class limit is asserted only at positive macroscopic time. No claim of pointwise positivity of the limiting fourth-order heat kernel is made.

## Proof

**1. Hat-function Gram matrices.** Put \(h=1/N\). Let \(\phi_j\), \(j\in\mathbb Z/N\mathbb Z\), be the periodic triangular hat with value one at \(jh\), zero at its two neighboring knots, and affine between knots. Let \(\psi_j(x)=\phi_j(x-h/2)\) be the shifted hats. If \(A=(\langle\phi_j,\phi_\ell\rangle)\) and \(B=(\langle\phi_j,\psi_\ell\rangle)\), both matrices are circulant. Direct integration of products of affine pieces gives the unshifted overlaps
\[
\langle\phi_0,\phi_0\rangle=\frac{2h}{3},\qquad
\langle\phi_0,\phi_{\pm1}\rangle=\frac h6
\]
and the shifted overlaps \(23h/48\) at center separation \(h/2\) and \(h/48\) at separation \(3h/2\), with zero at larger separations. In the small cyclic cases, coefficients referring to the same residue class are added. In terms of \(z=e^{i\omega}\), the Fourier symbols, up to the harmless orientation of the cross matrix, are
\[
\alpha(\omega)=\frac h6(z^{-1}+4+z)
=\frac h3(2+\cos\omega),
\qquad
\beta(\omega)=\frac h{48}(z^{-2}+23z^{-1}+23+z).
\]
Factoring the latter Laurent polynomial yields
\[
|\beta(\omega)|=\frac h{12}|\cos(\omega/2)|(11+\cos\omega).
\]
The strictly positive matrix \(A\) is the same for both grids. Writing the synthesis maps as \(\Phi,\Psi:\mathbb C^N\to L^2(\mathbb T)\), the projectors are \(P_N=\Phi A^{-1}\Phi^*\) and \(Q_N=\Psi A^{-1}\Psi^*\). On \(S_N\), the coefficient matrix of \(T_N\) is \(A^{-1}BA^{-1}B^*\). All factors are circulant, so Fourier diagonalization gives exactly \(|\beta(2\pi k/N)|^2/\alpha(2\pi k/N)^2\), proving the eigenvalue formula without a finite-section approximation.

**2. The sharp gap.** With \(x=|\cos(\omega/2)|\in[0,1]\), the principal cosine simplifies to
\[
\gamma(\omega)=\frac{x(5+x^2)}{2(1+2x^2)}.
\]
Its derivative with respect to \(x\) is
\[
\frac{(1-x^2)(5-2x^2)}{2(1+2x^2)^2}>0\quad(0\le x<1).
\]
Hence the unique unit eigenvalue is at frequency zero, and among all nonconstant cyclic modes the largest eigenvalues are \(\mu_{1,N}=\mu_{N-1,N}\). Taylor expansion at \(\omega=0\) gives
\[
\gamma(\omega)=1-\frac{\omega^4}{384}+O(\omega^6),
\qquad
\gamma(\omega)^2=1-\frac{\omega^4}{192}+O(\omega^6).
\]
Substitution of \(\omega=2\pi/N\) yields the claimed coefficient \(\pi^4/12\). The fourth rather than second order arises from cancellation of the quadratic angular term in the two normalized spline Gram symbols.

**3. Identification of the limiting Fourier modes.** For fixed \(k\in\mathbb Z\) and \(N>2|k|\), set
\[
v_{k,N}(x)=\sum_{j=0}^{N-1}e^{2\pi i kj/N}\phi_j(x).
\]
This is precisely the periodic nodal linear interpolant of \(e_k(x)=e^{2\pi i kx}\), hence \(\|v_{k,N}-e_k\|_{L^2}=O_k(N^{-2})\). Its Fourier coefficient vector diagonalizes the coefficient matrix of \(T_N\), so \(T_Nv_{k,N}=\mu_{k,N}v_{k,N}\). Normalizing to \(u_{k,N}=v_{k,N}/\|v_{k,N}\|_2\) gives \(u_{k,N}\to e_k\) in \(L^2\). The \(u_{k,N}\), over a complete set of residues, form an orthonormal basis of \(S_N\), because the Fourier coefficient vectors are orthogonal for the circulant positive Gram matrix \(A\).

For fixed \(k\), the previous expansion gives
\[
\mu_{k,N}=1-\frac{\pi^4k^4}{12N^4}+O_k(N^{-6}).
\]
Thus if \(m_N/N^4\to\tau\in(0,\infty)\), then \(\mu_{k,N}^{m_N}\to e^{-\tau\pi^4k^4/12}\); in the subcritical and supercritical regimes, these modal limits are respectively one and \(\mathbf 1_{\{k=0\}}\). Since every \(T_N\) is a contraction, convergence on each trigonometric polynomial and density prove the stated strong limits.

**4. Upgrade to trace norm.** The normalized exact eigenvectors give, for \(m\ge1\),
\[
T_N^m=\sum_{k\in I_N}\mu_{k,N}^{m}
|u_{k,N}\rangle\langle u_{k,N}|,
\]
where \(I_N\) is any set of \(N\) consecutive integer frequency representatives centered on zero. The symbol \(\mu(\omega)=\gamma(\omega)^2\) is below one away from integral multiples of \(2\pi\), and its fourth-order expansion at zero shows that for some absolute \(c>0\),
\[
1-\mu(\omega)\ge c\,\operatorname{dist}(\omega,2\pi\mathbb Z)^4
\qquad(\omega\in\mathbb R).
\]
Indeed the ratio of the two sides is continuous and strictly positive on the punctured compact half-circle and has a positive limit at zero. From \((1-y)^m\le e^{-my}\), for sufficiently large \(N\) with \(m_N/N^4\ge\tau/2>0\),
\[
0\le\mu_{k,N}^{m_N}\le \exp(-c_\tau |k|^4)
\quad(k\in I_N)
\]
for some \(c_\tau>0\) independent of \(N\). This provides a uniformly summable tail. For each fixed \(k\), the rank-one projections \(|u_{k,N}\rangle\langle u_{k,N}|\) converge in trace norm to \(|e_k\rangle\langle e_k|\), since their trace distance is bounded by \(2\|u_{k,N}-e_k\|_2\). Split both spectral sums at \(|k|\le K\), take \(N\to\infty\) at fixed \(K\), and then let \(K\to\infty\). The tail bound proves trace-norm convergence and consequently the trace identity. If \(m_N/N^4\to\infty\), the same bound with a diverging coefficient proves convergence in trace norm to the one-dimensional constant projection \(E\). This completes all claims.

## Verification

The accompanying self-contained `check.py` computes the relevant Gram coefficients by exact rational integration of piecewise-linear hats for seven cyclic mesh sizes, independently Fourier-diagonalizes them, checks all predicted principal cosines and the small-mesh spectral identities, and tests the sharp gap and fourth-order heat-trace scaling on increasing meshes. It passed 236 assertions when run as `python3 check.py`. Finite checks are supplementary; the all-size and trace-class statements follow from the exact formulas and summable-tail argument above.

## Relationship to prior work

Antonopoulos–Dougalis (arXiv:2106.09060v1, 16 June 2021) establish Sobolev stability of a single periodic spline orthoprojector using cyclic Gram matrices, but do not study powers of a product of two **shifted** projections, an exact principal-angle spectrum, or a fourth-order semigroup limit. De Bernardi–Miglierina (2021) study variational stability of alternating projections for general convex sets, not the mesh-dependent trace-class scaling limit. The 2019 Ueda–Saito successive-projection work studies stability and error of a B-spline-based time approximation, not the alternating orthogonal projections considered here; full text was not available in the inspected material.

Relevant published calculations on the exact \(L^\infty\) norm of a **single** periodic linear-spline orthoprojector concern a different operator statistic. Likewise, the published exact Hilbert principal-angle formula for **shifted histogram conditional expectations** concerns discontinuous degree-zero ranges; its explicitly computed angles do not imply the cubic hat-overlap symbols or quartic normalized-gap cancellation above. Published periodic biharmonic resolvent studies establish fourth-order smoothing for a directly discretized squared Laplacian, not the emergence of that generator from alternating mesh projections. The general Fourier, spline-approximation, and principal-angle techniques are established prior art; no first-discovery claim is made for those tools.

## Limitations

Only uniform periodic **linear** splines and a half-cell offset are covered. Arbitrary offsets, higher degrees, nonperiodic endpoints, nonuniform meshes and nonlinear splines are not classified. The leading asymptotic norm gap and trace-norm semigroup limit are derived analytically; the checker is not an independent proof or independent audit. The precise trace-class limit could be implicit in older general spline-product approximation theorems or unindexed numerical-analysis literature. The accessible 2019 successive-projection source was limited to its abstract, but its stated method and quantities do not directly imply this theorem. The boundary \(\tau=0\) is excluded from trace-norm convergence because the limiting identity has infinite trace.

## References

1. D. C. Antonopoulos and V. A. Dougalis, *On the stability of the \(L^2\) projection and the quasiinterpolant in the space of smooth periodic splines*, arXiv:2106.09060v1, first posted 2021-06-16. https://arxiv.org/abs/2106.09060 . Full text inspected at https://www.researchgate.net/publication/352506002_On_the_stability_of_the_L2_projection_and_the_quasiinterpolant_in_the_space_of_smooth_periodic_splines .
2. C. A. De Bernardi and E. Miglierina, *A variational approach to the alternating projections method*, Journal of Global Optimization 81 (2021), 323–350, first online 2021-04-23. https://doi.org/10.1007/s10898-021-01025-y .
3. Y. Ueda and N. Saito, *Stability and error estimates for the successive-projection technique with B-splines in time*, Journal of Computational and Applied Mathematics 358 (2019), 266–278. https://doi.org/10.1016/j.cam.2019.03.026 . Abstract inspected; full paper not read.
4. *Exact endpoint norms of uniform periodic linear-spline orthoprojectors*, published mathematical finding (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-endpoint-norms-of-uniform-periodic-linear-spline-orthoproj--9499aea3bfb2 .
5. *Sharp endpoint commutator instability for translated histogram projections*, published mathematical finding (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-endpoint-commutator-instability-for-translated-histogram-p--491d3bae8ceb .
6. *Parity-split positivity thresholds for periodic biharmonic smoothing*, published mathematical finding (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-parity-split-positivity-thresholds-for-periodic-biharmonic-smoot--c19471e10093 .
