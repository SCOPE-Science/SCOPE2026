# Global extinction and sharp critical decay in a harvested Holling-II Ricker predator–prey map

## Finding
For the positive-population map
\[
 x_{n+1}=x_n\exp\!\left(1-a-x_n-\frac{y_n}{b+x_n}\right),\qquad
 y_{n+1}=y_n\exp\!\left(\frac{d x_n}{b+x_n}-s\right),
\]
assume \(0<a<1\), \(b,d,s>0\), and \(x_0,y_0>0\). Set \(r=1-a\) and \(\Delta=dr/(b+r)-s\).

**Theorem.** If \(\Delta\le0\), every positive orbit converges to the prey-only equilibrium \((r,0)\). If \(\Delta<0\), then \(\lim_{n\to\infty}n^{-1}\log y_n=\Delta\). At the sharp neutral-invasion boundary \(\Delta=0\), both populations have universal amplitudes
\[
 \lim_{n\to\infty}n y_n=\frac{(b+r)^3}{db},\qquad
 \lim_{n\to\infty}n(r-x_n)=\frac{(b+r)^2}{db}.
\]
In particular, the predator vanishes algebraically rather than exponentially, and prey approaches its carrying level from below. The invasion restriction is sharp for universal predator exclusion: when \(\Delta>0\), a strictly positive coexistence fixed point exists and itself fails to approach \((r,0)\).

## Assumptions and scope
All parameters are fixed real numbers with \(0<a<1\) and \(b,d,s>0\); no smallness of initial positive population densities is required. Time is the integer iteration index \(n\ge0\). Every iterate stays strictly positive because each coordinate is multiplied by a positive exponential. The assertion concerns the unforced discrete model, not its continuous counterpart, and uses no claim about trajectories when \(\Delta>0\) beyond existence of a coexistence equilibrium.

## Proof
**1. An upper scalar comparison.** Write \(f_t(x)=x e^{t-x}\). Since \(r\in(0,1)\), for every \(x>0\), \(f_r(x)\le e^{r-1}<1\). Hence \(0<x_1<1\). Define \(U_1=1\), \(U_{n+1}=f_r(U_n)\). On \([0,1]\), \(f_r\) is increasing because \(f_r'(x)=e^{r-x}(1-x)\ge0\). Since \(x_{n+1}\le f_r(x_n)\), induction yields \(x_n\le U_n\le1\) for \(n\ge1\). The scalar sequence decreases to its only positive fixed point \(r\): for \(r<U_n\le1\), \(r<f_r(U_n)<U_n\). Moreover \(U_n-r\) decays geometrically for large \(n\), since \(f_r'(r)=1-r\in(0,1)\). Consequently \(\sum_{n\ge1}(U_n-r)<\infty\).

**2. Predator extinction.** Let \(g(x)=d x/(b+x)-s\), a strictly increasing function with bounded derivative \(g'(x)=db/(b+x)^2\). If \(g(r)=\Delta<0\), the comparison \(g(x_n)\le g(U_n)\to\Delta\) proves exponential extinction of \(y_n\). If \(g(r)=0\), then \(g(x_n)\le g(U_n)\le C(U_n-r)\), and \(\sum_n\max\{g(x_n),0\}<\infty\). Since
\[
 \log y_n=\log y_0+\sum_{k=0}^{n-1}g(x_k),
\]
its positive increments have finite sum; therefore \(\log y_n\) has an extended limit and \(y_n\to L\ge0\) is finite. If \(L>0\), then eventually \(y_n\ge L/2\) and \(x_n\le1\), giving \(x_{n+1}\le f_{r-c}(x_n)\), where \(c=L/[2(b+1)]>0\). Comparing with this scalar Ricker map shows \(\limsup x_n\le\max\{r-c,0\}<r\): for \(r-c>0\) its positive orbits converge to \(r-c\), while for \(r-c\le0\) they tend to zero; the first comparison iterate can be bounded by one. Thus eventually \(g(x_n)\le-\eta<0\), forcing \(y_n\to0\), a contradiction. Therefore \(L=0\).

**3. Prey recovery.** Since \(y_n\to0\), for any \(\varepsilon\in(0,r)\) one eventually has \(y_n/(b+x_n)\le\varepsilon\). Then \(f_{r-\varepsilon}(x_n)\le x_{n+1}\le f_r(x_n)\). Both comparison sequences, started sufficiently late with the actual positive prey value, converge to their respective carrying levels \(r-\varepsilon\) and \(r\), because the corresponding Ricker parameters are in \((0,1)\). Thus \(r-\varepsilon\le\liminf x_n\le\limsup x_n\le r\); let \(\varepsilon\downarrow0\). This proves convergence to \((r,0)\) in both cases. For \(\Delta<0\), telescoping logarithms and Cesàro convergence yield \(n^{-1}\log y_n\to g(r)=\Delta\).

**4. The critical universal amplitude.** Suppose \(\Delta=0\), and set \(u_n=x_n-r\) and \(v_n=y_n\). Both tend to zero and \(v_n>0\). Taylor expansion of the prey update about \((r,0)\) gives
\[
 u_{n+1}=(1-r)u_n-\frac{r}{b+r}v_n+O((|u_n|+v_n)^2).
\]
Because the first coordinate multiplier has derivative \(1-r\in(0,1)\), smoothness supplies constants \(\lambda\in(1-r,1)\), \(C>0\) such that eventually \(|u_{n+1}|\le\lambda|u_n|+Cv_n\). Meanwhile \(v_{n+1}/v_n=e^{g(x_n)}\to1\), so for some \(\delta>0\) with \(1-\delta>\lambda\), eventually \(v_{n+1}\ge(1-\delta)v_n\). Dividing the former inequality by the latter bounds \(|u_n|/v_n\) uniformly by a scalar contraction estimate. Consequently the Taylor remainder divided by \(v_n\) tends to zero, and the exact quotient recurrence implies
\[
 \frac{u_{n+1}}{v_{n+1}}=(1-r)\frac{u_n}{v_n}-\frac{r}{b+r}+o(1).
\]
A stable affine recurrence with vanishing error converges to its unique fixed point, yielding
\[
 \frac{u_n}{v_n}\longrightarrow-\frac{1}{b+r}.
\]
At neutrality \(g(r)=0\). Taylor expansion of the predator multiplier gives
\[
 v_{n+1}=v_n\exp\left(\frac{db}{(b+r)^2}u_n+O(u_n^2)\right)
 =v_n-\frac{db}{(b+r)^3}v_n^2+o(v_n^2).
\]
Thus \(v_{n+1}^{-1}-v_n^{-1}\to db/(b+r)^3\), and the Cesàro lemma gives \(v_n^{-1}/n\to db/(b+r)^3\). Combining with the quotient limit yields the two displayed amplitudes for all strictly positive initial data.

**5. Sharpness.** If \(\Delta>0\), then \(d>s\) and \(x_*=sb/(d-s)<r\). The fixed-point prey equation has \(y_*=(b+x_*)(r-x_*)>0\). Thus a positive fixed point exists, so universal convergence to the boundary point cannot hold beyond the stated threshold.

## Verification
The analytic proof establishes the infinite-time claims. The accompanying `check.py` uses exact rational arithmetic to verify the equilibrium and coefficient identities on several rational parameter tuples, and numerically iterates selected strictly positive initial states to check the predicted critical large-\(n\) amplitudes and the strict-invasion decay exponent. These finite computations are consistency tests, not a substitute for the proof. Run `python3 check.py` with Python 3.10 or later and no third-party dependencies.

## Relationship to prior work
Ruan, Li, Yu, and Qian (2025), Equation (4), derive this exact harvested semi-discrete Rosenzweig–MacArthur map; Sections 2–4 analyze fixed-point existence, local stability, transcritical and Neimark–Sacker bifurcations, and numerical trajectories. Their local predator-invasion boundary and coexistence branch are prior work. The new contribution is the all-positive-data global extinction result together with the explicit, initial-condition-independent neutral-invasion \(n^{-1}\) amplitudes. Wang and Niu (2025) give general global-boundary-convergence criteria for a different discrete Kolmogorov model; their abstract may subsume a global qualitative statement in suitable general settings, but does not specify these two sharp amplitudes. That full text was inaccessible, so possible broader implications remain a priority risk. Other discrete Ricker predator–prey maps with different functional responses do not directly yield these formulas.

## Limitations
The sharp asymptotic is proved only for \(0<a<1\) at \(\Delta=0\); rates for higher prey growth parameters and for forced or stochastic dynamics are not covered. No claim of global convergence to coexistence for \(\Delta>0\) is made. Independent validation and a complete literature-priority guarantee have not been performed.

## References
- M. Ruan, X. Li, Y. Yu, and F. Qian, "Transcritical Bifurcation and Neimark–Sacker Bifurcation in a Discrete Predator–Prey Model with Constant-Effort Harvesting," *Mathematics* **13** (2025), 3935. https://doi.org/10.3390/math13243935.
- S. Wang and L. Niu, "On the Global stability of a discrete-time predator-prey model of Kolmogorov type," *Discrete and Continuous Dynamical Systems B* **30** (2025), 3526–3540. https://doi.org/10.3934/dcdsb.2025033.
- Wikan and Kristensen, "Prey-Predator Interactions in Two and Three Species Population Models," *International Journal of Differential Equations* (2019). https://doi.org/10.1155/2019/9543139.
