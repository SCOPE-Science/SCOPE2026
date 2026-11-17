# A logarithmic housekeeping clock for active-matter battery charging

## Finding

In the two-state active-matter battery of Lin, Liu and Ma [1], a positive constant housekeeping cost changes the optimum charging duration from infinite to finite. The precise singular law at small housekeeping is determined here for **every fixed finite positive active affinity**, and the whole optimizer curve is classified in the weak-affinity (linear-response) scaling.

Let \(\beta,E,a,k_{\rm c}>0\), let \(p_0=(1+e^{\beta E})^{-1}\), \(p_a=(1+e^{\beta(E-a)})^{-1}\), \(d=p_a-p_0>0\), and \(\lambda=2k_{\rm c}\cosh[\beta(a-E)/2]\). Put \(s=\lambda t\), \(y=1-e^{-s}\), and
\[
 f(y)=\frac{D_{\rm KL}(\operatorname{Bern}(p_0+dy)\Vert\operatorname{Bern}(p_0))}{\beta a d},\qquad
 h=\frac{\mathcal P_{\rm hk}}{\lambda a d}>0,\qquad \rho=f(1).
\]
The fuel-to-storage efficiency is precisely
\[
 \eta_h(s)=\frac{f(1-e^{-s})}{1-e^{-s}+hs},\qquad 0<\rho<1.
\]

**Finite-affinity weak-housekeeping law.** For every fixed \(\beta,E,a,k_{\rm c}>0\) there exists \(h_0>0\) such that for all \(0<h<h_0\), \(\eta_h\) has exactly one global maximizer \(s_h\in(0,\infty)\), and, as \(h\downarrow0\),
\[
 s_h=\log\frac1h+\log\frac{1-\rho}{\rho}+O\bigl(h\log(1/h)\bigr),
\]
\[
 \max_{s>0}\eta_h(s)
 =\rho-\rho h\left[\log\frac1h+\log\frac{1-\rho}{\rho}+1\right]
 +O\bigl(h^2\log^2(1/h)\bigr).
\]
In particular, a **logarithmically divergent** optimum charging time coexists with an **\(h\log(1/h)\)** loss in the best fuel efficiency. The constants in the remainders can depend on the fixed physical parameters.

**Complete linear-response clock.** In the simultaneous weak-affinity limit \(\beta a\to0\) with \(h\) held fixed, the efficiency becomes
\[
 \eta_h^{\rm LR}(s)=\frac{(1-e^{-s})^2}{2(1-e^{-s}+hs)}.
\]
For every \(h>0\), this function has exactly one global maximizer \(s_h^{\rm LR}\), strictly decreasing in \(h\), and \(s_h^{\rm LR}>s_p\), where \(s_p=1.256431208626\ldots\) is the unique strictly positive solution of \(e^{s_p}=1+2s_p\). The maximizer is the unique solution on \((s_p,\infty)\) of
\[
 h=\frac{1-e^{-s}}{e^s-1-2s}.
\]
Write \(y_p=1-e^{-s_p}\). At the weak- and strong-housekeeping endpoints,
\[
 \begin{aligned}
 s_h^{\rm LR}&=\log(1/h)+2h\log(1/h)+O\bigl(h^2\log^2(1/h)\bigr), &&h\downarrow0,\\
 \max\eta_h^{\rm LR}&=\tfrac12-\tfrac h2[\log(1/h)+1]+O\bigl(h^2\log^2(1/h)\bigr), &&h\downarrow0,\\
 s_h^{\rm LR}&=s_p+\frac{y_p}{(2s_p-1)h}+O(h^{-2}), &&h\to\infty,\\
 \max\eta_h^{\rm LR}&=\frac{y_p^2}{2s_p h}+O(h^{-2}), &&h\to\infty.
 \end{aligned}
\]
This quantifies the crossover from the indefinitely long ideal optimum to the familiar maximum-power clock, while furnishing the singular logarithmic selection rule absent from the forward model.

## Assumptions and scope

Charging starts at thermal equilibrium \(p_0\) and obeys the exact two-state master equation with **constant**, **positive** active affinity \(a\) and fixed relaxation rate \(\lambda\). The housekeeping rate \(\mathcal P_{\rm hk}\) is constant, positive and does not alter the transition rates. Only the charging duration is optimized; the affinity, barrier, load, temperature, and housekeeping rate are not optimized over time. The single-run stored resource is the excess relative-entropy free energy above the equilibrium state; it is not the total work delivered after a finite discharge. All logarithms are natural. The finite-affinity theorem concerns asymptotically small \(h\) at fixed physical parameters, **not** all positive \(h\). The separate linear-response theorem applies to every positive \(h\) within that limiting model.

## Proof

**1. Exact reduction and endpoint inequalities.** The parent model gives \(p(t)=p_0+d(1-e^{-\lambda t})\), stored free energy \(\beta^{-1}D_{\rm KL}\), input interface work \(ad(1-e^{-\lambda t})\), and housekeeping expenditure \(\mathcal P_{\rm hk}t\) [1]. Dividing numerator and denominator by \(ad\) gives the stated \(\eta_h\). Differentiating the Bernoulli divergence yields
\[
 f'(y)=\frac{1}{\beta a}\log\frac{(p_0+dy)(1-p_0)}{p_0(1-p_0-dy)},\qquad
 f''(y)=\frac{d}{\beta a(p_0+dy)(1-p_0-dy)}>0.
\]
The stationarity identity \(\log[p_a/(1-p_a)]-\log[p_0/(1-p_0)]=\beta a\) implies \(f'(1)=1\). Also \(f(0)=f'(0)=0\), so strict convexity gives \(0<f(1)<f'(1)=1\). Denote \(\rho=f(1)\). For \(s\downarrow0\), \(f(1-e^{-s})=\Theta(s^2)\), hence \(\eta_h(s)\to0\); for \(s\to\infty\) and any \(h>0\), \(\eta_h(s)\to0\). Thus the maximum is attained at a positive finite \(s\).

**2. Critical-branch uniqueness at small housekeeping.** Set \(u=e^{-s}\), \(y=1-u\),
\[
 Q(y)=yf'(y)-f(y)=\int_0^y z f''(z)\,dz>0,\qquad
 B(s)=f(y)-suf'(y).
\]
Direct differentiation gives, after multiplication by the strictly positive denominator squared,
\[
 \operatorname{sgn}\eta_h'(s)=\operatorname{sgn}\bigl[uQ(y)-hB(s)\bigr].
\]
For the ideal case \(h=0\) this is strictly positive for every \(s>0\), so its supremum \(\rho\) occurs only as \(s\to\infty\). On every fixed compact interval bounded away from zero, \(uQ(y)>0\). Near zero, writing \(c=f''(0)/2>0\), one has \(uQ(y)=cs^2+O(s^3)\) and \(B(s)=-cs^2+O(s^3)\), so the derivative numerator is positive there for all sufficiently small \(h\) (indeed uniformly for bounded \(h\)). It follows that, for any prescribed sufficiently large \(S\), the derivative is positive on \((0,S]\) when \(h\) is small enough.

As \(s\to\infty\), smoothness at \(y=1\), \(f(1)=\rho\), and \(f'(1)=1\) give
\[
 Q(1-e^{-s})=1-\rho+O(e^{-s}),\qquad B(s)=\rho+O(se^{-s}).
\]
Choose \(S\) sufficiently large that \(B(s)>0\) for \(s\ge S\). The threshold function
\[
 T(s)=\frac{e^{-s}Q(1-e^{-s})}{B(s)}
 =\frac{1-\rho}{\rho}e^{-s}\left[1+O(se^{-s})\right]
\]
has \(T'(s)=-(1-\rho)e^{-s}/\rho\,[1+O(se^{-s})]<0\) for all \(s\ge S\); this differentiated expansion is valid because \(f\) is smooth on the closed interval. For all small enough \(h\), the derivative is positive before \(S\), changes sign exactly once where \(T(s)=h\), and is negative afterward. Hence the global maximizer is unique in that regime.

**3. Finite-affinity asymptotics.** The equation \(T(s_h)=h\), with \(s_h\to\infty\), yields
\[
 e^{-s_h}=\frac{\rho}{1-\rho}h\left[1+O(h\log(1/h))\right],
\]
which proves the clock law. Taylor expansion at \(y=1\) gives \(f(1-u)=\rho-u+O(u^2)\), and therefore, uniformly for \(u=O(h)\), \(s=O(\log(1/h))\),
\[
 \frac{f(1-u)}{1-u+hs}
 =\rho-(1-\rho)u-\rho hs+O(u^2+uhs+h^2s^2).
\]
Substituting the clock law proves the claimed two-term efficiency expansion with remainder \(O(h^2\log^2(1/h))\). These are asymptotics of the true global optimizer, not merely a stationary branch.

**4. Complete linear-response branch.** For fixed \(\beta E\), the Bernoulli divergence has quadratic expansion \(D_{\rm KL}(\operatorname{Bern}(p_0+dy)\Vert\operatorname{Bern}(p_0))=d^2y^2/[2p_0(1-p_0)]+O(d^3)\), and \(d=\beta a p_0(1-p_0)+O(a^2)\). Thus \(f(y)\to y^2/2\) as \(\beta a\to0\), uniformly for \(0\le y\le1\) at fixed \(\beta E\), yielding \(\eta_h^{\rm LR}\). Its derivative has the sign of
\[
 y\{yu+h(2su-y)\}.
\]
The positive solution \(s_p\) of \(e^s=1+2s\) is unique: the function \(e^s-1-2s\) is initially negative and becomes strictly increasing after \(s=\log 2\). For \(s\le s_p\) the derivative is positive. For \(s>s_p\), stationarity is equivalent to \(h=H(s)\), with
\[
 H(s)=\frac{1-e^{-s}}{e^s-1-2s}.
\]
Its derivative has the sign of \(4-e^s-(3+2s)e^{-s}\). This expression is zero at \(s=0\), with derivative \(-e^s+(1+2s)e^{-s}<0\) for \(s>0\), by \(e^{2s}>1+2s\). Thus \(H\) is strictly decreasing for \(s>s_p\), with limits \(+\infty\) at \(s_p\) and zero at infinity. It has exactly one intersection with each \(h>0\), and the efficiency changes from increasing to decreasing there. The implicit function theorem gives strict decrease of the optimizer with \(h\).

For \(h\downarrow0\), expansion of \(H(s)=e^{-s}[1+2se^{-s}+O(s^2e^{-2s})]\) yields \(s_h^{\rm LR}=\log(1/h)+2h\log(1/h)+O(h^2\log^2(1/h))\); substitution into \(\eta_h^{\rm LR}\) gives its efficiency expansion. For \(h\to\infty\), expand \(H(s)\) at its simple pole \(s=s_p\):
\[
 H(s)=\frac{y_p}{(2s_p-1)(s-s_p)}+O(1).
\]
Inversion gives the strong-housekeeping clock law, and substituting \(s=s_p+O(h^{-1})\) gives the efficiency law. This completes the complete linear-response classification.

## Verification

Run `python3 verify.py` using the Python standard library. The program checks the implicit optimizer identities, derivative signs, small- and large-cost asymptotic predictions, positivity/convexity relations, and finite-affinity asymptotics across several explicit parameter settings. On the included version, it reports `PASS: 458 deterministic checks (all-parameter proofs are analytic).` The checks are finite consistency diagnostics; the all-parameter uniqueness, endpoint laws, and asymptotic quantifiers are established in the proof above.

## Relationship to prior work

Lin, Liu and Ma [1] give the exact two-state charge dynamics, relative-entropy energy and full housekeeping-corrected efficiency (their Eqs. (1), (4), (7) and (16)); they report a finite-time full-efficiency maximum and plot the maximum full efficiency against housekeeping, and give an analytic expression for **efficiency at maximum power** in linear response (their Eq. (17)). These are not new here. The distinction is the explicit asymptotically optimal **charging duration**, its rigorous weak-housekeeping logarithmic constant, the two-term loss in **maximum full efficiency**, and uniqueness/strict housekeeping monotonicity throughout the **linear-response** family. The published efficiency-at-maximum-power point is not the maximum-efficiency point at finite housekeeping. Lei, Lin, Ou and Ma [2] establish the passive RC power-efficiency curve and an optimal multi-step charging protocol, without the present constant-housekeeping stopping law. General single-exponential charging formulas are therefore acknowledged as shared structure; the singular optimizer classification and its finite-affinity coefficient are the specific extension.

## Limitations

The all-cost uniqueness theorem is proved only in the linear-response limiting model, while full finite-affinity uniqueness is proved for sufficiently small housekeeping, not arbitrarily large housekeeping. Error constants in the small-housekeeping expansions are not uniform as active affinity vanishes or grows without bound, or as temperature and occupation approach singular limits. The result optimizes **one fixed-affinity charging stroke** and does not claim globally optimal time-dependent affinity, discharge scheduling, housekeeping feedback, storage leakage, or experimental realization. The result does not establish a general model-independent theorem for arbitrary battery dynamics or a new thermodynamic fluctuation relation. Independent publication-priority assessment has not been performed.

## References

[1] Y.-Q. Lin, R.-H. Liu and Y.-H. Ma, *Active-Matter Battery*, arXiv:2610.00428v1, first publicly submitted 2026-09-30, https://arxiv.org/html/2610.00428v1 .

[2] J.-R. Lei, Y.-Q. Lin, S.-G. Ou and Y.-H. Ma, *Universal power-efficiency trade-off in battery charging*, Frontiers of Physics 20 (2025), article 042202, https://doi.org/10.15302/frontphys.2025.042202 .
