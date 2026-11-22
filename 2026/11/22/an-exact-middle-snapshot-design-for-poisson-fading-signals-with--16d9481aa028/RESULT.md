# An exact middle-snapshot design for Poisson fading signals with unknown sky background

## Finding

An ideal three-snapshot instrument estimating source amplitude, exponential decay rate, and unknown constant sky background has one and only one locally D-optimal interior observation date when the first and final observation dates are compulsory. The middle date moves **strictly earlier** as the background-to-source amplitude ratio increases. Both its short-horizon displacement and long-horizon limit are explicit.

Put \(q=\lambda T>0\), \(\rho=\beta/\theta>0\), \(c=q/(e^q-1)\), and \(h(z)=z-c(e^z-1)\). For \(0<z<q\), the unique optimum \(z_*=\lambda t_*\) solves

\[
2\frac{1-ce^{z_*}}{z_*-c(e^{z_*}-1)}-2+\frac1{1+\rho e^{z_*}}=0.
\]

The optimum satisfies \(\partial z_*/\partial\rho<0\). Define the unique limiting solutions \(z_0(q)\) and \(z_G(q)\) of \(h'/h=1/2\) and \(h'/h=1\), respectively, inside \((0,q)\). Then \(z_G(q)<z_*(q,\rho)<z_0(q)\) for every finite positive \(\rho\); these become equalities only in the respective infinite-background and zero-background limits. For fixed \(\rho>0\),

\[
\frac{t_*}{T}=\frac12-\frac{1+4\rho}{48(1+\rho)}q+O(q^2),\qquad q\downarrow0,
\]

and \(z_*(q,\rho)\to z_\infty(\rho)\in(1,2)\) as \(q\to\infty\), where \(z_\infty\) solves \(2/z-2+(1+\rho e^z)^{-1}=0\).

With \(\lambda=\theta=\beta=1\) and \(T=4\), the optimum is \(t_*=1.043396317665198\ldots\), and its Fisher determinant is \(2.013109816346372\ldots\) times that of the equally spaced choice \(t=2\).

## Assumptions and scope

Three equally exposed count measurements are independent, and their means are \(\mu(s)=\theta e^{-\lambda s}+\beta\) at times \(s\in\{0,t,T\}\), with strictly positive amplitude \(\theta\), decay rate \(\lambda\), constant background \(\beta\), and fixed final horizon \(T>0\). The free date lies strictly between the compulsory dates. The criterion is the determinant of Fisher information for **joint** inference of \((\theta,\lambda,\beta)\) at fixed nominal parameter values. Each snapshot is an instantaneous-rate idealization with equal effective exposure, **not** an overlapping time-integral of photon arrivals. Strictly positive background is assumed for the main parameter domain; one-sided limiting formulas extend to zero.

## Proof

**Step 1: exact determinant.** Write \(u=e^{-z}\), \(v=e^{-q}\), and \(\rho=\beta/\theta\). The three means are \(\theta(1+\rho)\), \(\theta(u+\rho)\), and \(\theta(v+\rho)\). The Jacobian of the mean vector with respect to \((\theta,\lambda,\beta)\) has row \((e^{-\lambda s},-\theta s e^{-\lambda s},1)\) at time \(s\). Its determinant, up to sign, equals

\[
\frac\theta\lambda(1-v)u\,h(z),\qquad h(z)=z-\frac{q}{e^q-1}(e^z-1).
\]

Since independent Poisson Fisher information equals \(J^\mathsf{T}\operatorname{diag}(1/\mu(s))J\), it follows by taking determinants that

\[
\det I(z)=\frac{(1-e^{-q})^2}{\theta\lambda^2(1+\rho)(e^{-q}+\rho)}\cdot\frac{e^{-2z}h(z)^2}{e^{-z}+\rho}.
\]

The common positive factor is independent of \(z\).

**Step 2: strict existence and uniqueness.** The function \(h\) vanishes at \(0\) and \(q\) and has \(h''(z)=-ce^z<0\). Strict concavity and its two zero endpoints show \(h(z)>0\) inside \((0,q)\). Thus the logarithm of the variable part of the Fisher determinant is

\[
L(z)=2\log h(z)-2z-\log(e^{-z}+\rho).
\]

Its second derivative obeys

\[
L''(z)=2\left(\frac{h''(z)}{h(z)}-\frac{h'(z)^2}{h(z)^2}\right)-\frac{\rho e^z}{(1+\rho e^z)^2}<0.
\]

Moreover \(L(z)\to-\infty\) at both endpoints. It therefore has exactly one critical point, the global maximizer. Setting \(L'(z)=0\) gives the stated equation. In particular, duplicating either endpoint produces zero determinant and is never optimal within the specified three-measurement problem.

**Step 3: background comparative statics and noise-model comparison.** Set

\[
G(z,\rho)=2h'(z)/h(z)-2+(1+\rho e^z)^{-1}.
\]

The foregoing strict concavity is precisely \(G_z=L''<0\). At every interior \(z\), \(G_\rho=-e^z/(1+\rho e^z)^2<0\). The implicit function theorem gives \(dz_*/d\rho=-G_\rho/G_z<0\). As \(\rho\to0^+\) or \(\rho\to\infty\), the score converges on every compact interior subinterval to \(2h'/h-1\) or \(2h'/h-2\), respectively. Those equations each have one root by strict log-concavity, and the roots stay interior since the score diverges with opposite signs at the endpoints. The limiting roots therefore exist and satisfy the stated strict ordering. For independent homoscedastic Gaussian observations with the identical exponential-plus-constant mean curve, the determinant is proportional to \(\det(J)^2\propto e^{-2z}h(z)^2\); its middle-date optimum consequently satisfies \(h'/h=1\). The equality of the **Jacobian factor** is not claimed as new; the Poisson mean-variance weighting is the distinguishing feature.

**Step 4: two temporal limits.** For \(q\downarrow0\), use \(c=1-q/2+q^2/12+O(q^4)\) and set \(z=qv\). Uniformly for \(v\) in compact subsets of \((0,1)\),

\[
h(qv)=\frac{q^2v(1-v)}2-\frac{q^3v(2v^2-3v+1)}{12}+O(q^4).
\]

Substitution into \(L'(qv)=0\), followed by the implicit function theorem at \(v=1/2\), yields \(v=1/2-q(1+4\rho)/[48(1+\rho)]+O(q^2)\). The strict maximum and uniformly vanishing determinant at the endpoint scales justify selecting this interior branch. For \(q\to\infty\), \(c=q/(e^q-1)\to0\). On any fixed bounded \(z>0\), \(h(z)\to z\) and \(h'(z)\to1\), whence the score tends to \(2/z-2+(1+\rho e^z)^{-1}\). This limit is strictly decreasing, positive at \(z=1\) and negative at \(z=2\). The finite-horizon score is also strictly decreasing and its root is therefore trapped in any arbitrarily small interval around the unique limit root for all sufficiently large \(q\). This proves the long-horizon limit with \(1<z_\infty<2\).

## Verification

The standalone \(check.py\) uses no third-party packages. Run `python3 check.py` in a directory containing this document and the script. It evaluates the analytic determinant against the direct three-by-three Jacobian determinant, solves the stationarity equation by bracketing, tests global grid dominance and strict comparative statics across reproducibly sampled parameter sets, and checks short- and long-horizon limits and the numerical example. The exact analytic inequalities above, not the numerical tests, prove the statements over all positive parameters.

## Relationship to prior work

Dette and Neugebauer (1997) and Han and Chaloner (2003) investigate optimal experimental designs for exponential regression. Their homoscedastic Gaussian observation models share the unweighted mean-function Jacobian; that classical factor is acknowledged here. The accessible full text of Shi, Zhang and Wong (2019), especially its exponential-model section, explicitly writes the three-parameter exponential-plus-background mean with independent \(N(0,\sigma^2)\) errors and treats general Bayesian numerical design. The present result instead addresses independent Poisson counts with source-dependent variance, precisely two pinned observation times, and a single free middle time, supplying strict uniqueness and monotonic dependence on background. Bélanger (2013) discusses photon counting and transient event detection, rather than joint three-parameter information-maximizing snapshot timing. Pauw and Tardif (2012) optimize division between separate sample and background measurement times; their decision variable and estimand differ. A 2026 fluorescence-lifetime preprint treats background-aware Poisson information and time-gated selection by numerical candidate-library optimization; only its abstract was inspected, leaving broader overlap as a documented residual risk. Published published-finding corpus results on pinned two-exponential-mode measurements and on Poisson Gaussian-plume sensor geometry concern different forward maps and free variables, and neither of their available summaries implies this Poisson single-exponential temporal monotonicity law.

## Limitations

The result is for an intentionally narrow constrained instrument design: no finite integration windows, readout overhead, unknown start-time shift, nonconstant background, intrinsic source stochasticity, detector saturation, prior uncertainty, or unrestricted choice of three dates is modeled. Local D-optimality is not global Bayesian or minimax optimality. The 1997 and 2003 original papers were not obtained in full; bibliographic abstracts and a detailed 2019 reproduction of their error model support only a provisional historical-priority assessment. The newer lifetime-imaging work was available only as an abstract in this inspection, so priority requires independent review.

## References

- Dette, H. and Neugebauer, H.-M. (1997). *Bayesian D-optimal designs for exponential regression models*. Journal of Statistical Planning and Inference 60, 331–349. https://doi.org/10.1016/S0378-3758(96)00131-0
- Han, C. and Chaloner, K. (2003). *D- and c-optimal designs for exponential regression models used in viral dynamics and other applications*. Journal of Statistical Planning and Inference 115, 585–601. https://doi.org/10.1016/S0378-3758(02)00175-1
- Pauw, B. R. and Tardif, S. (2012). *The optimal division between sample and background measurement time for photon counting experiments*. https://arxiv.org/abs/1210.5329
- Bélanger, G. (2013). *On Detecting Transient Phenomena*. https://arxiv.org/abs/1303.7408
- Shi, Y., Zhang, Z. and Wong, W. K. (2019). *Particle swarm based algorithms for finding locally and Bayesian D-optimal designs*. https://doi.org/10.1186/s40488-019-0092-4
- Sumaya-Martinez, J. and Torres-Garcia, E. (2026). *Fisher-Information-Driven Adaptive Acquisition for Photon-Efficient FLIM: A Dual-Implementation Framework for TCSPC and Programmable Time-Gating*. https://arxiv.org/abs/2601.00490
