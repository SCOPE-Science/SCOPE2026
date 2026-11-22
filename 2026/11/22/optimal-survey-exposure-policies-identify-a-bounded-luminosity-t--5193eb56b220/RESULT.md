# Optimal survey exposure policies identify a bounded luminosity-threshold distribution

## Finding

Let \(T\) denote a source-specific exposure threshold at the outer edge of an idealized flux-limited survey. An entire distribution of these thresholds can be recovered **solely from the optimal exposure durations** chosen as the per-pointing overhead varies, without observing the attained detection rates. For any continuous strictly interior-positive threshold density on a bounded nonzero interval, the optimal dwell time is uniquely defined at every positive overhead, rises strictly across the complete support interval, and yields an explicit inversion formula.

Put \(0<a<b<\infty\), \(0<\gamma<1\), and let \(f\) be a continuous probability density, zero outside \([a,b]\), strictly positive on \((a,b)\). Write

\[
H(t)=\int_a^b\min\{(t/s)^\gamma,1\}\,f(s)\,ds,\qquad R_u(t)=\frac{H(t)}{t+u}.
\]

For every overhead \(u>0\), there is a unique maximizer \(t_*(u)\in(0,b)\). The map \(u\mapsto t_*(u)\) is a strictly increasing bijection from \((0,\infty)\) to \((0,b)\). Let \(U:(0,b)\to(0,\infty)\) be its inverse. Then

\[
H(t)=\exp\!\left[-\int_t^b\frac{ds}{s+U(s)}\right],\quad
f(t)=\frac{H(t)}{\gamma[t+U(t)]^2}\left[tU'(t)-(1-\gamma)(t+U(t))\right]
\]

for \(a<t<b\). This is a full ideal-data identifiability theorem, not just recovery of a moment or parameter. In addition,

\[
U(t)=\frac{1-\gamma}{\gamma}t\quad (0<t\le a),\qquad
 tU'(t)>(1-\gamma)(t+U(t))\quad(a<t<b).
\]

Thus the first departure from the universal small-exposure straight line identifies \(a\), while \(b=\lim_{u\to\infty}t_*(u)\). The low-overhead optimum is exactly

\[
t_*(u)=\frac{\gamma}{1-\gamma}u\quad\text{for}\quad 0<u\le\frac{1-\gamma}{\gamma}a.
\]

If \(f(s)\sim c(b-s)^\beta\) near \(b\), where \(c>0\) and \(\beta>0\), the approach to the highest threshold obeys the sharp law

\[
b-t_*(u)\sim\left[\frac{b(\beta+1)}{\gamma c\,u}\right]^{1/(\beta+1)}\qquad(u\to\infty).
\]

## Assumptions and scope

The statistical object is an independent source-threshold variable \(T\) with the above density \(f\). Its support endpoints \(a,b\) are finite and strictly positive. The density is continuous on the nonnegative real axis after extension by zero, and its positivity is assumed only in the open support. All integrals and derivatives below are classical for \(0<t<b\), and the derivative formula is understood at every strictly interior point.

The count exponent \(q\) of a radially distributed source population is related by \(\gamma=q/4\). Indeed, when point-source flux sensitivity improves proportionally to the square root of exposure duration, the detection radius scales as \(L^{1/2}t^{1/4}\); a count law proportional to radius to the power \(q\) then gives fraction \(\min\{(t/T)^{q/4},1\}\) up to a fixed outer horizon. Uniform Euclidean volume corresponds to \(q=3\), hence \(\gamma=3/4\). The result requires \(0<q<4\). The objective is the ideal continuous field-throughput proxy of repeated independent fields with positive per-field overhead \(u\), not a finite-integer telescope scheduling guarantee.

## Proof

**Detection transform.** Define, for \(0<t<b\),

\[
J(t)=\int_{\max\{t,a\}}^b s^{-\gamma}f(s)\,ds.
\]

Splitting the integral at \(s=t\) yields

\[
H(t)=\int_a^{\min\{t,b\}}f(s)\,ds+t^\gamma J(t),\quad
H'(t)=\gamma t^{\gamma-1}J(t),
\]

because the boundary terms cancel. For all \(0<t<b\), \(J(t)>0\) and

\[
H''(t)=\gamma(\gamma-1)t^{\gamma-2}J(t)-\frac{\gamma}{t}f(t)<0.
\]

In particular \(H\) is strictly increasing and strictly concave until \(b\). Since \(a>0\), \(H(t)=Ct^\gamma\) near zero, where \(C=\int_a^b s^{-\gamma}f(s)\,ds>0\). We also have \(H(b)=1\), \(H'(b-)=0\), and \(H(t)=1\) for \(t\ge b\).

**Existence and uniqueness.** The sign of the derivative of \(R_u\) equals the sign of

\[
Q_u(t)=(t+u)H'(t)-H(t).
\]

For \(0<t<b\), \(Q'_u(t)=(t+u)H''(t)<0\). As \(t\downarrow0\), \(Q_u(t)\sim\gamma C u\,t^{\gamma-1}>0\), and \(Q_u(b-)=-1\). Therefore exactly one critical point occurs inside \((0,b)\), the unique strict global maximum. Beyond \(b\), \(R_u(t)=1/(t+u)\) decreases.

**Policy inversion.** Solving \(Q_u(t)=0\) for overhead defines

\[
U(t)=\frac{H(t)}{H'(t)}-t,
\quad U'(t)=-\frac{H(t)H''(t)}{[H'(t)]^2}>0.
\]

Near zero, \(U(t)=(1-\gamma)t/\gamma\to0\); near \(b\), \(H'(t)\to0\), so \(U(t)\to\infty\). It follows that \(U\) is the inverse of the optimal-policy function for all positive overheads.

From \(H'/H=1/(t+U(t))\) and \(H(b)=1\), integration gives exactly

\[
H(t)=\exp\!\left[-\int_t^b \frac{ds}{s+U(s)}\right].
\]

Differentiating the relation \(H'=H/(t+U)\) gives \(H''=-HU'/(t+U)^2\). Differentiating \(H'=\gamma t^{\gamma-1}J\) and using \(J'=-t^{-\gamma}f(t)\) gives \(\gamma f(t)=-tH''(t)-(1-\gamma)H'(t)\). Substitution proves the stated exact inverse-density formula. Every piece of \(f\) follows from the inverse curve, and different positive continuous densities cannot share it.

**Sharp curvature, support detection, and low overhead.** The density formula gives

\[
tU'(t)-(1-\gamma)[t+U(t)]=\frac{\gamma f(t)[t+U(t)]^2}{H(t)}.
\]

It is zero when \(t\le a\) and strictly positive on \((a,b)\). With \(H(t)=Ct^\gamma\) below \(a\), \(U(t)=(1-\gamma)t/\gamma\) there. Consequently the first departure from that line is exactly at \(a\). Applying the inverse map proves the low-overhead formula including its endpoint.

**Endpoint asymptotics.** Suppose \(f(s)\sim c(b-s)^\beta\) at \(b\), with \(c,\beta>0\). Then

\[
J(t)\sim\frac{c b^{-\gamma}}{\beta+1}(b-t)^{\beta+1},\quad
H'(t)\sim\frac{\gamma c}{b(\beta+1)}(b-t)^{\beta+1}.
\]

As \(H(t)\to1\), the inverse policy obeys \(U(t)\sim b(\beta+1)[\gamma c]^{-1}(b-t)^{-\beta-1}\). Inverting this equivalent gives the claimed asymptotic. No finite grid computation is used to infer these infinite-domain conclusions.

## Verification

`verify_policy.py` is a standalone standard-library numerical checker for the exactly normalized smooth density \(f(s)=6(s-1)(2-s)\) on \([1,2]\), with \(\gamma=3/4\). It computes the detection transform through exact analytic primitives, checks the analytic derivative identities and inverse-density formula on a deterministic grid, solves each optimality equation by bisection, and checks the unique optimizer against sampled alternatives. It also checks the low-overhead law and the leading high-overhead asymptotic for three large overheads. Reproduce using `python verify_policy.py` in the extracted package. A successful run prints `PASS 139 assertions`.

These are finite numerical diagnostics only; the global quantifiers and uniqueness come from the preceding analytic argument, not from checked grid points.

## Relationship to prior work

Macquart (2011, arXiv:1106.5817) gives the source-count/sensitivity formulation and finite-volume effects for fast-transient surveys. Macquart (2014, arXiv:1406.5790; first public June 23, 2014) solves **forward** sensitivity-versus-area optimization in slow-transient radio surveys for specified power-law luminosity functions and survey geometries. Its known homogeneous low-overhead optimum is consistent with the special \(\gamma=3/4\) linear behavior above, which is not claimed as a discovery in isolation. The claim here is different: the entire otherwise unknown bounded threshold density is uniquely recoverable from the continuously varying *choice of optimal dwell time* alone, with an exact positive-density curvature certificate and support-tail asymptotics. No such result was found in the inspected Macquart texts or relevant indexed mathematical result summaries.

The classic Breeden–Litzenberger relationship reconstructs a state distribution from a complete family of *observed derivative-price values* across strikes. The present theorem reconstructs a detection distribution from *optimal exposure choices* across overheads, with unknown attained values; it is not a claimed discovery of generic second-derivative inversion. The extent to which older generalized revealed-preference or inverse-optimization theory may imply the exact statement remains a historical-priority risk.

## Limitations

The theorem concerns an idealized expected-fraction model, a known exponent \(\gamma\), compact continuous source threshold support, a continuum of noiseless exactly optimal exposures indexed by an adjustable overhead, and no exposure-dependent incompleteness beyond geometric saturation. The inverse uses differentiation of the policy curve and is potentially very ill-conditioned with noisy decisions; no statistical stability rate, finite-sample estimator, correlated-field model, finite survey scheduling theorem, or physical flux completeness assessment is asserted. The classification does not apply unchanged for \(\gamma\ge1\), discontinuous threshold laws, or unknown heterogeneous detection exponents. Publication priority has not been independently established.

## References

1. J.-P. Macquart, *Detection Rates for Surveys for Fast Transients with Next Generation Radio Arrays*, arXiv:1106.5817, first public June 28, 2011. https://arxiv.org/abs/1106.5817
2. J.-P. Macquart, *Optimization of Survey Strategies for Detecting Slow Radio Transients*, arXiv:1406.5790, first public June 23, 2014; *Publications of the Astronomical Society of Australia* 31, e026. https://arxiv.org/abs/1406.5790 ; https://doi.org/10.1017/pasa.2014.27
3. D. T. Breeden and R. H. Litzenberger, *Prices of State-Contingent Claims Implicit in Option Prices*, *Journal of Business* 51 (1978), 621–651. https://doi.org/10.1086/296025
