# Exact hazard-turning-point phase diagram for discrete Marshall–Olkin length-biased exponential lifetimes

## Finding

For every scale \(\beta>0\) and Marshall–Olkin tilt \(\gamma>0\), the discrete Marshall–Olkin length-biased exponential (DMOLBE) count has a sharp, finitely computable increasing-hazard boundary, and its hazard can have **at most two changes of monotonicity**. Every strictly decreasing stretch of the discrete hazard consists of one contiguous block of steps. A nonempty two-turn regime has increasing, then decreasing, then increasing hazard; its sharp boundary and the macroscopic positions of both turns admit explicit formulas.

Put \(t=1/\beta\), \(c=1-\gamma\), \(q=e^{-t}\), and \(U_j=(1+jt)q^j\) for integers \(j\ge0\). For real \(z\ge0\), define

\[
P_t(z)=(1+z+t)\left[(1+z+t)\left(e^t(1+z)+e^{-t}(1+z+2t)\right)-2(1+z)(1+z+2t)\right],
\]
\[
C_n(t)=\frac{e^{(n+1)t}t^2}{P_t(nt)}\qquad(n=0,1,\ldots).
\]

These quantities are strictly positive. There is exactly one positive root \(z_t\) of the cubic \(P_t(z)-P_t'(z)=0\). Let \(k=\lfloor z_t/t\rfloor\) and \(C_*(t)=\min\{C_k(t),C_{k+1}(t)\}\). Then the **usual discrete hazard** \(h_n=\Pr\{X=n\mid X\ge n\}\) is nondecreasing at every integer age if and only if

\[
\boxed{\gamma\ge \gamma_*(\beta):=1-C_*(1/\beta).}
\]

For every \(n\ge0\), \(h_{n+1}<h_n\) holds **if and only if** \(1-\gamma>C_n(t)\); equality of adjacent hazards occurs exactly at equality of these two quantities. If \(\gamma<\gamma_*(\beta)\), the decreasing steps are precisely one nonempty contiguous finite integer interval. If additionally \(C_*(t)<1-\gamma<C_0(t)\), at least one strictly increasing step precedes the decreasing block and strictly increasing steps follow it; equality may occur at a block boundary, while generic parameters yield exactly two strict direction reversals. The failure-odds hazard \(p_n/\Pr\{X>n\}\) employed in the source article has the same monotonicity directions because it is \(h_n/(1-h_n)\).

For example, for \(\beta=2\) and \(\gamma=1/2\), the exact pattern is

\[
\boxed{h_0<h_1<h_2<h_3>h_4>h_5<h_6<h_7<\cdots.}
\]

In the fine-resolution limit \(\beta\to\infty\), the critical tilt has the sharp limit

\[
\boxed{\gamma_*(\beta)\longrightarrow1-\frac{e^{1+\sqrt2}}{(2+\sqrt2)\left[1+(1+\sqrt2)^2\right]}=0.5204120459413476\ldots.}
\]

More precisely, put \(z_*=1+\sqrt2\) and \(C_\infty=e^{z_*}/[(1+z_*)(1+z_*^2)]\). For every fixed \(c\in(C_\infty,1)\), let \(0<z_-(c)<z_*<z_+(c)\) be the two solutions of \(c e^{-z}(1+z)(1+z^2)=1\). If \(n_-(t)\) and \(n_+(t)\) are the smallest and largest indices with \(h_{n+1}<h_n\) when \(\gamma=1-c\), then

\[
\boxed{t n_-(t)\to z_-(c),\qquad t n_+(t)\to z_+(c)\quad(t\downarrow0).}
\]

Thus the two turns separate on the natural scale \(\beta\), not merely on a bounded number of counts.

## Assumptions and scope

The domain is \(\beta>0\), \(\gamma>0\), and \(n\in\mathbb Z_{\ge0}\). The survival function at integer ages is \(S_n=\Pr\{X\ge n\}=\gamma U_n/(1-cU_n)\), with \(U_n=(1+nt)e^{-nt}\). It obeys \(S_0=1\), \(S_n>S_{n+1}>0\), and \(S_n\to0\); hence \(p_n=S_n-S_{n+1}\) is a normalized positive mass function. This agrees exactly with the survival discretization of Aljohani et al. (2023). The standard discrete hazard \(h_n=1-S_{n+1}/S_n\) lies in \((0,1)\); the source's alternative failure-odds convention \(p_n/S_{n+1}\) is an increasing transformation and has the identical age-order comparisons. The theorem concerns monotonicity, not numerical equality of those two hazard conventions.

## Proof

**1. Exact coefficient test.** Put \(A=U_n\), \(B=U_{n+1}\), \(D=U_{n+2}\). Direct calculation gives \(B^2-AD=e^{-2(n+1)t}t^2>0\). Also

\[
E=B\big[B(A+D)-2AD\big]>0,
\]

since \(B>\sqrt{AD}\) and \(A+D\ge2\sqrt{AD}\). The comparison \(h_{n+1}<h_n\) is equivalent to \(S_{n+1}^2<S_nS_{n+2}\). Clearing the strictly positive denominators in the latter inequality yields

\[
B^2(1-cA)(1-cD)-AD(1-cB)^2=(B^2-AD)-cE<0.
\]

The quadratic terms in \(c\) cancel identically. Hence \(h_{n+1}<h_n\) if and only if \(c>(B^2-AD)/E\), with equality precisely at \(c=(B^2-AD)/E\). Writing \(z=nt\), the explicit factorization \(E=e^{-(3n+3)t}P_t(z)\) proves \((B^2-AD)/E=C_n(t)\). In particular, \(P_t(z)>0\) for all \(z\ge0\) (the same algebra applies to real \(n=z/t\)).

**2. The unique minimizer.** Write \(P_t(z)=p_0+p_1z+p_2z^2+p_3z^3\) and \(Q_t(z)=P_t(z)-P_t'(z)\). For \(q=e^{-t}\), direct expansion gives

\[
[z^0]Q_t=\frac{2[q(1+t)-1]\left[(1+t)(1-q)+qt^2\right]}q<0,
\]
\[
[z^1]Q_t=\frac{t^2(5q^2-4q+1)-3(1-q)^2}q,
\]
\[
[z^2]Q_t=\frac{2t(1-q)(1-2q)}q,\qquad[z^3]Q_t=\frac{(1-q)^2}q>0.
\]

If \(t\le\log2\), then \(q\ge1/2\), so the quadratic coefficient is nonpositive. Moreover \(1-q\ge qt\) and, putting \(w=1/q\in[1,2]\), we have \(5-4w+w^2=(w-2)^2+1\le2<3\). Consequently the linear coefficient is strictly negative. The descending cubic coefficient signs are \((+,-,-,-)\), allowing zeros, so Descartes' rule of signs gives at most one positive zero. If \(t>\log2\), the quadratic coefficient is positive and the descending sign pattern is \((+,+,\pm,-)\), again exactly one sign change. Since \(Q_t(0)<0\) and its leading coefficient is positive, it has exactly one positive real zero \(z_t\) in both cases. Finally

\[
\frac{d}{dz}\left(\frac{e^{z+t}t^2}{P_t(z)}\right)=\frac{e^{z+t}t^2 Q_t(z)}{P_t(z)^2}.
\]

Thus the continuous threshold function strictly decreases to \(z_t\) and then strictly increases. On the lattice \(z=nt\), its global minimum is therefore among the two indices \(k=\lfloor z_t/t\rfloor\) and \(k+1\). A level strictly above that minimum cuts out just one consecutive finite block of lattice indices because the thresholds diverge exponentially as \(n\to\infty\). This proves the exact hazard boundary and all possible monotonicity patterns. The minimum lies strictly below \(1\): at \(n=0\), \(A=1\), and \(E-(B^2-AD)=D(1-B)^2>0\), so \(0<C_*(t)\le C_0(t)<1\).

**3. An exact two-turn example.** At \(t=1/2\), \(c=1/2\), the signs of \(cE-(B^2-AD)\) for \(n=0,1,2,3,4,5\) are respectively \((-,-,-,+,+,-)\). The standalone checker establishes these six strict signs using only rational interval arithmetic and alternating Taylor bounds for \(e^{-1/2}\), with no floating-point assumption. By the unimodality of \(C_n(t)\), no further negative-hazard steps can appear after \(n=5\), and none occur before \(n=3\). The displayed infinite pattern follows.

**4. Fine-resolution asymptotics.** On every compact \(z\)-interval, elementary Taylor expansion gives

\[
\frac{P_t(z)}{t^2}\longrightarrow (1+z)(1+z^2),\qquad \frac{Q_t(z)}{t^2}\longrightarrow z(z^2-2z-1).
\]

The unique positive minimum root \(z_t\) converges to the unique positive root of \(z^2-2z-1=0\), namely \(z_*\). The nearest lattice points lie within \(t\) of \(z_t\), whence the global discrete critical value tends to \(C_\infty\). For fixed \(C_\infty<c<1\), the limiting smooth function \(e^z/[(1+z)(1+z^2)]\) has exactly two positive level crossings with \(c\); local uniform convergence and unimodality imply the claimed convergence of the two extreme lattice indices after multiplying by \(t\).

## Verification

Run \(\texttt{python3 check_hazard.py}\) using a standard Python 3 installation. It obtains upper and lower *rational* Taylor bounds for \(e^{-1/2}\), propagates exact intervals through the six decisive inequalities for the explicit example, compares independent conventional-hazard computations, and runs supplementary consistency checks on selected parameter grids. The strict six-sign certificate and the analytic Descartes argument, not the grids, justify the infinite-support example and theorem. The supplied code has no network access or third-party dependencies.

## Relationship to prior work

Aljohani et al. (2023) introduced the DMOLBE distribution and gave its mass, survival and failure-odds formulas, together with plots illustrating different hazard behavior. The present claim starts from those formulas and proves the sharp all-parameter hazard-order criterion, a finite cubic minimization, the restriction to at most two reversals, an exact two-turn example, and a scale-resolved onset law. Ahsan-ul-Haq et al. (2017) introduced the underlying *continuous* Marshall–Olkin length-biased exponential family; its continuous formulas do not themselves entail these discrete lattice thresholds. General Marshall–Olkin stochastic-order results and a distinct 2026 power-half-logistic hazard analysis provide related methodology but neither contains an implication of this specific discrete shape classification identified in the accessible materials. Mathematical search findings with similar descriptive language involve different baselines or observables. This is a best-knowledge literature comparison, not independent proof of worldwide priority.

## Limitations

The threshold is given by a uniquely solvable cubic and comparison of two lattice candidates, not a universal elementary expression solely in \(\beta\). Ties at threshold values may produce flat adjacent hazard values; the monotonicity classification explicitly allows them. The phase diagram describes the distribution's theoretical hazard under correct specification, not estimation uncertainty or observed-data fit. Historical-priority verification remains subject to unindexed and inaccessible literature; no independent mathematical audit has been performed.

## References

1. Aljohani, H. M., Ahsan-ul-Haq, M., Zafar, J., Almetwally, E. M., Alghamdi, A. S., Hussam, E., and Muse, A. H. (2023). “Analysis of Covid-19 data using discrete Marshall–Olkinin Length Biased Exponential: Bayesian and frequentist approach.” *Scientific Reports* 13, 12243. Published 2023-07-28. https://doi.org/10.1038/s41598-023-39183-6
2. Ahsan-ul-Haq, M., Usman, R. M., Hashmi, S., and Al-Omeri, A. I. (2017). “The Marshall-Olkin length-biased exponential distribution and its applications.” *Journal of King Saud University – Science*. https://doi.org/10.1016/j.jksus.2017.09.006
3. Nanda, A. K. and Das, S. (2012). “Stochastic orders of the Marshall–Olkin extended distribution.” *Statistics & Probability Letters* 82, 295–302. https://doi.org/10.1016/j.spl.2011.10.003
4. Adlan, R., Haj Ahmad, H., and Aboshady, M. (2026). “The Marshall–Olkin Power Half-Logistic Distribution for Reliability Modeling of Degradation Data Under Generalized Hybrid Censoring.” *Mathematics* 14, 973. https://doi.org/10.3390/math14060973
