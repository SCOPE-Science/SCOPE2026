# Matched reset-size statistics conceal a finite-versus-infinite stationary fourth moment

## Finding

Two natural independently marked Poisson partial-reset protocols have *identical event rate, mean reset fraction, reset-fraction variance, stationary position variance, and Gaussian diffusion approximation*, but sharply different stationary fourth moments. At reset fraction scale \(s=1/4\), protocol A has infinite fourth spatial moment whereas protocol B has
\[
\mathbb E_B X^4=\frac{12288D^2}{31\lambda^2}<\infty,
\qquad \mathbb E_A X^4=\infty,
\qquad \mathbb E_A X^2=\mathbb E_B X^2=\frac{4D}{\lambda}.
\]
More generally their exact stationary moment cutoffs satisfy \(2<\kappa_A(s)<\kappa_B(s)<2/s\) for every \(0<s<1/3\). As resetting becomes arbitrarily weak and frequent, the thresholds separate on the singular inverse-reset-fraction scale:
\[
\lim_{s\downarrow0}s\kappa_A(s)=z_A=0.7968121300\ldots,
\qquad\lim_{s\downarrow0}s\kappa_B(s)=z_B=1.0209751006\ldots.
\]
The common Gaussian-diffusion surrogate has cutoff \(\kappa_{\mathrm{diff}}(s)=1+1/(2s)\), and therefore distinguishes neither protocol.

## Assumptions and scope

Fix \(D,\lambda>0\), \(0<s<1/3\), and independent standard Brownian motion, Poisson event clock of rate \(r=\lambda/s\), and independent reset marks \(U\). On \(\mathbb R\), let
\[
 dX_t=\frac{\lambda}{2}X_t\,dt+\sqrt{2D}\,dB_t
\]
between event times; at each event replace \(X_{t-}\) by \((1-sU)X_{t-}\). All reset multipliers are strictly positive and at most one. At each event draw a fresh mark from one of the distributions
\[
\begin{array}{c|cc}
&\text{reset size }U&\text{probability}\\\hline
 A&0,\ 2&1/2,\ 1/2\\
 B&1/2,\ 3&4/5,\ 1/5
\end{array}
\]
(the pairs are listed in the same order). Both have \(\mathbb E U=1\) and \(\mathbb E U^2=2\); in particular the random centred reset fluctuation \(U-1\) has variance one. For each law \(j\in\{A,B\}\) and real \(p\ge0\) put
\[
 \psi_j(p;s)=\frac{\lambda p}{2}+\frac{\lambda}{s}\left(\mathbb E_j(1-sU)^p-1\right).
\]
The exact stationary moment cutoff \(\kappa_j(s)\) is the unique *strictly positive* zero of \(\psi_j(\cdot;s)\) (the zero at \(p=0\) is excluded). At the cutoff the moment is infinite. Here \(D\) is the diffusion constant, so Brownian variance increases at rate \(2D\) before resetting.

## Proof

**Existence, uniqueness, and the Gaussian scale mixture.** Define the homogeneous growth multiplier over elapsed time \(t\) by
\[
H_t=e^{\lambda t/2}\prod_{k=1}^{N_t}(1-sU_k).
\]
It has almost-sure exponential decay because the strong law gives
\[
\lim_{t\to\infty}t^{-1}\log H_t
=\lambda/2+(\lambda/s)\mathbb E\log(1-sU)
\le-\lambda/2<0.
\]
The last inequality follows from \(\log(1-x)\le-x\) and \(\mathbb EU=1\). Thus the unique invariant position law is the convergent past-noise integral, which conditioned on the reset environment is centred Gaussian. By reversing the stationary Poisson time axis, its random conditional variance has the distribution
\[
 V=2D\int_0^\infty e^{\lambda t}\prod_{k=1}^{N_t}(1-sU_k)^2\,dt.
\]
Strict decay of the homogeneous multiplier yields almost-sure finiteness; synchronous coupling erases initial conditions, establishing uniqueness. Writing \(X\stackrel d=\sqrt V\,Z\) with independent standard normal \(Z\), moments of \(X\) of order \(p>0\) are finite exactly when moments of \(V\) of order \(p/2\) are finite.

**Exact fractional moment threshold.** If \(T\) is the first exponential event waiting time and \(V'\) is an independent copy, conditioning on that first event gives
\[
 V\stackrel d=C+AV',\qquad
 C=\frac{2D}{\lambda}(e^{\lambda T}-1)>0,\quad
 A=e^{\lambda T}(1-sU)^2>0.
\]
For \(q=p/2>0\), \(\mathbb EA^q=(r/(r-\lambda q))\,\mathbb E(1-sU)^p\) if \(q<r/\lambda\), and is infinite otherwise. Under the first condition, \(\mathbb EA^q<1\) is equivalent to \(\psi_j(p;s)<0\). Iterating the recurrence produces an almost-sure positive perpetuity sum. If \(\psi_j(p;s)<0\), then \(\mathbb EC^q<\infty\); for \(0<q\le1\) apply subadditivity and a geometric series, and for \(q>1\) apply the \(L^q\) triangle inequality to obtain \(\mathbb EV^q<\infty\). Conversely, if \(\mathbb EV^q<\infty\), the strict inequality \(V^q>(AV')^q\) almost surely forces \(\mathbb EA^q<1\); this is impossible when \(\psi_j(p;s)\ge0\). Hence
\[
\mathbb E_j|X|^p<\infty\quad\Longleftrightarrow\quad\psi_j(p;s)<0
\quad(p>0).
\]
The function \(\psi_j\) is strictly convex; it vanishes at zero, has negative right derivative there by the logarithmic contraction calculation, and tends to infinity because of the positive linear drift. It therefore has precisely one further positive zero \(\kappa_j(s)\). Moreover \(\psi_j(2;s)=\lambda(-1+2s)<0\) and \(\psi_j(2/s;s)>0\), yielding \(2<\kappa_j(s)<2/s\).

**Strict matched-protocol ordering.** For fixed \(p>2\), let \(f(u)=(1-su)^p\), \(0\le u\le3\). Direct third-divided-difference interpolation at knots \(0,1/2,2,3\) gives
\[
\mathbb E_Af(U)-\mathbb E_Bf(U)
=-\frac32 f[0,1/2,2,3].
\]
On this interval \(f^{(3)}(u)=-s^3p(p-1)(p-2)(1-su)^{p-3}<0\). The generalized mean-value theorem for divided differences makes the right-hand side strictly positive. Thus \(\psi_A(p;s)>\psi_B(p;s)\) for every real \(p>2\). Evaluating at the positive zero of \(\psi_B\), strict convexity then gives \(\kappa_A(s)<\kappa_B(s)\).

**An exact finite/infinite fourth-moment split.** At \(s=1/4\), the multipliers of A are \(1,1/2\), and of B are \(7/8,1/4\), with their specified probabilities. Exact rational arithmetic yields
\[
\mathbb E_A(1-sU)^4=17/32,\qquad
\mathbb E_B(1-sU)^4=481/1024,
\]
so \(\psi_A(4;1/4)=\lambda/8>0\) while \(\psi_B(4;1/4)=-31\lambda/256<0\). Both have \(\mathbb E(1-sU)^2=5/8\) and \(\psi_j(2;1/4)=-\lambda/2\). Stationarity of the degree-two and degree-four generator identities (legitimate for B because their moments are finite),
\[
0=2D+\psi_j(2;s)\mathbb E_jX^2,
\qquad0=12D\mathbb E_jX^2+\psi_j(4;s)\mathbb E_jX^4,
\]
gives the asserted exact variance and B fourth moment. For A the threshold theorem precludes a finite fourth moment, so its degree-four identity is not applied.

**High-order singular scaling and the common approximation.** For \(p=z/s\) and fixed \(z\ge0\),
\[
(s/\lambda)\psi_j(z/s;s)=z/2+\mathbb E_j(1-sU)^{z/s}-1
\longrightarrow h_j(z)=z/2+\mathbb E_je^{-zU}-1
\]
uniformly on compact \(z\)-intervals. Each \(h_j\) is strictly convex, with \(h_j'(0)=-1/2\) and a unique positive zero \(z_j\); hence the unique positive roots converge. More explicitly,
\[
h_A(z)=z/2+(1+e^{-2z})/2-1,\qquad
h_B(z)=z/2+(4/5)e^{-z/2}+(1/5)e^{-3z}-1.
\]
The interpolating inequality above (or the corresponding strict exponential divided difference) proves \(z_A<z_B\), giving an order-\(1/s\) asymptotic cutoff separation. Finally, the drift and infinitesimal second jump moment for either protocol equal \(-\lambda x\) and \(\lambda s\mathbb E U^2\,x^2=2\lambda s x^2\). Therefore the shared second-order Gaussian closure is
\[
d\widetilde X_t=-\frac\lambda2\widetilde X_t\,dt+
\sqrt{2D}\,dB_t+\sqrt{2\lambda s}\,\widetilde X_t\,dW_t
\]
with independent Brownian noises; its moment growth exponent is \(-\lambda p/2+\lambda s p(p-1)\). It has invariant moment cutoff \(1+1/(2s)\) and exact second moment \(2D/[\lambda(1-2s)]\), shared by both original protocols.

## Verification

The standalone Python file `check.py` evaluates every reset distribution's first two moments, rational multiplier moments, fourth-moment growth signs and the exact B fourth moment. It tests the divided-difference inequality for many integer powers and scales, computes positive cutoff roots numerically, and checks the limiting roots. Run `python check.py` using only the Python standard library. Exact rational identities are machine checked; strict inequalities for arbitrary real powers, existence and all fractional moment thresholds are proved above and are not inferred from finite tests.

## Relationship to prior work

Galla (2026), Appendix A.4 and Supplement S1.2, introduces independently random proportional reset amplitudes, their first-two-moment Gaussian diffusion closure and numerical comparisons. Its linear example and surrogate stationary density are also credited. The new claim isolates two genuinely different **random** amplitude laws with equal first two moments and exactly equal stationary variance, but opposite fourth-moment finiteness, and proves strict cutoff ordering at all real orders above two with a singular inverse-reset-fraction split. It does not claim the Gaussian diffusion approximation, the general random-coefficient perpetuity method, or the existence of power-law stationary tails as new. Biroli et al. (2024) analyze a fixed proportional multiplier for Brownian diffusion without the positive drift and matched random-mark comparison; Nakao (1998) analyzes multiplicative Gaussian noise with additive noise. Generalized Ornstein–Uhlenbeck exponential-functional theory (Behme–Lindner, 2013) supplies related stationary-process principles, but the explicit matched-protocol separation is not a stated result in the inspected passages. Its possible implication through a general moment theorem remains a priority risk.

## Limitations

The exact protocols are two-point random amplitude laws and the bulk dynamics has specified positive linear drift; the theorem does not assert that every pair of moment-matched reset laws is ordered. The cutoff compares stationary *moments*, not a fully proved asymptotic pointwise tail equivalence or an empirical estimation bound. Brownian diffusion and event marks are independent, and \(0<s<1/3\) ensures strictly positive multipliers. At \(s=1/4\) the fourth-moment divergence does not mean nonexistence of the invariant probability law or infinite variance. Novelty is assessed against inspected primary texts and available indexed claims, not established by a negative search or certified independently.

## References

1. T. Galla, *A diffusion approximation for systems with frequent weak resetting*, arXiv:2602.21635v1, first posted 2026-02-25, especially Appendix A.4 and Supplement S1.1–S1.2, https://arxiv.org/html/2602.21635 .
2. M. Biroli, Y. Feld, A. K. Hartmann, S. N. Majumdar, G. Schehr, *Resetting by rescaling: exact results for a diffusing particle in one-dimension*, arXiv:2406.08387, https://arxiv.org/abs/2406.08387 .
3. H. Nakao, *Asymptotic power law of moments in a random multiplicative process with weak additive noise*, arXiv:cond-mat/9802030, https://arxiv.org/abs/cond-mat/9802030 .
4. A. Behme and A. Lindner, *On exponential functionals of Lévy processes*, arXiv:1301.3272, https://arxiv.org/abs/1301.3272 .
