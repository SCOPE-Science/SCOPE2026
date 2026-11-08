# Exact minimax SGD schedules with heterogeneous oracle noise and a sharp step-order reversal criterion

## Finding

For a prescribed horizon \(N\), a smooth convex objective and an unbiased stochastic-gradient oracle with a *different* variance bound at each iteration, the exact short-step worst-case terminal objective gap is
\[
\Phi(h)=\frac{LD^2}{2T_0}+\frac{1}{2L}\sum_{i=0}^{N-1}\frac{v_i h_i^2}{T_{i+1}},\qquad T_i=1+2\sum_{j=i}^{N-1}h_j,\quad T_N=1.
\]
Here \(L,D>0\), \(v_i>0\) and \(0\le h_i\le 3/2\). For dimension at least \(N+1\), equality is attained by a separable Huber-type convex objective and independent two-point oracle errors. Thus this is a *sharp* formula, not merely an upper bound.

There is a unique minimizer \(h^*\) of \(\Phi\) over all nonnegative schedules. It is explicitly determined by the unique positive solution \(c_0\) of
\[
 v_0c_0\left\{\prod_{j=0}^{N-1}(1+2c_j)\right\}^{2}=L^2D^2,
 \qquad c_{i+1}=\frac{v_i}{v_{i+1}}c_i(1+c_i),
\]
followed by
\[
 h_i^*=c_i\prod_{j=i+1}^{N-1}(1+2c_j).
\]
Whenever the resulting steps lie in \([0,3/2]\), this is the unique **globally minimax** nonnegative fixed stepsize schedule (even compared with nonnegative schedules outside this range), since the Huber lower bound holds for every such competitor.

Unlike the constant-variance case, its step sizes need not decrease. For every \(i<N-1\), the exact sharp local criterion is
\[
 \boxed{h_i^*\ge h_{i+1}^*\quad\Longleftrightarrow\quad
 \frac{v_{i+1}}{v_i}\ge 1-c_i-2c_i^2.}
\]
In particular, nondecreasing variance bounds force decreasing steps. In the high-noise regime \(v_i=s w_i\), with fixed positive \(w_i\) and \(s\to\infty\),
\[
 h_i^*=\frac{L^2D^2}{s w_i}+O(s^{-2}),
\]
so *every prescribed strict ordering* of step sizes can arise from the inverse ordering of nonidentical noise variances, with all steps below \(3/2\) for large \(s\).

An exact two-step witness of reversal is \(L=D=1\), \(v_0=78125/39762\), \(v_1=78125/159048\): the unique optimum is \(h_0^*=47/250<h_1^*=11/25\), both strictly below \(3/2\); the exact terminal gap is \(7625/26508\).

## Assumptions and scope

Let \(N\ge1\), \(d\ge N+1\), \(L,D>0\), and deterministic positive variance ceilings \(v_0,\ldots,v_{N-1}\). An objective \(f:\mathbb R^d\to\mathbb R\) is convex, differentiable, has \(L\)-Lipschitz gradient, and has a minimizer \(x_\star\). The initial iterate obeys \(\|x_0-x_\star\|\le D\). For a deterministic fixed schedule of nonnegative normalized steps \(h_i\), the iteration is
\[
 x_{i+1}=x_i-\frac{h_i}{L}\bigl(\nabla f(x_i)+\epsilon_i\bigr),\qquad
 \mathbb E(\epsilon_i\mid\mathcal F_i)=0,\quad
 \mathbb E(\|\epsilon_i\|^2\mid\mathcal F_i)\le v_i.
\]
The terminal criterion is the supremum of \(\mathbb E[f(x_N)-f(x_\star)]\) over this entire problem class. The objective is fixed throughout the run; errors may depend on the preceding history subject to the conditional moments. Variance ceilings, rather than variance realizations, are known when choosing the schedule. The term *short step* refers to \(0\le h_i\le 3/2\).

## Proof

**1. Weighted sharp performance formula.** The smooth-convex interpolation certificate for last-iterate SGD in Grimmer and Shen (2026), Theorem 1.1 and proof of Lemma 2.2, uses only the conditional-zero-mean identity
\[
 \mathbb E\|a-h_i\epsilon_i/L\|^2
 =\mathbb E\|a\|^2+(h_i^2/L^2)\mathbb E\|\epsilon_i\|^2
\]
for a history-measurable vector \(a\), followed by nonnegative weighted interpolation inequalities. In that certificate the error at iteration \(i\) is multiplied by precisely \(h_i^2/(2LT_{i+1})\). Substituting the valid *individual* upper bound \(v_i\) for each conditional second moment yields the stated \(\Phi(h)\) upper bound; no step requires common variance. The nonnegative certificate coefficients require exactly the stated short-step assumption. This is a direct variance-by-variance use of the published interpolation proof, not an assumption that its homogeneous-variance theorem alone already states the extension.

To prove *attainment* independently, define \(H_a(z)=Lz^2/2\) for \(|z|\le a\) and \(H_a(z)=L(a|z|-a^2/2)\) otherwise. Use orthonormal coordinate vectors \(e_0,\ldots,e_N\), initialize \(x_0=De_0\), and let
\[
 f(x)=\sum_{j=0}^N H_{a_j}(\langle e_j,x\rangle),
 \quad a_0=D/T_0,\quad
 a_{i+1}=\frac{\sqrt{v_i}h_i}{LT_{i+1}}.
\]
At step \(i\), take an independent symmetric sign \(\xi_i\in\{-1,1\}\) and \(\epsilon_i=\xi_i\sqrt{v_i}e_{i+1}\). Each coordinate stays on its initial linear Huber branch after it is activated. At termination the absolute \(e_0\) coordinate equals \(a_0(1+R_0)\), and the absolute \(e_{i+1}\) coordinate equals \(a_{i+1}(1+R_{i+1})\), where \(R_i=(T_i-1)/2\). Consequently their respective objective contributions are exactly \(LD^2/(2T_0)\) and \(v_i h_i^2/(2LT_{i+1})\). Every error-sign realization attains \(\Phi(h)\). The construction remains valid for any nonnegative step sizes, which establishes the lower bound beyond the short-step regime.

**2. Unique optimizer.** Put \(t_i=T_i\), so \(t_N=1\) and \(h_i=(t_i-t_{i+1})/2\). The optimization objective becomes
\[
 \frac{LD^2}{2t_0}+\sum_{i=0}^{N-1}\frac{v_i}{8L}\frac{(t_i-t_{i+1})^2}{t_{i+1}},
 \qquad t_0\ge\cdots\ge t_N=1.
\]
Every summand is convex: the fraction is a quadratic perspective. The sum is strictly convex because equality along any segment in the last perspective, whose last denominator is fixed, forces the last numerator to agree; induction backward forces all coordinates to agree. It is coercive: setting \(H=\sum h_i\), Cauchy--Schwarz gives \(\sum h_i^2/T_{i+1}\ge H^2/[N(1+2H)]\), so the positive-noise term grows without bound as \(H\to\infty\). Hence a unique minimizer exists. It is interior: at \(h_i=0\), increasing that coordinate lowers the strictly positive initial-error term and any earlier-noise terms to first order, while its own contribution has zero first derivative.

Define \(c_i=h_i/t_{i+1}\), so \(t_i/t_{i+1}=1+2c_i\). Setting the derivative with respect to \(t_0\) to zero gives \(v_0 c_0t_0^2=L^2D^2\). At each interior \(t_i\), the derivative is zero precisely when \(v_ic_i=v_{i-1}c_{i-1}(1+c_{i-1})\). These yield the displayed recurrence and product equation. The left side of its scalar initial condition is strictly increasing continuously from zero to infinity as \(c_0\) grows (all positive variances), so it has exactly one positive solution. The reconstruction formula follows by taking products of the ratios \(t_i/t_{i+1}\).

**3. Exact step-order boundary.** Since \(h_i=c_it_{i+1}=c_i(1+2c_{i+1})t_{i+2}\), the difference \(h_i-h_{i+1}\) has the sign of \(c_i(1+2c_{i+1})-c_{i+1}\). Substitute \(c_{i+1}=(v_i/v_{i+1})c_i(1+c_i)\) and divide by the positive factor \(c_iv_i/v_{i+1}\). The remainder has the sign of \(v_{i+1}/v_i-1+c_i+2c_i^2\), proving the equivalence at equality as well as on either side. In particular, for constant variances it is strictly positive.

**4. High-noise reversal and exact witness.** Under \(v_i=sw_i\) the scalar initial condition and recurrence imply \(c_0=L^2D^2/(sw_0)+O(s^{-2})\) and, inductively, \(c_i=L^2D^2/(sw_i)+O(s^{-2})\). Each later product in \(h_i\) is \(1+O(s^{-1})\), yielding the stated limit and arbitrary orderings. For the rational witness, choose \(c_0=1/10\), \(c_1=11/25\), giving \(t_0=282/125\). The initial condition fixes \(v_0=78125/39762\) and the recurrence fixes \(v_1=v_0/4\); reconstruction gives \(h_0=47/250\) and \(h_1=11/25\). Both are short steps, so the minimax interpretation applies.

## Verification

The accompanying Python-standard-library checker independently implements the separable Huber construction, the risk functional, the one-dimensional root solution and the exact rational witness. It checks per-sign attainment over random problem parameters; verifies the stationarity recurrence, local strict-minimality perturbations, the adjacent-step criterion and the inverse-variance high-noise limit. Run `python3 check.py`. These finite checks support arithmetic and implementations; infinite mathematical conclusions follow from the analytic proof and cited interpolation certificate.

## Relationship to prior work

Grimmer and Shen (arXiv:2610.42048v1, 2026) prove a sharp *common-variance* last-iterate bound, determine its unique optimum and show the corresponding steps decrease. Their interpolation proof is the source of the sharp weighted upper certificate used here. Their published theorem neither formulates a sequence of separate variance ceilings nor gives the nonuniform optimizer recurrence or step-order threshold. The Huber construction here is an explicitly weighted adaptation of their extremal mechanism; originality is asserted for the combined heteroscedastic minimax classification and exact reversal, **not** for the underlying potential certificate or Huber device.

Bai and Zhou (arXiv:2608.15035v1, 2026) study two steps with a common variance bound and a *strongly convex* function class, optimizing squared distance rather than expected objective gap. Their setting does not imply this arbitrarily long-horizon smooth-convex heterogeneous-variance result. General SGD step-decay and variance-dependent adaptive literature concerns different or less sharp criteria. No claim is made that inverse-variance weighting as a heuristic is new.

## Limitations

The exact global minimax interpretation of the algebraic optimizer requires its steps to lie in \([0,3/2]\); outside that range, the sharp upper certificate is not established even though the lower witness is valid. The noise-dominated asymptotic holds with \(N,L,D\) and the relative variance pattern fixed. This does not optimize stochastic methods with momentum, data-dependent steps, discrete mini-batch costs, or varying objectives. Full independent review, and a comprehensive historical-priority certification against inaccessible or unindexed equivalent derivations, remain outstanding.

## References

1. B. Grimmer and Q. Shen, *Exact Theory and Optimal Stepsizes for Stochastic Gradient Descent in Smooth Convex Minimization*, arXiv:2610.42048v1, first public 2026-10-30. https://arxiv.org/abs/2610.42048
2. L. Bai and B. Zhou, *Optimal Two-Step Stepsize Schedule for Stochastic Gradient Methods*, arXiv:2608.15035v1, first public 2026-08-15. https://arxiv.org/abs/2608.15035
3. A. Attia, M. Schliserman, U. Sherman and T. Koren, *Fast Last-Iterate Convergence of SGD in the Smooth Interpolation Regime*, arXiv:2507.11274, first public 2025-07-15. https://arxiv.org/abs/2507.11274
