# A one-fifth short-horizon penalty and a universal edge-priority reversal in optimal path diffusion

## Finding

**Theorem (two limiting designs for every path).** Fix an integer \(n\ge4\), a total edge-conductance budget \(B>0\), and the combinatorial Laplacian \(L(w)\) on the path with ordered vertices \(1,\ldots,n\). Edge \(\{i,i+1\}\) has an independently selectable nonnegative conductance \(w_i\), with \(\sum_{i=1}^{n-1}w_i=B\). For every observation horizon \(t>0\), the heat-trace design problem
\[
\min_{w_i\ge0,\,\sum_iw_i=B}\quad H_t(w):=\operatorname{tr}(e^{-tL(w)})
\]
has a unique global optimizer \(w(t)\), without any imposed symmetry assumption.

Put \(\rho=2-\sqrt3\), and for \(1\le i<n\) define
\[
y_i=\frac16\left(1-\frac{(-\rho)^i+(-\rho)^{n-i}}{1+(-\rho)^n}\right).
\]
The unique small-horizon limiting design is
\[
\boxed{\lim_{t\downarrow0}w_i(t)=w_i^{\mathrm{short}}:=\frac{B y_i}{\sum_{j=1}^{n-1}y_j}.}
\]
The unique large-horizon limiting design is
\[
\boxed{\lim_{t\to\infty}w_i(t)=w_i^{\mathrm{long}}:=\frac{6B\,i(n-i)}{n(n^2-1)}.}
\]
Both limiting allocations have strictly positive weights. Their priorities at the first two edges are opposite:
\[
w_1^{\mathrm{short}}>w_2^{\mathrm{short}},\qquad
w_1^{\mathrm{long}}<w_2^{\mathrm{long}}.
\]
Consequently, for every \(n\ge4\) there exist finite positive observation times at which the uniquely optimal design has either strict edge ordering, and at least one intermediate positive time at which its first two conductances are equal. No uniqueness of that crossing is asserted.

Finally, if \(Q_n(w)=\operatorname{tr}(L(w)^2)\), then the finite-size price of applying the asymptotically fast-mixing design to the initial, design-dependent heat-loss coefficient has the universal limit
\[
\boxed{\lim_{n\to\infty}
\frac{Q_n(w^{\mathrm{long}})}{Q_n(w^{\mathrm{short}})}=\frac65.}
\]
The factor \(6/5\) concerns the first design-dependent Taylor coefficient \(Q_n/2\), **not** a ratio of the heat traces themselves.

## Assumptions and scope

The edge-weight design is time independent; observation time changes the objective, not the weights during evolution. The Laplacian is unnormalized: its diagonal entries are adjacent conductance sums, its adjacent off-diagonal entries are negatives of the corresponding conductances, and all other entries vanish. The feasible simplex includes disconnected allocations, though both limiting designs are strictly connected. No per-vertex rate caps or stochastic-matrix row constraints are imposed. The budget equality is appropriate since increasing any edge conductance decreases the heat trace for positive time. The result requires \(n\ge4\); the three-vertex path does not exhibit the stated priority reversal.

The observation functional is the squared Frobenius norm of the diffusion operator at half the stated time, \(H_t=\|e^{-tL/2}\|_F^2\). It is not the normalized random-walk mixing objective, the graph's total effective resistance, or a claim about time-varying control.

## Proof

**1. Strict convexity and continuity of the optimizer.** Each \(L(w)\) depends affinely and injectively on its edge-weight vector. The symmetric spectral trace of the exponential is strictly convex: along a nonzero symmetric direction \(D\), with a spectral basis of \(L\), its second derivative equals
\[
t^2\sum_{a,b}|D_{ab}|^2\int_0^1
 e^{-t[(1-s)\lambda_a+s\lambda_b]}\,ds>0.
\]
Thus \(H_t(w)\) is strictly convex on the compact feasible simplex and has one minimizer. Joint continuity in \(t\) and \(w\), compactness, and uniqueness show that \(w(t)\) is continuous for all \(t>0\).

**2. Exact small-horizon design.** Since \(\operatorname{tr}L(w)=2B\), Taylor expansion uniformly over the simplex gives
\[
H_t(w)=n-2Bt+\frac{t^2}{2}Q_n(w)+O(t^3),\qquad t\downarrow0.
\]
A direct matrix multiplication gives
\[
Q_n(w)=4\sum_{i=1}^{n-1}w_i^2+
2\sum_{i=1}^{n-2}w_iw_{i+1}=w^{\mathsf T}Tw,
\]
where \(T\) is the \((n-1)\)-dimensional tridiagonal matrix with diagonal \(4\) and adjacent entries \(1\). It is positive definite (every eigenvalue lies in \((2,6)\)). Its unconstrained simplex stationary point satisfies \(Tw=\alpha\mathbf1\). Solve \(Ty=\mathbf1\) with boundary values \(y_0=y_n=0\): the recurrence \(4y_i+y_{i-1}+y_{i+1}=1\) has the stated explicit solution, since its characteristic roots are \(-\rho\) and \(-1/\rho\). Positivity holds because \(\rho<1/3\), \(n\ge4\), and \(|(-\rho)^i+(-\rho)^{n-i}|\le2\rho<1-\rho^n\le1+(-\rho)^n\). Hence the stationary point is feasible, and positive definiteness makes it the unique global minimizer of \(Q_n\). Uniform convergence of \(2[H_t-n+2Bt]/t^2\) to \(Q_n\) implies convergence of the unique heat-trace minimizers to this point.

To establish its strict boundary priority, the first two recurrence equations read \(4y_1+y_2=1\) and \(y_1+4y_2+y_3=1\). Therefore \(3(y_1-y_2)=y_3>0\), valid also when \(n=4\).

**3. Exact gap-optimal long-horizon design.** Let \(x_i=i-(n+1)/2\); then \(\sum_i x_i=0\), \(x_{i+1}-x_i=1\), and \(\sum_i x_i^2=n(n^2-1)/12\). The Rayleigh bound for the second Laplacian eigenvalue yields for *every* feasible \(w\), including disconnected cases,
\[
\lambda_2(L(w))\le\frac{\sum_iw_i}{\sum_i x_i^2}
=\frac{12B}{n(n^2-1)}=:\lambda_*.
\]
Set \(c=6B/[n(n^2-1)]\) and \(\widehat w_i=c\,i(n-i)\). Their sum is \(B\), and the exact flux relation gives \(L(\widehat w)x=2c\,x=\lambda_*x\). This is the second, not a higher, eigenvalue: on vertex-polynomial functions of degree \(k\), the difference operator \(L(\widehat w)\) preserves degree and has leading coefficient \(c\,k(k+1)\). Evaluating the monomial basis of degrees \(0,\ldots,n-1\) at the \(n\) vertices triangularizes \(L(\widehat w)\), producing the entire spectrum \(\{c\,k(k+1):0\le k<n\}\). Thus \(\lambda_2=2c\), attaining the universal upper bound.

If any other feasible allocation also attained \(\lambda_*\), equality in the same fixed test-vector Rayleigh bound would make \(x\) its second-eigenvalue eigenvector. The node equations \(L(w)x=\lambda_*x\), telescoped from the left endpoint, force \(w_i=\lambda_*i(n-i)/2\) at every edge. Hence \(\widehat w\) is the unique gap maximizer. Its second edge outweighs its first since \(2(n-2)>n-1\) for \(n>3\).

To pass from spectral gap to the heat trace, write \(\lambda_j(w)\) for the ordered eigenvalues and use
\[
1+e^{-t\lambda_2(w)}\le H_t(w),\qquad
H_t(\widehat w)\le1+(n-1)e^{-t\lambda_*}.
\]
At any heat-trace minimizer, these imply
\[
\lambda_2(w(t))\ge\lambda_*-\frac{\log(n-1)}t.
\]
Compactness and the uniqueness of the gap maximizer force \(w(t)\to\widehat w\) as \(t\to\infty\).

**4. A crossing and a universal penalty.** The two strict edge inequalities, continuity and the intermediate-value theorem establish the crossing statement. For the final limit, the geometric boundary corrections to \(y_i=1/6\) have total bounded size, so
\[
w_i^{\mathrm{short}}=\frac Bn\left(1+O(n^{-1})+
O(\rho^{\min(i,n-i)})\right)
\]
uniformly, with summed squared corrections of bounded size. Consequently
\[
Q_n(w^{\mathrm{short}})=\frac{6B^2}{n}(1+o(1)).
\]
For the long-horizon parabola, Riemann sums and the adjacent-product identity give
\[
Q_n(w^{\mathrm{long}})=\frac{6B^2}{n}
\left(\int_0^1[6s(1-s)]^2\,ds+o(1)\right)
=\frac{6B^2}{n}\left(\frac65+o(1)\right),
\]
proving the exact asymptotic ratio.

## Verification

Run `python3 verify.py` with Python 3, NumPy, SciPy and SymPy. The program checks the tridiagonal exact quadratic solution, the closed boundary-layer expression, positivity, normalized budgets, the full polynomial-spectrum identities for small paths, the exact centered-vector eigenrelation, finite-horizon numerical optima, and the asymptotic quadratic penalty. Its recorded execution ended with `PASS 1157 finite checks`. The proof above, not that finite replay, establishes the infinitely many sizes and all real positive times.

For a concrete exact example, on four vertices with unit total budget, the short design is \((3/8,1/4,3/8)\) and the long design is \((3/10,2/5,3/10)\). The exact first two conductances reverse their ranking.

## Relationship to prior work

The earlier heterogeneous-price reversible-path gap theorem, *The price-metric variance law for fastest mixing on weighted birth-death paths* (2026), already contains the unit-price, equal-mass formula for \(w^{\mathrm{long}}\). The uncapped long-horizon spectral-gap formula is therefore **not claimed as new**. An additional exact central-edge-capacity theorem on even paths also contains that unconstrained formula. Their objective is the smallest nonzero Laplacian eigenvalue, not the entire finite-time exponential trace; their statements do not give the short-horizon optimum, the boundary-edge priority reversal, or the universal \(6/5\) initial-curvature penalty.

Boyd, Diaconis, Sun and Xiao (2006) optimize the second-largest eigenvalue modulus of a **discrete-time symmetric stochastic** path walk and obtain uniform transition probabilities under row constraints; this is a different feasible region and objective. Ghosh, Boyd and Saberi (2006/2008) optimize **total effective resistance**, equivalently an inverse-Laplacian spectral moment, including weighted-path examples; that is not a finite-horizon heat trace. Kempton, Herrmann and di Bernardo (arXiv:1505.07279v1, 2015) optimize algebraic connectivity or spectral eigenratio under degree constraints, and do not address the heat-trace horizon-dependent allocation or the one-fifth penalty. These comparisons distinguish statements and feasible sets rather than titles alone.

## Limitations

The theorem proves two unique endpoint limits and at least one finite-horizon priority crossing; it does not assert monotonicity of individual edge rates, a unique crossing time, an explicit finite-time optimizer, or interior support for every intermediate time. The \(6/5\) ratio concerns the quadratic heat-trace coefficient, not the full time-dependent error or a stochastic-matrix mixing time. Graphs with cycles, per-vertex budgets, edge prices, asymmetric generators, and time-dependent conductances are not covered. The novelty comparison rests on inspected literature and accessible published records; unindexed equivalent work remains possible. No independent mathematical audit has been performed.

## References

1. L. Kempton, G. Herrmann and M. di Bernardo, *Self-organization of weighted networks for optimal synchronizability*, arXiv:1505.07279v1, first posted 2015-05-27, https://arxiv.org/abs/1505.07279 .
2. *The price-metric variance law for fastest mixing on weighted birth-death paths*, publicly available mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-the-price-metric-variance-law-for-fastest-mixing-on-weighted-bir--03df0802fe13 .
3. *Sharp central-edge capacity transition for fastest diffusion on even paths*, publicly available mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-central-edge-capacity-transition-for-fastest-diffusion-on--81038e484a4f .
4. S. Boyd, P. Diaconis, J. Sun and L. Xiao, *Fastest Mixing Markov Chain on a Path*, Amer. Math. Monthly 113 (2006), 70–74, https://stanford.edu/~boyd/papers/pdf/fmmc_path.pdf .
5. A. Ghosh, S. Boyd and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50 (2008), 37–66, based on a 2006 MTNS proceedings paper, https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf .
