# Exact angular resonances and minimal two-meridian sampling of pure spherical harmonics

## Finding

Let \(\ell\ge 1\) be an integer. Write \(\mathcal H_\ell(S^2;\mathbb C)\) for complex spherical harmonics of pure degree \(\ell\), of complex dimension \(2\ell+1\). Fix an azimuthal separation \(0<\theta<\pi\). Define \(s_j=\pi j/(\ell+1)\) for \(0\le j\le\ell\), and points
\[
\gamma_\phi(s)=(\sin s\cos\phi,\sin s\sin\phi,\cos s)\in S^2.
\]
Sample every \(f\in\mathcal H_\ell\) at the \(\ell+1\) points \(\gamma_0(s_j)\), \(0\le j\le\ell\), and the \(\ell\) additional points \(\gamma_\theta(s_j)\), \(1\le j\le\ell\). These \(2\ell+1\) points are pairwise distinct. Let \(E_{\ell,\theta}\) denote the resulting complex linear evaluation map.

**Exact rank and blind modes.** Its nullity is
\[
\dim_\mathbb C\ker E_{\ell,\theta}=\#\{m\in\{1,\ldots,\ell\}:\sin(m\theta)=0\}.
\]
If \(\theta/\pi=p/q\) in lowest terms, with \(q\ge2\), the nullity is exactly \(\lfloor\ell/q\rfloor\); for irrational \(\theta/\pi\), it is zero. When rational, a basis of the nullspace consists of the functions
\[
P_\ell^{jq}(\cos s)\sin(jq\phi),\qquad 1\le j\le\lfloor\ell/q\rfloor,
\]
where \(P_\ell^m\) is the associated Legendre function with the convention below. In particular, the explicitly specified \(2\ell+1\) samples reconstruct every pure degree-\(\ell\) spherical harmonic exactly if and only if the reduced denominator of \(\theta/\pi\) exceeds \(\ell\), or that ratio is irrational. The cardinality is then minimal for *complex linear* recovery of arbitrary coefficients in this space.

**Exact sampling determinant.** Use the ordered harmonic basis
\[
\big(P_\ell^m(\cos s)\cos(m\phi)\big)_{m=0}^{\ell}
\quad\text{followed by}\quad
\big(P_\ell^m(\cos s)\sin(m\phi)\big)_{m=1}^{\ell}.
\]
Let \(M_\ell(\theta)\) be the square sample matrix in that basis and the stated row order. Set
\[
 A_{jm}=P_\ell^m(\cos s_j)\ (0\le j,m\le\ell),\qquad
 B_{jm}=P_\ell^m(\cos s_j)\ (1\le j,m\le\ell).
\]
Both \(A\) and \(B\) are nonsingular, and the exact factorization, with no missing angular prefactor, is
\[
\boxed{\det M_\ell(\theta)=\det A\,\det B\prod_{m=1}^{\ell}\sin(m\theta).}
\]
Every rational resonance has determinant vanishing order exactly \(\lfloor\ell/q\rfloor\). At a fixed resonance, exactly that many singular values of the sampling matrix vanish *linearly* with angular perturbation; the others remain bounded away from zero. The full-circle joint trace operator has the same nullspace as this finite sample map.

## Assumptions and scope

All assertions concern complex-valued **pure degree** spherical harmonics on the standard unit two-sphere, not the cumulative space of degrees at most \(\ell\). The planes through the polar axis at azimuths \(0\) and \(\theta\) are distinct because \(0<\theta<\pi\). The ratio \(\theta/\pi\) has reduced denominator \(q\) when rational. Define the Legendre polynomial \(P_\ell(t)\) by Rodrigues' formula, and
\[
P_\ell^m(t)=(-1)^m(1-t^2)^{m/2}\frac{d^m}{dt^m}P_\ell(t),\qquad 0\le m\le\ell.
\]
This fixes the determinant normalization. We use non-normalized real angular factors even though the coefficient space and linear map are complex.

## Proof

**(1) Basis and meridian Fourier sampling.** Separation of variables gives the displayed \(2\ell+1\) independent harmonic basis functions. More explicitly, as \(s\downarrow0\),
\[
P_\ell^m(\cos s)=c_{\ell,m}s^m+O(s^{m+2}),\qquad c_{\ell,m}\ne0,
\]
where nonvanishing follows from the explicit positive value of the \(m\)-th Legendre derivative at \(1\). Consequently the functions \(P_\ell^m(\cos s)\), for distinct \(m\), are linearly independent. Restricted to any fixed complete meridian, a homogeneous degree-\(\ell\) harmonic polynomial is a trigonometric polynomial in arclength \(s\) with frequencies exactly in \(\{\ell,\ell-2,\ldots,-\ell\}\). The corresponding space has dimension \(\ell+1\), and the \(\ell+1\) nodes \(s_j\) are unisolvent: after factoring out \(e^{i\ell s_j}\), the evaluation matrix is the discrete Fourier transform of order \(\ell+1\). Hence \(A\) is nonsingular.

The \(\ell\) functions \(P_\ell^m(\cos s)\) with \(1\le m\le\ell\) all vanish at \(s_0=0\), remain linearly independent, and belong to the same meridian trace space. If a combination vanished at every \(s_j\) with \(1\le j\le\ell\), it would vanish at all \(\ell+1\) Fourier nodes, and hence identically. Thus \(B\) is also nonsingular.

**(2) Exact factorization.** The first \(\ell+1\) rows of \(M_\ell(\theta)\) have block form \((A\ \ 0)\). The final \(\ell\) rows have block form
\[
\left(C_\theta\quad B\,\operatorname{diag}(\sin\theta,\sin2\theta,\ldots,\sin(\ell\theta))\right),
\]
where \((C_\theta)_{jm}=P_\ell^m(\cos s_j)\cos(m\theta)\) for \(1\le j\le\ell\), \(0\le m\le\ell\). This is an exact block triangular identity, so taking determinants proves the factorization. Because both diagonal blocks outside the sine factor are nonsingular, taking kernels gives the stated basis and nullity.

**(3) Arithmetic and minimality.** For rational \(\theta/\pi=p/q\) in lowest terms, \(\sin(m\theta)=0\) exactly when \(q\) divides \(m\), giving \(\lfloor\ell/q\rfloor\). Irrational angles have no such integer \(m\). A complex vector space of dimension \(2\ell+1\) cannot be recovered by fewer scalar complex-linear measurements. Thus the given unisolvent design is cardinal-minimal.

**(4) Complete trace and transition order.** On each meridian, the Fourier-node argument proves that vanishing at the stated nodes is equivalent to vanishing on the whole corresponding great circle; the shared north-pole value handles the missing second-meridian node. Hence the finite map and complete joint trace have the same nullspace. At rational \(\theta_0/\pi=p/q\), every resonant sine factor has a simple zero in \(\theta\) and each other factor is nonzero, giving total determinant order \(\lfloor\ell/q\rfloor\). Subtracting \(C_\theta A^{-1}\) times the top block and using the invertible fixed blocks \(A,B\) shows that, near \(\theta_0\), the singular values are comparable to those of the diagonal sine matrix together with \(\ell+1\) unit entries. Thus exactly \(\lfloor\ell/q\rfloor\) singular values vanish linearly and the remaining ones have positive limits.

## Verification

The supplied `verify.py` uses the explicit associated Legendre basis and evaluates both sides of the determinant factorization, as well as numerical ranks at rational and irrational angles, for degrees one through eight. It reports `TWO_MERIDIAN_TRACE_CHECK_PASS checks=98 degrees=1..8`. It requires Python 3, NumPy and SciPy. These floating-point computations are corroborating finite checks only; the proof above establishes the statements for every positive integer degree and every permitted angle. No computer algebra or numerical tolerance is used in the universal proof.

## Relationship to prior work

The 2004 paper of zu Castell, Laín Fernández and Xu develops unisolvent spherical-polynomial configurations on multiple **latitude** circles for the cumulative degree-at-most space of dimension \((n+1)^2\); its factorization methods do not give this two-meridian, pure-harmonic arithmetic resonance theorem. General nonuniform spherical harmonic transforms, including recent full-text methods using meridian doubling, address rapid evaluation on arbitrary spatial samples rather than the exact rank and determinant of this cardinal-minimal two-meridian sampling scheme. Spherical Slepian work motivates sparse or geographically incomplete spherical observation; the present calculation addresses a specific exact, lower-dimensional interpolation geometry instead of concentration eigenfunctions. Gichev's null-cone and nodal-set determinant representations address different constraints and do not state the two-meridian evaluation determinant. Low-degree trace results are compatible with the degree-two and degree-three special cases of the formula.

## Limitations

This is a result for one *known pure degree* and for two meridians sharing a polar axis. It does not establish reconstruction of unknown mixtures of degrees, stability uniformly in \(\ell\), optimal conditioning among all node placements, or any sharp bound independent of distance to the nearest resonance. An exact angular factorization may have a more general representation-theoretic predecessor; priority beyond the inspected literature remains open to independent review.

## References

1. W. zu Castell, N. Laín Fernández and Y. Xu, *Polynomial Interpolation on the Unit Sphere II*, arXiv:math/0407448 (first posted 2004-07-27), especially Sections 1–3.
2. P. J. Roddy and J. D. McEwen, *Slepian Scale-Discretised Wavelets on the Sphere*, arXiv:2106.02023 (first posted 2021-06-03).
3. *cunuSHT: GPU accelerated spherical harmonic transforms on arbitrary pixelizations*, RAS Techniques and Instruments, DOI:10.1093/rasti/rzae045 (2024), especially Section 2 on spherical harmonic synthesis and the double Fourier sphere construction.
4. V. M. Gichev, *Some remarks on spherical harmonics*, arXiv:0705.2547 (first posted 2007-05-17), especially Sections 1–2 on nodal-set and determinant representations.
5. Y. Xu, *Polynomial Interpolation on the Unit Sphere*, SIAM Journal on Numerical Analysis 41 (2003), 751–766, DOI:10.1137/S003614290139946X.
