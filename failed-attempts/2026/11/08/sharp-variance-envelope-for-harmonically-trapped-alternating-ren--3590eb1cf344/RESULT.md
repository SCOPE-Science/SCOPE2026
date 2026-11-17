# Sharp variance envelope for harmonically trapped alternating-renewal swimmers

## Finding
For a one-dimensional particle in a harmonic trap, whose propulsion sign reverses after independent arbitrary positive run times with fixed mean, the stationary spatial variance depends on the run law through exactly one Laplace-transform value. **Deterministic run times uniquely minimize variance among every positive run-time distribution of the same mean.** The full sharp variance interval, including a nonattained ballistic upper endpoint, and its ordering under convex variability are explicit.

Let \(\kappa,v,m>0\), \(T>0\) almost surely with \(\mathbb E T=m\), and \(\varphi=\mathbb E[e^{-\kappa T}]\). Then
\[
\operatorname{Var}(X)=\frac{v^2}{\kappa^2}\left[1-\frac{2(1-\varphi)}{\kappa m(1+\varphi)}\right].
\]
For all such distributions, the **sharp** range is
\[
\frac{v^2}{\kappa^2}\left[1-\frac{2}{\kappa m}\tanh\left(\frac{\kappa m}{2}\right)\right]
\le \operatorname{Var}(X)<\frac{v^2}{\kappa^2}.
\]
The left endpoint occurs if and only if \(T=m\) almost surely. The upper endpoint is a supremum approached by fixed-mean two-point run laws, not attained. If \(T_1\preceq_{\rm cx} T_2\) in convex order at common mean, then the stationary variance for \(T_1\) is no larger than for \(T_2\), strictly smaller for distinct distributions in this convex order.

## Assumptions and scope
The athermal trajectory solves \(\dot X_t=-\kappa X_t+v\sigma_t\), with \(\sigma_t\in\{+1,-1\}\). At each renewal of independent identically distributed run lengths \(T\), the sign reverses (it does **not** choose an independent new sign). Construct the two-sided *stationary equilibrium renewal process*: the initial sign is symmetric; the interval containing time zero is length-biased, with position uniformly distributed therein. This construction is valid for every positive finite-mean \(T\), even with atoms, arithmetic support, or infinite second moment. The bounded stationary solution is \(X_t=v\int_0^\infty e^{-\kappa u}\sigma_{t-u}\,du\), with mean zero. These claims concern one-point stationary variance only, not the full spatial law or convergence rates.

## Proof
1. Put \(\varphi(s)=\mathbb E[e^{-sT}]\). Starting at a sign reversal, let \(M(t)\) denote the expected sign relative to its initial value. The renewal equation is \(M(t)=\Pr(T>t)-\int_{(0,t]}M(t-u)\,dF(u)\). Its Laplace transform is \(\widehat M(s)=(1-\varphi(s))/[s(1+\varphi(s))]\). This follows by multiplying the renewal equation by \(e^{-st}\) and using Fubini, since \(|M|\le1\).
2. At a stationary time the forward residual to the next reversal \(R\) satisfies \(\Pr(R>t)=m^{-1}\int_t^\infty\Pr(T>u)\,du\). Therefore its survival Laplace transform is \(1/s-(1-\varphi(s))/(ms^2)\), and the Laplace transform of its distribution is \((1-\varphi(s))/(ms)\). Conditioning on \(R\), the stationary sign covariance \(C(t)=\mathbb E[\sigma_0\sigma_t]\) obeys \(C(t)=\Pr(R>t)-\mathbb E[\mathbf1_{R\le t}M(t-R)]\). Hence
\[
\widehat C(s)=\frac1s-\frac{2(1-\varphi(s))}{ms^2(1+\varphi(s))}.
\]
3. The stable convolution representation, boundedness, stationarity and Fubini give \(\operatorname{Var}(X)=v^2\int_0^\infty\!\int_0^\infty e^{-\kappa(u+w)}C(|u-w|)\,du\,dw=(v^2/\kappa)\widehat C(\kappa)\). Substitution gives the stated exact formula.
4. Strict convexity of \(t\mapsto e^{-\kappa t}\) gives \(\varphi\ge e^{-\kappa m}\), equality exactly for a constant run. The right side of the formula is strictly increasing in \(\varphi\), since its derivative is \(4v^2/[\kappa^3m(1+\varphi)^2]>0\). This gives the exact unique minimum and convex-order comparison. Since \(0<\varphi<1\), the ballistic upper bound is strict. For \(0<\delta<m<L\), choose \(T=\delta\) with probability \((L-m)/(L-\delta)\) and \(T=L\) otherwise. Sending \(\delta\downarrow0\) and \(L\uparrow\infty\) makes \(\varphi\uparrow1\), proving sharpness. Continuous mixing of this law with \(\delta_m\) realizes all intermediate variances.

## Verification
Run `python3 verify.py` from the extracted artifact directory. The checker independently integrates the deterministic periodic orbit, solves Markov and Erlang-two stage models, verifies 143 exact-rational Markov identities, and tests mean-preserving spreads. It reports 468 passing assertions. The infinite-family claims follow from the renewal identities and Jensen's strict inequality, not finite enumeration.

## Relationship to prior work
Farago and Smith (arXiv:2401.01576, first public January 3, 2024) develop a general numerical approach to stationary non-Markovian run-and-tumble confinement for arbitrary waiting laws; their discussion compares exponential, semi-Gaussian and heavy-tailed examples. They do not in the inspected text state an all-waiting-laws sharp fixed-mean spatial-variance envelope. Guéneau, Majumdar and Schehr (arXiv:2306.09453) analyze a related trapped active particle driven by *resetting noise*, including periodic and Poisson resetting; its noise dynamics and reset protocol differ from sign-alternating renewal driving. Standard alternating-renewal correlation transforms are mathematical background. The contribution claimed here is the sharp fixed-mean extremal **classification**, including uniqueness, nonattainment and convex-order monotonicity, not invention of the renewal process or its general convolution tools.

## Limitations
The exact transform and Jensen proof do not classify stationary density shape, higher moments, arbitrary nonharmonic traps or nonsymmetric two-run laws. The general stationary sign-covariance transform is a classical renewal object: some earlier literature could implicitly contain the full variance formula or an equivalent convex-order theorem. Publication priority remains qualified. No independent validation or external certification is claimed.

## References
- O. Farago and N. R. Smith, *Confined run and tumble particles with non-Markovian tumbling statistics*, arXiv:2401.01576 (2024), https://arxiv.org/abs/2401.01576.
- M. Guéneau, S. N. Majumdar, and G. Schehr, *Active particle in a harmonic trap driven by a resetting noise: an approach via Kesten variables*, arXiv:2306.09453 (2023), https://arxiv.org/abs/2306.09453.
