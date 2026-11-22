# Sharp clustering and critical escape for favorable trait islands under directional mutation

## Finding

Consider the infinite-trait, density-regulated population model specified below. For a nonempty finite set of favorable traits \(S=\{a_1<\cdots<a_k\}\subset\mathbb Z\), define \(s=\sqrt{q/p}\in(0,1)\), \(\delta=p-q\), and the strictly positive matrix
\[
K_S=(s^{|a_i-a_j|})_{1\leq i,j\leq k}.
\]
The exact mortality threshold for the existence of **any** nonzero summable equilibrium, for sufficiently large birth rate, is
\[
\boxed{d_*(S)=1-\frac{\delta}{\rho(K_S)}.}
\]
If \(d\geq d_*(S)\), no positive summable equilibrium exists at **any** finite birth rate. If \(0<d<d_*(S)\), one unique effective birth factor \(t_S(d)\in(0,1)\) exists, defined by the finite-dimensional Green-kernel equation in the proof. There is precisely one nonzero nonnegative summable equilibrium when \(\lambda>t_S(d)\), and none when \(\lambda\leq t_S(d)\); its total population mass equals \(1-t_S(d)/\lambda\).

For every fixed number \(k\geq2\) of favorable trait values, \(d_*(S)\) is uniquely maximized, up to translation, by a consecutive block. Writing \(d_k\) for this maximum, the exact large-block law is
\[
\boxed{d_k\uparrow 2\sqrt{pq},\qquad
  \lim_{k\to\infty}k^2(2\sqrt{pq}-d_k)=\pi^2\sqrt{pq}.}
\]
Thus no finite number or arrangement of favorable traits can sustain a localized equilibrium when \(d\geq2\sqrt{pq}\), regardless of the birth rate. Conversely, for every \(d<2\sqrt{pq}\), a sufficiently long consecutive favorable block admits a positive equilibrium for all sufficiently large birth rates.

Finally, for any fixed finite favorable set \(S\) and fixed \(\lambda>1\), as \(d\uparrow d_*(S)\), the unique positive equilibrium has total mass converging to \(1-1/\lambda>0\) but its mass in **every fixed finite collection of traits** converges to zero. The missing mass escapes to increasing positive trait values; at the critical parameter no nonzero summable equilibrium remains.

## Assumptions and scope

Let \(p,q,d,\lambda>0\), \(p+q=1\), \(p>q\), and \(d<1\). A parent of trait \(i\in\mathbb Z\) produces offspring of trait \(i+1\) with probability \(p\) and trait \(i-1\) with probability \(q\). The state \(x=(x_i)_{i\in\mathbb Z}\) belongs to the nonnegative unit ball of \(\ell^1(\mathbb Z)\), with total mass \(m=\sum_i x_i\). Mortality equals \(d\) on \(S\) and equals \(1\) outside \(S\). The differential equation is
\[
\dot x_i=\lambda(1-m)(p x_{i-1}+q x_{i+1})-\mu_i x_i,
\qquad \mu_i=d\; (i\in S),\quad \mu_i=1\; (i\notin S).
\]
Only stationary nonnegative \(\ell^1\) states are classified. No stochastic finite-population survival, global convergence of trajectories, or clinical/ecological data fit is claimed. All rates are per the same chosen time unit.

## Proof

**1. Equilibrium reduction and exclusion of non-summable solutions.** Let \(P\) be the column-stochastic nearest-neighbor mutation operator and let \(0\ne x\in\ell^1_+\) be a stationary solution. The effective factor \(t=\lambda(1-m)\) is positive because \(m=1\) would force \(x=0\). Irreducibility makes every coordinate strictly positive. Summing the stationary equations gives
\[
tm=\sum_i\mu_i x_i=m-(1-d)\sum_{i\in S}x_i,
\]
so \(0<t<1\). In particular, any proposed solution with effective factor at least one is ruled out *before* a spectral calculation. Let \(E_S\) be diagonal projection onto the favorable sites. Then
\[
(I-tP)x=(1-d)E_Sx,
\quad
x=(1-d)G_t E_Sx,
\quad G_t=(I-tP)^{-1}=\sum_{n\geq0}t^nP^n.
\]
The positive vector \(v=(x_{a_i})_{1\leq i\leq k}\) therefore satisfies
\[
v=(1-d)\,G_t[S,S]v.
\]
Conversely, a positive Perron vector of this finite-dimensional equation reconstructs a positive summable \(x\) via the displayed Green formula. Normalize it to total mass one and multiply by \(1-t/\lambda\); this is an equilibrium precisely when \(\lambda>t\). Strict Perron uniqueness gives uniqueness of the positive equilibrium.

**2. The sharp finite-set threshold.** For \(0<t\leq1\), put \(\Delta_t=\sqrt{1-4pqt^2}\), \(A_t=(1-\Delta_t)/(2qt)\), and \(B_t=(1-\Delta_t)/(2pt)\), interpreted continuously at \(t=0\). The Green kernel is
\[
G_t(i,j)=\frac1{\Delta_t}\begin{cases}
A_t^{i-j},&i\geq j,\\
B_t^{j-i},&i<j.
\end{cases}
\]
These formulas follow by substituting the two characteristic roots into \((I-tP)G_t(\cdot,j)=e_j\). Because \(p>q\), the expression is finite for each fixed \(i,j\) even at \(t=1\), although \(G_1\) is not a bounded inverse on \(\ell^1\). At \(t=1\), \(\Delta_1=\delta\), \(A_1=1\), and \(B_1=q/p\). Hence the finite matrix \(G_1[S,S]\) is diagonally similar to \(K_S/\delta\), and
\[
\rho(G_1[S,S])=\rho(K_S)/\delta.
\]
For \(t\in[0,1)\), all entries of \(G_t[S,S]\) and its Perron root increase strictly with \(t\); at \(t=0\), \((1-d)\rho(G_0[S,S])=1-d<1\). Consequently the positive eigenvalue equation has exactly one solution \(t\in(0,1)\) if and only if \((1-d)\rho(G_1[S,S])>1\), which is precisely \(d<d_*(S)\). Equality at the boundary is not sufficient, since a stationary solution must have \(t<1\).

**3. Optimal clustering.** If \(a_1<\cdots<a_k\) are distinct integers, \(|a_i-a_j|\geq |i-j|\), so
\[
(K_S)_{ij}\leq s^{|i-j|}=(K_k)_{ij},
\qquad K_k=(s^{|i-j|})_{1\leq i,j\leq k}.
\]
For a nonconsecutive configuration and \(k\geq2\), some entry is strictly smaller. Strict Perron monotonicity therefore yields \(\rho(K_S)<\rho(K_k)\). Consecutive blocks alone maximize the threshold, up to translation.

**4. Exact large-block correction.** For \(k\geq2\) the inverse \(K_k^{-1}\) is \((1-s^2)^{-1}\) times the tridiagonal matrix with first and last diagonal entries \(1\), other diagonal entries \(1+s^2\), and nearest-neighbor off-diagonal entries \(-s\). Its lowest eigenvector is positive and symmetric about the midpoint. Solving its interior second-order recurrence gives
\[
\rho(K_k)=\frac{1-s^2}{1+s^2-2s\cos\theta_k},
\]
where \(\theta_k\in(0,\pi/k)\) uniquely solves
\[
k\theta_k+2\arctan\!\left(\frac{1+s}{1-s}\tan\frac{\theta_k}{2}\right)=\pi.
\]
The boundary condition follows from the ghost-site identities \(u_0=s u_1\) and \(u_{k+1}=s u_k\). The equation implies \(\theta_k=\pi/k+O(k^{-2})\). Taylor expansion at zero yields
\[
\rho(K_k)=\frac{1+s}{1-s}-\frac{\pi^2s(1+s)}{(1-s)^3k^2}+O(k^{-3}).
\]
It follows that
\[
1-\frac{\delta}{\rho(K_k)}=2\sqrt{pq}-\frac{\pi^2\sqrt{pq}}{k^2}+O(k^{-3}),
\]
as asserted. Each finite-block Perron root is strictly below \((1+s)/(1-s)\), giving the strict upper bound for every finite favorable set.

**5. Critical loss of mass at fixed traits.** Fix \(S\) and \(\lambda>1\), and let \(d\uparrow d_*(S)\) through the persistence regime. By strict monotonicity of the finite Green Perron root, \(t_S(d)\uparrow1\). Let \(w^{(d)}\) denote the equilibrium profile divided by its total mass. Summation of its stationary equations gives
\[
(1-d)\sum_{i\in S}w_i^{(d)}=1-t_S(d)\longrightarrow0.
\]
For each fixed \(j\), the Green representation and finite-site boundedness \(G_t(j,i)\leq G_1(j,i)<\infty\) imply \(w_j^{(d)}\to0\). The same representation bounds all mass to the left of any fixed index by a constant times \(\sum_{i\in S}w_i^{(d)}\), so the normalized mass escapes specifically to \(+\infty\). Meanwhile the total population converges to \(1-1/\lambda>0\). This is loss of tightness, not an equilibrium at the limiting parameter.

**6. Exact two-island rescue and separation.** For \(S=\{0,L\}\) with positive integer \(L\),
\[
d_*(\{0,L\})=1-\frac{p-q}{1+(q/p)^{L/2}}.
\]
Take \(p=3/4\), \(q=1/4\), \(d=3/5\), and \(\lambda=2\). Each favorable site in isolation has threshold \(1-(p-q)=1/2<d\), so no one-site equilibrium exists for any birth rate. Two favorable sites at separation \(L\) support an equilibrium exactly when \(3^{-L/2}>1/4\), that is, exactly for \(L=1,2\). For \(L\geq3\), there is none at any birth rate. At \(L=1\), the unique effective factor is approximately \(0.923760430703401\), and the equilibrium total mass is approximately \(0.538119784648299\); these decimals illustrate, and do not replace, the exact inequalities and proof.

## Verification

Run `python3 checker.py` with Python 3.9 or later, no third-party dependencies. It checks the stated Green-kernel recurrence for four distinct mutation biases, independently computes top eigenvalues of small island kernels with a positive-matrix iteration and compares them to the tridiagonal quantization, checks exact rational separation inequalities, reconstructs the illustrative equilibrium and its coordinatewise residuals, and numerically confirms convergence toward the analytic large-block coefficient. These finite tests are supplementary: the proof above, not enumeration, establishes the claims for arbitrary finite sets and block sizes.

## Relationship to prior work

Pollett's mutation–selection model on a countably infinite trait space (2026, arXiv:2609.02086v1) provides the motivating density-regulated equation and contrasts unconfined with confining mortality. The claim here is the **sharp pattern-dependent localization phase boundary for finitely many favored traits under directional nearest-neighbor mutation**, strict optimality of clustering, the \(k^{-2}\) correction, and critical escape with nonzero total biomass; it does not claim to invent mutation–selection balance or general operator spectral methods.

The matrix \(K_k\) is the classical Kac–Murdock–Szegö matrix, whose tridiagonal inverse and spectral properties are prior linear algebra. The elementary finite-rank resolvent reduction is likewise an instance of the established Birman–Schwinger principle. Literature on catalytic branching random walks has related localization transitions but studies a different stochastic process. The specific ecological theorem combines these established mathematical ingredients; a historical-priority search cannot rule out every unindexed equivalent specialization.

## Limitations

This is a deterministic \(\ell^1\) stationary-state classification for a constant-bias, nearest-neighbor, infinite trait chain, with finitely many equal-benefit sites. It makes no claim about transient stability, stochastic extinction, general mutation kernels, unequal favorable mortality rates, or spatial population data. At the critical boundary, positive equilibria disappear despite the positive limiting total mass, because profiles cease to be tight. The initiating source's abstract and introduction were examined, but complete section-by-section full-text comparison was not accessible during this analysis; direct historical priority is therefore not independently established.

## References

1. P. Pollett, *Mutation–selection balance on an infinite trait space: confinement, drift and equilibrium*, arXiv:2609.02086v1 (first public September 2, 2026), https://arxiv.org/html/2609.02086.
2. M. Kac, W. L. Murdock, G. Szegö, *On the Eigen-values of Certain Hermitian Forms*, Journal of Rational Mechanics and Analysis **2** (1953), 767–800.
3. N. J. Higham, *What Is the Kac–Murdock–Szegö Matrix?* (2021), https://nhigham.com/2021/07/06/what-is-the-kac-murdock-szego-matrix/.
4. C. Mailler, B. Schapira, *A localisation phase transition for the catalytic branching random walk*, Annals of Applied Probability **36** (2026), 1737–1768, https://doi.org/10.1214/25-AAP2268 (preprint arXiv:2412.11842).
