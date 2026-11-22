# A unique noise-monotone observation time for a zero-initialized Ornstein–Uhlenbeck trajectory

## Finding

Fix any reversion rate \(a>0\). For the zero-initialized process \(dX_s=-aX_s\,ds+dW_s\) on \([0,1]\), observe exactly one value \(Y_t=X_t+\epsilon\), where independent centered Gaussian noise has variance \(\eta>0\). Choose \(t\in[0,1]\) to minimize the integrated conditional trajectory variance \(R_{a,\eta}(t)=\int_0^1\operatorname{Var}(X_s\mid Y_t)\,ds\).

**Theorem.** There is exactly one minimizing observation time \(t_{a,\eta}\), and it satisfies
\[
\frac12<t_{a,\eta}<T_a<1,
\]
where \(T_a\) is the unique root in \((1/2,1)\) of
\[
e^{4aT_a}=1+4aT_a e^{2a}.
\]
For each fixed \(a>0\), the map \(\eta\mapsto t_{a,\eta}\) is strictly increasing on \((0,\infty)\), with finite interior limiting position \(\lim_{\eta\to\infty}t_{a,\eta}=T_a\). More sharply, writing \(q_a(t)=(1-e^{-2at})/(2a)\) and \(G_a(t)=\int_0^1\operatorname{Cov}(X_s,X_t)^2\,ds\),
\[
T_a-t_{a,\eta}=\frac{G_a(T_a)e^{-2aT_a}}{-G_a''(T_a)}\frac1\eta+O_a(\eta^{-2}),
\qquad
G_a''(T_a)=\frac{e^{-2aT_a}-e^{-2a(1-T_a)}}{a}<0.
\]
Thus even arbitrarily noisy measurements favor a unique, nonterminal sampling time when the reversion is strictly positive. In the limiting nonreverting model, for each fixed \(\eta>0\), the optimal time tends to the Brownian-design value
\[
\lim_{a\downarrow0}t_{a,\eta}=\frac{3-6\eta+\sqrt{(3-6\eta)^2+96\eta}}8,
\]
and \(T_a=1-a/3+O(a^2)\) as \(a\downarrow0\).

## Assumptions and scope

The state is real-valued and has zero deterministic initial condition, unit diffusion variance, positive constant reversion \(a\), and known covariance parameters. There is one scalar point observation at an unrestricted time in the closed interval, with independent Gaussian noise of known variance \(\eta>0\). Risk is the unweighted integral over the full time interval of posterior state variance; this is neither parameter-estimation variance nor prediction at a single future endpoint. The noise-free time \(\eta=0\) is used only as a continuous limiting comparison.

## Proof

The covariance is
\[
K_a(s,t)=\frac{e^{-a|s-t|}-e^{-a(s+t)}}{2a},
\qquad q_a(t)=K_a(t,t)=\frac{1-e^{-2at}}{2a}.
\]
Gaussian conditioning gives
\[
R_{a,\eta}(t)=\int_0^1q_a(s)\,ds-\frac{G_a(t)}{q_a(t)+\eta}.
\]
Consequently minimize risk by maximizing \(J_{a,\eta}(t)=G_a(t)/(q_a(t)+\eta)\). Splitting the covariance-square integral at \(s=t\) gives the exact formula
\[
G_a(t)=\frac{2(1+e^{-2a})-(2+4at+e^{-2a})e^{-2at}-e^{-2a(1-t)}}{8a^3}.
\]
Its derivative has the factorization
\[
G_a'(t)=\frac{e^{-2a(t+1)}}{4a^2}F_a(t),
\quad F_a(t)=1+4at e^{2a}-e^{4at},
\quad F_a'(t)=4a(e^{2a}-e^{4at}).
\]
Thus \(F_a(0)=0\), \(F_a\) increases strictly to \(t=1/2\) and decreases strictly afterwards. It is positive at \(1/2\), while \(F_a(1)<0\), because \(\sinh(2a)>2a\). Hence \(G_a'\) is positive on \((0,T_a)\), zero at \(T_a\), and negative on \((T_a,1]\), with unique \(T_a\in(1/2,1)\).

For \(0<t<T_a\), define the noise response function
\[
E_a(t)=\frac{G_a(t)q_a'(t)}{G_a'(t)}-q_a(t).
\]
The derivative of the gain takes the exact form
\[
J_{a,\eta}'(t)=\frac{G_a'(t)}{(q_a(t)+\eta)^2}[\eta-E_a(t)].
\]
Crucially, \(q_a'(t)=e^{-2at}\), \(q_a''=-2aq_a'\), and the following nonstandard identity holds by direct differentiation of the exact \(G_a\) formula:
\[
G_a''(t)+2aG_a'(t)=\frac{e^{-2at}-e^{-2a(1-t)}}{a}.
\]
Therefore
\[
E_a'(t)=-\frac{G_a(t)q_a'(t)}{G_a'(t)^2}\,[G_a''(t)+2aG_a'(t)],
\]
which is strictly negative for \(0<t<1/2\) and strictly positive for \(1/2<t<T_a\). The expansion \(G_a(t)=((1-e^{-2a})/(2a))t^2+O_a(t^3)\) implies \(E_a(t)=-t/2+O_a(t^2)\); so \(E_a<0\) on \((0,1/2]\). As \(t\uparrow T_a\), \(E_a(t)\to+\infty\) because \(G_a(T_a)q_a'(T_a)>0\) and \(G_a'(t)\downarrow0\).

For each \(\eta>0\), there is consequently one and only one \(t_{a,\eta}\in(1/2,T_a)\) with \(E_a(t_{a,\eta})=\eta\). The derivative of \(J\) is positive before this point and negative after it, including the region \([T_a,1]\) where \(G_a'\le0\) and \(q_a'>0\). This proves the global unique optimum. Since \(E_a\) is strictly increasing on the right-hand interval, its inverse is strictly increasing in the noise variance.

At \(T_a\), \(G_a''<0\); expanding the stationary equation \(G_a'(t)(q_a(t)+\eta)-G_a(t)q_a'(t)=0\) around \(T_a\) gives the asserted \(\eta^{-1}\) expansion. Finally, as \(a\downarrow0\), the covariance converges uniformly to \(\min(s,t)\), giving \(q_a(t)\to t\) and \(G_a(t)\to t^2(1-2t/3)\). The unique Brownian optimality equation becomes \(2\eta(1-t)+t(1-4t/3)=0\), yielding the stated root. Expanding the defining equation for \(T_a\) near \(a=0\) gives \(T_a=1-a/3+O(a^2)\).

## Verification

The standalone `verify.py` uses symbolic differentiation and independent numerical integration to check the covariance-square formula, the gain derivative, and the decisive one-sign-switch identity; it also checks numeric optimization at multiple reversion rates and noise variances. Execute `python verify.py` with Python 3, SymPy and SciPy. Its 60 numeric covariance/optimization instances are checks, not substitutes for the analytic sign argument. Illustratively, at \(a=1\), \(T_a\approx0.801632185750\) and \(t_{a,0.1}\approx0.732468944318\); at \(\eta=100\), the optimum is \(0.801353826779\).

## Relationship to prior work

Ji and Müller (2016) give a general integrated trajectory-recovery optimal-design functional for noisy Gaussian measurements; the one-site specialization yields the conditioning objective used here but does not establish the exact OU zero-start geometry, global uniqueness, or strictly monotone noise response. Baran, Sikolya and Stehlík (2013) give optimal designs for a **stationary** OU *sheet* on monotonic sets, with a different covariance and sampling model. Sikolya and Baran (2018) treat a **stationary complex** OU process with a shifted mean and ordinary Kriging; their full-text results do not give this zero-initialized, independently noisy single-site theorem. The 2010 paper of Baldi Antognini and Zagoraiou gives exact optimal Kriging designs for a stationary exponential correlation with ordinary Kriging; its full text could not be inspected, leaving a bounded equivalence risk. The covariance-design functional itself is established prior methodology, not asserted as new.

## Limitations

No claim is made for nonzero/random initial states, stationary OU covariances, non-Gaussian observation noise, multiple sensors, interval averages, unknown reversion, weighted risk, or multivariate OU dynamics. The asymptotic result is at fixed positive \(a\) and is not uniform as \(a\downarrow0\). The evidence supports an independently reproducible analytic result, not a guarantee against inaccessible or unindexed publication equivalence. Independent mathematical validation has not been performed.

## References

- H. Ji and H.-G. Müller, *Optimal Designs for Longitudinal and Functional Data*, arXiv:1604.05375v1, first posted 18 April 2016, https://arxiv.org/abs/1604.05375.
- S. Baran, K. Sikolya, and M. Stehlík, *On the optimal designs for the prediction of Ornstein–Uhlenbeck sheets*, Statistics & Probability Letters 83 (2013), 1580–1587, available online 15 March 2013, https://doi.org/10.1016/j.spl.2013.03.003.
- K. Sikolya and S. Baran, *On the optimal designs for the prediction of complex Ornstein–Uhlenbeck processes*, arXiv:1808.03444v1, first posted 10 August 2018, https://arxiv.org/abs/1808.03444.
- A. Baldi Antognini and M. Zagoraiou, *Exact optimal designs for computer experiments via Kriging metamodelling*, Journal of Statistical Planning and Inference 140 (2010), 2607–2617, https://doi.org/10.1016/j.jspi.2010.03.027 (full text not inspected).
