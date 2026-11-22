# An atomic minimum-rate criterion and exact integer staircase for heterogeneous survey rotation

## Finding

Let \(\Lambda\) be a nonnegative, nonconstant random encounter rate with \(0<\mathbb E\Lambda<\infty\). A survey visits new, statistically independent sites. During each visit, the rate is drawn independently from the law of \(\Lambda\), is then fixed, and produces Poisson encounters. The objective is to maximize the probability of at least one encounter before a fixed deadline \(H>0\). Each relocation after the first costs \(c>0\) units of the deadline. Set
\[
\lambda_0=\operatorname*{ess\,inf}\Lambda,\qquad q=\Pr(\Lambda=\lambda_0).
\]
There is an **all-deadline no-rotation phase** if and only if
\[
\lambda_0>0,\quad q>0,\quad c\ge c_{\rm crit}:=\frac{-\log q}{\lambda_0}.
\]
In that phase, precisely one site is uniquely optimal at **every** \(H>0\), including at equality of costs. In every other case, rotation eventually becomes worthwhile and there is an infinite, strictly increasing sequence \(H_1<H_2<\cdots\) of finite, exact budget thresholds: at \(H_n\), exactly \(n\) and \(n+1\) sites tie globally, and between thresholds exactly one site count wins. No support size is skipped.

For any prescribed site count \(n\), equal observation durations are the unique optimum. Whenever rotation is potentially worthwhile, let \(\tau_*\) be the unique positive solution
\[
(\tau_*+c)\phi'(\tau_*)=\phi(\tau_*),\qquad
\phi(t)=-\log\mathbb E[e^{-\Lambda t}].
\]
The global integer optimum at deadline \(H\) is among the two feasible integers neighboring the continuous target \((H+c)/(\tau_*+c)\), with \(n=1\) imposed as a lower bound. In particular \(n_{\rm opt}(H)/H\to1/(\tau_*+c)\) for any choice of optimal count (including ties), and every threshold obeys
\[
n(\tau_*+c)-c<H_n<(n+1)(\tau_*+c)-c.
\]
The limiting criterion depends only on the *smallest possible encounter rate and the atom at that rate*, not on the remaining mixture shape. In particular, a continuous encounter-rate law with no atom at its lower endpoint has a finite preferred visit duration for **every** finite positive relocation cost.

## Assumptions and scope

For fixed \(H,c>0\), choose a positive integer \(n\) with \((n-1)c\le H\), and nonnegative observation durations \(t_1,\ldots,t_n\) summing to \(H-(n-1)c\). The first location is available without a relocation delay; every subsequent independent location requires exactly \(c\) units of unavailable observing time. Conditioned on iid site rates \(\Lambda_i\), their encounter counts are independent Poisson variables with means \(\Lambda_i t_i\). At least one detection suffices: a zero-detection schedule is specified in advance, with no benefit to extra observations after success. The site-rate law is known, iid across visits, nondegenerate, nonnegative, of finite strictly positive mean, and not changed by relocation or observation. All positive integer counts and all nonnegative durations satisfying the deadline are allowed. A relocation does not enhance the rate of a site already visited.

The expected no-detection probability is \(\prod_{i=1}^{n}L(t_i)\), where \(L(t)=\mathbb E[e^{-\Lambda t}]\); maximizing detection is equivalent to maximizing the log-survival exponent \(\sum_i\phi(t_i)\). No claim is made about correlated sites, adaptive site selection using other information, switching back to old sites, non-Poisson encounters, or alternative objectives (abundance estimation, expected total count, or time-to-first-detection).

## Proof

**1. Strict concavity and balanced visits.** For \(t>0\), exponential tilting by \(e^{-t\Lambda}\) gives
\[
\phi'(t)=\mathbb E_t\Lambda>0,\qquad
\phi''(t)=-\operatorname{Var}_t(\Lambda)<0.
\]
The inequalities are strict by nondegeneracy. The finite first moment gives the right derivative at zero \(\phi'(0)=\mathbb E\Lambda\); the tilt gives all higher derivatives needed away from zero. Thus \(\phi(0)=0\), and strict Jensen concavity shows that for each feasible \(n\), the unique maximizing durations are equal. Consequently its optimal exponent is
\[
F_n(H)=n\phi\!\left(\frac{H-(n-1)c}{n}\right).
\]

**2. A strictly decreasing marginal-departure function.** Extend site count to real \(x\in[1,1+H/c]\) and write \(t=(H+c)/x-c\), \(F(x;H)=x\phi(t)\). Define
\[
h(t)=(t+c)\phi'(t)-\phi(t).
\]
Then
\[
F_x=-h(t),\quad F_{xx}=\frac{(t+c)^2}{x}\phi''(t)<0,\quad
h(0)=c\mathbb E\Lambda>0,\quad h'(t)=(t+c)\phi''(t)<0.
\]
Therefore \(F\) is strictly concave in continuous count, and \(h\) can cross zero at most once.

**3. Exact asymptotic sign.** Put \(X=\Lambda-\lambda_0\ge0\), \(\psi(t)=-\log\mathbb E[e^{-tX}]\), so \(\phi(t)=\lambda_0t+\psi(t)\) and
\[
h(t)=c\lambda_0+(t+c)\psi'(t)-\psi(t).
\]
The essential infimum of \(X\) is zero. For every \(\varepsilon>0\), \(\Pr(X\le\varepsilon)>0\), and Laplace-transform bounds imply \(\psi(t)/t\to0\). The derivative \(\psi'(t)\downarrow0\) by concavity and that sublinear limit. If \(q>0\), dominated convergence gives \(\psi(t)\to-\log q\). As \(\psi'\) is nonnegative, decreasing and integrable on \([1,\infty)\), \(t\psi'(t)\to0\), hence
\[
\lim_{t\to\infty}h(t)=c\lambda_0+\log q \quad(q>0).
\]
If \(q=0\), then \(\psi(t)\to\infty\). Let \(g(t)=\psi(t)-t\psi'(t)\), which is nondecreasing because \(g'(t)=-t\psi''(t)\ge0\). If \(g\) were bounded by \(M\), differentiation of \(\psi(t)/t\), followed by its zero limit, would give \(\psi(t)/t=\int_t^\infty g(s)/s^2\,ds\le M/t\); this would bound \(\psi\), a contradiction. Thus \(g\to\infty\), and \(h(t)=c\lambda_0+c\psi'(t)-g(t)\to-\infty\). Combining the cases yields a finite positive root of \(h\) if and only if \(\lambda_0c+\log q<0\) when \(q>0\), or automatically when \(q=0\). Its absence is exactly the displayed all-deadline no-rotation condition; at equality \(h(t)>0\) for each finite \(t\), because \(h\) is strictly decreasing toward zero.

**4. Integer staircase with no skipped sizes.** If no root exists, \(h(t)>0\), so \(F\) strictly decreases in \(x\) at every deadline: \(n=1\) wins uniquely. If \(\tau_*\) exists, the strictly concave \(F(x;H)\) increases up to its continuous critical point \(x_*=(H+c)/(\tau_*+c)\) and decreases afterward (or decreases on the full domain if \(x_*\le1\)). This proves the two-neighbor integer rule.

For every \(n\ge1\), consider \(\Delta_n(H)=F_{n+1}(H)-F_n(H)\) for \(H\ge nc\). At \(H=nc\), \(\Delta_n=-F_n(nc)<0\). For \(H>nc\) put \(t_j=(H-(j-1)c)/j\); then \(t_{n+1}<t_n\) and
\[
\Delta_n'(H)=\phi'(t_{n+1})-\phi'(t_n)>0.
\]
By the mean-value theorem applied to \(F(x;H)\) between \(n\) and \(n+1\), \(\Delta_n(H)=-h(t_\xi)\) for some \(\xi\in(n,n+1)\). Sending \(H\to\infty\) with fixed \(n\) makes \(t_\xi\to\infty\); in the root-present case \(h(\infty)<0\), so \(\Delta_n\) eventually becomes positive. The intermediate-value theorem gives one and only one \(H_n>nc\) with \(\Delta_n(H_n)=0\). Strict concavity in site count implies \(\Delta_{n+1}(H_n)<0\) whenever \(n+2\) is feasible; otherwise \(H_{n+1}\) must exceed the feasibility boundary \((n+1)c\ge H_n\). Hence \(H_n<H_{n+1}\), and at any threshold exactly two neighboring integer counts tie, with no other count optimal. At their tie, the mean-value theorem forces \(x_*\in(n,n+1)\), yielding the strict displayed bounds on \(H_n\). They imply \(H_n\to\infty\) and \(n_{\rm opt}(H)/H\to 1/(\tau_*+c)\).

**5. Illustration and boundary.** For \(\Pr(\Lambda=1)=1/10\) and \(\Pr(\Lambda=10)=9/10\), the critical cost is \(\log 10\approx2.302585092994\). At \(c=1\), the continuous preferred dwell is \(\tau_*\approx0.501982104933\); at deadline \(H=3\), the optimal three-site plan has observation durations \(1/3\) and detection probability approximately \(0.9988829144\), compared with \(0.9950212932\) for a single site. If \(c=3\), one site wins for *every* positive deadline. A uniform rate on \([1,3]\) has the same positive lower endpoint as the two-atom law but no atom there; therefore no finite positive relocation cost can suppress eventual rotation for all deadlines. This sharp atom/no-atom distinction is part of the theorem, not an extrapolation from finite-rate examples.

## Verification

Run `python3 checker.py` in the same directory. The standard-library program independently evaluates finite-mixture Laplace exponents, numerical derivatives and strict-concavity consequences; it checks the two-rate threshold, integer optima, and the atomless uniform family. These finite computations are supplementary tests only: the claims for all rate distributions and all horizons follow from the analytic steps above. The test's printed assertion count is the count from its actual invocation, not a proof certificate.

## Relationship to prior work

Palencia et al. (2024) use simulated and field camera-trap rotations to study **precision of detection-rate estimates** under wildlife aggregation; the objective here is instead **at least one true detection**. Moore et al. (2014) and Moore and McCarthy (2016) already study maximizing this latter probability with Poisson visit rates, travel costs and repeated visits; their lognormal and gamma calculations motivate the general question and must not be claimed as new cases of the present analysis. Their specified-law results do not state the present sharp all-law low-rate-atom criterion or the complete all-integer, strict-threshold staircase, as judged from the publicly accessible full texts. General restart/deadline results of van Moorsel and Wolter (2006) and Lorenz (2016) supply closely related survival-product optimization and equi-hazard principles. The present proof establishes the additional exact distributional endpoint classification and the complete ordered integer phase diagram for exponentially mixed Poisson rates with fixed relocation overhead. Nishimura (1991) studies heterogeneous Poisson prey encounter and finite giving-up times, but maximizes long-run *gain per expected time* with stopping at the first item; that objective does not by itself imply the fixed-deadline product-of-failure classification proved here.

## Limitations

This is a theoretical statement for a known iid rate law, a single device or sequential team, identical new-site overhead, no false positives and fixed real-time budget. It makes no empirical claim that an actual wildlife detector obeys the exact Poisson-mixture model. If site rates are dependent, placement quality is known before sampling, relocation costs vary, or the target is estimation precision rather than mere detection, the conclusion can change. The threshold may be practically unachievable at relevant deadlines when the rate distribution is sharply concentrated near its lower endpoint. Historical novelty is supported only by inspected literature and mathematical-record comparisons, not guaranteed across all publications; independently conducted external validation has not occurred.

## References

1. Palencia, P., et al. (2024). *Clustered and rotating designs as a strategy to obtain precise detection rates in camera trapping studies*. Journal of Applied Ecology. First published 2024-05-27. https://doi.org/10.1111/1365-2664.14690
2. Moore, J. L., et al. (2014). *The Optimal Number of Surveys when Detectability Varies*. PLOS ONE. https://doi.org/10.1371/journal.pone.0115345
3. Moore, J. L. and McCarthy, M. A. (2016). *Optimizing ecological survey effort over space and time*. Methods in Ecology and Evolution. https://doi.org/10.1111/2041-210X.12564
4. van Moorsel, A. and Wolter, K. (2006). *Analysis of Restart Mechanisms in Software Systems*. IEEE Transactions on Software Engineering. https://doi.org/10.1109/TSE.2006.73
5. Lorenz, J.-H. (2016). *Completion Probabilities and Parallel Restart Strategies under an Imposed Deadline*. PLOS ONE. https://doi.org/10.1371/journal.pone.0164605
6. Nishimura, K. (1991). *Optimal patch residence time of a sit-and-wait forager*. Behavioral Ecology. https://doi.org/10.1093/beheco/2.4.283
