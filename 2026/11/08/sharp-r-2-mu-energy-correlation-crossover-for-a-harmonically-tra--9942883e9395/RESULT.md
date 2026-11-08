# Sharp \(r=2\mu\) energy-correlation crossover for a harmonically trapped reset-noise particle

## Finding

For every \(\mu,r,D>0\), consider a one-dimensional harmonic particle with Brownian forcing that resets to zero at rate \(r\), but whose position is not reset. In its unique stationary law, its **quadratic-energy autocovariance** has a closed positive form, with an exact switch between the noise-memory rate \(r\) and the twice-confinement rate \(2\mu\). At their coincidence there is an extra linear-time factor, with an explicit uniform transition profile.

Write \(\beta=r/\mu\), \(s=\mu t\), and let
\[
\begin{aligned}
 A_\beta&=\frac{8\beta^2(\beta^2+26\beta+15)}{(\beta+1)^2(\beta+2)(\beta+3)},\\
 B_\beta&=\frac{8\beta(\beta^2+26\beta+15)}{(\beta+1)^2(\beta+2)(\beta+3)},\\
 C_\beta&=\frac{8(8\beta+5)}{(\beta+1)^2(\beta+2)}.
\end{aligned}
\]
Define the continuous nonnegative divided exponential
\[
 \Phi_\lambda(s)=\int_0^s e^{-2(s-u)}e^{-\lambda u}\,du
 =\begin{cases}
 \dfrac{e^{-\lambda s}-e^{-2s}}{2-\lambda},&\lambda\ne2,\\
 s e^{-2s},&\lambda=2.
 \end{cases}
\]
Then for all \(t\ge0\),
\[
\boxed{\operatorname{Cov}(X_0^2,X_t^2)=\left(\frac D\mu\right)^2 H_\beta(\mu t)},
\]
\[
\boxed{H_\beta(s)=A_\beta e^{-2s}+2\beta B_\beta\Phi_{\beta+1}(s)
 +2\beta^2C_\beta\bigl(\Phi_\beta(s)-\Phi_{\beta+1}(s)\bigr)>0.}
\]
The inequality is strict for every finite \(s\ge0\) and every \(\beta>0\). As \(s\to\infty\), there are exactly three long-lag regimes:
\[
H_\beta(s)\sim
\begin{cases}
 L_<(\beta)e^{-\beta s},&0<\beta<2,\\
 \dfrac{112}{3}s e^{-2s},&\beta=2,\\
 L_>(\beta)e^{-2s},&\beta>2,
\end{cases}
\]
where both amplitudes are positive and explicitly
\[
 L_<(\beta)=\frac{16\beta^2(8\beta+5)}{(2-\beta)(\beta+1)^2(\beta+2)},\qquad
 L_>(\beta)=A_\beta+\frac{2\beta B_\beta}{\beta-1}
 +\frac{2\beta^2C_\beta}{(\beta-2)(\beta-1)}.
\]
At the collision itself, the identity is exact for every \(s\ge0\):
\[
\boxed{H_2(s)=e^{-2s}\left(\frac{112}{3}s+\frac8{15}\right)
 +\frac{544}{45}e^{-3s}.}
\]
There is a uniform critical crossover: for every fixed real \(z\), with the rate \(\beta=2+z/s\),
\[
 \boxed{\lim_{s\to\infty}\frac{e^{2s}}s H_{2+z/s}(s)
 =\frac{112}{3}\frac{1-e^{-z}}z,}
\]
where the right-hand side is \(112/3\) at \(z=0\); convergence is uniform for \(z\) in each compact set.

## Assumptions and scope

The physical process obeys \(dX_t=(-\mu X_t+rY_t)\,dt\), where between independent Poisson resetting events of rate \(r\), \(Y_t\) is Brownian with \(dY_t=\sqrt{2D}\,dB_t\); each such event sends \(Y_t\) to zero and leaves \(X_t\) unchanged. The two-sided stationary realization is assumed in the covariance. The only parameter requirements are \(\mu,r,D>0\); the result is exact at all finite lags, including \(t=0\), and its rate statements take \(t\to\infty\) with positive physical parameters fixed unless a stated critical scaling is used. This agrees with the normalization of the source model [1, Eq. (33)].

Set \(Z_s=\sqrt{\mu/D}\,X_{s/\mu}\), \(W_s=\sqrt{\mu/D}\,Y_{s/\mu}\), and \(\beta=r/\mu\). Between reset events, \(dZ_s=(-Z_s+\beta W_s)\,ds\) and \(dW_s=\sqrt2\,dB_s\), with rate-\(\beta\) resetting of \(W\) alone. These definitions fix every normalization used above.

The stationary resetting Brownian process can be constructed on the entire time axis by Poisson resets, and its harmonic filter \(Z_s=\beta\int_{-\infty}^s e^{-(s-u)}W_u\,du\) exists almost surely and in every fixed finite \(L^p\). This construction gives uniqueness of the stationary pair and finiteness of the moments used here.

## Proof

**1. Stationary moments.** The generator on smooth polynomials is
\[
 (\mathcal Lf)(z,w)=(-z+\beta w)\partial_zf+\partial_w^2f
 +\beta\bigl(f(z,0)-f(z,w)\bigr).
\]
For \(m_{a,b}=\mathbb E[Z^aW^b]\) and nonnegative integers \(a,b\) with positive total degree, stationarity gives
\[
 (a+\beta\mathbf1_{b>0})m_{a,b}
 =a\beta m_{a-1,b+1}+b(b-1)m_{a,b-2},
\]
with absent or negative-exponent terms interpreted as zero. The relations are solved from the largest power of \(W\) downward at each even degree. At degree two,
\[
 m_{20}=\frac{2\beta}{\beta+1},\qquad
 m_{11}=\frac2{\beta+1},\qquad m_{02}=\frac2\beta.
\]
At degree four, the three needed stationary moments are
\[
\begin{aligned}
 m_{40}&=\frac{12\beta^2(\beta^2+19\beta+12)}{(\beta+1)^2(\beta+2)(\beta+3)},\\
 m_{31}&=\frac{12\beta(\beta^2+19\beta+12)}{(\beta+1)^2(\beta+2)(\beta+3)},\\
 m_{22}&=\frac{4(\beta^2+19\beta+12)}{(\beta+1)^2(\beta+2)}.
\end{aligned}
\]
Consequently \(A_\beta=m_{40}-m_{20}^2=\operatorname{Var}(Z_0^2)\), \(B_\beta=m_{31}-m_{20}m_{11}=\operatorname{Cov}(Z_0^2,Z_0W_0)\), and \(C_\beta=m_{22}-m_{20}m_{02}=\operatorname{Cov}(Z_0^2,W_0^2)\). Substitution gives the three positive rational functions in the finding. The one-time moments are not claimed as new; [1] already treats them.

**2. Exact lag law.** For \(s\ge0\), put
\[
 H(s)=\operatorname{Cov}(Z_0^2,Z_s^2),\quad
 G(s)=\operatorname{Cov}(Z_0^2,Z_sW_s),\quad
 F(s)=\operatorname{Cov}(Z_0^2,W_s^2).
\]
The Markov property and the generator identities \(\mathcal L(z^2)=-2z^2+2\beta zw\), \(\mathcal L(zw)=-(1+\beta)zw+\beta w^2\), \(\mathcal L(w^2)=2-\beta w^2\) imply the **exact** triangular closed system
\[
 \frac d{ds}\begin{pmatrix}H\\G\\F\end{pmatrix}
 =\begin{pmatrix}-2&2\beta&0\\0&-(1+\beta)&\beta\\0&0&-\beta\end{pmatrix}
 \begin{pmatrix}H\\G\\F\end{pmatrix},\qquad
 (H,G,F)(0)=(A_\beta,B_\beta,C_\beta).
\]
In particular \(F(s)=C_\beta e^{-\beta s}\), \(G(s)=B_\beta e^{-(\beta+1)s}+\beta C_\beta(e^{-\beta s}-e^{-(\beta+1)s})\). Variation of constants for \(H\) gives the claimed expression. The integral form implies \(\Phi_{\beta}(s)>\Phi_{\beta+1}(s)\ge0\) for \(s>0\), and all \(A,B,C\) are positive, proving strict positivity (also at zero because \(H(0)=A>0\)). Brownian noise and resetting introduce no missing covariance term: the constant \(2\) in \(\mathcal L(w^2)\) disappears under centering.

**3. Sharp rate switch and critical case.** For \(0<\beta<2\), \(\Phi_\beta(s)\sim e^{-\beta s}/(2-\beta)\), and all other terms decay faster; this gives \(L_<\). For \(\beta>2\), \(\Phi_\lambda(s)\sim e^{-2s}/(\lambda-2)\) for \(\lambda=\beta,\beta+1\), giving \(L_>\). Both amplitudes are strictly positive, so there is no cancellation or hidden additional phase. At \(\beta=2\), use \(\Phi_2(s)=se^{-2s}\) and \(\Phi_3(s)=e^{-2s}-e^{-3s}\), and \(A_2=568/45\), \(B_2=284/45\), \(C_2=14/3\) to obtain the displayed exact critical expression. The phase division is exhaustive for every positive rate ratio.

**4. Critical scaling.** For bounded real \(z\), with \(\beta=2+z/s\), exactly
\[
 \Phi_\beta(s)=s e^{-2s}\frac{1-e^{-z}}z.
\]
Here \(2\beta^2C_\beta\to112/3\) uniformly on compact \(z\)-sets. The remaining terms are bounded by a constant times \(e^{-2s}\) uniformly for \(\beta\) sufficiently near two because \(\Phi_{\beta+1}(s)\le e^{-2s}/(\beta-1)\). Dividing by \(se^{-2s}\) yields the asserted locally uniform crossover limit. No finite experiment is used as an infinite-time argument.

## Verification

The companion file `checks/verify_energy_autocovariance.py` requires only Python 3 and can be run with `python3 checks/verify_energy_autocovariance.py` from the extracted package directory. It reconstructs the stationary moment recurrence in exact rational arithmetic at nine parameter values; independently integrates the three-dimensional covariance ODE for 70 parameter-time combinations; and checks asymptotic amplitudes, the exact critical expression, and five near-critical values. It reports `PASS: 265 exact and finite checks; independent moment recurrence and ODE integration`. The symbolic generator proof above establishes the continuous-parameter and infinite-lag claims; tests are not substitutes for that proof.

## Relationship to prior work

Guéneau, Majumdar and Schehr [1] introduce precisely this Poisson-reset Brownian-driven harmonic model, compute stationary one-time position moments and a two-time **linear** position covariance, and derive a time-dependent one-point renewal equation. Those ingredients are credited here. The present statement instead concerns the **connected mixed-time quartic observable** \(\operatorname{Cov}(X_0^2,X_t^2)\), its complete lag dependence and a new asymptotic collision at \(r=2\mu\); neither the one-time fourth moment nor the linear two-time covariance specifies this function. Majumdar and Oshanin [2] investigate correlation spectra of reset Brownian noise itself, without this filtered quartic observable. Shee [3] considers a different active-particle resetting protocol and transient one-time higher moments. More general Markov polynomial-semigroup methods can imply the triangular evolution after fresh computation; no assertion is made that the underlying generator technique is new.

## Limitations

The theorem applies to a single harmonic particle with Poisson resetting of a Brownian driving noise to zero; it does not address nonharmonic confinement, resetting of particle position, non-Poisson renewal laws, multiparticle correlations, finite-time initialization effects, or fluctuation-dissipation identities. Its physical quadratic energy equals \(\mu X_t^2/2\) up to a constant, so the covariance law rescales accordingly. The exact function is derived from a classical polynomial generator and could be implicitly obtainable from an unindexed general formula; publication priority is not independently certified. The limits do not assert uniformity for rate ratios away from a fixed compact critical scaling.

## References

1. M. Guéneau, S. N. Majumdar, and G. Schehr, *Active particle in a harmonic trap driven by a resetting noise: an approach via Kesten variables*, arXiv:2306.09453, first public 15 June 2023, https://arxiv.org/abs/2306.09453.
2. S. N. Majumdar and G. Oshanin, *Spectral content of fractional Brownian motion with stochastic reset*, arXiv:1806.03435, https://arxiv.org/abs/1806.03435.
3. A. Shee, *Active Brownian particle under stochastic position and orientation resetting in a harmonic trap*, arXiv:2409.06920, https://arxiv.org/abs/2409.06920.
