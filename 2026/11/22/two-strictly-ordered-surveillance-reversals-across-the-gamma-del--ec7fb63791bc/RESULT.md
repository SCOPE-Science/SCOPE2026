# Two strictly ordered surveillance reversals across the gamma-delay shape boundary

## Finding

Let incidence grow exponentially until time zero and remain constant thereafter. Compare two normalized, noise-free surveillance streams formed by convolving this incidence with delay distributions of the **same mean**: an exponential delay and a gamma delay with arbitrary real shape \(\nu>0\). Their reported-count rankings reverse exactly once, and their instantaneous **logarithmic-growth** rankings reverse exactly once at a **strictly later** positive time, for every \(\nu\ne1\) and every positive pre-halt growth rate and mean delay. The direction of both reversals switches sharply at \(\nu=1\).

For \(\nu>1\), the gamma-delayed count starts below the exponentially delayed count and ends above it; its instantaneous logarithmic growth starts greater and eventually becomes smaller. For \(0<\nu<1\), **both inequalities reverse**. The ratio of reported counts has a unique strict maximum if \(\nu>1\), a unique strict minimum if \(0<\nu<1\), and approaches one from the appropriate side after the growth-rate reversal. When \(\nu=1\), the two streams agree identically. These are exact all-parameter classifications, not claims about inferred effective reproduction numbers.

## Assumptions and scope

Fix \(r>0\), \(a>0\), and a real delay-shape parameter \(\nu>0\). Define a prescribed incidence history

\[
I(t)=\begin{cases}e^{rt},&t<0,\\1,&t\ge0.\end{cases}
\]

A delay \(S_\nu\) has gamma density

\[
f_\nu(s)=\frac{(\nu a)^\nu}{\Gamma(\nu)}s^{\nu-1}e^{-\nu a s}\mathbf1_{s>0},\qquad \mathbb E S_\nu=\frac1a.
\]

Write \(J_\nu(t)=\mathbb E[I(t-S_\nu)]\) for reported incidence and \(g_\nu(t)=J_\nu'(t)/J_\nu(t)\) for its instantaneous logarithmic growth. The reference shape \(\nu=1\) has an exponential delay with the **same mean**. All comparisons refer to \(t\ge0\). Reporting is normalized, with no missed cases, time variation, or data noise. The incidence is imposed, not derived from a compartmental epidemic model.

For any shape \(\nu\), let \(b=\nu a\), \(\lambda=b+r\), and \(L_\nu=(b/\lambda)^\nu\). Let \(\overline G_{\nu,\lambda}(t)\) denote the survival function of a shape-\(\nu\), rate-\(\lambda\) gamma law, and set \(Q(t)=J_\nu(t)/J_1(t)\). The two strictly positive crossover times are denoted \(t_{\mathrm{count}}\) (where \(Q=1\)) and \(t_{\mathrm{growth}}\) (where \(g_\nu=g_1\)).

## Proof

**1. Exact response and derivative.** Splitting the convolution at the delay \(s=t\) yields, for \(t\ge0\),

\[
J_\nu(t)=1-\overline G_{\nu,b}(t)+L_\nu e^{rt}\overline G_{\nu,\lambda}(t),
\]
\[
J_\nu'(t)=r L_\nu e^{rt}\overline G_{\nu,\lambda}(t)>0.
\]

Here the second equation follows directly by differentiating \(I(t-s)\) for \(s>t\); the boundary terms cancel because \(I\) is continuous. In particular

\[
J_1(t)=1-\frac{r}{a+r}e^{-at},\qquad J_1'(t)=rL_1e^{-at}>0,
\]

and \(J_\nu(0)=L_\nu\), \(J_\nu'(0)=rL_\nu\). Both counts are positive and tend to one. Define the positive *slope ratio*

\[
R(t)=\frac{J_\nu'(t)}{J_1'(t)}=\frac{L_\nu}{L_1}e^{(a+r)t}\overline G_{\nu,\lambda}(t).
\]

**2. Unique slope-ratio extremum for every real gamma shape.** The gamma hazard function is \(h_{\nu,\lambda}(t)=f_{\nu,\lambda}(t)/\overline G_{\nu,\lambda}(t)\). Its reciprocal admits the exact representation

\[
\frac{1}{h_{\nu,\lambda}(t)}=\int_0^\infty e^{-\lambda u}\left(1+\frac{u}{t}\right)^{\nu-1}\,du,\qquad t>0.
\]

For \(\nu>1\), the integral strictly decreases with \(t\), so the hazard strictly increases from zero to \(\lambda=\nu a+r\). For \(0<\nu<1\), the integral strictly increases, so the hazard strictly decreases from infinity to the same limit \(\lambda\). The endpoint limits follow respectively from the gamma density near zero and dominated convergence in the displayed integral as \(t\to\infty\). Consequently

\[
(\log R)'(t)=a+r-h_{\nu,\lambda}(t)
\]

changes sign exactly once for every \(\nu\ne1\). If \(\nu>1\), it goes from positive to negative because \(\lambda>a+r\); if \(0<\nu<1\), it goes from negative to positive because \(\lambda<a+r\). Thus \(R\) has exactly one strict maximum or minimum, respectively. Standard integration by parts of the gamma tail gives \(\overline G_{\nu,\lambda}(t)\sim f_{\nu,\lambda}(t)/\lambda\); hence

\[
R(t)\asymp t^{\nu-1}e^{(1-\nu)at}\quad(t\to\infty).
\]

It follows that \(R(t)\to0\) for \(\nu>1\) and \(R(t)\to\infty\) for \(0<\nu<1\). No sampling or finite enumeration is used to infer these global statements.

**3. Exactly one positive extremum of the count ratio.** Let \(H(t)=J_1(t)R(t)-J_\nu(t)\). The identity \(J_\nu'=R J_1'\) gives \(H'=J_1R'\). At time zero, \(H(0)=0\). For \(\nu>1\), \(H\) strictly increases and then strictly decreases, with \(H(\infty)=-1\). Thus it has exactly one strictly positive zero \(t_{\mathrm{growth}}\), after the unique maximum of \(R\). For \(0<\nu<1\), \(H\) strictly decreases and then strictly increases, with \(H(\infty)=+\infty\); again it has exactly one strictly positive zero, after the unique minimum of \(R\). Since

\[
Q'(t)=\frac{J_1'(t)}{J_1(t)^2}H(t),
\]

it follows that \(Q\) has exactly one positive strict maximum for \(\nu>1\) and exactly one positive strict minimum for \(0<\nu<1\). Since \(Q(t)\to1\), the tail of \(Q\) lies strictly above one for \(\nu>1\), and strictly below one for \(0<\nu<1\).

**4. The earlier count crossing and exact growth signs.** The initial count ratio satisfies

\[
Q(0)=\frac{L_\nu}{L_1}=\frac{1+r/a}{(1+r/(\nu a))^\nu}.
\]

For \(\nu>1\), strict convexity of \(u\mapsto(1+u/\nu)^\nu\) gives \((1+r/(\nu a))^\nu>1+r/a\), so \(Q(0)<1\). For \(0<\nu<1\), strict concavity reverses this inequality, giving \(Q(0)>1\). Together with the unique extremum and its strictly one-sided tail behavior, these inequalities force exactly one \(t_{\mathrm{count}}\in(0,t_{\mathrm{growth}})\) satisfying \(Q=1\), and prove all claimed count signs. Finally,

\[
g_\nu(t)-g_1(t)=(\log Q)'(t)=Q'(t)/Q(t).
\]

Thus for \(\nu>1\) the growth difference is positive before the unique strictly positive \(t_{\mathrm{growth}}\) and negative after; for \(0<\nu<1\) the signs reverse. At \(t=0\), both growth rates equal \(r\). At \(\nu=1\), the delay laws and reported series are identical. This settles every endpoint and all quantifiers.

## Verification

A completely elementary special case is \(a=r=1\), \(\nu=2\), for which

\[
J_1(t)=1-\tfrac12e^{-t},\qquad J_2(t)=1-\bigl(\tfrac59+\tfrac23t\bigr)e^{-2t}.
\]

The unique strictly positive count crossover solves \(e^t=10/9+4t/3\), with rigorously checked decimal bracket

\[
0.74240778603337<t_{\mathrm{count}}<0.74240778603338.
\]

The unique strictly positive logarithmic-growth crossover solves \(9e^{2t}=8(1+3t)e^t+1-6t\), with bracket

\[
1.60428846844183<t_{\mathrm{growth}}<1.60428846844184.
\]

The latter equation also has the boundary root \(t=0\), expressing the initial equality of logarithmic-growth rates; the former has no root at zero. The global number of roots is established by the proof, not these brackets.

The standalone standard-library `verify.py` checks exact-rational polynomial-derivative identities for integer shapes, the exact sign pattern underlying the integer Erlang subfamily, and 165 representative positive-rate cases; it additionally checks the stated high-precision root brackets. Its output is `PASS 2398 assertions; exact coefficient signs; 165 two-crossing samples; k=2 rigorous decimal brackets`. For real noninteger shapes, the theorem relies on the explicit all-real-shape hazard integral proved above, rather than a finite numerical grid. Run `python3 verify.py` with Python 3.10 or later; no network, randomness, third-party packages or other data are required.

## Relationship to prior work

Eales and Riley (2023; arXiv:2307.03415) establish the convolution representation of reported epidemic time series and analyze biases caused by gamma-like observation delays, including mean and variance effects on apparent reproduction-number inference. Their accessible full text does not state this exact two-stream, all-gamma-shape **level and instantaneous log-growth crossover ordering** for a prescribed exponential-to-constant incidence. The present logarithmic-growth comparison is not an apparent reproduction-number estimator.

Yu (2016; arXiv:1607.02689) proves general single-crossing results for distributions of weighted sums of gamma variables. The **count-level crossing alone** is adjacent to, and can be approached via, existing single-crossing and variation-diminishing theory; no novelty of generic gamma-CDF crossing is asserted. The extra strict chronological separation from the *log-growth* crossover, both sign orientations for real gamma shapes, and the exact single-extremum ratio classification comprise the stated contribution. Standard hazard monotonicity underlies the proof and is not claimed as a novel fact.

Bizzotto et al. (2023; arXiv:2309.14801) analyze reproduction-number nowcasting in real surveillance. Only its abstract was available for comparison; it did not resolve the theorem and remains a residual literature risk. Priority against all historical phase-type filtering and stochastic-order results is not independently certified.

## Limitations

The prescribed incidence has infinite exponential prehistory and a perfectly abrupt transition to a permanent plateau. Both delays have exactly equal mean and constant shape/rate; both normalized streams report all cases without noise. The theorem is about deterministic expected curves and their instantaneous derivatives, not practical numerical growth estimators, retrospective counts with missing reports, or effective reproduction numbers. Non-gamma kernels, reporting regime changes, finite-window regression, gradual or multiple change points, and actual outbreak fitting remain outside its scope. No public-health intervention or nowcasting method is validated by this idealized mathematical benchmark.

## References

1. Oliver Eales and Steven Riley, “Differences between the true reproduction number and the apparent reproduction number of an epidemic time series,” arXiv:2307.03415, first posted 2023-07-07, https://arxiv.org/abs/2307.03415 .
2. Yaming Yu, “On the Unique Crossing Conjecture of Diaconis and Perlman on Convolutions of Gamma Random Variables,” arXiv:1607.02689, posted 2016-07-10, https://arxiv.org/abs/1607.02689 .
3. Andrea Bizzotto et al., “Increasing situational awareness through nowcasting of the reproduction number,” arXiv:2309.14801, posted 2023-09-26, https://arxiv.org/abs/2309.14801 .
