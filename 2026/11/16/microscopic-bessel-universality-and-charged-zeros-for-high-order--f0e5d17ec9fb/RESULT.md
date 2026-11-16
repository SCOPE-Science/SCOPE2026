# Microscopic Bessel universality and charged zeros for high-order Hermite spectrograms

## Finding
Let \(\xi_k\) be independent standard circular complex Gaussians, let
\[
G(z)=\sum_{k\ge 0}\frac{\xi_k z^k}{\sqrt{k!}},\qquad
f_n(z,\bar z)=\frac{1}{\sqrt{n!}}(\partial_z-\bar z)^nG(z),\qquad
X_n(u)=e^{-|u|^2/(2n)}f_n(u/\sqrt n,\bar u/\sqrt n)
\]
for integers \(n\ge1\). These are normalized white-noise Hermite-window spectrogram fields in the Fock-coordinate normalization; their zero sets coincide with those of the corresponding STFTs after the usual fixed linear conversion of coordinates.

Write \(t=|u-v|^2\), \(\omega=\operatorname{Im}(u\bar v)\), and \(H(t)=J_0(2\sqrt t)\), with \(H(0)=1\). For every \(R>0\) and every nonnegative integer \(s\), the following expansion holds uniformly for \(|u|,|v|\le R\), including every real mixed partial derivative of total order at most \(s\):
\[
\boxed{\mathbb E\,[X_n(u)\overline{X_n(v)}]
=H(t)+\frac1n\left[\frac t2H'(t)+i\omega H(t)\right]
+O_{R,s}(n^{-2}).}
\]
The pseudocovariance \(\mathbb E[X_n(u)X_n(v)]\) vanishes identically. Consequently, for each finite \(s\), the fields \(X_n\) converge in distribution in \(C^s_{\mathrm{loc}}(\mathbb R^2;\mathbb C)\) to the **proper complex monochromatic Gaussian random wave** \(W\) with
\[
\mathbb E[W(u)\overline{W(v)}]=J_0(2|u-v|),\quad
\mathbb E[W(u)W(v)]=0,\quad (\Delta+4)W=0\quad\text{almost surely}.
\]

Each zero is assigned its local topological charge \(\operatorname{sgn}\det D(\Re X_n,\Im X_n)\). The joint counting measures of positive and negative zeros of \(X_n\) converge **in distribution, vaguely on \(\mathbb R^2\)** to the corresponding charged zero measures of \(W\). Their exactly constant one-point intensities (with respect to Lebesgue area in the \(u\)-plane) are
\[
\boxed{\rho_{n,\pm}=\frac{n+\frac12+\frac1{4n+2}\pm1}{2\pi n},\qquad
\rho_{n,+}-\rho_{n,-}=\frac1{\pi n}.}
\]
In the limit the two intensities are equal, each \(1/(2\pi)\). The \(n^{-1}\) phase term of the kernel records the residual magnetic twist, while the limiting zeros are those of a genuinely translation-invariant Helmholtz random wave.

## Assumptions and scope
All statements concern a fixed compact spatial window in the microscopically rescaled variable \(u\), with \(n\to\infty\). Complex Gaussian means \(\mathbb E|\xi_k|^2=1\) and \(\mathbb E\xi_k^2=0\). The field \(G\) is almost surely entire, hence every \(f_n\) is real analytic. The topological charge is defined at regular zeros and agrees with the sign of \(|\partial_z f|^2-|\partial_{\bar z}f|^2\). No joint convergence in the Hermite index, no global unscaled-window result, and no quantitative convergence rate for the point process is asserted.

## Proof
**1. Exact covariance.** The standard pure polyanalytic Fock reproducing-kernel identity (and proper complex Gaussianity) gives
\[
K_n(u,v):=\mathbb E[X_n(u)\overline{X_n(v)}]
=e^{i\omega/n}\,e^{-t/(2n)}L_n(t/n),
\qquad L_n(x)=\sum_{k=0}^{n}(-1)^k\binom nk\frac{x^k}{k!}.
\]
All phases and lengths here are in the Fock-coordinate convention, not the physical STFT convention with \(\pi\)-factors. This identity fixes the normalization \(K_n(u,u)=1\).

**2. A two-term uniform Mehler--Heine expansion.** Put
\[
a_{n,k}=\begin{cases}\prod_{j=0}^{k-1}(1-j/n),&0\le k\le n,\\0,&k>n.\end{cases}
\qquad S_{n,k}=\frac{k(k-1)}{2n}.
\]
Bonferroni's product inequalities imply \(0\le a_{n,k}-1+S_{n,k}\le S_{n,k}^2/2\) for \(k\le n\). The same inequality holds for \(k>n\), since then \(S_{n,k}\ge1\) and \(a_{n,k}=0\). Therefore
\[
L_n(t/n)=\sum_{k\ge0}\frac{(-t)^k}{(k!)^2}a_{n,k}
=H(t)-\frac{t^2}{2n}H''(t)+O_{T,s}(n^{-2})
\]
uniformly with any fixed number of \(t\)-derivatives on compact \(t\)-sets. Indeed, after differentiation the remainder is bounded by \(Cn^{-2}\sum_{k\ge0}k^{4+s}T^{\max(k-s,0)}/(k!)^2\), which converges. The series \(H(t)=\sum_{k\ge0}(-t)^k/(k!)^2=J_0(2\sqrt t)\) satisfies \(tH''+H'+H=0\), including at \(t=0\) by its power series. Hence, after multiplying by \(e^{-t/(2n)}e^{i\omega/n}\), the order-\(n^{-1}\) real correction simplifies from \(-[tH+t^2H'']/2\) to \(tH'/2\). The same uniform estimate applies to real derivatives of \(u,v\) of each prescribed finite order, proving the displayed covariance expansion.

**3. Gaussian field limit.** The proper complex Gaussian laws are determined by covariance and zero pseudocovariance. The limit kernel has the representation
\[
H(|u-v|^2)=\frac1{2\pi}\int_0^{2\pi}e^{2i(u-v)\cdot(\cos\theta,\sin\theta)}\,d\theta.
\]
It therefore defines a proper complex stationary isotropic Gaussian field \(W\) with smooth sample paths and \((\Delta+4)W=0\). Differentiating the uniformly convergent covariances gives convergence of every finite collection of field derivatives. Uniform derivative variance bounds, and bounds on their increments obtained by one additional derivative, give Gaussian moment estimates of every order. The two-dimensional Kolmogorov--Chentsov criterion and compact embeddings give tightness in \(C^s\) on compact rectangles for each fixed \(s\). This proves \(X_n\Rightarrow W\) in \(C^s_{\mathrm{loc}}\).

**4. Charged-zero continuity.** For each fixed \(n\), and for \(W\), the random value at each point is a nondegenerate circular complex Gaussian of variance one. Hence its real two-dimensional density is uniformly bounded by \(1/\pi\). The vector-valued Bulinskaya lemma applies to these almost surely smooth fields: all their zeros are regular almost surely. Regular zero configurations are locally finite. Under \(C^1\) convergence, the inverse function theorem and compactness match the zeros in every compact region with zero-free boundary, with their Jacobian signs preserved. A deterministic boundary has zero expected zero count because the one-point densities are locally bounded; a countable family of such boundaries suffices. The continuous-mapping theorem thus proves joint vague convergence of the positive and negative zero point measures.

**5. Exact intensity and charge.** At the origin, \(f_n(0)=\xi_n\), \(\partial_z f_n(0)=\sqrt{n+1}\,\xi_{n+1}\), and \(\partial_{\bar z}f_n(0)=-\sqrt n\,\xi_{n-1}\), with the last two independent of the value. After \(u=z\sqrt n\), the Jacobian of the complex field at a zero is distributed as \(a E_1-b E_2\), with \(a=(n+1)/n\), \(b=1\), and \(E_1,E_2\) independent exponential variables of mean one. The zeros have stationary spatial statistics: by the exact covariance identity, translation of the input changes the field law only by a nonvanishing deterministic unit-modulus phase, so the one-point intensity computed at the origin applies everywhere. The Kac--Rice density multiplier is \(1/\pi\). As \(\mathbb E(aE_1-bE_2)=a-b=1/n\) and \(\mathbb E|aE_1-bE_2|=(a^2+b^2)/(a+b)\), the claimed charged intensities follow from half the sum/difference. At the limit, the real and imaginary parts of \(W\) have independent isotropic unit-variance gradient coordinates, giving equal positive and negative Kac--Rice densities \(1/(2\pi)\).

## Verification
The accompanying standalone \`CHECK.py\` runs exact rational tests of the falling-factorial coefficient bounds, the Bessel differential-equation identity, and the Laguerre series representation; it also runs finite high-precision checks of the \(n^{-2}\) remainder and the one-point intensity formulas. A run with Python's standard library passed 457 finite assertions. The full uniform asymptotic, field tightness, regular-zero assertion, and point-process convergence are analytical arguments above and are not certified by finite tests.

## Relationship to prior work
Haimi--Koliander--Romero (2020/2022) supply the Weyl--Heisenberg covariance and first-intensity framework for Hermite windows. Abreu--Shirai (first posted May 17, 2026) establish cross-level zero correlations and averaged-field laws. Bellourak--Meignen--Polisano--Nahon (first posted October 9, 2026) derive charged one- and two-point intensities at fixed Hermite order. Those contributions include the exact finite-order covariance and intensity inputs used here; neither the inspected statements nor relevant proof sections assert a single-high-order \(n^{-1/2}\)-microscopic random-wave limit, joint convergence of its charged zero point processes, or the \(n^{-1}\) magnetic correction to that limit. Standard Mehler--Heine convergence and the Gaussian transversality principle are also used as known mechanisms, rather than claimed as new.

## Limitations
The statement does not establish any convergence rate of joint zero correlations, higher-point intensities, number variances, or large-deviation probabilities. The first intensity formulas are antecedent consequences of the fixed-order covariance/Kac--Rice calculations; their microscopic reexpression is included to identify the limiting process, not claimed as separately original. A proof of publication priority against every historical treatment of high-Landau-level random fields is not available; the closest inspected literature and residual terminology risk are recorded separately.

## References
1. L. D. Abreu and T. Shirai, *Zero correlations and averaged fields of orthonormal Gaussian functions*, arXiv:2605.17296v1, May 17, 2026, https://arxiv.org/abs/2605.17296.
2. C. Bellourak, S. Meignen, K. Polisano, and M. Nahon, *Zeros of the Spectrogram of White Noise with Hermite Windows*, arXiv:2610.13531v1, October 9, 2026, https://arxiv.org/abs/2610.13531.
3. A. Haimi, G. Koliander, and J. L. Romero, *Zeros of Gaussian Weyl--Heisenberg Functions and Hyperuniformity of Charge*, arXiv:2012.12298v1, December 22, 2020; *J. Stat. Phys.* 187 (2022), https://arxiv.org/abs/2012.12298.
4. Y. Canzani and B. Hanin, *Local Universality for Zeros and Critical Points of Monochromatic Random Waves*, arXiv:1610.09438, October 29, 2016, https://arxiv.org/abs/1610.09438.
