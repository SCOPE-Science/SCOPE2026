# Exact disorder crossover and minimal correlation length in the one-dimensional maximal hard-core gas

## Finding

Consider the nearest-neighbor maximal hard-core gas on the cycle \(C_N\), with \(N\ge3\), in which every maximal independent set \(I\) carries weight \(z^{|I|}\), for activity \(z>0\). Let \(\eta_j\in\{0,1\}\) denote occupancy at site \(j\), and let \(\langle\cdot\rangle_z\) be the unique infinite-volume, translation-invariant Gibbs limit of these cycle measures. Define the connected covariance \(C_z(r)=\langle\eta_0\eta_r\rangle_z-\langle\eta_0\rangle_z^2\) and its exponential correlation length by

\[
\xi(z)^{-1}=-\limsup_{r\to\infty}\frac1r\log|C_z(r)|.
\]

For every \(z>0\), the positive number \(\lambda=\lambda(z)\) is uniquely defined by \(\lambda^3=z(\lambda+1)\). Set \(z_c=27/4\), which is equivalent to \(\lambda=3\). Then

\[
\xi(z)=\begin{cases}
\displaystyle \frac{2}{\log(1+\lambda)},&0<z\le z_c,\\[5pt]
\displaystyle \frac{1}{\log\!\left(\frac{2}{1+\sqrt{(\lambda-3)/(\lambda+1)}}\right)},&z\ge z_c.
\end{cases}
\]

The two formulae agree at \(z_c\). The function \(\xi(z)\) is strictly decreasing on \((0,z_c)\), strictly increasing on \((z_c,\infty)\), and attains its **unique global minimum** \(\xi(z_c)=1/\log2\).

For \(0<z<z_c\), the dominant subleading poles form a complex-conjugate pair; density correlations are damped oscillations with wave number \(q(z)=\arccos(-\sqrt{1+\lambda}/2)\), progressing from the three-site wave number \(2\pi/3\) to \(\pi\). For \(z>z_c\), the leading subdominant root is simple, negative and real, so correlations are asymptotically alternating. Exactly at the crossover,

\[
\boxed{C_{z_c}(r)=\frac{4(3r+5)}{81}\left(-\frac12\right)^r\quad\text{for all integers }r\ge0.}
\]

The extra linear factor in \(r\) is caused by a defective double transfer eigenvalue; this is an **oscillatory-to-staggered disorder crossover**, not a thermodynamic phase transition. Moreover \(\xi(z)\sim2z^{-1/3}\) as \(z\downarrow0\), while \(\xi(z)\sim z^{1/2}\) as \(z\to\infty\).

## Assumptions and scope

The graph \(C_N\) has vertices \(\mathbb Z/N\mathbb Z\) and nearest-neighbor edges. A configuration is allowed exactly when its cyclic binary word avoids adjacent \(11\) and avoids three consecutive \(000\): the former is independence; the latter is maximality. The probability of an allowed word is its weight \(z^{\sum_j\eta_j}\) divided by \(Z_N(z)\). All assertions concern fixed \(z>0\) followed by \(N\to\infty\), and then separations \(r\to\infty\) where specified. No boundary condition or complex activity is being asserted.

## Proof

**1. Transfer and uniqueness.** In the ordered pair-state basis \((00,01,10)\), the matrix recording a newly appended occupied symbol with factor \(z\) is

\[
T(z)=\begin{pmatrix}0&z&0\\0&0&1\\1&z&0\end{pmatrix},\quad
Z_N(z)=\operatorname{tr}T(z)^N,\quad
\det(\lambda I-T)=\lambda^3-z\lambda-z.
\]

The two directed cycles through \(01\) have lengths two and three, so for \(z>0\) this nonnegative matrix is primitive. Perron–Frobenius therefore supplies a unique positive Perron root \(\lambda\) and a unique translation-invariant thermodynamic limit. Since \(z=\lambda^3/(1+\lambda)\) is strictly increasing in \(\lambda>0\), \(\lambda(z)\) is unique and strictly increasing. The pressure \(\log\lambda(z)\) is analytic at all positive activities.

**2. Renewal description and actual covariance poles.** The successive occupied sites are separated by independently sampled gaps of length two or three under the limiting Gibbs law, with probabilities

\[
p_2=\frac{z}{\lambda^2}=\frac{\lambda}{1+\lambda},\qquad
p_3=\frac{z}{\lambda^3}=\frac1{1+\lambda}.
\]

Their mean gap gives the density \(\rho=(1+\lambda)/(3+2\lambda)\). Conditional on occupancy at zero, let \(u_r\) be the probability of occupancy at distance \(r\), with \(u_0=1\). The renewal identity gives

\[
U(s)=\sum_{r\ge0}u_rs^r=\frac1{1-p_2s^2-p_3s^3},\qquad C_z(r)=\rho(u_r-\rho).
\]

The denominator has three poles, corresponding to the three roots \(\lambda,\mu_1,\mu_2\) of the transfer characteristic cubic, at \(s=\lambda/\lambda=1,\lambda/\mu_1,\lambda/\mu_2\). As the numerator is identically one, every non-Perron simple pole is present with a nonzero residue. At a repeated non-Perron pole, its order is exactly two. Hence the dominant subleading root modulus determines the limsup decay rate even in an oscillatory regime.

**3. Exact crossover and uniqueness of the minimum.** The cubic discriminant is \(z^2(4z-27)\). When \(0<z<27/4\), the two other roots are conjugate, with real part \(-\lambda/2\), modulus \(\lambda/\sqrt{1+\lambda}\), and angle \(q=\arccos(-\sqrt{1+\lambda}/2)\). Thus their modulus relative to the Perron root is \(R=(1+\lambda)^{-1/2}\), strictly decreasing from one to one half.

When \(z>27/4\), write \(d=\sqrt{(\lambda-3)/(\lambda+1)}\). The two negative roots are \(-\lambda(1\pm d)/2\), and the larger absolute-value ratio is \(R=(1+d)/2\), strictly increasing from one half toward one. The correlation length is \(1/(-\log R)\), proving both monotonicity claims and uniqueness of its minimum.

At \(z=27/4\), the roots are \(3,-3/2,-3/2\). The matrix has a one-dimensional eigenspace at \(-3/2\), and the renewal denominator factors as \((1-s)(1+s/2)^2\). Its exact partial fractions are

\[
U(s)=\frac{4/9}{1-s}+\frac{2/9}{1+s/2}+\frac{1/3}{(1+s/2)^2}.
\]

The coefficient of \(s^r\) is \(u_r=4/9+(3r+5)(-1/2)^r/9\). Multiplication by \(\rho=4/9\) proves the boxed covariance formula for every \(r\ge0\).

**4. Endpoint scales.** As \(z\downarrow0\), \(\lambda\sim z^{1/3}\), giving \(\xi\sim 2z^{-1/3}\). As \(z\to\infty\), \(\lambda\sim z^{1/2}\) and \(d=1-2/\lambda+O(\lambda^{-2})\), giving \(\xi\sim z^{1/2}\). These are distinct density-ordering length scales, with no finite-activity singularity in the pressure.

## Verification

The accompanying `verify.py` uses exact symbolic identities to check the cubic discriminant, its defective critical eigenvalue, and the rational-function partial fractions. It exhaustively enumerates all cyclic occupancy words for each length from three through fourteen and checks their weighted partition polynomials against \(\operatorname{tr}T^N\). At the critical activity it checks eighty-one exact covariance coefficients from the recurrence; finite numerical checks test the spectral branches and endpoint approximations. Running `python verify.py` prints `VERIFY_OK`. The universal claims follow from the preceding proof, not from the finite tests.

## Relationship to prior work

Barg, He and Wang (2026) define maximal hard-core models, prove a contour-expansion crystallization framework, and analyze nearest-neighbor examples in dimensions at least two. In particular, their model and examples sections distinguish low-activity and high-activity order; they do not state the present one-dimensional finite-fugacity correlation crossover or its exact double-pole law. Earlier work of Wang, Barg and Kashyap treats square-lattice and triangular-lattice maximal hard-core Gibbs measures, not the one-dimensional correlation length. Independently of those crystallization results, the transfer and renewal construction here resolves the one-dimensional crossover exactly. Related classical Fisher–Widom transitions in other finite-range lattice gases are conceptually analogous but do not by themselves imply the exact activity or the specific critical covariance for this maximality constraint.

## Limitations

This theorem is only for the single-species nearest-neighbor maximal hard-core gas on a one-dimensional cycle in its infinite-volume limit and positive real activity. It is not a claim of multiple positive-activity Gibbs phases; indeed the pressure is analytic for all positive activity. The exact disorder threshold concerns the asymptotic correlation mode, not a jump in a thermodynamic observable. Other constrained-shift or lattice-gas literature might contain an equivalent spectral criterion not indexed under the model's current name; that remains a literature-priority uncertainty. The proof does not imply a quantitative phase boundary for higher-dimensional maximal hard-core systems.

## References

1. A. Barg, Q. He and G. Wang, *A general framework for crystallization in maximal hard-core models*, arXiv:2610.11042, first posted 2026-10-08. https://arxiv.org/abs/2610.11042 . Full text consulted via https://www.paperpeel.com/paper/2610.11042 .
2. G. Wang, A. Barg and N. Kashyap, *The maximal hard-core model as a recoverable system: Gibbs measures and phase coexistence*, arXiv:2510.19746, first posted 2025-10-22. https://arxiv.org/abs/2510.19746 .
3. G. Wang, A. Barg and N. Kashyap, *Recoverable systems and the maximal hard-core model on the triangular lattice*, arXiv:2602.18310, first posted 2026-02-20. https://arxiv.org/abs/2602.18310 .
