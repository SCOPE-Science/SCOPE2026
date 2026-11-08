# A universal quadratic conditioning tail at typical Hermite spectrogram zeros

## Finding

Let \(n\geq1\). For the spectrogram of complex Gaussian white noise with the normalized Hermite window of order \(n\), consider the real two-dimensional derivative at a zero, and let \(K_n\geq1\) be its spectral condition number (ratio of largest to smallest singular value). A zero is selected in the *intensity-Palm* sense: marks are averaged over zeros in a fixed bounded positive-area observation region, then divided by the expected number of such zeros. This is not the distribution of a derivative conditioned merely on the field being zero at a prescribed point.

Set \(a=n+1\), \(b=n\), and \(E=(a^2+b^2)/(a+b)\). Define, for \(y\geq0\),
\[
H_{a,b}(y)=\frac{1}{a^2}\left(\frac{1}{b+ay}-\frac{a+b}{2(b+ay)^2}\right).
\]
For every \(k\geq1\), put \(q=(k-1)/(k+1)\). The **exact survival function** is
\[
\boxed{\mathbb P_{\rm Palm}(K_n>k)
=\frac{2a^2b^2}{E}\bigl[
 H_{a,b}(1)-H_{a,b}(q^2)
 +H_{b,a}(1)-H_{b,a}(q^2)
\bigr].}
\]
In particular, for every fixed \(n\geq1\),
\[
\boxed{\lim_{k\to\infty}k^2\mathbb P_{\rm Palm}(K_n>k)
 =\frac{32n^2(n+1)^2}{(2n^2+2n+1)(2n+1)^2}>0.}
\]
Consequently \(\mathbb E_{\rm Palm}[K_n^r]<\infty\) exactly when \(0\leq r<2\). In particular, the mean condition number is finite but its second moment is infinite, despite the almost-sure nondegeneracy of every zero. There is also a **universal high-Hermite-order law**: for every \(k\geq1\),
\[
\boxed{\lim_{n\to\infty}\mathbb P_{\rm Palm}(K_n>k)
 =\frac{4k^2}{(k^2+1)^2}.}
\]
The limiting law again has the sharp quadratic upper tail, with coefficient \(4\). These statements use dimensionless Bargmann coordinates; the condition number is identical in the original isotropically scaled time-frequency coordinates.

## Assumptions and scope

Let \((\xi_j)_{j\geq0}\) be independent standard circular complex Gaussian random variables, so \(\mathbb E|\xi_j|^2=1\), and define the Gaussian entire function and its normalized Landau-level descendants by
\[
f_0(z)=\sum_{j=0}^{\infty}\xi_j\frac{z^j}{\sqrt{j!}},\qquad
f_n(z)=\frac{1}{\sqrt{n!}}(\partial_z-\bar z)^n f_0(z),\qquad z\in\mathbb C.
\]
The zeros of \(f_n\) are exactly those of the Gaussian white-noise spectrogram analyzed with the order-\(n\) Hermite window, up to an invertible isotropic coordinate scaling and a nowhere-vanishing factor. The field \(F_n(z)=e^{-|z|^2/2}f_n(z)\) is twisted-stationary; at each zero the condition number of the real differential of \(F_n\) equals that of \(f_n\). The order \(n=0\) is excluded: in that holomorphic case the condition number at simple zeros is identically \(1\).

For any bounded Borel set \(B\subset\mathbb C\) with \(0<|B|<\infty\), and any nonnegative Borel test function \(\Phi\), define the marked intensity-Palm expectation by
\[
\mathbb E_{\rm Palm}[\Phi(K_n)]
 :=\frac{\mathbb E\sum_{z\in B:f_n(z)=0}\Phi(K_n(z))}
 {\mathbb E\#\{z\in B:f_n(z)=0\}}.
\]
Stationarity implies the ratio is independent of \(B\). Zeros are almost surely isolated and nondegenerate; no conditioning on a particular realized finite zero count is used.

## Proof

**1. Derivatives and singular values.** The raising/lowering relations give
\[
f_n(0)=\xi_n,\qquad
\partial_z f_n(0)=\sqrt{n+1}\,\xi_{n+1},\qquad
\partial_{\bar z}f_n(0)=-\sqrt n\,\xi_{n-1}.
\]
These three random variables are independent. Put \(U=|\partial_z f_n(0)|\) and \(V=|\partial_{\bar z}f_n(0)|\). Thus \(U^2=aX\), \(V^2=bY\), with \(X,Y\) independent unit-rate exponential variables. The real differential of the map \(z\mapsto f_n(z)\) is \(h\mapsto Ah+B\bar h\). Orthogonal rotations of its domain and range reduce it to an ellipse with singular values \(U+V\) and \(|U-V|\); therefore
\[
K_n=\frac{U+V}{|U-V|},\qquad |\det Df_n|=|U^2-V^2|.
\]
At a zero, multiplying \(f_n\) by a nonvanishing scalar function changes its differential only by a common nonzero complex factor; that leaves the condition number unchanged. Isotropic physical-coordinate scaling also cancels from the ratio.

**2. The actual Palm weighting.** The one-point Kac–Rice formula for the vector field \((\Re f_n,\Im f_n)\) gives, for every nonnegative measurable mark test \(\Psi\),
\[
\frac{1}{|B|}\,\mathbb E\sum_{z\in B:f_n(z)=0}\Psi(U_z,V_z)
=\frac1\pi\mathbb E\left[|U^2-V^2|\Psi(U,V)\right].
\]
It follows that the Palm joint density on \(u,v>0\) is
\[
\frac{4uv|u^2-v^2|}{abE}
 \exp\!\left(-\frac{u^2}{a}-\frac{v^2}{b}\right),
\]
where \(E=\mathbb E|aX-bY|=(a^2+b^2)/(a+b)\). To verify \(E\), the signed variable \(aX-bY\) has density \(e^{-j/a}/(a+b)\) for \(j\geq0\) and \(e^{j/b}/(a+b)\) for \(j<0\). Integrating \(|j|\) gives the displayed normalization. In particular, the zero intensity is \(E/\pi\), in agreement with the known first-intensity formula.

**3. Distribution of the singular-value ratio.** Set \(t=v/u\). The change of variables \((u,v)\mapsto(u,t)\) has Jacobian \(u\). Since
\(\int_0^\infty u^5e^{-cu^2}\,du=c^{-3}\), the exact Palm density of \(t\) is
\[
p_n(t)=\frac{4a^2b^2}{E}\frac{t|1-t^2|}{(b+at^2)^3},\qquad t>0.
\]
For \(k>1\), the inequality \(K_n>k\) is equivalent to \(q<t<q^{-1}\), where \(q=(k-1)/(k+1)\). Split at \(t=1\) and substitute \(t\mapsto1/t\) in the second interval. This gives
\[
\mathbb P_{\rm Palm}(K_n>k)
=\frac{4a^2b^2}{E}\int_q^1
 t(1-t^2)\left[\frac1{(b+at^2)^3}+\frac1{(a+bt^2)^3}\right]dt.
\]
The same expression is valid for \(k=1\) by setting \(q=0\). Direct differentiation yields
\[
\frac{d}{dy}H_{a,b}(y)=\frac{1-y}{(b+ay)^3},
\]
so \(y=t^2\) integrates this expression and proves the exact formula in the Finding.

**4. Sharp tail and moment threshold.** As \(k\to\infty\), \(1-q=2/(k+1)\) and, uniformly for \(t\in[q,1]\),
\[
t(1-t^2)\left[(b+at^2)^{-3}+(a+bt^2)^{-3}\right]
\sim\frac{4(1-t)}{(a+b)^3}.
\]
Integration gives the displayed coefficient
\(32a^2b^2/[(a^2+b^2)(a+b)^2]\). The standard layer-cake identity \(\mathbb E[K_n^r]=1+r\int_1^\infty k^{r-1}\mathbb P(K_n>k)\,dk\), for \(r>0\), now proves the exact threshold \(r=2\).

**5. High-order limit.** Divide \(a\) and \(b\) by \(n\) in the ratio density. As \(n\to\infty\), it converges in distribution to
\[
p_\infty(t)=\frac{4t|1-t^2|}{(1+t^2)^3},\qquad t>0.
\]
The integral expression above, by dominated convergence on \([q,1]\), becomes
\[
8\int_q^1\frac{t(1-t^2)}{(1+t^2)^3}dt
=\left(\frac{1-q^2}{1+q^2}\right)^2
=\frac{4k^2}{(k^2+1)^2}.
\]
This completes the proof.

## Verification

The self-contained `CHECK.py` uses exact rational calculations to compare the closed survival formula with its integral representation at six Hermite orders and seven condition-number thresholds, checks the first-intensity normalization, numerically verifies the sharp tail coefficient, and verifies the high-order limiting law. Run `python3 CHECK.py` with Python 3. The expected output is `HERMITE_PALM_CONDITIONING_CHECKS_PASSED`. The analytic derivation above, not finite checks, proves the infinite ranges of \(n\) and \(k\).

## Relationship to prior work

Bellourak, Meignen, Polisano and Nahon (arXiv:2610.13531, first submitted October 9, 2026) established Hermite spectrogram zero charges, one- and two-point intensities, and a winding-number detection algorithm. Their formulas provide the local Gaussian derivative data used in Step 1, but the exact intensity-Palm law of the real derivative condition number, its quadratic tail, and the universal large-order limit are different observables. Haimi, Koliander and Romero (2022) developed the Gaussian Weyl–Heisenberg and charged-zero Kac–Rice theory, including the required first-intensity normalization. Abreu and Shirai (arXiv:2605.17296) studied cross-Hermite-order zero correlations and averaged fields. Feldheim, Haimi, Koliander and Romero (2026) studied hyperuniformity and fluctuations of zero counts. None of the materially inspected statements identifies the Palm conditioning law or sharp condition-number moments; the present result does not claim novelty for Kac–Rice itself or the existing charge-intensity formulas.

## Limitations

The result describes a local real-derivative mark at a stationary random spectrogram zero, not a finite-grid detection error distribution or a global recovery condition number. The condition-number law is invariant under the stated smooth nonvanishing gauge and isotropic coordinate scaling; an anisotropic coordinate transformation would generally change it. It assumes standard circular complex white noise and one fixed normalized Hermite window. An equivalent marked-Kac–Rice calculation in unindexed or differently named earlier literature remains possible; publication priority is not independently established. No independent mathematical audit has been performed.

## References

1. C. Bellourak, S. Meignen, K. Polisano and M. Nahon, *Zeros of the Spectrogram of White Noise with Hermite Windows*, arXiv:2610.13531v1, October 9, 2026. https://arxiv.org/abs/2610.13531
2. A. Haimi, G. Koliander and J. L. Romero, *Zeros of Gaussian Weyl–Heisenberg Functions and Hyperuniformity of Charge*, Journal of Statistical Physics 187 (2022), article 22. https://doi.org/10.1007/s10955-022-02917-3
3. L. D. Abreu and T. Shirai, *Zero correlations and averaged fields of orthonormal Gaussian functions*, arXiv:2605.17296v1, May 17, 2026. https://arxiv.org/abs/2605.17296
4. N. Feldheim, A. Haimi, G. Koliander and J. L. Romero, *Hyperuniformity and non-hyperuniformity of zeros of Gaussian Weyl-Heisenberg Functions*, Probability Theory and Related Fields (2026). https://doi.org/10.1007/s00440-026-01512-x
