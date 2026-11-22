# Sharp survivor staircases and a resource ceiling in a shared/local nutrient community

## Finding

In the one-nutrient, common-isolation specialization of the spatial consumer–resource system of ElGamel and Mugler [1], **every number of consumer species** admits an exact nested-survivor classification at stationary states. Suppose the distinct break-even nutrient levels are ordered as \(0<q_1<\cdots<q_S\). For any fixed exchange rate \(\beta>0\) and isolation fraction \(0<\theta\leq1\), varying the external supply \(R_0\) produces a succession of hyperbolically attracting equilibria with survivor sets \(\{1\},\{1,2\},\ldots\), possibly ending before all \(S\) species survive. The precise entry supplies are the finite numbers \(C_j\) given below. Every attracting equilibrium off the entry boundaries has *exactly* the initial-segment survivor set prescribed by these thresholds, and no other equilibrium in the nonnegative state space is a local attractor.

There is also a sharp **supply-independent exclusion ceiling**: if \(0<\theta<1\), any species with \(q_j\geq q_1/(1-\theta)\) is excluded from every locally attracting equilibrium, however large \(R_0\) becomes. With \(\theta=1\), every species becomes viable for sufficiently large supply. Consequently, nutrient abundance alone cannot always replace niche isolation.

Put \(B=q_1/(1-\theta)\) for \(0<\theta<1\), and \(B=+\infty\) for \(\theta=1\). Define \(C_1=q_1\). For each \(2\leq j\leq S\) with \(q_j<B\), define

\[
C_j=q_j+\frac{\beta}{\theta}\sum_{i<j}\frac{q_i(q_j-q_i)}{q_i-(1-\theta)q_j}.
\]

For \(q_j\geq B\), set \(C_j=+\infty\). For any \(R_0>0\) not equal to a finite \(C_j\), the unique locally exponentially attracting equilibrium has precisely species \(j\) with \(R_0>C_j\) present (none if \(R_0<C_1\)). For finite \(C_j\), the threshold increases strictly with \(\beta\) and decreases strictly with \(\theta\) in its admissible range. In particular the survivor count is nondecreasing as supply or isolation increases and nonincreasing as nutrient exchange increases, for fixed other parameters and away from boundaries.

## Assumptions and scope

Let \(S\geq2\) be a finite integer. For each \(i=1,\ldots,S\), let \(N_i\geq0\) be consumer abundance, \(T_i>0\) its local nutrient concentration, and \(R>0\) a common global nutrient pool. Take \(\gamma,\beta,R_0,\alpha_i,k_i>0\) and a **common, fixed** local-consumption fraction \(0<\theta\leq1\), and define \(q_i=k_i/\alpha_i\). Assume all \(q_i\) are pairwise distinct and relabel so \(q_1<\cdots<q_S\). The ODE is exactly

\[
\begin{aligned}
\dot N_i&=\big[\alpha_i((1-\theta)R+\theta T_i)-k_i\big]N_i,\\
\dot R&=R_0-R-\gamma(1-\theta)R\sum_{i=1}^{S}\alpha_iN_i-\beta\sum_{i=1}^{S}(R-T_i),\\
\dot T_i&=\beta(R-T_i)-\gamma\theta\alpha_iT_iN_i.
\end{aligned}
\]

It is the single-resource case of equations (3)–(5), or (S4)–(S6), of [1] with \(\theta_i=\theta\). All stability conclusions concern the finite-dimensional continuous-time dynamics with this fixed \(\theta\); they do not concern the paper's adaptive \(\theta_i\) dynamics, more than one nutrient, stochastic resilience, or global convergence of every trajectory. A hyperbolically attracting equilibrium means all eigenvalues of its Jacobian have strictly negative real parts. The theorem explicitly omits the threshold values \(R_0=C_j\), where a zero invasion eigenvalue occurs.

## Proof

**1. Nonzero species fix their local nutrient.** Consider any stationary state and write \(I=\{i:N_i>0\}\). If \(i\in I\), its zero per-capita growth forces

\[
T_i=\frac{q_i-(1-\theta)R}{\theta}.
\]

The local nutrient balance gives

\[
N_i=\frac{\beta(R-q_i)}{\gamma\theta\alpha_i[q_i-(1-\theta)R]}.
\tag{1}
\]

Because \(\dot T_i=0\) and \(N_i>0\), one has \(0<T_i<R\). Thus for an active species \(q_i<R\) and, if \(\theta<1\), \(R<q_i/(1-\theta)\). For any absent species, \(N_i=0\) and \(T_i=R\). At its rare-invasion linearization the absent species has the real eigenvalue

\[
\lambda_i=\alpha_i(R-q_i).
\tag{2}
\]

**2. Exact scalar closure.** Sum the global and local nutrient equations and \(\gamma\) times the consumer equations. The exchange and consumption terms cancel, leaving

\[
\frac{d}{dt}\left(R+\sum_iT_i+\gamma\sum_iN_i\right)=R_0-R-\gamma\sum_i k_iN_i.
\]

At a stationary state, substitute (1):

\[
R_0=R+\frac{\beta}{\theta}\sum_{i\in I}\frac{q_i(R-q_i)}{q_i-(1-\theta)R}.
\tag{3}
\]

Every attracting stationary state must include all species with \(q_i<R\), because omitting one gives the strictly positive eigenvalue (2). Every present species necessarily has \(q_i<R\); hence any hyperbolically attracting state has exactly \(I=\{i:q_i<R\}\). If \(R_0<q_1\), washout \(N_i=0\), \(R=T_i=R_0\) is hyperbolically attracting (the consumer invasion eigenvalues \(\alpha_i(R_0-q_i)\) are negative and the nutrient subsystem is a stable linear exchange system). For \(R_0>q_1\), the stable support must contain species 1; therefore \(R<B\).

Define for \(q_1<R<B\)

\[
H(R)=R+\frac{\beta}{\theta}\sum_{q_i<R}\frac{q_i(R-q_i)}{q_i-(1-\theta)R}.
\tag{4}
\]

It is continuous even at \(R=q_i\), where the new summand is zero. On every open interval between such points,

\[
H'(R)=1+\beta\sum_{q_i<R}\frac{q_i^2}{[q_i-(1-\theta)R]^2}>0.
\tag{5}
\]

Also \(H(q_1^+)=q_1\), and \(H(R)\to+\infty\) as \(R\uparrow B\): if \(\theta<1\), the \(i=1\) denominator tends to zero; for \(\theta=1\), the leading term \(R\) diverges. Thus for each \(R_0>q_1\) there is **exactly one** solution \(R_*=H^{-1}(R_0)\). Define \(N_i\) and \(T_i\) by (1) and the local formula for \(q_i<R_*\), otherwise set \(N_i=0\), \(T_i=R_*\). All terms are nonnegative and local nutrients positive; (3), the local balances and the consumer balances then imply the original global balance. This constructs an equilibrium for each supply.

**3. Strict local stability.** Let \(I=\{i:q_i<R_*\}\) and suppose \(R_*\ne q_j\) for all \(j\). For the linearized subsystem on the active consumers and **all** nutrients, put \(s_i=(1-\theta)\alpha_i\), \(t_i=\theta\alpha_i\), and let \(x_i,y,z_i\) denote perturbations of \(N_i,R,T_i\). Use the positive definite quadratic form

\[
E=\frac{\gamma}{2}\sum_{i\in I}\frac{x_i^2}{N_i^*}+\frac{y^2}{2R_*}+\sum_{i=1}^S\frac{z_i^2}{2T_i^*}.
\]

Linear consumer–resource cross terms cancel exactly. The local balance implies \(\beta+\gamma t_iN_i^*=\beta R_*/T_i^*\) for active species, and the same equation holds for missing species (both sides equal \(\beta\)). Direct differentiation yields

\[
\begin{aligned}
-\dot E={}&\frac{1+\gamma\sum_{i\in I}s_iN_i^*}{R_*}y^2\\
&+\beta\sum_{i=1}^{S}\left[\frac{y^2}{R_*}-\left(\frac1{R_*}+\frac1{T_i^*}\right)yz_i+\frac{R_*}{(T_i^*)^2}z_i^2\right].
\end{aligned}
\tag{6}
\]

Each bracket is nonnegative. Indeed its symmetric matrix has positive first diagonal entry and determinant

\[
\frac{(1-T_i^*/R_*)(3+T_i^*/R_*)}{4(T_i^*)^2}\geq0.
\]

It is strictly positive definite for active species (\(T_i^*<R_*\)); for absent species (\(T_i^*=R_*\)) it is exactly \((y-z_i)^2/R_*\). The first term of (6) forces \(y=0\) whenever \(\dot E=0\), and then all \(z_i=0\). A trajectory remaining in this zero-dissipation subspace also satisfies \(\dot z_i=-\gamma T_i^* t_i x_i\) for each active \(i\), forcing all \(x_i=0\). Consequently the active-consumer/all-nutrient linear subsystem has no eigenvalues with nonnegative real part (linear LaSalle/strict spectral dissipativity) and is Hurwitz. The omitted consumer equations decouple in first order as scalar modes with eigenvalues (2), all strictly negative because the absent species satisfy \(q_i>R_*\). Hence the full equilibrium is locally exponentially attracting.

Any other equilibrium omits at least one species with \(q_i<R\) unless its active set equals the one constructed above. In that case (2) makes it linearly unstable. If an equilibrium omitted a species with \(q_i=R\), its invasion eigenvalue would be zero; off the listed supply thresholds this cannot be the constructed equilibrium, and a missing lower-ranked species still makes it unstable. Therefore the constructed equilibrium is the only hyperbolically attracting equilibrium.

**4. Sharp entry supplies and the ceiling.** A new species \(j\geq2\) can become present only when \(R\) passes \(q_j\). The admissible resource interval ends at \(B\). Hence species \(j\) has no finite entry supply if \(q_j\geq B\); otherwise its unique entry supply is \(R_0=H(q_j)=C_j\), exactly the stated formula. Because \(H\) is increasing, all finite \(C_j\) are strictly ordered by \(j\). Every nonzero summand in \(C_j-q_j\) is strictly increasing in \(\beta\) and strictly decreasing in \(\theta\) (both \(1/\theta\) and the reciprocal denominator decrease with \(\theta\)). This gives the monotonicity claims. For fixed \(R_0>C_j(1)=q_j+\beta\sum_{i<j}(q_j-q_i)\), the threshold \(C_j(\theta)=R_0\) has exactly one solution in \((1-q_1/q_j,1)\), because it diverges at the lower endpoint and decreases continuously to \(C_j(1)\).

**5. Exact three-species instance.** Let \(S=3\), \(\alpha_i=\gamma=\beta=1\), \((k_1,k_2,k_3)=(1,6/5,7/5)\), and \(\theta=1/2\). The thresholds are exactly \(C_1=1\), \(C_2=11/5\), and \(C_3=377/75\). At \(R_*=3/2\) and supply \(R_0=979/130\), the attracting full-coexistence equilibrium is

\[
(N_1,N_2,N_3)=(4,4/3,4/13),\qquad (T_1,T_2,T_3)=(1/2,9/10,13/10).
\]

All seven stationarity equations hold as exact rational identities. By contrast, at \(\theta=1/4\) the ceiling is \(B=4/3<q_3\), so species 3 never belongs to the attracting equilibrium for **any** supply; species 2 first enters at \(C_2=46/5\). This illustrates a genuine supply-independent diversity limit.

## Verification

The independent-of-platform Python 3 script `checker.py` uses exact rational arithmetic and the standard library. Run `python3 checker.py` alongside this file. It verifies the displayed three-species equilibrium, all exchange and population stationarity equations, the sharp cutoffs, the transfer-block principal minors, and 800 additional randomly sampled **exact rational** stationary states (two to seven species). Output: `PASS: exact three-species example, thresholds, transfer-block determinants, 800 rational steady states`.

Those finite checks support, but do not replace, the all-parameter proof above; strict monotonicity (5), all-species construction, and the spectral argument (6) are analytic.

## Relationship to prior work

ElGamel and Mugler [1], sections II, III.1 and supplemental V–VI, introduce the exact shared/local one-resource equations and obtain coexistence formulas for **two** species only at the endpoints \(\theta=0\) and \(\theta=1\) (supplemental S12–S24); their intermediate-isolation multi-species outcomes are illustrated numerically. Supplemental VII concerns additional poor nutrients and a lower richness bound at complete separation, not exact intermediate-isolation survivor sets, and explicitly leaves intermediate parameters for more detailed analysis. Here the new statement supplies an arbitrary-species, arbitrary positive intermediate-isolation formula, complete attracting-support classification, strict stability proof, and a hard richness ceiling.

Related consumer–resource coexistence and patch-dispersal theories [2–4] establish substantial background results, including convergence in models with crowding and spatial migration. Their resource, consumer, and transport couplings differ: they do not immediately yield the stated explicit \(q_1/(1-\theta)\) ceiling or the exact \(C_j\) for the equations in [1]. The structural idea of monotone resource closure is familiar; the precise all-support classification for this specified new model is the contribution assessed here. The literature comparison is bounded, not a claim of exhaustive historical priority.

## Limitations

The theorem assumes one global nutrient with one niche per consumer, constant common \(\theta>0\), positive linear uptake and distinct \(q_i\). It proves equilibrium support and **local** exponential stability, not global attraction or robustness to stochastic perturbations. At \(R_0=C_j\), the entering species has a zero eigenvalue and this theorem does not classify nonlinear critical relaxation. With equal \(q_i\), several species enter together, which requires grouping the thresholds. The stable-survivor count is not an operational census when extremely small positive abundances are below detection limits. The old paper's qualitative numerical survival counts at small exchange rates should not be equated automatically with mathematically positive stationary equilibria. More complex resource kinetics and adaptive isolation are not covered. Historical overlap remains possible outside accessible indexed literature; independent scientific verification is not performed.

## References

[1] M. ElGamel and A. Mugler, *Spatial structure promotes coexistence, resilience, and synergy in microbial communities*, arXiv:2611.00222v1 (first posted 2026-10-30), https://arxiv.org/html/2611.00222v1 . Especially equations (3)–(5), (S4)–(S24), and supplemental VII.

[2] P. De Leenheer, D. Angeli, and E. D. Sontag, *Crowding effects promote coexistence in the chemostat*, Journal of Mathematical Analysis and Applications 319 (2006), 48–60, DOI:10.1016/j.jmaa.2006.02.036, https://www.sontaglab.org/FTPDIR/leenheer_angeli_sontag_JMAA06.pdf .

[3] F. Yu, W. Song, and Y. Wang, *Effect of diffusion on a consumer-resource system with source-sink patches*, Discrete and Continuous Dynamical Systems B 28 (2023), 1905–1937, DOI:10.3934/dcdsb.2022152, https://www.aimsciences.org/article/doi/10.3934/dcdsb.2022152 .

[4] S. Wang, *Dynamics of a chemostat system with two patches*, Discrete and Continuous Dynamical Systems B 24 (2019), 6261–6278, DOI:10.3934/dcdsb.2019138, https://www.aimsciences.org/article/doi/10.3934/dcdsb.2019138 .
