# A sharp seasonal allocation law for fixed-budget Beverton–Holt harvesting

## Finding

Consider alternating Beverton–Holt recruitment with two independently chosen proportional harvests. For fixed *cumulative fishing mortality*, every admissible allocation has the same low-density persistence multiplier, but its sustainable catch generally differs. Whenever positive persistence is possible, the total two-season sustainable catch has exactly one maximizing allocation. An explicit monotone-ratio test decides whether the entire effort should be concentrated in the first season, concentrated in the second, or split strictly between them. In the interior case, the loss from any suboptimal allocation is an **exact strictly positive quadratic expression**, not merely a local approximation.

Specifically, write \(s_0=t\), \(s_1=S/t\), with \(0<S<1\) and \(S\le t\le1\). Define

\[
Q=r_0r_1S-1,\quad
U(t)=\frac{K_1+r_0K_0t}{r_1SK_1+K_0t},\quad
R=\sqrt{\frac{K_1+r_0SK_0}{S(K_0+r_1SK_1)}}.
\]

If \(Q>0\), the unique maximizing allocation \(t_*\) is precisely

\[
t_*=\begin{cases}
S,&U(S)\ge R,\\
1,&U(1)\le R,\\
\displaystyle \frac{K_1(Rr_1S-1)}{K_0(r_0-R)},&U(S)<R<U(1).
\end{cases}
\]

The inequalities are mutually exclusive because \(U\) is strictly increasing. In the third case the displayed quotient belongs strictly to \((S,1)\).

## Assumptions and scope

Take \(r_0,r_1>1\) and crowding scales \(K_0,K_1>0\). The populations immediately before seasonal recruitment are \(x_n\ge0\), and the model is

\[
f_i(x)=\frac{r_ix}{1+x/K_i},\qquad
x_{n+1}=s_i f_i(x_n),\quad i=n\bmod2.
\]

Here \(s_i\in(0,1]\) is the fraction surviving the harvest immediately **after** recruitment in season \(i\), and that season's catch is \((1-s_i)f_i(x_n)\). The linear-effort mortality convention \(s_i=e^{-e_i}\), \(e_i\ge0\), makes the constraint \(e_0+e_1=E>0\) equivalent to \(s_0s_1=S=e^{-E}\). The total budget is prescribed; this theorem does not optimize the total magnitude \(E\). The \(K_i\) are denominator crowding scales; for an unharvested single season the corresponding equilibrium biomass is \((r_i-1)K_i\), so they should not be confused with that equilibrium.

The objective is the sum \(Y\) of the two catches on the attracting two-cycle, equal to twice the per-season average sustainable catch. No stochastic immigration, age structure, price, ecological constraints on individual harvest, implementation costs, or uncertainty is included. The endpoints \(t=S\) and \(t=1\) are allowed and respectively mean no harvest in season 1 and no harvest in season 0.

## Proof

**1. Global population dynamics and a schedule-invariant persistence threshold.** For a positive state let \(y_n=1/x_n\). The inverse-population dynamics is affine:

\[
y_{n+1}=\frac{y_n+K_i^{-1}}{r_is_i}.
\]

Every two-season step therefore has multiplier \((r_0r_1S)^{-1}\) and a strictly positive additive term. Consequently, when \(r_0r_1S>1\), the inverse dynamics contracts to one positive two-cycle from every positive initial state. If \(r_0r_1S=1\), inverse biomass grows linearly along the two-season subsequence; if \(r_0r_1S<1\), it grows exponentially. Both latter cases force extinction \(x_n\to0\) and zero limiting catch. Thus no distribution of the same total effort changes the basic persistence verdict.

**2. Closed positive cycle.** Assume \(Q=r_0r_1S-1>0\) and put \(t=s_0\), \(s_1=S/t\). Solving the affine inverse cycle yields the two positive biomass levels

\[
\bar x_0=\frac{QK_0K_1}{K_1+r_0K_0t},\qquad
\bar x_1=\frac{tQK_0K_1}{r_1SK_1+K_0t}.
\]

Indeed \(\bar x_1=t f_0(\bar x_0)\) and \(\bar x_0=(S/t)f_1(\bar x_1)\). Since catch 0 is \((1-t)\bar x_1/t\) and catch 1 is \((t-S)\bar x_0/S\), their sum is

\[
Y(t)=QK_0K_1\left[\frac{1-t}{r_1SK_1+K_0t}
+\frac{t-S}{S(K_1+r_0K_0t)}\right].
\]

**3. Exact global optimizer.** Direct differentiation, with all denominators positive, gives

\[
\frac{Y'(t)}{QK_0K_1}=
\frac{K_1+r_0SK_0}{S(K_1+r_0K_0t)^2}
-\frac{K_0+r_1SK_1}{(r_1SK_1+K_0t)^2}.
\]

Its sign equals that of \(R-U(t)\). Crucially,

\[
U'(t)=\frac{K_0K_1Q}{(r_1SK_1+K_0t)^2}>0.
\]

Thus \(Y\) strictly increases before the possible crossing \(U=R\) and strictly decreases afterward. If this crossing lies outside the feasible interval, the appropriate endpoint is the unique maximizer. If it lies within, rearranging the one linear-fractional equation gives the third formula in the Finding. Equality at either endpoint still gives that unique boundary maximizer, since the derivative is strictly of one sign in the interior.

**4. Exact regret inside the split-effort regime.** In the strict interior case let \(t_*\) denote the critical allocation. Rearranging \(Y\) as a difference of two reciprocal affine functions and using \(Y'(t_*)=0\) yields, for every \(t\in[S,1]\),

\[
\begin{aligned}
Y(t_*)-Y(t)={}&\frac{Q^2(K_0K_1)^2(K_0+r_1SK_1)(t-t_*)^2}{
(r_1SK_1+K_0t_*)^2
(r_1SK_1+K_0t)
(K_1+r_0K_0t)}.
\end{aligned}
\]

All factors except the square are strictly positive. This independently certifies strict and global optimality in that regime, and quantifies the full finite-perturbation penalty.

**5. Interpretable contrasting cases.** In the symmetric environment \(r_0=r_1=r\), \(K_0=K_1=K\), the unique allocation is \(t_*=\sqrt S\): equal log-effort in the two seasons. But with \(r_0=r_1=4\), \(S=1/5\), \(K_0=10\), \(K_1=1\), one has \(U(S)>R\) and all effort in season 0 is uniquely best, yielding \(Y=44/7\) per two-season cycle. Equal-effort harvesting yields about \(3.7463942534\), so the constrained optimum improves the long-run catch by about \(67.78\%\). Swapping the two crowding scales reverses which season receives all the harvest effort.

## Verification

The bundled \(check.py\) is a standalone Python 3 standard-library checker. Run it from the directory containing the files as `python3 check.py`. It independently computes the periodic orbit from the two recurrence equations, recomputes the yield from catches, verifies exact rational identities, checks the optimizer and regret against deterministic parameter sweeps, and iterates the population dynamics on both sides of the extinction threshold. A completed replay gave 59,764 passed diagnostic assertions. The all-parameter claims follow from the explicit algebra above; no finite test is offered as a replacement for proof.

## Relationship to prior work

AlSharawi and Rhouma (2010) examine constant and periodic *additive catch quotas* with variable environmental carrying capacity, persistence, and sustainable-yield comparisons; see in particular sections 2–4 and Theorems 4.3 and 4.8. Their schedule constraint is not a fixed product of proportional escapement factors. Bohner and Streipert (2016) prove periodic Beverton–Holt equilibria and an **unconstrained** optimal seasonal harvest-effort theorem (Theorems 3.8–3.10). The present statement instead fixes the aggregate cumulative mortality, allowing the same persistence multiplier under every split; its explicit clipped constrained allocation, phase-boundary cases, and exact full-range quadratic regret are not consequences of quoting that unconstrained optimizer. Filar, Qiao and Streipert (2020) examine risk sensitivity with constant multiplicative harvest and periodic carrying capacities rather than two independently allocated seasonal efforts. These comparisons support a limited best-knowledge originality assessment, not a claim of exhaustive historical priority.

## Limitations

This is a deterministic idealization with exactly two periodically repeated environmental seasons and proportional post-recruitment removal. The model excludes effort-dependent prices, travel or fleet constraints, stochastic recruitment, density-dependent catchability, stock-viability lower bounds, and uncertainty in biological parameters. The optimum is for long-run sustainable **biomass catch** at a fixed total hazard budget, not economic profit or transient catch. The exact phase boundary may be sensitive to unknown crowding scales. No independent mathematical audit or historical-priority certification has been performed.

## References

- Z. AlSharawi and M. Ben Haj Rhouma, “The Discrete Beverton-Holt Model with Periodic Harvesting in a Periodically Fluctuating Environment,” *Advances in Difference Equations* (2010), article 215875. First published 2010-03-08. DOI: https://doi.org/10.1155/2010/215875 . Full text: https://link.springer.com/article/10.1155/2010/215875
- M. Bohner and S. Streipert, “Optimal Harvesting Policy for the Beverton–Holt Model,” *Mathematical Biosciences and Engineering* 13 (2016), 673–695. Published online 2016-05. DOI: https://doi.org/10.3934/mbe.2016014 . Author-hosted full text: https://web.mst.edu/bohner/papers/ohpftbhm.pdf
- J. A. Filar, Z. Qiao and S. Streipert, “Risk Sensitivity in Beverton–Holt Fishery with Multiplicative Harvest,” *Natural Resource Modeling* 33 (2020), e12257. DOI: https://doi.org/10.1111/nrm.12257 . Published online 2020-01-24.
