# Arbitrarily many oscillatory wave-number bands from positive multiscale Gaussian repulsion

## Finding

In the two-dimensional Gaussian density–polarization closure of interacting active Brownian particles, the number of connected wave-number intervals with complex relaxation eigenvalues has **no universal finite upper bound**, even among smooth, strictly positive, purely repulsive radial pair potentials with positive Fourier transform. Explicitly, for every integer \(K\geq1\), there is a sum of \(K\) positive Gaussian-core potentials, all with the **same positive amplitude**, and a sufficiently small but nonzero propulsion speed for which the oscillatory wave-number set has **exactly \(2K+1\) connected components**: \(2K\) bounded bands and one unbounded tail.

The assertion is an exact structural property of the specified two-field Gaussian linearization, not a prediction that this closure is quantitatively reliable at arbitrarily high wave numbers. In particular, it proves no such component count for the unclosed microscopic particle dynamics.

## Assumptions and scope

Fix mean density \(\rho>0\), translational diffusivity \(D_t>0\), rotational diffusivity \(D_r>0\), and propulsion speed \(v>0\). At a nonzero radial Fourier wave number \(q>0\), use the Gaussian density–longitudinal-polarization linearization with drift matrix

\[
M_q=\begin{pmatrix}
(D_t+\rho\widetilde V(q))q^2&\rho v\\
-vq^2/(2\rho)&D_r+D_tq^2
\end{pmatrix},
\]

where \(\widetilde V\) is the two-dimensional Fourier transform of a radial pair potential \(V\). This is the matrix of Soriani–Cameron–Markovich–Tjhung (2026), with their scalar Fourier conventions. Call a wave number *oscillatory* when the two eigenvalues of \(M_q\) form a nonreal conjugate pair. The associated density intermediate scattering function then has the decaying sinusoidal form from the same Gaussian theory.

For every \(K\geq1\), set \(R=32K\), \(q_j=R^j\), \(\ell_j=\sqrt2/q_j\), and

\[
A=\frac{eD_r}{2\pi\rho},\qquad
V(x)=A\sum_{j=0}^{K-1}\exp\left(-\frac{|x|^2}{2\ell_j^2}\right),\qquad x\in\mathbb R^2.
\]

Every coefficient is positive, \(V\) is radial and strictly positive, and \(\widetilde V(q)>0\) at all wave numbers. The theorem holds for all \(D_t>0\), with a sufficiently small positive \(v\) depending on \(K,D_r\). No claim of uniformity in \(K\), or of microscopic validity outside the closure's controlled scales, is made.

## Proof

**1. Exact oscillation criterion.** Directly from the displayed matrix, the quadratic eigenvalue discriminant is

\[
\Delta(q)=\left(D_r-\rho\widetilde V(q)q^2\right)^2-2v^2q^2.
\]

The trace and determinant of \(M_q\) are positive: its diagonal entries are positive and the product of its off-diagonal entries is negative. Thus both eigenvalues have positive real parts; they are nonreal exactly when \(\Delta(q)<0\). Define

\[
T(q)=\frac{\rho}{D_r}q^2\widetilde V(q),\quad
G(q)=\frac{1-T(q)}q,\quad P=\frac{\sqrt2v}{D_r}>0.
\]

The open oscillatory set is precisely

\[
\Omega_P=\{q>0:|G(q)|<P\}.
\]

**2. \(K\) separated peaks and valleys.** The two-dimensional Gaussian Fourier identity gives

\[
T(q)=2e\sum_{j=0}^{K-1}\left(\frac q{q_j}\right)^2
\exp\left[-\left(\frac q{q_j}\right)^2\right].
\]

The term with index \(j\) contributes exactly \(2\) at \(q=q_j\), so \(T(q_j)\geq2>1\). At each geometric midpoint \(r_j=\sqrt{q_jq_{j+1}}\), \(0\leq j<K-1\), every ratio \(q/q_i\) is either at most \(R^{-1/2}\) or at least \(R^{1/2}\). Since \(u^2e^{-u^2}\leq1/R\) for \(u\leq R^{-1/2}\), and also for \(u\geq R^{1/2}\) when \(R\geq32\), it follows that

\[
T(r_j)\leq \frac{2eK}{R}=\frac e{16}<1.
\]

Also \(T(q)\to0\) both as \(q\downarrow0\) and as \(q\to\infty\). Consequently the sign sequence of \(T-1\) is negative, positive, negative, positive, and so forth through the \(K\) peaks, finally negative at infinity. It has at least \(2K\) distinct positive zeros.

**3. There are exactly \(2K\) simple zeros.** Put \(y=q^2>0\). Then

\[
T(\sqrt y)-1=-1+\sum_{j=0}^{K-1}\frac{2e}{q_j^2}
 y\exp\left(-\frac{y}{q_j^2}\right).
\]

We use the real-exponential-polynomial zero bound: a nonzero function \(\sum_{i=1}^m e^{\lambda_i y}p_i(y)\), with distinct real \(\lambda_i\), real polynomials \(p_i\), and total order \(N=\sum_i(1+\deg p_i)\), has at most \(N-1\) real zeros, counting multiplicity. For completeness, divide by the exponential with smallest exponent and differentiate. The resulting function is another real exponential polynomial of total order at most \(N-1\) because the polynomial multiplying the smallest exponent loses one degree. By Rolle's theorem, \(z\) zeros counted with multiplicity before differentiation give at least \(z-1\) afterward. Induction on \(N\), with the single constant-exponential case as base, proves the bound. The case of an identically zero derivative is immediate.

Here the constant term has order one and each of the \(K\) distinct negative exponents has polynomial degree one, giving \(N=2K+1\). There are at most \(2K\) real zeros, counted with multiplicity. Combined with Step 2, the \(2K\) positive zeros are all simple and there are no other zeros. Since \(q\mapsto q^2\) is strictly increasing on \((0,\infty)\), the same holds for the zeros of \(G\).

**4. Small activity produces exactly \(2K+1\) components.** The \(2K\) simple zeros of the continuously differentiable \(G\) have disjoint neighborhoods in which \(G\) is strictly monotone. For all sufficiently small \(P>0\), each of these neighborhoods contains exactly one bounded interval where \(|G|<P\). On compact sets separated from these zero neighborhoods, \(|G|\) has a positive minimum, so no additional oscillatory bands appear there at sufficiently small \(P\).

Moreover, \(T(q)\) and all its derivatives decay faster than any reciprocal power as \(q\to\infty\). Therefore \(G(q)=1/q+o(q^{-2})\) and \(G'(q)=-1/q^2+o(q^{-3})\): on a fixed sufficiently distant tail, \(G\) is positive and strictly decreasing to zero. For sufficiently small \(P\), the tail contributes exactly one additional unbounded component. Near zero, \(G(q)\sim1/q\) diverges, so no extra component occurs there. There are exactly \(2K+1\) components in total. Finally set \(v=PD_r/\sqrt2>0\).

## Verification

The accompanying standalone Python program `verify_bands.py` uses only the standard library. It builds the stated positive Gaussian mixtures for \(K=1,2,3,4,5\), checks alternating peak and valley signs, bisects one root in each of the \(2K\) forced intervals, and independently compares the actual two-field matrix discriminant with the normalized oscillation inequality on multiple wave numbers. In the supplied execution it passes 97 finite arithmetic and discriminant checks. The universal \(K\)-statement and exact zero-count are established analytically in the proof, not by these finite tests.

Run using `python3 verify_bands.py`.

## Relationship to prior work

Soriani, Cameron, Markovich, and Tjhung (arXiv:2610.41613, first public October 30, 2026) derive the density–polarization closure, the eigenvalues, and a *pointwise* wave-number threshold, including a single Gaussian-core example; see their equations (33), (43), (47), and (48). The present statement takes that equation as its starting point rather than claiming a new closure. Its added structural result is an unbounded number of **disconnected oscillatory wave-number bands** produced by a physically natural positive Gaussian mixture, with an exact component count for every \(K\). The global count uses separation of interaction scales and the sharp real-zero bound, neither supplied by the pointwise formula.

Kurzthaler, Leitmann, and Franosch (arXiv:1701.03671) study the single-particle intermediate scattering function and its oscillatory regime, not the interacting Gaussian density–polarization closure with multiscale repulsions. Bickmann and Wittkowski (arXiv:1909.03369) derive interacting-active-matter field theories and analyze a motility-induced phase-separation stability boundary, but not the present oscillatory component count.

## Limitations

This theorem is only about the analytically specified Gaussian two-field closure. In particular, the unbounded far-wave-number component need not describe true microscopic scattering: neglected orientational moments, nonlinear terms, finite-range resolution, and the loss of long-wavelength validity matter. The theorem does not claim that all \(2K+1\) bands would be experimentally observable, that the nonlinear stationary state shares this topology, or that finite-particle ABPs have the same number of oscillatory modes. The result is a sharp mathematical classification/construction within the model and a caution about extrapolating its pointwise dispersion relation globally.

## References

1. A. Soriani, S. Cameron, T. Markovich, E. Tjhung, *Static and dynamic density correlations of interacting active Brownian particles*, arXiv:2610.41613v1, October 30, 2026. https://arxiv.org/pdf/2610.41613
2. C. Kurzthaler, S. Leitmann, T. Franosch, *Intermediate scattering function of an anisotropic active Brownian particle*, arXiv:1701.03671v1, January 13, 2017. https://arxiv.org/pdf/1701.03671
3. J. Bickmann, R. Wittkowski, *Predictive local field theory for interacting active Brownian spheres in two spatial dimensions*, arXiv:1909.03369v1, September 8, 2019. https://arxiv.org/pdf/1909.03369
