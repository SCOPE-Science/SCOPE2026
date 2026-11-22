# A singular noise boundary layer in one-bit telegraph-path quadrature

## Finding

Let \(T>0\), \(\lambda>0\), and let \(N_t\) be a rate-\(\lambda\) Poisson process with \(N_0=0\). Put \(X_t=(-1)^{N_t}\) and estimate the time-averaged signed occupation
\[
J=\frac1T\int_0^T X_s\,\mathrm ds.
\]
At one predetermined time \(t\in[0,T]\), record the single bit \(Y_t=X_t\Xi\), where \(\Xi\) is independent of the entire process and \(\Pr(\Xi=-1)=\varepsilon\in[0,1/2]\). The estimator can be any measurable function of this bit, under squared-error loss. Define
\[
a=2\lambda T,\quad p=e^{-a},\quad c=1-2\varepsilon,\quad u=t/T,\quad z=e^{-au},\quad D(z)=2-(2-p)z-p/z.
\]
For \(0<c\le1\), there is exactly one Bayes-risk-optimal time \(t_*=Tu_*\) strictly between the endpoints. Its coordinate \(z_*=e^{-au_*}\) is the unique root in \((p,1)\) of
\[
\boxed{\frac{p}{z^2}-(2-p)+2c^2(z-p)=0.}
\]
For a perfect bit, \(c=1\), this root is explicitly \(z_*=(p+\sqrt{p^2+8p})/4\). For \(c=0\), the bit is independent of the process and all observation times tie. For every fixed \(a>0\), the optimal normalized time \(u_*\) strictly increases as the bit becomes less reliable (as \(c\) decreases through \((0,1]\)).

**Singular rare-switching law.** As \(a\downarrow0\), a perfect bit has \(u_*\to2/3\), but every fixed imperfect informative bit \(0<c<1\) has \(u_*\to1\), in fact
\[
1-u_*\sim\frac{a}{2(1-c^2)}.
\]
More precisely, for any family of informative channels satisfying \((1-c(a)^2)/a\to\kappa\in[0,\infty)\),
\[
\boxed{u_*\longrightarrow\Phi(\kappa)=\frac{1-\kappa+\sqrt{\kappa^2+4\kappa+1}}3.}
\]
If \((1-c(a)^2)/a\to\infty\), then \(u_*\to1\). Thus the rare-switching and perfect-detection limits do not commute, with an explicit transition layer. In the opposite fast-switching limit \(a\to\infty\), uniformly across all \(0<c\le1\),
\[
u_*=\frac12+\frac{\log2}{2a}+o(a^{-1}).
\]

## Assumptions and scope

The symmetric two-state continuous-time Markov chain begins in the known \(+1\) state; both transition rates equal \(\lambda\). The horizon \(T\), rate \(\lambda\), and symmetric bit-flip probability \(\varepsilon\) are known. One predetermined nonadaptive binary observation is allowed. The objective is the unconditional Bayes mean-square error of the optimal estimator of the path average \(J\), not an estimate of \(\lambda\) or the instantaneous state. The endpoints are permitted. There is no observation-price dependence on time.

## Proof

**1. Exact risk.** The Poisson parity identity gives \(\mathbb E X_s=e^{-2\lambda s}\) and, for \(0\le s,t\le T\),
\[
\operatorname{Cov}(X_s,X_t)=e^{-2\lambda|t-s|}-e^{-2\lambda(s+t)}.
\]
Integrating these identities and rescaling time yields
\[
\mathbb EJ=\frac{1-p}{a},\quad \operatorname{Var}(J)=V_a:=\frac{2a-3+4p-p^2}{a^2},\quad
\operatorname{Cov}(J,X_{Tu})=\frac{D(z)}a.
\]
Because \(\Xi\) is independent, \(\mathbb E Y_{Tu}=cz\), \(\operatorname{Var}(Y_{Tu})=1-c^2z^2\), and \(\operatorname{Cov}(J,Y_{Tu})=cD(z)/a\). Every function of the two-valued bit \(Y_{Tu}\in\{-1,1\}\) is affine in it, hence the conditional mean is exactly
\[
\widehat J=\frac{1-p}{a}+\frac{cD(z)}{a(1-c^2z^2)}(Y_{Tu}-cz),
\]
with minimum risk
\[
R_a(z,c)=V_a-\frac{c^2D(z)^2}{a^2(1-c^2z^2)}.
\]
These formulas hold when the denominator is positive. At \(c=1,u=0\), the bit is deterministic and the risk is \(V_a\) by direct conditioning; the risk expression has the same continuous limit. At \(c=0\), the risk is \(V_a\) at every time.

**2. Global optimizer and uniqueness.** For \(0<c\le1\), maximize \(F(z)=D(z)^2/(1-c^2z^2)\) over \(p\le z\le1\), using the continuous value at the degenerate corner. The factor \(D(z)>0\) for \(p\le z<1\); indeed the covariance integral displayed above has a strictly positive integrand over a set of positive measure for any \(t>0\). Direct differentiation gives
\[
F'(z)=\frac{2D(z)}{(1-c^2z^2)^2}S(z),\qquad
S(z)=\frac p{z^2}-(2-p)+2c^2(z-p).
\]
We have \(S''(z)=6p/z^4>0\), \(S(p)=(1-p)^2/p>0\), and \(S(1)=-2(1-p)(1-c^2)\). If \(c<1\), strict convexity and opposite endpoint signs give exactly one crossing in \((p,1)\), positive before and negative afterward. For \(c=1\), the polynomial factorization
\[
z^2 S(z)=(z-1)(2z^2-pz-p)
\]
shows that the only interior zero is \((p+\sqrt{p^2+8p})/4\), which is in \((p,1)\), with the same sign pattern. Thus \(F\) has exactly one global maximizer in the admissible interval. Since \(z=e^{-au}\) is one-to-one, the optimal time is unique.

**3. Strict noise ordering.** At the interior root, \(S'(z_*)<0\), since strict convexity, \(S(z_*)=0\), and \(S(1)\le0\) force the right-hand secant slope to dominate the derivative. Implicit differentiation in \(k=c^2\) gives
\[
\frac{\mathrm dz_*}{\mathrm dk}=-\frac{2(z_*-p)}{S'(z_*)}>0.
\]
Consequently \(-\log(z_*)/a\) strictly decreases in detector reliability \(c\).

**4. Rare-switching limits.** Put \(z=e^{-au}\), \(p=e^{-a}\), and \(\delta=1-c^2\). Uniformly for \(0\le u\le1\) and \(0\le\delta\le1\), Taylor expansion of the *exact* root equation gives
\[
S(e^{-au})=-2a\delta(1-u)+a^2\{2u^2-2u+1+(1-\delta)(u^2-1)\}+O(a^3).
\]
For a fixed positive \(\delta\), the root must converge to \(u=1\), and substituting \(u=1-o(1)\) gives \(1-u\sim a/(2\delta)\). If \(\delta/a\to\kappa<\infty\), division by \(a^2\) yields the limiting equation
\[
3u^2-2u-2\kappa(1-u)=0.
\]
Its unique positive root is \(\Phi(\kappa)\). To exclude the other limiting root \(u=0\) when \(\kappa=0\), note that reliability monotonicity places each optimal \(u\) at least as late as the perfect-bit optimum. The exact perfect-bit root above has limit \(u=2/3\) as \(a\downarrow0\). If \(\delta/a\to\infty\), the uniform expansion instead forces \(1-u\to0\). In particular, \(\Phi(0)=2/3\), \(\Phi(\kappa)\uparrow1\), and the perfect/imperfect limits differ.

**5. Fast-switching limit.** For any \(0<c\le1\), the root satisfies \(S(\sqrt p/2)>0>S(\sqrt p)\) for all sufficiently small \(p\), uniformly in \(c\). Hence \(z_*=O(\sqrt p)\), and the root identity gives \(p/z_*^2=2+O(\sqrt p)\) uniformly. Thus \(z_*\sim\sqrt{p/2}\). Since \(p=e^{-a}\), taking logarithms proves \(u_*=1/2+(\log2)/(2a)+o(a^{-1})\).

## Verification

Run `python verify.py` after installing the packages in `requirements.txt`. The supplied checker independently verifies derivative, cubic, factorization and convexity identities; direct numerical integrations of the Markov covariance; multiple optimality and reliability comparisons; rare- and fast-switching limits; and independent Poisson-path simulations. Symbolic algebra and the analytical sign proof, not finite grids or simulations, establish the universal optimizer. The run used for this result passed all bundled checks.

## Relationship to prior work

The integrated telegraph process itself is established in earlier Markov-filtering literature. In particular, Bäuerle–Gilitschenski–Hanebeck (2014), §3.1, studies the *reverse observation problem*: a continuous integrated telegraph signal observed with Gaussian noise, used to filter the instantaneous hidden switching state. Here the switching state is measured just once through an erroneous binary channel, and the target is its unobserved path integral. Pozdnyakov–Elbroch–Hu–Meyer–Yan (2018) develop occupation distributions and likelihood methods for switching paths, not this single-bit timing optimization. Michel (2018/2020) optimizes repeated sampling intervals to estimate the *unknown transition rate*, whereas the present problem takes the rate as known and estimates one path's occupation integral from one corrupted bit. The older integrated-path formulas and filtering/rate-information objectives therefore do not imply the global noisy-bit timing classification or singular boundary layer. These are statement-level comparisons, not an unconditional publication-priority claim.

## Limitations

The result does not treat asymmetric transition rates, an unknown initial state, asymmetric observation channels, more than one reading, adaptive timing, or loss functions other than squared error. Detector accuracy is not optimized jointly with timing. The singular limit refers to the known-rate symmetric model and is not a universal law for arbitrary Markov chains. An earlier equivalent result outside the located material cannot be ruled out without additional independent literature review.

## References

1. V. Pozdnyakov, L. M. Elbroch, C. Hu, T. Meyer, J. Yan, *On estimation for Brownian motion governed by telegraph process with multiple off states*, arXiv:1806.00849 (first version dated 2018-06-03), https://arxiv.org/abs/1806.00849.
2. J. Michel, *Optimal adaptive sampling for a symmetric two-state continuous time Markov chain*, manuscript dated 2018-02-20, https://bpb-us-w2.wpmucdn.com/u.osu.edu/dist/6/56774/files/2017/12/optimal_sampling_design_ctmc9-1nt190d.pdf; published in *Econometric Reviews* (2020), https://doi.org/10.1080/07474938.2019.1701808.
3. N. Bäuerle, I. Gilitschenski, U. D. Hanebeck, *Exact and Approximate Hidden Markov Chain Filters Based on Discrete Observations*, arXiv:1411.0849 (2014), https://arxiv.org/abs/1411.0849.
