# A sharp two-site cusp for boundary-reaction throughput under position-only resetting

## Finding

Consider reflected Brownian motion on the half-line with generator \(D\partial_{xx}\), \(D>0\). At times of an independent rate-\(r\) Poisson clock, its *position alone* is replaced by an independent point \(R\) having distribution \(\mu\) supported in \((0,\infty)\). The accumulated boundary local time is **not** reset. Normalize the local time by
\[
L_t=\lim_{\varepsilon\downarrow0}\frac{D}{\varepsilon}\int_0^t\mathbf1_{[0,\varepsilon]}(X_s)\,ds
\]
(the almost-sure, jointly continuous occupation-density version), and let \(\tau_\ell=\inf\{t:L_t>\ell\}\) for \(\ell>0\). Define \(\mathcal A(k)=\mathbb E[e^{-kR}]\), \(k>0\), and \(k_s=\sqrt{(s+r)/D}\).

**Exact retained-local-time law.** When \(X_0=0\), \(\tau_\ell\) is the inverse-local-time subordinator and
\[
\mathbb E_0[e^{-s\tau_\ell}]=\exp\!\left[-\ell\,\frac{s\sqrt{(s+r)/D}}{s+r\mathcal A(k_s)}\right],\qquad s>0.
\]
In particular, \(\mathbb E_0\tau_\ell=\ell/[\sqrt{Dr}\,\mathcal A(\sqrt{r/D})]\). If the initial position is independently sampled from \(\mu\) (as at a reset), then
\[
\mathbb E_\mu[e^{-s\tau_\ell}]
=\frac{(s+r)\mathcal A(k_s)}{s+r\mathcal A(k_s)}
\exp\!\left[-\ell\,\frac{s\sqrt{(s+r)/D}}{s+r\mathcal A(k_s)}\right]
\]
and
\[
\mathbb E_\mu\tau_\ell=
\frac{1-\mathcal A(k_0)}{r\mathcal A(k_0)}+
\frac{\ell}{\sqrt{Dr}\,\mathcal A(k_0)},\qquad k_0=\sqrt{r/D}.
\]
Moreover \(L_t/t\to J(r)=\sqrt{Dr}\,\mathcal A(\sqrt{r/D})\) almost surely, for either initial condition. Thus \(J(r)\) is both the long-term boundary-contact throughput and the inverse asymptotic mean threshold-completion time per unit local-time demand.

**Sharp two-site optimization.** Fix \(0<a<b\) and \(0\le p\le1\), and reset to \(a\) with probability \(p\) and to \(b\) with probability \(1-p\). Put \(\beta=b/a\) and \(y=a\sqrt{r/D}\). Maximizing the exact throughput \(J(r)\) over \(r>0\) is equivalent to maximizing
\[
F_{\beta,p}(y)=y\big[p e^{-y}+(1-p)e^{-\beta y}\big],\qquad y>0.
\]
There is a sharp dimensionless geometry threshold
\[
\boxed{\beta_c=3+2\sqrt2.}
\]
For \(1<\beta\le\beta_c\), \(F_{\beta,p}\) has exactly one global maximizer for every \(p\in[0,1]\). For \(\beta>\beta_c\), a unique coexistence probability \(p_*(\beta)\in(0,1)\) exists. At \(p=p_*\) there are exactly **two distinct global throughput-maximizing reset rates**. For every other \(p\), the maximizer is unique, and the optimal rate jumps discontinuously from the lower-rate branch to the higher-rate branch as \(p\) increases through \(p_*\).

The threshold and coexistence probability are constructive. For \(\beta>\beta_c\) define
\[
y_\pm=\frac{\beta+1\pm\sqrt{\beta^2-6\beta+1}}{2\beta},\qquad
H_\beta(y)=e^{-(\beta-1)y}\frac{\beta y-1}{1-y},\quad\frac1\beta<y<1.
\]
Put \(h_{\min}=H_\beta(y_+)\) and \(h_{\max}=H_\beta(y_-)\). The two-local-maximum region is exactly
\[
\frac{h_{\min}}{1+h_{\min}}<p<\frac{h_{\max}}{1+h_{\max}}.
\]
For each such \(p\), let \(u_1(p)<u_2(p)<u_3(p)\) be the three roots of \(H_\beta(y)=p/(1-p)\). The unique \(p_*\) is specified by
\[
F_{\beta,p_*}(u_1(p_*))=F_{\beta,p_*}(u_3(p_*)).
\]
At coexistence the two optimal physical rates are \(r_{\mathrm{lo}}=D[u_1(p_*)/a]^2\) and \(r_{\mathrm{hi}}=D[u_3(p_*)/a]^2\). For example, with \(b/a=10\), \(p_*\approx0.1228819700\), and with \(D=a=1\) the two rates are approximately \(0.020660589\) and \(0.983120201\).

## Assumptions and scope

The reflected diffusion is constructed from independent Brownian motions between resets with instantaneous jumps to fresh \(R\), and the boundary local time is cumulative across *all* reset intervals. Every stated Laplace-transform and mean identity holds for any positive reset-position distribution \(\mu\) supported on \((0,\infty)\) with \(\mathcal A(k)>0\); the two-site optimization assumes \(0<a<b<\infty\). The exact inverse-local-time transform starts at the reflecting boundary. The formula with a prefactor starts at a fresh \(\mu\)-distributed location. Reset clocks are homogeneous Poisson, and the threshold \(\ell>0\) is deterministic. No inference about thresholds that are themselves erased by resetting is made.

## Proof

**1. Boundary resolvent and local-time inversion.** The Neumann heat kernel on \([0,\infty)\) with generator \(D\partial_{xx}\) has Laplace resolvent
\[
G_z^{\mathrm{ref}}(x,0)=\frac{e^{-x\sqrt{z/D}}}{\sqrt{Dz}},\quad z>0.
\]
Because a Poisson reset to \(R\) erases the position but not the local time, conditioning on the most recent reset gives the *position-only* resolvent, starting at \(0\),
\[
G_s^r(0,0)=G_{s+r}^{\mathrm{ref}}(0,0)+\frac r s\mathbb E[G_{s+r}^{\mathrm{ref}}(R,0)]
=\frac{1+(r/s)\mathcal A(k_s)}{\sqrt{D(s+r)}}.
\]
The process is strong Markov; its inverse boundary local time has independent stationary increments because every crossing of a prescribed local-time level occurs at the state \(X=0\), and the independent Poisson clock is memoryless. For this normalization, occupation density implies
\[
\mathbb E_0\!\int_0^\infty e^{-st}dL_t=D G_s^r(0,0).
\]
Changing variables from physical time to local-time level and using the subordinator property yields
\[
\mathbb E_0\!\int_0^\infty e^{-st}dL_t
=\int_0^\infty\mathbb E_0[e^{-s\tau_\ell}]d\ell
=\int_0^\infty e^{-\ell\phi(s)}d\ell=\frac1{\phi(s)}.
\]
Inverting gives \(\phi(s)=1/[D G_s^r(0,0)]\), the displayed exact exponent. Since \(\phi(s)/s\to1/[\sqrt{Dr}\mathcal A(k_0)]\) as \(s\downarrow0\), differentiating the Laplace transform establishes the mean; standard subordinator strong laws give \(\tau_\ell/\ell\to\phi'(0)\) almost surely, and inversion gives \(L_t/t\to1/\phi'(0)=J(r)\).

**2. Starting at a reset location.** Let \(H\) be the first hitting time of \(0\) for the reflected reset process started with an independent \(\mu\)-distributed position. Before the first hit it is ordinary Brownian motion on \((0,\infty)\), reset to fresh \(\mu\)-distributed points. A no-reset successful excursion has transform \(\mathcal A(k_s)\); an intervening reset before the hit has discounted probability \(r[1-\mathcal A(k_s)]/(s+r)\). Renewal at the *first hit*, not at absorption of the accumulated local-time threshold, gives
\[
\mathbb E[e^{-sH}]=\frac{\mathcal A(k_s)}{1-r[1-\mathcal A(k_s)]/(s+r)}
=\frac{(s+r)\mathcal A(k_s)}{s+r\mathcal A(k_s)}.
\]
At \(H\), accumulated local time is zero; the strong Markov property supplies an independent copy of the first-step inverse local-time process. Multiplication of transforms yields the second formula. Differentiation at \(s=0\) gives \(\mathbb EH=[1-\mathcal A(k_0)]/[r\mathcal A(k_0)]\), and therefore the stated exact mean.

**3. Complete stationary-point classification.** For \(0<p<1\), the derivative of \(F_{\beta,p}\) is positive for \(0<y\le1/\beta\) and negative for \(y\ge1\). On \((1/\beta,1)\),
\[
\operatorname{sgn}F_{\beta,p}'(y)
=\operatorname{sgn}\!\left(\frac p{1-p}-H_\beta(y)\right).
\]
A direct logarithmic derivative calculation gives
\[
\frac{H_\beta'(y)}{H_\beta(y)}=-(\beta-1)+\frac1{y-1/\beta}+\frac1{1-y}.
\]
The last two terms have minimum \(4\beta/(\beta-1)\), attained at the midpoint of \((1/\beta,1)\). Consequently \(H_\beta\) is strictly increasing except possibly at one horizontal tangent when \((\beta-1)^2\le4\beta\), which is equivalent to \(\beta\le3+2\sqrt2\). In this region each derivative has exactly one zero, giving a unique maximum. Above the threshold the two critical points of \(H_\beta\) are precisely \(y_-,y_+\), a local maximum and minimum respectively. Its three-root interval is the displayed open interval in \(p\); the first and third roots are strict local maxima of \(F\), separated by a strict local minimum.

**4. Unique first-order switch.** At the lower spinodal endpoint \(p=h_{\min}/(1+h_{\min})\), the high-rate stationary pair is born by tangency while the low-rate maximum is strictly higher. At the upper spinodal endpoint \(p=h_{\max}/(1+h_{\max})\), the low-rate stationary pair annihilates by tangency and the high-rate maximum is strictly higher. The two local peak heights therefore cross at least once. To prove they cross only once, observe that, for fixed \(y>0\),
\[
\partial_p\log F_{\beta,p}(y)
=\frac{e^{(\beta-1)y}-1}{1+p(e^{(\beta-1)y}-1)},
\]
which is strictly increasing in \(y\). Along either stationary maximum the envelope theorem applies; hence the logarithm of the high-peak/low-peak ratio is strictly increasing in \(p\). Thus there is exactly one crossing \(p_*\), and the globally optimal rate changes discontinuously there. Since \(r=D(y/a)^2\), distinct maximizing values of \(y\) give distinct physical reset rates. The endpoint cases \(p=0,1\) each have their single obvious maximum. This proves the entire phase diagram.

## Verification

The standalone checker `checker.py` uses only Python's standard library. It verifies the closed-form critical points of \(H_\beta\), the sign structure below/at/above the critical ratio, the unique three-root window for several distinct geometries, the monotonic logarithmic peak-height ratio, the \(\beta=10\) two-rate coexistence example, and the \(R\equiv0\) and \(R\equiv a\) transform reductions. These are diagnostic finite checks. The proofs above, rather than numerical testing, establish all quantifiers, asymptotics and uniqueness assertions.

## Relationship to prior work

Bressloff (2022, arXiv:2203.04868), section 3, derives the exact mean threshold-reaction time for a *single* reset site when local time is retained; its equation (3.17) is recovered from the present single-atom initial-reset formula. Colantoni, D'Ovidio and Pagnini (2025) prove the inverse-local-time subordinator exponent for reflected Brownian motion reset to the **boundary itself**; this corresponds here to \(\mathcal A\equiv1\). Julián-Salgado, Dagdug and Boyer (2023/2024, arXiv:2311.11897) derive a two-site *first-hitting time for a fully absorbing boundary* and show discontinuous optimal rates in that different objective. Their first-hitting-time formula is closely related: its near-boundary initial-position derivative contains the same exponential mixture. The contribution assessed here is not the resolvent or the mixture formula in isolation, but the **sharp universal distance-ratio criterion \(3+2\sqrt2\)** and **unique weight-driven coexistence** for throughput of *cumulatively retained surface contact*, with the full threshold-time transform supplying its physical interpretation.

## Limitations

The theorem assumes one-dimensional reflection, Poisson relocation, strictly positive two-site reset distances and boundary local time retained across resets. It does not establish analogous critical ratios for higher dimensions, non-Poisson relocation, or finite threshold size optimization: at finite \(\ell\), the extra first-contact term may shift the optimal reset rates. Numerical constants are diagnostics, not independently certified computations. A general optimization theorem elsewhere for two-exponential mixtures or a boundary-contact specialization of distributed-resetting results might cover some or all of the phase diagram; independent literature assessment remains necessary.

## References

- P. C. Bressloff, *Threshold surface reactions and local time resetting*, arXiv:2203.04868 (first posted 2022-03-09), especially sections 2.3 and 3, equations (3.11)–(3.17): https://arxiv.org/abs/2203.04868
- P. Julián-Salgado, L. Dagdug, D. Boyer, *Diffusion with two resetting points*, arXiv:2311.11897 (first posted 2023-11-20), especially sections III–V: https://arxiv.org/html/2311.11897v4
- F. Colantoni, M. D'Ovidio, G. Pagnini, *Time reversal of Reflected Brownian Motion with Poissonian Resetting*, Journal of Statistical Physics **192**, 147 (2025), section 6: https://doi.org/10.1007/s10955-025-03527-5
