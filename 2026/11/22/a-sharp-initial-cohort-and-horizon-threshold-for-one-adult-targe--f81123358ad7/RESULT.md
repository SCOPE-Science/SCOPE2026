# A sharp initial-cohort and horizon threshold for one adult-targeted mosquito intervention

## Finding
Consider a finite monitoring horizon \(T\) and one instantaneous adult-targeted intervention. A protected immature cohort supplies newly mature mosquitoes to the exposed adult cohort, so applying treatment immediately may waste it before immature mosquitoes emerge. There is an **exact and unique** optimal time for minimizing cumulative adult abundance, with a sharp initial-cohort threshold that is independent of immature loss and adulticide efficacy.

Write \(b=\beta L_0\), \(a=A_0/b\), and \(H(t)=(1-e^{-\mu t})/\mu\). The sharp answer is
\[
s_* =0\quad\Longleftrightarrow\quad a\ge H(T).
\]
If \(0\le a<H(T)\), the unique optimal time is the unique solution of
\[
H(T-s_*)=a e^{(\alpha-\mu)s_*}+\int_0^{s_*} e^{(\alpha-\mu)u}\,du,
\qquad 0<s_*<T/2.
\]
In this delayed regime, the optimum decreases strictly with immature loss \(\alpha\) and initial adult-to-emergence ratio \(a\), and increases strictly with horizon \(T\). The decision between immediate and delayed treatment is independent of treatment strength \(q\in(0,1]\). If \(0<a<1/\mu\), delaying begins exactly when
\[
T>T_c:=-\mu^{-1}\log(1-\mu a).
\]
For \(a\ge 1/\mu\), no horizon makes delaying optimal. For \(a=0\), every positive horizon favors delay.

For the formal continuous-emergence limit \(\alpha=0\), the delayed optimum has the closed form
\[
s_*={T}\over 2}+{\log(1-\mu a)}\over 2\mu};
\]
this boundary is a mathematical comparison, not a finite immature cohort with positive emergence.

## Assumptions and scope
For every \(T,\alpha,\beta,\mu,L_0>0\) and \(A_0\ge0\), untreated abundances satisfy
\[
L'(t)=-\alpha L(t),\qquad A'(t)=\beta L(t)-\mu A(t),
\quad L(0)=L_0,\ A(0)=A_0.
\]
A single instantaneous pulse at \(s\in[0,T]\) replaces \(A(s^-)\) by \((1-q)A(s^-)\), with \(0<q\le1\), and leaves \(L\) unchanged. When \(s=0\), the initial adult cohort is treated; when \(s=T\), endpoint removal has zero contribution to the time integral. The objective is \(J_q(s)=\int_0^T A_q(t)\,dt\). No new immature production, density dependence, migration, resistance or residual pesticide action occurs. For a literal finite immature cohort with maturation as part of its loss, one may impose \(\beta\le\alpha\); the theorem remains valid under that restriction. Rates are time homogeneous.

## Proof
**1. Exact objective.** The untreated adult trajectory is
\[
A(t)=A_0e^{-\mu t}+b\int_0^t e^{-\alpha u-\mu(t-u)}\,du,
\qquad b=\beta L_0.
\]
An adult removed at time \(s\) cannot contribute later because adult recruitment does not depend on adult abundance. Hence, relative to no treatment, the exact avoided adult-days equal
\[
R_q(s)=q A(s)H(T-s),\qquad
H(v)=\int_0^v e^{-\mu u}du.
\]
It is enough to maximize \(F(s)=A(s)H(T-s)\); because \(q>0\) is a common factor, the optimizer is independent of \(q\).

**2. Root equation.** From \(A'(s)=be^{-\alpha s}-\mu A(s)\), and \(\mu H(v)+e^{-\mu v}=1\),
\[
F'(s)=b e^{-\alpha s}H(T-s)-A(s)
=b e^{-\alpha s}[H(T-s)-D(s)],
\]
where
\[
D(s):={A(s)}\over be^{-\alpha s}}
=a e^{(\alpha-\mu)s}+\int_0^s e^{(\alpha-\mu)u}du,
\qquad a={A_0}\over b}.
\]
Thus \(F'(0)=b[H(T)-a]\) and \(F'(T)=-A(T)<0\).

**3. Global classification.** If \(a<H(T)\), then \(D'(s)=e^{(\alpha-\mu)s}[1+(\alpha-\mu)a]>0\). The only nonobvious case is \(\alpha<\mu\): here \(a<H(T)<1/\mu<1/(\mu-\alpha)\), so the bracket is positive. Since \(H(T-s)\) strictly decreases with \(s\), the difference \(H(T-s)-D(s)\) strictly decreases from a positive number to a negative number. Consequently \(F\) first strictly increases and then strictly decreases; its unique maximizer is the stated root.

If \(a\ge H(T)\), and \(\alpha\ge\mu\), then \(D(s)\ge a\ge H(T)\). If \(\alpha<\mu\), set \(k=\mu-\alpha>0\) and write
\[
D(s)=e^{-ks}a+(1-e^{-ks})/k.
\]
This is a convex combination of \(a\) and \(1/k\), both at least \(H(T)\) because \(1/k>1/\mu>H(T)\). Thus in either case \(H(T-s)-D(s)<0\) for \(s>0\), establishing the unique boundary maximizer \(s_*=0\), including equality \(a=H(T)\).

**4. Comparative statics and half-horizon bound.** In the interior regime, \(D(s)\) is strictly increasing in each of \(a\) and \(\alpha\) for \(s>0\), since
\[
{\partial D}\over{\partial\alpha}
=as e^{(\alpha-\mu)s}+\int_0^s u e^{(\alpha-\mu)u}du>0.
\]
(The integral is strictly positive.) Meanwhile \(H(T-s)\) increases in \(T\). Uniqueness of the root implies the stated strict monotonicities, holding while parameters remain inside the delayed regime. To bound its time, formally extend to \(\alpha=0\): with \(D(s)=a e^{-\mu s}+H(s)\), the root solves
\[
e^{2\mu s}=e^{\mu T}(1-\mu a).
\]
It equals \(T/2+\log(1-\mu a)/(2\mu)\le T/2\). Since the genuine model assumes \(\alpha>0\), increasing \(\alpha\) shifts the interior root strictly left, proving \(s_*<T/2\). Finally \(a<H(T)\) is equivalent to the stated horizon threshold when \(0<a<1/\mu\). For \(a\ge1/\mu\), this strict inequality is impossible. This completes the global proof.

## Verification
A standalone standard-library script `impulse_benchmark.py` independently computes the root by bisection, compares its benefit against an 81-point time grid for 300 deterministic seeded parameter sets, tests comparative statics, and numerically integrates the forward system to cross-check the exact avoided-adult-days identity. It reports 25,556 finite supplementary assertions passed. These tests check software arithmetic and illustrations; the preceding analytic proof establishes the universal result.

For \(T=2\), \(\alpha=\beta=\mu=L_0=1\), \(A_0=1/5\), the exact threshold is \(a_c=1-e^{-2}\), so this initial condition is in the delayed regime. The unique optimum lies in \((0.56248,0.56249)\), and the removed adult-days exceed \(1.91\) times those removed by an immediate application of the same efficacy. In contrast, \(A_0=0.9\) makes immediate treatment uniquely optimal, with all other rates unchanged.

## Relationship to prior work
Kummer and colleagues (2024) use field-informed mosquito activity patterns, a stage-structured simulation and timed adulticide applications to compare dengue-control scenarios. This result instead isolates a linear one-pulse, cumulative adult-abundance benchmark and gives an exact global initial-stage threshold. Barclay and colleagues (2018) optimize numbers and spacing of repeated insecticide sprays in a stage-structured density-dependent insect model, with a different knockdown target. Agusto and colleagues (2022) treat a higher-dimensional epidemic system with impulsive control and necessary optimality conditions; those do not by themselves give the present explicit all-rate timing classification. The exact elementary reductions, and especially the uniform independence of the threshold from immature loss and kill fraction, are the asserted contribution; no general theorem for complex mosquito populations is claimed.

## Limitations
The model omits mosquito reproduction, density feedback, temperature, diel activity, variable spray uptake, residual insecticide, resistance, disease transmission and multiple pulses. The mathematical choice \(\alpha=0\) is a limiting constant-emergence scenario, not a finite depleting larval cohort. Real schedules require empirical parameter calibration and evaluation of collateral costs. An optimal cumulative adult-day criterion need not optimize an epidemic outcome or terminal adult density. Historical priority is provisional beyond the inspected sources; no independent external audit has been performed.

## References
1. Kummer, A. G., et al. (2024). *Comparing the effectiveness of adulticide application interventions on mitigating local transmission of dengue virus*. Journal of Pest Science. First online 10 May 2024. https://doi.org/10.1007/s10340-024-01787-w
2. Barclay, H. J., Hargrove, J. W., Steacy, R., and van den Driessche, P. (2018). *Modelling optimal timing and frequency of insecticide sprays for knockdown in preparation for other control measures*. International Journal of Pest Management. https://doi.org/10.1080/09670874.2018.1475690
3. Agusto, F., et al. (2022). *Optimal impulse control of West Nile virus*. AIMS Mathematics. https://doi.org/10.3934/math.20221075
4. Djerdj, T., et al. (2022). *Modelling can reduce contamination from mosquito population control*. https://doi.org/10.1007/s00477-022-02326-8
