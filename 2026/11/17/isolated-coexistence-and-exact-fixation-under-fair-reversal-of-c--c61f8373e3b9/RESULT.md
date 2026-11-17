# Isolated coexistence and exact fixation under fair reversal of cyclic Volterra competition

## Finding
For a cyclic three-species Volterra quadratic stochastic map with independent, fair, whole-environment reversals, the unique positive coexistence state remains fixed, but EVERY other initial state converges almost surely to a single-species vertex. The exact winner law is \(\mathbb P_x(I=i)=x_i\); positive starts also have explicit, pairwise extinction exponents. All stationary probability measures are convex combinations of the three vertices and the coexistence point.

## Assumptions and scope
Choose real parameters \(0<a,b,c<1\) and set
\[
A=\begin{pmatrix}0&a&-c\\-a&0&b\\c&-b&0\end{pmatrix},\qquad
r=\frac{(b,c,a)}{a+b+c}.
\]
Write \(\Delta_2=\{x\in[0,1]^3:\sum_i x_i=1\}\). Fix an arbitrary deterministic \(X_0=x\in\Delta_2\). Let \((\sigma_n)_{n\ge1}\) be independent random signs, each equal to \(+1\) or \(-1\) with probability \(1/2\). Set, for all \(n\ge0\) and \(i\in\{1,2,3\}\),
\[
 X_{n+1,i}=X_{n,i}\bigl(1+\sigma_{n+1}(AX_n)_i\bigr).
\]
This is a Volterra quadratic stochastic operator for either sign: because \(|A_{ij}|<1\) and \(\sum_i x_i(Ax)_i=0\), all coordinates stay in the simplex, and positive coordinates remain positive at every finite time.

The claimed dichotomy is exact:

* At \(x=r\), both signs fix the state, so \(X_n=r\) for every \(n\).
* For every \(x\ne r\), there is an almost surely defined random \(I\in\{1,2,3\}\) such that \(X_n\to e_I\) and \(\mathbb P_x(I=i)=x_i\).
* For every strictly positive \(x\ne r\), on \(\{I=i\}\) and simultaneously for each \(j\ne i\),
\[
 \lim_{n\to\infty}\frac{\log X_{n,j}}{n}=\frac12\log(1-A_{ji}^2)<0.
\]
* The invariant probability measures are exactly \(\sum_{i=1}^3 q_i\delta_{e_i}+q_r\delta_r\), with nonnegative weights totaling one.

## Proof
**1. Bounded martingales and possible limits.** Skew symmetry gives \(x^{\mathsf T}Ax=0\), so each sign map preserves total mass. Also \(|(Ax)_i|<1\) uniformly for \(x\in\Delta_2\); hence it preserves nonnegativity and strict positivity of existing positive coordinates. With the natural filtration, the fair-sign identity gives
\[
\mathbb E[X_{n+1,i}\mid\mathcal F_n]=X_{n,i},\qquad
\mathbb E[(X_{n+1,i}-X_{n,i})^2\mid\mathcal F_n]=X_{n,i}^2(AX_n)_i^2.
\]
Each bounded coordinate martingale converges almost surely and in \(L^2\). Orthogonality of martingale increments yields
\[
\sum_{n\ge0}\mathbb E[X_{n,i}^2(AX_n)_i^2]
=\mathbb E[X_{\infty,i}^2]-x_i^2\le1.
\]
Since the integrands are nonnegative, their infinite sums are almost surely finite. Their terms therefore approach zero, and continuity yields \(X_{\infty,i}(AX_\infty)_i=0\) for all three indices.

**2. The exact stationary-point census.** If two distinct coordinates of a point are positive and the third is zero, one active coordinate has a strictly nonzero interaction against the other, since \(a,b,c>0\). Such a point cannot satisfy all three equations \(x_i(Ax)_i=0\). If all three coordinates are positive, those equations reduce to \(Ax=0\). The displayed skew matrix has rank two, with positive kernel spanned by \((b,c,a)\), so the only interior solution is \(r\). The other solutions are exactly the vertices. Thus \(X_\infty\in\{e_1,e_2,e_3,r\}\) almost surely.

**3. Exclusion of coexistence from every other initial state.** Define the continuous weighted geometric mean
\[
H(x)=x_1^{r_1}x_2^{r_2}x_3^{r_3},
\]
with value zero on the boundary. Since \(r^{\mathsf T}A=0\), weighted arithmetic-geometric mean gives, for any positive \(x\) and sign \(s\),
\[
\frac{H(T_sx)}{H(x)}
=\prod_{i=1}^3\bigl(1+s(Ax)_i\bigr)^{r_i}
\le\sum_{i=1}^3 r_i\bigl(1+s(Ax)_i\bigr)=1.
\]
The inequality is strict unless \(Ax=0\). At boundary points, \(H\) remains zero. Consequently \(H(X_n)\) is nonincreasing on every sample path. A second weighted arithmetic-geometric mean inequality proves that \(H\) has a unique global maximum at \(r\). For any \(x\ne r\), \(H(X_n)\le H(x)<H(r)\), so convergence to \(r\) is impossible. Hence the limit is a vertex. Conversely, \(Ar=0\), so \(r\) is fixed by either sign.

**4. Winner probabilities and precise exponents.** As \(X_{\infty,i}=\mathbf1_{\{I=i\}}\), bounded-martingale expectation gives
\[
\mathbb P_x(I=i)=\mathbb E X_{\infty,i}=x_i.
\]
If every initial coordinate is positive, it remains strictly positive at each finite time. On the event \(I=i\), for every \(j\ne i\),
\[
\log X_{n,j}=\log x_j+\sum_{k=0}^{n-1}\log\bigl(1+\sigma_{k+1}(AX_k)_j\bigr).
\]
On this event \((AX_k)_j\to A_{ji}\). All these values and \(A_{ji}\) lie in a fixed interval \([-\rho,\rho]\) for some \(\rho<1\), where the logarithms are uniformly Lipschitz. By the Cesàro theorem, replacing \((AX_k)_j\) by \(A_{ji}\) changes the average by \(o(1)\), pathwise. The strong law for the same independent fair signs then gives
\[
\frac1n\sum_{k=0}^{n-1}\log(1+\sigma_{k+1} A_{ji})
\longrightarrow \tfrac12\log(1-A_{ji}^2).
\]
Intersecting the finitely many probability-one sign-law events establishes all stated exponents simultaneously.

**5. Invariant measures.** Each of the four stationary points is fixed by either map, so any probability mixture of their Dirac masses is invariant. Conversely, start the Markov chain with an arbitrary invariant law \(\nu\) independent of future signs. Its distribution is \(\nu\) at every time. The just-proved almost-sure convergence and bounded convergence for continuous test functions show that \(\nu\) must equal the distribution of \(X_\infty\), which is supported on those four points. This proves the complete stationary-measure classification.

## Verification
The reproducible checker `check_cyclic.py` uses only the Python standard library and exact rational arithmetic. At \((a,b,c)=(1/2,1/3,1/4)\) it confirms the kernel \(r=(4,3,6)/13\), positivity, fixed coexistence, martingale means, conditional quadratic variation, and strict weighted-product contraction for all \(62\) sign words of lengths one through five. Its recorded output is `CYCLIC_VOLTERRA_EXACT_OK words=62 kernel=PASS Lyapunov=PASS martingale=PASS`. These finite checks do **not** prove the infinite-time theorem; the bounded-martingale, stationary-set, weighted-AMGM and strong-law arguments above do.

## Relationship to prior work
Avelino–de Oliveira–Trintin (arXiv:2212.11687, first posted 22 December 2022) study reversible predation at the level of spatial May–Leonard reaction events, including empty sites, reproduction, and mobility. Their model is not the synchronous, mass-preserving sign-reversed Volterra map studied here. Yao–Swailem–Dobramysl–Täuber (arXiv:2303.08713, first posted 15 March 2023) motivate cyclic three-species stochastic competition and study reaction-diffusion field-theoretic fluctuations, not this exact fair-sign iteration or its fixation law.

Jamilov–Scheutzow–Wilke-Berenguer (arXiv:1401.7840, 2014), Theorem 3.1, prove vertex selection for a random-Volterra family only when the operator support contains, for every coordinate, an operator replacing that coordinate by its square. Their required extremal support condition fails here because every interaction coefficient has magnitude strictly less than one; moreover, the shared fixed point \(r\) rules out universal vertex selection at all starts. The previously established transitive-competition fair-sign theorem assumes a strict total ordering of all pairwise interactions, so its absence of an interior coexistence point cannot cover this cyclic case. West–Mobilia (arXiv:1907.05184, 2019) consider finite-population demographic noise and randomly switching carrying capacity, rather than the synchronous deterministic-frequency maps with fair sign choices.

## Limitations
The outcome does not concern lattice simulations, finite-population demographic fluctuations, mutually independent per-pair reversals, correlated signs, or biased sign probabilities. For initial boundary coordinates that are zero, logarithmic extinction-rate expressions are not stated, although vertex fixation still holds. Starting at the positive equilibrium is an essential, exact exception. No finite enumeration can substitute for the infinite-time proof. The present originality assessment is relative to inspected literature; an unindexed equivalent theorem remains possible. Independent validation has not been performed.

## References
1. P. P. Avelino, B. F. de Oliveira, and R. S. Trintin, *Role of predator-prey reversal in Rock-Paper-Scissors models*, arXiv:2212.11687, first posted 2022-12-22. https://arxiv.org/abs/2212.11687
2. L. H. Yao, M. Swailem, U. Dobramysl, and U. C. Täuber, *Perturbative Field-Theoretical Analysis of Three-Species Cyclic Predator-Prey Models*, arXiv:2303.08713, first posted 2023-03-15. https://arxiv.org/abs/2303.08713
3. U. U. Jamilov, M. Scheutzow, and M. Wilke-Berenguer, *On the Random Dynamics of Volterra Quadratic Operators*, arXiv:1401.7840, 2014. https://arxiv.org/abs/1401.7840
4. R. West and M. Mobilia, *Fixation properties of rock-paper-scissors games in fluctuating populations*, arXiv:1907.05184, 2019. https://arxiv.org/abs/1907.05184
