# Sharp quadratic-loss phase transition in path variation for sliding three-point \(p\)-means

## Finding
For every integer \(n\ge3\) and real \(1<p<\infty\), let \(T_{n,p}:\mathbb R^n\to\mathbb R^{n-2}\) be the full-window three-sample \(p\)-mean filter (defined below). Put \(V_m(h)=\sum_{i=1}^{m-1}|h_{i+1}-h_i|\). Its **exact two-input variation Lipschitz coefficient** is
\[
K_{n,p}:=\sup_{V_n(f-g)>0}\frac{V_{n-2}(T_{n,p}f-T_{n,p}g)}{V_n(f-g)}
=\begin{cases}
0,&n=3,\\
\min\{n-3,3\},&n\ge4,\quad1<p<2,\\
\min\{(n-3)/3,1\},&n\ge4,\quad p=2,\\
1,&n\ge4,\quad2<p<\infty.
\end{cases}
\]
The sharp coefficient is a supremum, not necessarily a maximum. For \(p=2\), it is attained by finite pairs whenever positive. For \(p>2\) and \(n\ge6\), it is also attained. In particular, for every \(n\ge6\) the sharp constants are \(3,1,1\) in the three exponent regimes \(1<p<2\), \(p=2\), and \(p>2\). The subquadratic value is three times the superquadratic value.

## Assumptions and scope
A real triple \(x=(x_1,x_2,x_3)\) has \(p\)-mean \(\mu_p(x)\), the unique minimizer of \(\sum_{j=1}^3|u-x_j|^p\) over \(u\in\mathbb R\). Define \((T_{n,p}f)_i=\mu_p(f_i,f_{i+1},f_{i+2})\) for \(1\le i\le n-2\). Windows are full, noncyclic, and unweighted, with no padding. The input and output variations use consecutive edges, without endpoint penalties. The denominator explicitly excludes pairs having zero difference variation. Translation-equivariance of \(\mu_p\) implies that pairs with zero denominator also have zero output-difference variation.

## Proof
**Step 1: regularity and the Jacobian.** Strict convexity for \(p>1\) gives a unique mean. The Euler equation is
\[
\sum_{j=1}^{3}(u-x_j)|u-x_j|^{p-2}=0,
\]
where the summand is zero when its argument is zero. Permutation and reflection symmetry, monotonicity in each datum, and translation-equivariance follow directly. Monotonicity plus translation-equivariance imply \(|\mu_p(x)-\mu_p(y)|\le\|x-y\|_\infty\), so the filter is locally Lipschitz. At generic triples the gradient of \(\mu_p\) is the probability vector
\[
w_j=\frac{|x_j-\mu_p(x)|^{p-2}}{\sum_{h=1}^{3}|x_h-\mu_p(x)|^{p-2}}.
\]
The formula is used at points with nonzero residuals and outside the exceptional all-equal triple; for \(p=2\), all three weights equal \(1/3\). All components are nonnegative and sum to one. Almost-everywhere differentiation is enough for global bounds by integration along generic segments and continuity at arbitrary endpoints.

**Step 2: a three-point superquadratic weight restriction.** Suppose \(p>2\). Set \(q=p-1>1\), and let \(r_j=x_j-\mu_p(x)\). Their signed \(q\)-powers sum to zero. For every \(i\),
\[
|r_i|^q\le\sum_{j\ne i}|r_j|^q,
\qquad
|r_i|^{q-1}\le\left(\sum_{j\ne i}|r_j|^q\right)^{(q-1)/q}\le\sum_{j\ne i}|r_j|^{q-1}.
\]
Thus \(w_i\le1/2\) for each coordinate. This conclusion also holds when exactly one residual vanishes, by continuity of the displayed weights. It is the structural difference from \(1<p<2\), for which one weight can approach one.

**Step 3: input-step variation and upper bounds.** Every input increment \(h\in\mathbb R^n\) decomposes as a constant plus its jumps: \(h=h_1\mathbf1+\sum_{k=1}^{n-1}(h_{k+1}-h_k)s^{(k)}\), where \(s^{(k)}_j=\mathbf1_{j>k}\). For a generic filter Jacobian \(J\), the components of \(Js^{(k)}\) equal zero for windows entirely left of the jump and one for windows entirely right. The only possible intermediate components are
\[
r=w_{k-1,k+1},\qquad 1-\ell=1-w_{k,k},
\]
where an unavailable boundary window is simply omitted. The subscript denotes the row's window start and the original-signal coordinate. Hence each step response is a subsequence of \((0,r,1-\ell,1)\), with \(0\le r,\ell\le1\). Its variation is at most \(3\), and also at most \(n-3\) because the output contains \(n-2\) entries. For \(p>2\), Step 2 gives \(r+\ell\le1\): the response is nondecreasing and has variation at most \(1\). At \(p=2\), the two intermediate values are \(1/3\) and \(2/3\); counting the available output edges gives precisely \(\min\{(n-3)/3,1\}\). The step decomposition and triangle inequality establish the corresponding Jacobian bounds for every \(h\). Since the filter is Lipschitz, integrating along almost every line segment gives the global two-input bounds. For any exceptional segment, translate its starting point by a generic arbitrarily small vector, apply the proven bound, and let the translation vanish.

**Step 4: simultaneous sharpness.** Take \(0<\delta<1\) and set \(a_p(\delta)=\mu_p(-1,1,\delta)\), \(r_p(\delta)=a_p(\delta)/\delta\). Strict monotonicity of the Euler equation implies \(0<a_p(\delta)<\delta\), and
\[
(\delta-a_p(\delta))^{p-1}=(1+a_p(\delta))^{p-1}-(1-a_p(\delta))^{p-1}
=2(p-1)a_p(\delta)+O(a_p(\delta)^3).
\]
Consequently,
\[
\lim_{\delta\downarrow0}r_p(\delta)=
\begin{cases}1,&1<p<2,\\1/3,&p=2,\\0,&p>2.\end{cases}
\]
The reflection identity \(\mu_p(c-x_1,c-x_2,c-x_3)=c-\mu_p(x_1,x_2,x_3)\) yields the exact following constructions. On four sites start from \((-1,1,0,2)\) and add \(\delta(0,0,1,1)\). The output-difference sequence is \((a_p(\delta),\delta-a_p(\delta))\), so the variation ratio is \(|1-2r_p(\delta)|\). On five sites append any fifth value and perturb the last three coordinates by \(\delta\); the output-difference sequence is \((a_p(\delta),\delta-a_p(\delta),\delta)\) and the ratio is \(|1-2r_p(\delta)|+r_p(\delta)\). On six or more sites start with \((0,-1,1,0,2)\), append arbitrary values, and perturb from the fourth input coordinate onward by \(\delta\). The output-difference sequence begins \((0,a_p(\delta),\delta-a_p(\delta),\delta)\) and all later components equal \(\delta\). Its ratio is \(2r_p(\delta)+|1-2r_p(\delta)|\). Passing to the displayed limits yields every claimed lower bound. In the quadratic case the formulas hold exactly for every positive \(\delta\). When \(p>2\) and \(n\ge6\), one can also take a zero input and an input equal to zero in its first three coordinates and a positive constant in the rest: monotonicity of the filter and its all-zero and all-constant endpoint windows give equality at finite inputs.

## Verification
The accompanying standalone `check_pmean.py` numerically evaluates the defining minimizers by bisection, tests 4,480 independently seeded two-input inequalities over eight exponents and seven lengths, and evaluates the explicit sharpness families for six nonquadratic exponents on four lengths. The test output ends in `ALL_THREE_SAMPLE_P_MEAN_CHECKS_PASS`. This computation checks examples, not the universal quantifiers, which follow from the proof above. For exponents extremely close to two, the approach to the singular sharpness limit can be slow, so the finite limiting tests deliberately use exponents away from two; the theorem itself covers every \(1<p<\infty\).

## Relationship to prior work
Falcone, Finzi Vita, Giorgi and Smits (arXiv:1301.7570, first public 2013-01-31), especially Appendix 7, define finite-set \(p\)-averages, prove translation-equivariance and coordinate monotonicity, and analyze a two-dimensional numerical scheme for the game \(p\)-Laplacian. Ishiwata, Magnanini and Wadade (arXiv:1604.00520, first public 2016-04-02), especially Sections 1–2, treat the \(p\)-mean as a best constant \(L^p\) approximation and use it for asymptotic mean-value properties. These results supply the underlying mean but do not state the two-input adjacent-variation coefficients of a sliding finite-path filter. Related finite-path median results and an indexed complete-pair Gini stability theorem for a star's \(p\)-harmonic center use different norms/operators and do not imply the present three-point path classification.

## Limitations
The result treats only full three-point moving windows on unweighted real paths and finite exponents strictly above one. In particular, it does not claim weighted data, longer windows, cyclic boundary conditions, two-dimensional images, or exact attained pairs for every supremum in the subquadratic regime. The novelty assessment is conditional on examined and indexed literature; an unindexed earlier equivalent remains possible. No independent audit has been conducted.

## References
1. M. Falcone, S. Finzi Vita, T. Giorgi and R. G. Smits, *A Semi-Lagrangian Scheme for the Game \(p\)-Laplacian via \(p\)-averaging*, arXiv:1301.7570v1 (2013), https://arxiv.org/pdf/1301.7570.
2. M. Ishiwata, R. Magnanini and H. Wadade, *A Natural Approach to the Asymptotic Mean Value Property for the \(p\)-Laplacian*, arXiv:1604.00520v1 (2016), https://arxiv.org/abs/1604.00520, publicly accessible full manuscript at https://flore.unifi.it/retrieve/e398c380-e2c7-179a-e053-3705fe0a4cff/1604.00520v1.pdf.
