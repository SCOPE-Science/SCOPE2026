# A sharp outdoor-decay transition in one-shot indoor-air purging

## Finding

Consider a well-mixed indoor air compartment with a continuing, constant pollutant source, natural first-order clearance, and one optional instantaneous partial replacement of indoor air by outdoor air. Suppose outdoor pollutant concentration decreases exponentially during the observation window. The exact cumulative-exposure-optimal purge has a **sharp feasibility horizon**, is **unique** whenever beneficial, and undergoes an exact **long-horizon timing transition** at equality of the outdoor clearance and indoor natural-clearance rates.

The full result is as follows. Fix \(a,g,B,\beta,T>0\), and \(0<\eta\leq 1\). Define the indoor no-purge equilibrium \(u=g/a\), outdoor-to-indoor concentration ratio \(x=B/u\), and
\[
D(t)=1-e^{-at}-xe^{-\beta t}.
\]
There is a unique \(t_0>0\) satisfying \(D(t_0)=0\). If \(T\leq t_0\), no purge can strictly reduce the integrated indoor pollutant concentration relative to doing nothing. If \(T>t_0\), exactly one time \(\tau_T\in(t_0,T)\) strictly maximizes cumulative-exposure savings; it solves
\[
\frac{ae^{-a\tau_T}+x\beta e^{-\beta\tau_T}}{1-e^{-a\tau_T}-xe^{-\beta\tau_T}}
=\frac{a}{e^{a(T-\tau_T)}-1}.
\tag{1}
\]
It is independent of the replacement fraction \(\eta\), obeys \(T/2<\tau_T<T\), and moves strictly but slower than the horizon: \(0<d\tau_T/dT<1\).

Near the first beneficial horizon, write \(\varepsilon=T-t_0\downarrow0\). Then
\[
\tau_T=t_0+\frac{\varepsilon}{2}+O(\varepsilon^2),\qquad
\max_\tau(J_0-J_\tau)
=\frac{\eta uD'(t_0)}4\,\varepsilon^2+O(\varepsilon^3).
\tag{2}
\]

For large horizons, let \(m=\min(a,\beta)\) and
\[
K=\begin{cases}
x,&\beta<a,\\
1+x,&\beta=a,\\
1,&\beta>a.
\end{cases}
\]
Then the exact first-order and constant-order asymptotic optimum is
\[
\boxed{\displaystyle
\tau_T=\frac{a}{a+m}T+\frac{\log(mK/a)}{a+m}+o(1).}
\tag{3}
\]
Thus the limiting fraction is \(a/(a+\beta)>1/2\) for slowly decaying outdoor pollution \(\beta<a\), and exactly \(1/2\) for \(\beta\geq a\). The optimal savings approaches the maximum possible single-purge savings \(\eta u/a\) with the sharp residual law
\[
1-\frac{a}{\eta u}\max_\tau(J_0-J_\tau)
\sim\left(1+\frac a m\right)
\left(\frac{mK}{a}\right)^{a/(a+m)}
\exp\left(-\frac{am}{a+m}T\right).
\tag{4}
\]
At the critical equality \(\beta=a\), there is an exact all-horizon expression for \(T>t_0=\log(1+x)/a\):
\[
\boxed{\displaystyle
\tau_T=\frac{T+t_0}{2},\qquad
\max_\tau(J_0-J_\tau)=\frac{\eta u}{a}
\left(1-\sqrt{(1+x)e^{-aT}}\right)^2.}
\tag{5}
\]
The slow-outdoor regime has a genuine noncommuting weak-pollution/long-horizon limit: for every fixed \(0<\beta<a\),
\[
\lim_{x\downarrow0}\lim_{T\to\infty}\frac{\tau_T}{T}
=\frac{a}{a+\beta},\qquad
\lim_{T\to\infty}\lim_{x\downarrow0}\frac{\tau_T}{T}=\frac12.
\tag{6}
\]

## Assumptions and scope

The pollutant concentration \(C(t)\) follows the scalar well-mixed mass balance
\[
\dot C(t)=g-aC(t),\qquad C(0)=0,
\]
except for one optional instantaneous purge at \(\tau\in[0,T]\). At that instant a fraction \(\eta\) of indoor air is replaced by outdoor air of pollutant concentration \(B e^{-\beta\tau}\), with no additional chemistry:
\[
C(\tau^+)=(1-\eta)C(\tau^-)+\eta B e^{-\beta\tau}.
\]
Between interventions the outdoor concentration has no effect on the compartment (sealed or negligibly infiltrating baseline); in particular, outdoor air enters *only during the modeled purge*. The source rate \(g\), natural loss rate \(a\), initial outdoor amplitude \(B\), outdoor decay \(\beta\), and purge fraction \(\eta\) are fixed positive inputs. The cumulative exposure proxy is \(J_\tau=\int_0^T C_\tau(t)\,dt\) for continuous unit occupancy. Either one purge or no purge is available; a purge at \(T\) has no effect on this integral.

The theorem is a model-specific exact result, not a clinical safety threshold, a calibrated household recommendation, a result about repeated ventilations, or a claim about real-world sources remaining strictly constant.

## Proof

**1. Reduction to a product.** Without purging, \(C_0(t)=u(1-e^{-at})\). The purge changes concentration at \(\tau\) by \(-\eta uD(\tau)\), after which the change decays as \(e^{-a(t-\tau)}\). Direct integration yields the savings identity
\[
F_T(\tau):=J_0-J_\tau=\frac{\eta u}{a}
\big(1-e^{-a(T-\tau)}\big)D(\tau),\quad 0\leq\tau\leq T.
\tag{7}
\]
The factor \(\eta u/a\) changes the magnitude, not the optimizer.

**2. Sharp onset and uniqueness.** We have \(D(0)=-x<0\), \(\lim_{t\to\infty}D(t)=1\), \(D'(t)=ae^{-at}+x\beta e^{-\beta t}>0\), and \(D''(t)<0\). Thus \(t_0\) exists and is unique. For \(T\leq t_0\), \(F_T(\tau)\leq0\); an absent purge or an end-of-horizon purge gives zero. For \(T>t_0\), \(F_T\) is positive on \((t_0,T)\) and zero at its endpoints. On this interval both \(D\) and \(1-e^{-a(T-\tau)}\) are positive with strictly negative second derivatives of their logarithms. The logarithm of their product is therefore strictly concave and has a unique interior maximum. Its derivative vanishes exactly at equation (1), proving existence, necessity, sufficiency, and uniqueness. At \(\tau=T/2\), if \(T/2\leq t_0\) the optimum is visibly later; otherwise
\[
\frac{D'(T/2)}{D(T/2)}>
\frac{ae^{-aT/2}}{1-e^{-aT/2}}
=\frac{a}{e^{aT/2}-1},
\]
so equation (1)'s strictly decreasing left-minus-right expression is still positive. Hence \(\tau_T>T/2\).

**3. Horizon monotonicity.** Write \(G(\tau,T)=(\log D)'(\tau)-a/(e^{a(T-\tau)}-1)\). At the unique optimum, \(G=0\). With \(z=a(T-\tau)>0\),
\[
G_\tau=(\log D)''-\frac{a^2e^z}{(e^z-1)^2}<0,
\qquad G_T=\frac{a^2e^z}{(e^z-1)^2}>0.
\]
The implicit-function theorem gives \(d\tau_T/dT=-G_T/G_\tau\in(0,1)\).

**4. Onset expansion.** When \(T=t_0+\varepsilon\), write \(\tau=t_0+y\). Uniform Taylor expansion for \(0\leq y\leq\varepsilon\) gives \(D(t_0+y)=D'(t_0)y+O(y^2)\) and \(1-e^{-a(\varepsilon-y)}=a(\varepsilon-y)+O((\varepsilon-y)^2)\). The maximizing logarithmic derivative condition (or its rescaled strict-concavity equation) yields \(y=\varepsilon/2+O(\varepsilon^2)\). Inserting into (7) proves (2).

**5. Large-horizon asymptotics.** The test placement \(\tau=T/2\) makes the normalized product in (7) tend to one. Its maximum also tends to one, and each of its two factors is at most one. Consequently \(\tau_T\to\infty\) and \(T-\tau_T\to\infty\). By definition of \(m,K\),
\[
1-D(\tau)=K e^{-m\tau}(1+o(1)),\qquad
D'(\tau)=mK e^{-m\tau}(1+o(1)).
\]
Equation (1) therefore reads
\[
mK e^{-m\tau_T}=a e^{-a(T-\tau_T)}(1+o(1)).
\]
Taking logarithms proves (3). The normalized savings differs from one by
\[
K e^{-m\tau_T}+e^{-a(T-\tau_T)}+o\big(e^{-m\tau_T}+e^{-a(T-\tau_T)}\big).
\]
The leading balance has ratio \(mK e^{-m\tau_T}/(a e^{-a(T-\tau_T)})\to1\), which gives (4).

**6. Equal-rate and singular limits.** When \(\beta=a\), \(D(\tau)=1-(1+x)e^{-a\tau}\), and equation (1) reduces exactly to \(e^{-a(T-\tau)}=(1+x)e^{-a\tau}\). This proves both formulas in (5). For the second iterated limit in (6), setting \(x=0\) in the continuous extension of (7) produces a symmetric product with unique optimum \(T/2\). The first iterated limit follows from (3) at every fixed \(x>0\). Since \(a/(a+\beta)>1/2\) for \(\beta<a\), the limits are unequal.

## Verification

The supplied standalone `check.py` is executable with Python 3 and only the standard library:

```sh
python3 check.py
```

Its tests independently integrate the piecewise mass-balance solution, compare computed savings to the closed formula, search 61 alternative placements in each of 1,500 varied parameter instances, check nonbeneficial short horizons and horizon monotonicity, verify 1,000 equal-rate exact cases, test onset coefficients, and test six large-horizon rate regimes. The run completed with `PASS 108524 numerical assertions`. These finite checks are a reproducibility aid; all universal claims rest on the analytic proof above.

For an illustrative normalized choice \(a=1\), \(x=0.7\), and \(T=20\), the optimum is about \(14.189653\) if \(\beta=0.3\), about \(10.265314\) if \(\beta=1\), and \(10.000000\) to six decimal places if \(\beta=3\). The units of \(T\) and the rates must be consistent. These are not measured household values.

## Relationship to prior work

Time-dependent indoor/outdoor pollutant differences, continuing indoor sources, and the benefits and hazards of ventilation are well established. Singh and coauthors (2024) measured strong room-to-room and activity-related variations in indoor pollutant levels. Kim, Kim, and Yeo (2020) developed a continuously adjusted ventilation/filtration strategy involving indoor generation and outdoor PM concentration; Wu and colleagues (2022) evaluated control combinations empirically; Park and colleagues (2022) developed a time-dependent mass-balance model for indoor particles; Shin and colleagues (2023, first available as a September 2023 preprint) compared mechanical ventilation performance against differing outdoor PM levels. These results motivate the scalar benchmark and establish that neither the mass-balance equation nor the indoor/outdoor competition is newly discovered. Their investigated interventions, objectives, and analyses do not themselves state equation (1), the all-horizon unique instant-purge optimizer, the exact equal-rate case, or the weak-pollution noncommuting limit (6).

A literature and mathematical-claim overlap search also examined variants such as one-time fractional exchange, pulsed ventilation, control of indoor-outdoor pollutants, and exponential decay; no inspected full text or indexed claim was found that already implies this combined exact theorem. Absence of a search hit does not prove novelty. In particular, broader optimal/impulse-control and building-services literature may contain an equivalent result not found in this inspection.

## Limitations

The intervention is instantaneous and well mixed; real window opening has a finite flow rate, outdoor infiltration may persist between openings, outdoor concentration may fluctuate rather than decay exponentially, occupancy may vary, and chemical reactions or surface reservoirs may matter. Only a single contaminant and one purge are considered. The result optimizes a concentration-time integral, not peak concentration, health risk, energy use, thermal comfort, or safety. The unusually long-horizon limit may be less relevant to practical occupancy periods. Independent external mathematical checking and empirical model calibration have not been performed. Historical priority remains provisional.

## References

1. Singh, A., Bartington, S. E., Abreu, P., Anderson, R., Cowell, N., and Leach, F. C. P. (2024). *Impacts of daily household activities on indoor particulate and NO2 concentrations; a case study from Oxford UK*. Heliyon 10, e34210. First published 2024-07-05. https://doi.org/10.1016/j.heliyon.2024.e34210 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC11333897/
2. Kim, J.-H., Kim, H.-G., and Yeo, M.-S. (2020). *Ventilation and Filtration Control Strategy Considering PM2.5, IAQ, and System Energy*. Atmosphere 11, 1140. https://doi.org/10.3390/atmos11111140 ; https://www.mdpi.com/2073-4433/11/11/1140
3. Wu, X. and colleagues (2022). *The energy and time saving coordinated control methods of CO2, VOCs, and PM2.5 in office buildings*. PLOS ONE 17, e0275157. https://doi.org/10.1371/journal.pone.0275157 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC9514625/
4. Park, S. B. and colleagues (2022). *Development and validation of a dynamic mass-balance prediction model for indoor particle concentrations in an office room*. Building and Environment 207, 108465. https://doi.org/10.1016/j.buildenv.2021.108465 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC11009930/
5. Shin, D. and colleagues (2023). *The Effectiveness of a Mechanical Ventilation System for Indoor PM2.5 in Residential Houses*. Toxics 11, 912. Preprint publicly posted 2023-09-26. https://www.preprints.org/manuscript/202309.1685 ; https://doi.org/10.3390/toxics11110912
