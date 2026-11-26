# Sharp survivor staircases and a resource ceiling in a shared/local nutrient community

## Finding

In the one-nutrient, common-isolation specialization of the consumer–resource model of ElGamel and Mugler [1], let the distinct break-even concentrations be \(0<q_1<\cdots<q_S\). For fixed exchange \(\beta>0\) and local-consumption fraction \(0<\theta\le1\), the locally attracting stationary survivor sets, off their entry boundaries, form an exact nested staircase as external supply \(R_0\) increases.

Put \(B=q_1/(1-\theta)\) for \(\theta<1\), and \(B=+\infty\) for \(\theta=1\). Define \(C_1=q_1\), and for \(j\ge2\) set
\[
C_j=\begin{cases}
q_j+\dfrac{\beta}{\theta}\displaystyle\sum_{i<j}\dfrac{q_i(q_j-q_i)}{q_i-(1-\theta)q_j},&q_j<B,\\[4pt]
+\infty,&q_j\ge B.
\end{cases}
\]
For \(R_0>0\) not equal to a finite \(C_j\), the unique locally attracting equilibrium is hyperbolically attracting and has exactly those species with \(R_0>C_j\) present; below \(C_1\) this means washout. All finite supplies are strictly ordered by the species index. The first entry supply \(C_1\) is independent of \(\beta,\theta\); every finite \(C_j\) with \(j\ge2\) increases strictly with \(\beta\) and decreases strictly with \(\theta\) in its finite range. Thus the survivor count is nondecreasing as supply or local-consumption fraction increases and nonincreasing as exchange increases, off entry boundaries.

For \(\theta<1\), species with \(q_j\ge q_1/(1-\theta)\) are excluded from every locally attracting equilibrium, even at entry boundaries and however large the finite supply. When \(\theta=1\), every species is present at the attracting equilibrium for sufficiently large supply. The ceiling is sharp: each species strictly below it enters at a finite supply.

## Assumptions and scope

There are \(S\ge2\) species with abundances \(N_i\ge0\), local concentrations \(T_i>0\), and common nutrient concentration \(R>0\). The parameters \(\gamma,\beta,R_0,\alpha_i,k_i\) are positive; \(q_i=k_i/\alpha_i\). A common fixed \(0<\theta\le1\) is used. The equations are
\[
\begin{aligned}
\dot N_i&=[\alpha_i((1-\theta)R+\theta T_i)-k_i]N_i,\\
\dot R&=R_0-R-\gamma(1-\theta)R\sum_i\alpha_iN_i-\beta\sum_i(R-T_i),\\
\dot T_i&=\beta(R-T_i)-\gamma\theta\alpha_iT_iN_i.
\end{aligned}
\]
These are the one-resource equations (3)–(5), equivalently (S4)–(S6), of [1] with \(\theta_i=\theta\). The result does not address adaptive isolation, multiple nutrients, global convergence or nonlinear stability at entry boundaries.

## Proof

**Stationary closure.** For the active set \(I=\{i:N_i>0\}\), the consumer and local balances force
\[
T_i=\frac{q_i-(1-\theta)R}{\theta},\qquad
N_i=\frac{\beta(R-q_i)}{\gamma\theta\alpha_i[q_i-(1-\theta)R]}\quad(i\in I).
\tag{1}
\]
Indeed, positive \(N_i\) implies \(0<T_i<R\), so \(q_i<R\) and \(q_i>(1-\theta)R\). An absent species has \(T_i=R\) and invasion eigenvalue \(\lambda_i=\alpha_i(R-q_i)\). If this is strictly positive, the equilibrium cannot be a local attractor even relative to nonnegative abundances: a trajectory from any nearby state with \(N_i>0\) cannot converge to it, since the per-capita rate would eventually be bounded below by a positive constant. Thus every locally attracting equilibrium has \(I=\{i:q_i<R\}\), including when an absent species has \(q_i=R\).

Summing the exchange balances and the consumer balances weighted by \(\gamma\) gives the total derivative \(R_0-R-\gamma\sum_i k_iN_i\). At stationarity, (1) gives
\[
R_0=R+\frac{\beta}{\theta}\sum_{i\in I}\frac{q_i(R-q_i)}{q_i-(1-\theta)R}.
\tag{2}
\]
For \(R\le q_1\), the candidate support is empty and (2) yields \(R=R_0\). For \(R>q_1\), species 1 must be present on the candidate support, hence \(R<B\). On \((q_1,B)\), write \(H(R)\) for the right side of (2) with \(I=\{i:q_i<R\}\). Denominators are positive. The sum is continuous at each \(q_j\) because the newly admitted term is zero there. Between those points,
\[
H'(R)=1+\beta\sum_{q_i<R}\frac{q_i^2}{[q_i-(1-\theta)R]^2}>0.
\]
We have \(H(q_1^+)=q_1\), and \(H(R)\to\infty\) as \(R\uparrow B\) (the first denominator vanishes for \(\theta<1\), and \(R\to\infty\) for \(\theta=1\)). Therefore for \(R_0>q_1\) there is exactly one candidate \(R_*=H^{-1}(R_0)\). Equation (1) and the absent values give all other coordinates. They give an equilibrium: the consumer and local balances vanish by construction, so the total balance (2) implies the global balance. For \(R_0\le q_1\), the candidate is the washout state \(R=T_i=R_0\), \(N_i=0\).

**Strict local stability off the entries.** On the candidate equilibrium, let \(s_i=(1-\theta)\alpha_i\), \(t_i=\theta\alpha_i\), and consider the linearization on the active consumers and all nutrients, with perturbations \(x_i,y,z_i\) of \(N_i,R,T_i\). The positive quadratic form
\[
E=\frac{\gamma}{2}\sum_{i\in I}\frac{x_i^2}{N_i^*}+\frac{y^2}{2R_*}+\sum_{i=1}^{S}\frac{z_i^2}{2T_i^*}
\]
cancels the linear consumer–resource cross terms. By local balance \(\beta+\gamma t_iN_i^*=\beta R_*/T_i^*\) for every \(i\). Thus
\[
-\dot E=\frac{1+\gamma\sum_{i\in I}s_iN_i^*}{R_*}y^2+\beta\sum_i\left[\frac{y^2}{R_*}-\left(\frac1{R_*}+\frac1{T_i^*}\right)yz_i+\frac{R_*}{(T_i^*)^2}z_i^2\right].
\]
Each bracket is positive semidefinite: its first diagonal entry is positive and its determinant is \((1-T_i^*/R_*)(3+T_i^*/R_*)/[4(T_i^*)^2]\ge0\). A zero-dissipation state has \(y=0\) and then all \(z_i=0\). If a linearized trajectory remains there, the local nutrient equation forces \(0=\dot z_i=-\gamma t_i T_i^*x_i\) for every active species, so the trajectory is zero. Equivalently, the quadratic identity applied as a Hermitian form to an eigenvector excludes every eigenvalue of nonnegative real part. This argument also works with no active consumers. The omitted consumer equations supply independent diagonal invasion modes in the block triangular linearization. Off entry boundaries, \(q_i>R_*\) for every absent species, so their eigenvalues are strictly negative. This proves local exponential attraction; any other equilibrium misses a species with \(q_i<R\) and is not locally attracting.

**Entry supplies and ceiling.** Entry at \(R_*=q_j\) is possible only for \(q_j<B\), and then \(H(q_j)=C_j\) for \(j\ge2\). Strict increase of \(H\) orders the finite thresholds. For \(j\ge2\), the sum is positive; both \(1/\theta\) and the reciprocal denominators decrease strictly as \(\theta\) increases on the finite range. This gives the claimed strict monotonicities, whereas \(C_1=q_1\) remains constant. For fixed \(R_0>C_j(1)=q_j+\beta\sum_{i<j}(q_j-q_i)\) and \(j\ge2\), the equation \(C_j(\theta)=R_0\) has exactly one solution in \((1-q_1/q_j,1)\): the threshold diverges at the lower endpoint and decreases continuously to \(C_j(1)\). The ceiling assertion only uses the necessary support condition and \(R<B\) when a species is present, so it does not require classifying stability at the boundaries. At a finite entry value the entering species has zero invasion eigenvalue at the candidate equilibrium.

**Three-species instance.** Take \(\alpha_i=\gamma=\beta=1\) and \((k_1,k_2,k_3)=(1,6/5,7/5)\). With \(\theta=1/2\) the thresholds are \(1,11/5,377/75\). At \(R_*=3/2\) and \(R_0=979/130\), the full-coexistence equilibrium is
\[
(N_1,N_2,N_3)=(4,4/3,4/13),\qquad (T_1,T_2,T_3)=(1/2,9/10,13/10).
\]
With \(\theta=1/4\), \(B=4/3<q_3\) and \(C_2=46/5\), so supply can admit species 2 but can never admit species 3 to an attracting equilibrium.

## Verification

The accompanying standard-library Python 3 script `checker.py` verifies the example, exact stationarity residuals, thresholds, transfer-block determinants, and 800 additional sampled rational stationary states with two to seven species. These finite checks supplement, rather than replace, the analytic monotonicity and stability proof.

## Relationship to prior work and limitations

The model and the common-resource/local-resource distinction come from [1]. Its supplemental two-species coexistence calculations at \(\theta=0\) and \(\theta=1\) and its numerical intermediate-isolation studies are different from the arbitrary-species, common positive isolation classification with explicit entries and an exclusion ceiling here. Related chemostat work on crowding and transport [2–4] studies different resource, consumer and transport couplings. The conclusion is an exact supply-dependent classification for the equations specified here, not a claim of historical priority. Equal \(q_i\), multiple resources, adaptive \(\theta_i\), nonlinear entry relaxation, global attraction, and experimental detectability are outside this theorem.

## References

1. M. ElGamel and A. Mugler, *Spatial structure promotes coexistence, resilience, and synergy in microbial communities*, arXiv:2611.00222v1, https://arxiv.org/html/2611.00222v1.
2. P. De Leenheer, D. Angeli, and E. D. Sontag, *Crowding effects promote coexistence in the chemostat*, J. Math. Anal. Appl. 319 (2006), 48–60, DOI:10.1016/j.jmaa.2006.02.036.
3. F. Yu, W. Song, and Y. Wang, *Effect of diffusion on a consumer-resource system with source-sink patches*, Discrete Contin. Dyn. Syst. B 28 (2023), 1905–1937, DOI:10.3934/dcdsb.2022152.
4. S. Wang, *Dynamics of a chemostat system with two patches*, Discrete Contin. Dyn. Syst. B 24 (2019), 6261–6280, DOI:10.3934/dcdsb.2019138.
