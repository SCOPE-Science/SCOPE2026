# Strict subgroup reinfection bounds distinguish leaky and all-or-none vaccination

## Finding

Consider the transient two-group, homogeneous-mixing SIRI epidemic of Gutierrez and Gog with leaky vaccine protection against **primary** infection and leaky immunity after infection. Let the vaccinated fraction be \(c\), let vaccinees' relative primary susceptibility be \(\theta\), let every recovered person's relative reinfection susceptibility be \(\phi\), and let the transmission-to-recovery ratio be \(R_0\). Assume
\[
0<c<1,\qquad 0<\phi\leq\theta<1,\qquad R_0\phi<1,
\qquad R_0(1-c+c\theta)>1.
\]
Work on the nontrivial, transient epidemic branch obtained from vanishing positive infectious seeding. Write \(H=\int_0^\infty\lambda(t)\,dt\in(0,\infty)\) for the integrated common force of infection, and \(P_U,P_V,Q_U,Q_V\) for cumulative primary and repeat infections in the unvaccinated and vaccinated groups, respectively. Define
\[
\rho=\frac{1-e^{-\theta H}}{1-e^{-H}},\qquad Q=Q_U+Q_V.
\]
Then the **strict three-level ordering** is
\[
\boxed{\quad
\theta<\frac{Q_V/c}{Q_U/(1-c)}<\rho<1,\qquad
\frac{Q_V}{P_V}<\frac{Q_U}{P_U}.
\quad}
\]
In particular, a lower fraction of all repeat infections occurs among vaccinees than their fraction of all primary infections, despite both groups having identical susceptibility once infected. The two unknown groupwise reinfection totals satisfy the directly usable bounds
\[
\boxed{\quad
\frac{c\theta}{1-c+c\theta}\,Q<Q_V<
\frac{c\rho}{1-c+c\rho}\,Q,
\qquad Q_U=Q-Q_V.
\quad}
\]
All the quantities in these bounds are computable from the already-known final-pressure equation, because
\[
P_U=(1-c)(1-e^{-H}),\quad P_V=c(1-e^{-\theta H}),
\quad Q=\frac{H-(1-e^{-\phi H})/\phi}{R_0}.
\]
For the **all-or-none immunity** version with the same group proportions and susceptibility factor, both groupwise counts instead obey exact proportionality \(Q_V/c=\theta Q_U/(1-c)\) and \(Q_V/P_V=Q_U/P_U\) within that version's epidemic. This is a difference in within-epidemic subgroup composition, not a comparison of total epidemic sizes between the two vaccination mechanisms.

More generally, **holding any one nonnegative, integrable common infection-pressure curve fixed**, let \(F(q)\) be the expected lifetime repeat-infection count of an initially never-infected individual with primary susceptibility \(q>0\), recovery rate one, and common postinfection susceptibility \(\phi>0\). Provided the curve has nontrivial positive exposure after an initial infection, every derivative exists and
\[
\boxed{\quad (-1)^{m-1}F^{(m)}(q)>0
\quad\text{for all integers }m\geq1.\quad}
\]
This fixed-force Bernstein-function property implies the ordering above, but makes no assertion about varying the vaccine parameter while allowing the epidemic pressure to change endogenously.

## Assumptions and scope

The transient model has a closed, well-mixed population with no births or deaths, exponential infectious durations of mean one, a common nonnegative force \(\lambda(t)=R_0(I_U(t)+I_V(t))\), and common relative susceptibility \(\phi\) after first recovery regardless of vaccine status. The two virgin-susceptible compartments have per-capita rates \(\lambda\) and \(\theta\lambda\); post-primary recovered individuals have rate \(\phi\lambda\); infectious individuals recover at rate one. Vaccination occurs only before the epidemic. All infection episodes have the same infectious duration and infectiousness. These are precisely the assumptions of the leaky-immunity branch of the cited SIRI model, not assumptions about real-world clinical outcomes.

The source's final-size convention uses an infinitesimal infectious seed: first solve with positive seeds, then take the limit on the nontrivial outbreak branch. The inequalities concern this limit, in which initially infected individuals form a vanishing proportion and all positive-mass subgroups begin susceptible. The conditions above ensure an initial outbreak and a finite total force of infection. Strictness assumes \(\lambda(t)>0\) over a nontrivial time interval and nonzero future exposure after infection, as occurs along the transient positive-infection branch. At \(\phi=0\) every repeat-infection count vanishes and these ratios are undefined.

The general fixed-force lemma does not assume the particular SIRI feedback law or temporal monotonicity of \(\lambda\). Its strictness applies when the force is nontrivial and continuous with positive exposure on an interval, and \(H<\infty\).

## Proof

**1. Conditional post-primary process.** Fix the common deterministic infection-pressure curve \(\lambda(t)\), without changing it when comparing the two already-present groups. Given a first infection at time \(t\), the host then occupies an infectious state \(I\) or a postinfection recovered state \(R\), with transitions \(I\to R\) at rate one and \(R\to I\) at rate \(\phi\lambda(s)\). Each \(R\to I\) transition counts one repeat infection. Let \(v_I(t)\), \(v_R(t)\) be the expected numbers of *future* repeat infections started at calendar time \(t\) in those states. Their backward equations are
\[
-v_I'(t)=v_R(t)-v_I(t),\qquad
-v_R'(t)=\phi\lambda(t)\bigl(1+v_I(t)-v_R(t)\bigr),
\]
with limits zero as \(t\to\infty\), because the remaining cumulative force tends to zero. Put \(w(t)=v_R(t)-v_I(t)\). Solving its scalar terminal-value equation yields
\[
w(t)=\int_t^\infty \phi\lambda(s)
\exp\left[-(s-t)-\phi\int_t^s\lambda(u)\,du\right]ds>0
\]
for every finite \(t\) along the positive epidemic branch. Consequently
\[
\frac{d}{dt}v_I(t)=-w(t)<0,\qquad
v_I(t)=\int_t^\infty w(s)\,ds.
\]
Both quantities are finite: \(0\le w(t)\le1\) and the expected number of repeat transitions cannot exceed the expected number of postinfection infectious challenges, which is bounded by \(\phi\int_t^\infty\lambda(s)\,ds\). Thus an earlier primary infection leaves a strictly greater expected repeat burden, even when the force of infection is nonmonotone.

**2. Hazard-coordinate representation.** Let \(x(t)=\int_0^t\lambda(s)ds\), so \(x\) increases from zero to \(H\). Conditional on beginning never infected with relative primary susceptibility \(q>0\), the first-infection cumulative-hazard time has density \(qe^{-qx}\) for \(0<x<H\), and an atom \(e^{-qH}\) for no infection. Define \(v(x)=v_I(t(x))\) and its positive Stieltjes measure \(\mu(dx)=-dv(x)\) on \((0,H)\). By step 1, \(v(x)\) strictly decreases to zero, so \(\mu\) is a positive, nonzero finite measure with positive mass at positive hazard. The per-capita repeat burden is therefore
\[
F(q)=\int_0^H qe^{-qx}v(x)\,dx
=\int_{(0,H)}(1-e^{-qs})\,\mu(ds).
\]
Dominated differentiation (\(H<\infty\)) gives for every integer \(m\ge1\)
\[
(-1)^{m-1}F^{(m)}(q)
=\int_{(0,H)}s^m e^{-qs}\,\mu(ds)>0.
\]
In particular \(F\) is strictly increasing and strictly concave, with \(F(0)=0\). Since \(0<\theta<1\), strict concavity yields \(F(\theta)>\theta F(1)\).

**3. Conditioning on a primary infection.** The per-capita primary-infection probability at susceptibility \(q\) is \(B(q)=1-e^{-qH}\). Conditional on a primary infection, its hazard-coordinate density is
\[
f_q(x)=\frac{qe^{-qx}}{1-e^{-qH}},\qquad 0<x<H.
\]
For \(q_1>q_2>0\), the likelihood ratio \(f_{q_1}(x)/f_{q_2}(x)\) is strictly decreasing in \(x\). Thus the former law is strictly stochastically earlier. Since \(v(x)\) is strictly decreasing, \(F(q_1)/B(q_1)>F(q_2)/B(q_2)\). Apply this at \(q_1=1\), \(q_2=\theta\) to obtain
\[
\frac{F(\theta)}{F(1)}<\frac{B(\theta)}{B(1)}
=\frac{1-e^{-\theta H}}{1-e^{-H}}=\rho.
\]
Combining this with step 2 yields \(\theta<F(\theta)/F(1)<\rho<1\). The epidemic's same-force linear subgroup equations identify \(Q_U=(1-c)F(1)\), \(Q_V=cF(\theta)\), \(P_U=(1-c)B(1)\), and \(P_V=cB(\theta)\), proving both claimed strict orderings.

**4. Quantitative disaggregation.** Put \(r=F(\theta)/F(1)\). The total repeat burden satisfies
\[
Q=(1-c)F(1)+cF(\theta)=[1-c+cr]F(1),
\quad Q_V=\frac{cr}{1-c+cr}\,Q.
\]
The rightmost factor is strictly increasing in \(r>0\); applying \(\theta<r<\rho\) gives both quantitative bounds. The source's final-size identity supplies \(Q=\bigl[H-(1-e^{-\phi H})/\phi\bigr]/R_0\); no group-specific repeat-infection formula is assumed. In the all-or-none model, vaccinated hosts either have complete vaccine protection or join the unvaccinated susceptibility/recovery mechanism, so its two groups' per-capita infection counts differ by exactly \(\theta\). This is also the published proportionality relation for that model.

## Verification

The accompanying `verify.py` uses only Python's standard library. Running `python verify.py` integrates the complete leaky two-group SIRI compartment equations with fourth-order Runge–Kutta, records primary and repeat infections separately, and checks conservation, the known aggregate final-size identity in the vanishing-seed approximation, all strict bounds, and six distinct biologically admissible parameter tuples. These finite calculations independently stress-test the stated formulas; the universal and strict claims are established by the analytic proof above, **not** by these computations.

For illustration, with \(R_0=2\), \(c=1/2\), \(\theta=1/2\), \(\phi=1/4\), a seed of size \(10^{-8}\) gives approximately \(H=1.719262\), \(Q_U=0.099069\), \(Q_V=0.061820\), \(\rho=0.702584\), and per-capita ratio \((Q_V/c)/(Q_U/(1-c))=0.624013\). The source-based bounds for the vaccinated repeat total are approximately \(0.053630<Q_V<0.066392\). These figures are numerical approximations to the positive infinitesimal-seed branch.

## Relationship to prior work

Gutierrez and Gog's SIRI model, originally made public September 14, 2025, derives the total reinfection count and both primary-infection counts in the leaky model (published article, Sect. 4.3, equations 39–42), while explicitly not giving separate cumulative reinfection counts for vaccinated and unvaccinated people. Its all-or-none model already establishes equal repeat-to-primary ratios in the two groups (Sect. 3.3, equation 18). Neither fact alone implies the new *strict leaky-subgroup ordering*, the measurable bounds on the uncomputed pieces, or the alternating derivative hierarchy for a fixed arbitrary force of infection.

Edlefsen (2014) investigates selection in time-to-*first-infection* data under leaky vaccines and explicitly stops following subjects after their first infection; it does not obtain a repeat-infection allocation theorem. Magpantay et al. (2014) study imperfect vaccines in an immunizing SIR setting and the resulting equilibrium/age composition, rather than this fixed post-primary-susceptibility transient reinfection comparison. Katriel (2010) derives partial-immunity final sizes without pre-epidemic vaccination groups. Gomes, White and Medley (2004) study an earlier model incorporating immune waning and vaccination, with materially different mechanisms, and a full-text priority comparison remains unresolved. This work is therefore a literature-bounded new statement, not a claim of exhaustive priority or independent certification.

## Limitations

The ordering is *within one realized epidemic*; if primary susceptibility or vaccination coverage is changed between experiments, the common force \(\lambda\) changes endogenously and the fixed-force derivative signs do not establish a comparative intervention effect. The bounds do not identify the exact subgroup counts without time-course information, and no parameter-independent narrower bounds are asserted. The analysis uses equal post-primary susceptibility across groups, exponential infectious periods, an idealized infinitesimal infectious seed, and a transient outbreak with finite total force. It does not cover endemic recurrent epidemics with infinite cumulative repeat burden, differential postinfection vaccine protection, demography, behavior, or clinical data. The historical-priority assessment has residual uncertainty from inaccessible earlier full texts; no independent audit has been performed.

## References

1. Gutierrez, M. A., and Gog, J. R. *Final-size solutions for SIRI models with vaccination*, medRxiv first version posted September 14, 2025. https://www.medrxiv.org/content/10.1101/2025.09.12.25335631v1 ; DOI: 10.1101/2025.09.12.25335631.
2. Gutierrez, M. A., and Gog, J. R. *Final-Size Solutions for SIRI Models with Vaccination*, Bulletin of Mathematical Biology 88 (2026), 64, March 24, 2026. https://doi.org/10.1007/s11538-026-01610-w.
3. Edlefsen, P. T. *Leaky Vaccines Protect Highly Exposed Recipients at a Lower Rate: Implications for Vaccine Efficacy Estimation and Sieve Analysis*, Computational and Mathematical Methods in Medicine (2014), 813789. https://doi.org/10.1155/2014/813789.
4. Magpantay, F. M. G., Riolo, M. A., Domenech de Celles, M., King, A. A., and Rohani, P. *Epidemiological Consequences of Imperfect Vaccines for Immunizing Infections*, SIAM Journal on Applied Mathematics 74 (2014), 1810–1830. https://doi.org/10.1137/140956695.
5. Katriel, G. *Epidemics with partial immunity to reinfection*, Mathematical Biosciences 228 (2010), 153–159. https://doi.org/10.1016/j.mbs.2010.09.003.
6. Gomes, M. G. M., White, L. J., and Medley, G. F. *Infection, reinfection, and vaccination under suboptimal immune protection: epidemiological perspectives*, Journal of Theoretical Biology 228 (2004), 539–549. https://doi.org/10.1016/j.jtbi.2004.02.015.
