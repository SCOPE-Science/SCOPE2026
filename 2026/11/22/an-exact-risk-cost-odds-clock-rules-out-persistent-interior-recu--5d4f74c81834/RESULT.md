# An exact risk–cost odds clock rules out persistent interior recurrence under imbalanced feedback

## Finding
For the three-variable collective-risk evolutionary game defined below, there is an exact environmental odds clock. Write
\[
  x_* = \frac{\mu_1}{\mu_1+\mu_2},\qquad
  r_* = \frac{\theta_2\mu_1-\theta_1\mu_2+\theta_4(\mu_1+\mu_2)}
               {(\theta_3+\theta_4)(\mu_1+\mu_2)},
\]
and set \(k=(\alpha-\beta)(\theta_1+\theta_2)/(\mu_1+\mu_2)\), \(h=(\alpha-\beta)(\theta_3+\theta_4)>0\). Every solution starting in the strict physical interior obeys
\[
 \mathcal L(t)=\log\frac{c(t)-\beta}{\alpha-c(t)}
       - k\log\frac{r(t)}{1-r(t)},\qquad
 \mathcal L'(t)=h\bigl(r(t)-r_*\bigr).
\]
Consequently, if \(r_*\leq0\) or \(r_*\geq1\), **there exists no nonempty compact forward-invariant subset of the strict interior**. In particular, no interior periodic orbit, compact recurrent attractor, or trajectory permanently bounded away from all physical boundaries is possible for any group size, quota, or payoff scale.

If \(r_*<0\), the exact bound \(e^{-\mathcal L(t)}\le e^{-\mathcal L(0)}e^{-h(-r_*)t}\) holds for all \(t\geq0\). If \(r_*>1\), the dual bound is \(e^{\mathcal L(t)}\le e^{\mathcal L(0)}e^{-h(r_*-1)t}\). Thus strict imbalance creates an exponential tradeoff forcing environmental risk or cost toward its corresponding boundary; the bounds do **not** assert which individual coordinate approaches a boundary.

Conversely, any solution contained for all positive time in a compact interior subset has exact limiting Cesàro averages
\[
 \lim_{T\to\infty}\frac1T\int_0^T x(t)\,dt=x_*,\qquad
 \lim_{T\to\infty}\frac1T\int_0^T r(t)\,dt=r_*.
\]
The restriction \(0<r_*<1\) is sharp **for the existence of some compact interior invariant set**, not for stability: for every prescribed \(r_*\in(0,1)\), there are strictly positive admissible model parameters with an interior equilibrium.

## Assumptions and scope
Fix integers \(N\geq2\) and \(1\leq M\leq N\), an endowment \(b>0\), and bounds \(0<\beta<\alpha\). Let \(\mu_1,\mu_2,\theta_1,\theta_2,\theta_3,\theta_4\) be arbitrary strictly positive constants. With the strategy and risk update speeds both normalized to one, the deterministic well-mixed equations are
\[
\begin{aligned}
\dot x&=x(1-x)\left[b\binom{N-1}{M-1}x^{M-1}(1-x)^{N-M}r-c\right],\\
\dot r&=r(1-r)\left[\mu_1-(\mu_1+\mu_2)x\right],\\
\dot c&=(\alpha-c)(c-\beta)\left[\theta_1-(\theta_1+\theta_2)x+(\theta_3+\theta_4)r-\theta_4\right].
\end{aligned}
\]
The domain is \(\Omega=\{(x,r,c):0<x<1,\ 0<r<1,\ \beta<c<\alpha\}\). The vector field is smooth on a neighborhood of the closed physical box and has boundary factors that preserve \(\Omega\) for every finite time, so a unique global forward solution exists for each point of \(\Omega\). Compact interior forward invariance means a nonempty compact \(K\subset\Omega\) with \(\Phi_t(K)\subset K\) for every \(t\geq0\); it need not consist of equilibria.

## Proof
The risk and cost equations imply the exact logarithmic derivatives
\[
 \frac{d}{dt}\log\frac r{1-r}=\mu_1-(\mu_1+\mu_2)x,
\]
\[
 \frac{d}{dt}\log\frac{c-\beta}{\alpha-c}
 =(\alpha-\beta)\left[\theta_1-\theta_4-(\theta_1+\theta_2)x+(\theta_3+\theta_4)r\right].
\]
Multiplying the first identity by \(k\) cancels the entire \(x\)-dependence in the second. Their difference is
\[
 \mathcal L'= (\alpha-\beta)(\theta_3+\theta_4)r
 +(\alpha-\beta)(\theta_1-\theta_4)
 -k\mu_1=h(r-r_*),
\]
with the specified \(r_*\). Integrating this identity yields all stated exponential bounds, because \(0<r(t)<1\).

Suppose \(r_*\leq0\) and some nonempty compact \(K\subset\Omega\) is forward invariant. By compactness, \(\min_K r=\varepsilon>0\); hence \(\mathcal L'\geq h\varepsilon\) along each orbit in \(K\). This forces \(\mathcal L(t)\to+\infty\), contradicting boundedness of the continuous function \(\mathcal L\) on \(K\). For \(r_*\geq1\), compactness gives \(\max_K r\leq1-\varepsilon\), so \(\mathcal L'\leq-h\varepsilon\) and the same contradiction applies. In particular, the closure of an orbit cannot be an interior compact set. Neither proof uses the equation for \(\dot x\), its group size, or its payoff normalization.

For any forward orbit contained in a compact subset of \(\Omega\), both \(\mathcal L\) and \(\log[r/(1-r)]\) are bounded. Divide the integrated odds-clock identity by \(T\) and let \(T\to\infty\) to obtain the mean-risk law; independently divide the integrated risk-logit derivative by \(T\) to obtain the mean-cooperation law. These results do not assume periodicity or ergodicity.

To show sharpness in the stated **existential** sense, fix an arbitrary \(q\in(0,1)\). Choose \(N=3\), \(M=2\), \(b=2\), \(\mu_1=\mu_2=\theta_1=\theta_2=1\), \(\theta_3=1-q\), \(\theta_4=q\), \(\beta=q/2\), and \(\alpha=(1+q)/2\). All these parameters are strictly admissible. The pivotal-benefit factor at \(x=1/2\) equals one, and direct substitution gives
\[
 (x,r,c)=(1/2,q,q)\in\Omega,\qquad (\dot x,\dot r,\dot c)=(0,0,0),\qquad r_*=q.
\]
The singleton containing this equilibrium is a compact forward-invariant subset. This construction makes no claim about its stability.

## Verification
Run the standalone standard-library checker `python verify.py`. It evaluates the odds-clock and risk-logit identities with exact rational arithmetic for 200 seeded admissible parameter/initial-state configurations; checks 19 rational members of the sharpness construction; and checks two strictly positive parameter witnesses with \(r_*=-7/4\) and \(r_*=11/4\). All checks passed. The infinite-time exclusion argument is the preceding compactness proof, not a conclusion drawn from finite experiments.

## Relationship to prior work
Wang, Hua, Liu, Zhang, Liu and Szolnoki (2026) introduced precisely the three-variable differential equations above and derived an interior-equilibrium existence condition using the same value \(r_*\). Their main text and stability table give a census of equilibria and local stability conditions. The finding here is not the expression for \(r_*\), nor another equilibrium classification: it is an all-initial-condition, all-payoff **global exclusion of any persistent compact interior behavior**, an exact exponential environmental odds tradeoff, and simultaneous universal time-average constraints. The earlier two-variable cooperation–dilemma-strength feedback model of Hua, Xu, Liu and Chen (2024) does not simultaneously evolve separate risk and cost variables, so its bistability criteria cannot directly provide this three-variable odds clock.

## Limitations
The result does not identify which boundary state a trajectory approaches, prove full defection, or rule out transient oscillations and recurrent motion on the boundary. At \(r_*=0\) or \(r_*=1\), the compact-interior exclusion remains valid, but the uniform exponential bound stated for strict imbalance is not asserted. For \(0<r_*<1\), the time-average identities are necessary conditional laws, not a proof of an attracting interior orbit or equilibrium. The theorem concerns the exactly printed three-variable ODE with unit-normalized strategy/risk update speeds, not its alternative feedback variant, finite-population processes, or arbitrary nonlinear feedback. Historical-priority uncertainty remains, especially because the separately hosted supplementary stability material could not be read.

## References
1. Wang, L., Hua, S., Liu, Y., Zhang, L., Liu, L., and Szolnoki, A. (2026). *Coevolutionary dynamics of cooperation, risk, and cost in collective risk games*. PLOS Computational Biology 22(2), e1013512. First public journal release February 20, 2026. https://doi.org/10.1371/journal.pcbi.1013512 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC12923141/ . Equations (6)–(10), Table 1, and Results.
2. Hua, S., Xu, M., Liu, L., and Chen, X. (2024). *Coevolutionary dynamics of collective cooperation and dilemma strength in a collective-risk game*. Physical Review Research 6, 023313. https://doi.org/10.1103/PhysRevResearch.6.023313 .
