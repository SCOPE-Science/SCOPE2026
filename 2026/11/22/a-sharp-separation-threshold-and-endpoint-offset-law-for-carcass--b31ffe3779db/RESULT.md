# A sharp separation threshold and endpoint-offset law for carcass-search calendars

## Finding

Consider a monitoring season of duration \(H>0\) with exactly \(n\ge 2\) instantaneous carcass searches, each independently detecting each carcass still present with probability \(0<p<1\). Wildlife fatalities arrive at a constant positive rate, independently of an exponential scavenging/removal time of rate \(\lambda>0\). The search at the season end is free to be scheduled and a search removes every carcass it finds. Simultaneous independent searches are permitted. Among all ordered schedules, the expected number of distinct carcasses discovered has a **unique** maximizer.

Set \(h=\lambda H\) and
\[
 h_c(n,p)=(n-2)\log(2-p)-\log p.
\]
The optimal calendar has \(n\) strictly positive consecutive gaps precisely when \(h>h_c(n,p)\). At equality its unique optimal last gap is zero; for \(h<h_c(n,p)\) at least one optimal gap is zero. For \(h\ge h_c(n,p)\), the optimal schedule is explicit: let \(q\in(0,1/(2-p)]\) be the unique solution of
\[
 h=-n\log q+2\log(1-(1-p)q)-\log p,
\]
put \(A=1-(1-p)q\), and let \(\delta_i=\lambda(t_i-t_{i-1})\), with \(t_0=0\). Then
\[
 \delta_1=-\log(pq/A),\qquad
 \delta_2=\cdots=\delta_{n-1}=-\log q,\qquad
 \delta_n=-\log(q/A).
\]
For \(n=2\) the middle equality is empty and these formulas still apply. In particular, **for every fully separated optimum**, its first gap exceeds its last by the invariant
\[
 t_1-(H-t_{n-1})=\lambda^{-1}\log(1/p),
\]
independent of search count and deployment horizon. For \(n\ge3\), all interior gaps are identical and strictly between the first and last gaps.

## Assumptions and scope

Fatalities form a homogeneous Poisson stream of intensity \(m>0\) on \([0,H]\), though only its constant mean intensity is used. No carcasses are present initially. Each carcass survives to age \(a\) with probability \(e^{-\lambda a}\), independent of other carcasses and observation events. Detection opportunities independently succeed with fixed probability \(p\) at each instantaneous visit; detected carcasses are removed. Search times satisfy \(0\le t_1\le\cdots\le t_n\le H\). Tied times represent distinct independent search passes on the same instant. The objective is the **expected total discovered count**, not the variance of a fatality estimator, biological risk reduction, or a field operational cost.

## Proof

**Step 1: The last search occurs at the deadline.** Let \(r_i\) be the expected number of carcasses immediately before search \(i\), divided by \(m/\lambda\). For dimensional gaps \(g_i=t_i-t_{i-1}\), set \(d_i=\lambda g_i\), \(z_i=e^{-d_i}\), and \(r_0=0\). Flow, scavenging and search thinning give
\[
 r_i=1-z_i+(1-p)z_i r_{i-1},\qquad
 \mathbb E[C]=\frac{mp}{\lambda}\sum_{i=1}^n r_i.
\]
Holding earlier times fixed, postponing the final search increases \(r_n\) strictly because \(1-(1-p)r_{n-1}>0\). Thus \(t_n=H\). The first search cannot be at time zero in an optimum: no carcasses exist then, so replacing a zero-time pass by an additional independent pass at \(H\) strictly increases discoveries (fresh carcasses between the last strictly earlier visit and \(H\) survive, and some present carcasses escape each pass). Hence \(d_1>0\) at every optimum. We maximize \(J=p\sum_i r_i\) over the closed simplex \(d_i\ge0\), \(\sum_i d_i=h\).

**Step 2: Strict concavity gives uniqueness.** Unrolling the recursion yields
\[
 r_i=1-\sum_{k=1}^i c_{ik}
 \exp\!\left(-\sum_{\ell=k}^i d_\ell\right),
 \quad c_{i1}=(1-p)^{i-1},\quad
 c_{ik}=p(1-p)^{i-k}\ (k\ge2).
\]
Every coefficient is strictly positive. Consequently \(J\) equals a constant minus a positive sum of exponentials of negative consecutive gap sums. Moreover each coordinate \(d_i\) occurs separately with a strictly positive coefficient in the term \(k=i\). Therefore the Hessian is everywhere strictly negative definite; \(J\) is strictly concave on the full simplex. There is exactly one global maximizer, and any feasible stationary point on its relative interior is that maximizer.

**Step 3: Interior optimality forces equal expected pre-search stocks.** Define \(U_i=1-r_i\), with \(U_0=1\), and
\[
 Q_n=1,\qquad Q_i=1+(1-p)e^{-d_{i+1}}Q_{i+1}.
\]
The recursions imply
\[
 U_i=e^{-d_i}[p+(1-p)U_{i-1}],\qquad
 \frac{\partial J}{\partial d_i}=p U_i Q_i.
\]
At an interior optimum all these partial derivatives coincide. Equality of the derivatives at adjacent indices implies
\[
 U_i=p e^{-d_{i+1}}Q_{i+1}\qquad(1\le i<n).
\]
For \(i\le n-2\), the next such relation gives \(Q_{i+1}=1+(1-p)U_{i+1}/p\), so
\[
 U_i=e^{-d_{i+1}}[p+(1-p)U_{i+1}].
\]
Comparing with \(U_{i+1}=e^{-d_{i+1}}[p+(1-p)U_i]\) gives
\[
 (1+(1-p)e^{-d_{i+1}})(U_i-U_{i+1})=0.
\]
Thus \(U_1=\cdots=U_{n-1}\), and \(d_2=\cdots=d_{n-1}\) when these middle gaps exist.

**Step 4: Solve all stationary equations and locate the boundary.** Write \(q=e^{-d_2}\) for \(n\ge3\); when \(n=2\), the same parameterization follows algebraically from the single derivative equality and the horizon constraint. The common value in Step 3 is \(U=pq/A\), with \(A=1-(1-p)q\). The first recurrence and last adjacent derivative equality give \(e^{-d_1}=pq/A\) and \(e^{-d_n}=q/A\). This proves all the displayed formulas and the horizon equation. Conversely, these formulas satisfy every stationary derivative equality: the fixed middle recursion gives the common \(U\), the final equality fixes the adjoint \(Q\), and its recursion propagates equality backwards. Strict concavity makes any such feasible point the unique global maximizer.

The horizon right-hand side is strictly decreasing in \(q\), because its derivative is \(-n/q-2(1-p)/(1-(1-p)q)<0\). The last gap is nonnegative exactly when \(q\le1/(2-p)\); the other gaps are positive there. Substituting \(q=1/(2-p)\) gives \(d_n=0\) and \(h=h_c(n,p)\). For \(h>h_c\), the unique stationary vector is strictly feasible and therefore globally optimal. At equality the same vector lies on the boundary but still has all gradient components equal; concavity yields global optimality. For \(h<h_c\), no all-positive stationary vector is feasible; therefore the global optimum lies on the boundary of the simplex and has at least one zero gap. As Step 1 proves \(d_1>0\), this zero gap occurs between consecutive searches, so at least two visits coincide. Strict concavity still gives its uniqueness. Finally \(d_1-d_n=-\log p\) and, for \(n\ge3\), \(d_1>-\log q>d_n\), as claimed.

**A reproducible example.** With \(n=4\), \(p=1/2\) and \(h=3\), the optimal dimensionless gaps are approximately \((1.12988253,0.71669106,0.71669106,0.43673535)\). Their normalized mean discovery count \(\lambda\mathbb E[C]/m\) is \(1.30167009\), compared with \(1.27510268\) for four equally spaced visits. Strict concavity, not the numerical comparison, proves global optimality.

## Verification

Run `python3 checker.py` with the Python 3 standard library. The checker independently sums expected finds over arrival cohorts, compares this against the state recursion, checks the analytical stationary solution over multiple values of \(n,p,h\), tests perturbations, and verifies selected calculations using exact rational arithmetic. The checked program reports 15,020 diagnostics passing. These finite checks are corroboration only; Steps 1–4 constitute the infinite-parameter proof.

## Relationship to prior work

Korner-Nievergelt et al. (2011) model imperfect carcass detection, scavenging and later discovery after a missed search, but develop estimation corrections mainly for regular schedules; their inspected Methods, Results and Discussion do not present the optimizing calendar and its sharp separation boundary. Etterson (2013) addresses variable intervals in a mortality-estimation framework; the full article was not accessible here, and its complete coverage cannot be ruled out from the abstract. The 2015 open-access tutorial by Korner-Nievergelt et al. explicitly describes irregular-interval probability calculations rather than the present global maximization theorem. Wolpert's 2015 arXiv treatment supplies a much more general survival-and-detection counting formula, into which the present objective embeds as a special case; the inspected model and estimator sections do not derive the sharp optimum. Published research records on transient ecological-presence surveys and repeated occupancy surveys optimize different objectives and do not entail this arbitrary-search-count formula for a continual arrival stream.

## Limitations

The exact law relies on constant arrival intensity, memoryless carcass removal, identical independent detection at each visit, full spatial search coverage, zero search duration, no setup or switching costs and no inter-visit adaptation. When zero gaps arise, simultaneous independent passes may be impractical; if strict chronological separation is mandatory, a boundary solution may only be approached. The conclusion does not optimize inferential precision in the presence of unknown detection/scavenging parameters or represent temporal risk variation. In practice, regular surveys can be essential for learning time-varying mortality, so this idealized maximizing schedule is not a field recommendation. The historical originality comparison is subject to residual uncertainty from inaccessible 2013 full text and the possibility of an equivalent classical inspection-design result.

## References

- Korner-Nievergelt, F., et al. (2011). *A new method to determine bird and bat fatality at wind energy turbines from carcass searches*. Wildlife Biology 17, 350–363. https://doi.org/10.2981/10-121. First published 2011-12-01.
- Etterson, M. A. (2013). *Hidden Markov models for estimating animal mortality from anthropogenic hazards*. Ecological Applications 23, 1915–1925. https://doi.org/10.1890/12-1166.1. Archived author version dated 2013-04-23 at https://digitalcommons.unl.edu/usepapapers/325/.
- Korner-Nievergelt, F., et al. (2015). *Mortality estimation from carcass searches using the R-package carcass — a tutorial*. Wildlife Biology 21, 30–43. https://doi.org/10.2981/wlb.00094.
- Wolpert, R. L. (2015). *ACME: A Partially Periodic Estimator of Avian & Chiropteran Mortality at Wind Turbines*. arXiv:1507.00749v1, 2015-07-02. https://arxiv.org/abs/1507.00749.
- Huso, M., Dietsch, T. & Nicolai, C. (2016). *Mortality Monitoring Design for Utility-Scale Solar Power Facilities*. USGS Open-File Report 2016-1087. https://doi.org/10.3133/ofr20161087.
