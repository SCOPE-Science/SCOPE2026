# A sharp random-to-deterministic ordering transition for two-component proximal reshuffling

## Finding

Consider two distinct-minimizer scalar strongly convex quadratics
\[
f_a(x)=\frac a2(x-u)^2,\qquad f_b(x)=\frac b2(x-v)^2,
\qquad a>b>0,\quad u\ne v.
\]
Their average objective \(F=(f_a+f_b)/2\) has unique minimizer \(x_\star=(au+bv)/(a+b)\). Fix any \(h>0\). In each epoch, apply the two individual proximal maps \(T_i=\operatorname{prox}_{h f_i}\) exactly once, choosing independently between epochs whether \(T_a\) is applied last, with probability \(p\in[0,1]\), or \(T_b\) is applied last, with probability \(1-p\). Write \(X_k\) for the endpoint after \(k\) epochs.

Let
\[
r=\frac1{(1+ha)(1+hb)},\quad
\Delta=\frac{h^2ab(u-v)}{(1+ha)(1+hb)},\quad
p_0=\frac a{a+b}.
\]
For every deterministic initial point, the stationary mean-square error exists and is **exactly**
\[
\mathcal E_h(p):=\lim_{k\to\infty}\mathbb E(X_k-x_\star)^2
=\Delta^2\left\{\frac{(p-p_0)^2}{(1-r)^2}+
\frac{p(1-p)}{1-r^2}\right\}.
\tag{1}
\]
The stationary mean equals \(x_\star\) **if and only if** \(p=p_0\), for every finite positive stepsize. In contrast, the unique stationary **mean-square-risk** minimizer among all independent epochwise two-order laws is
\[
\boxed{\ p_\star(h)=\min\!\left\{1,\;
\frac a{a+b}+\frac{a-b}{4}h+\frac{ab(a-b)}{4(a+b)}h^2\right\}.\ }
\tag{2}
\]
There is a unique positive threshold \(h_c\) determined by
\[
(1+h_c a)(1+h_c b)=\frac{a+3b}{a-b}.
\tag{3}
\]
For \(0<h<h_c\), the unique optimal policy genuinely randomizes, with \(p_0<p_\star(h)<1\). For \(h\ge h_c\), the unique minimizer is deterministic: the component of larger curvature is processed last in every epoch. At equality, the endpoint optimum is still unique.

A further sharp consequence is a **stationary error-order improvement**: as \(h\downarrow0\), letting \(d=u-v\),
\[
\mathcal E_h(1/2)\sim
\frac{a^2b^2(a-b)^2d^2}{4(a+b)^4}h^2,
\qquad
\mathcal E_h(p_0)\sim
\frac{a^3b^3d^2}{2(a+b)^3}h^3.
\tag{4}
\]
The risk at the optimal \(p_\star(h)\) has the same leading \(h^3\) term as \(p_0\), but is strictly smaller at every finite \(h\). Thus curvature-weighted (rather than uniform) ordering removes an entire leading stationary squared-error order when curvatures and component minimizers differ.

## Assumptions and scope

All expectations are over fresh, independent epochwise order draws with the same probability \(p\). A complete epoch always uses precisely two component proximal calls, one per component; it is **not** the regularizer-proximal-after-SGD construction commonly also called proximal random reshuffling. The objective consists of exactly two scalar quadratic components, with the strict inequalities displayed above and common stepsize \(h\). There are no additive oracle errors. Risk is assessed only at epoch endpoints, after infinitely many epochs; no claim is made for intermediate points or a fixed finite number of epochs. Every minimizer statement concerns the one-dimensional family of order laws parameterized by \(p\), not all conceivable optimization algorithms. The limiting expectation is finite because the epoch maps are affine contractions with uniformly bounded offsets.

The risk in objective units is \(\lim\mathbb E[F(X_k)-F(x_\star)]=(a+b)\mathcal E_h(p)/4\); therefore it has exactly the same optimizers.

## Proof

**Step 1: exact two-order maps.** Define \(r_a=(1+ha)^{-1}\) and \(r_b=(1+hb)^{-1}\). Direct minimization of the strictly convex proximal subproblem gives
\[
T_a(x)=r_ax+(1-r_a)u,\qquad T_b(x)=r_bx+(1-r_b)v.
\]
For the two orders, the epoch map always has slope \(r=r_ar_b\) and a random offset \(C\), taking values
\[
C_a=(1-r_a)u+r_a(1-r_b)v\quad(T_a\text{ last}),
\]
\[
C_b=(1-r_b)v+r_b(1-r_a)u\quad(T_b\text{ last}).
\]
Their difference is \(C_a-C_b=(1-r_a)(1-r_b)(u-v)=\Delta\ne0\). Thus \(X_{k+1}=rX_k+C_{k+1}\), where the \(C_k\) are independent and identically distributed with \(\Pr(C_k=C_a)=p\).

**Step 2: limiting mean and variance.** Since \(0<r<1\), the convergent random series \(\sum_{j\ge0}r^jC_{-j}\) defines the unique stationary law and the laws from all deterministic initial data converge to it in mean square. Write \(m_p\) and \(V_p\) for its mean and variance. Elementary moment recurrences give
\[
m_p=\frac{pC_a+(1-p)C_b}{1-r},\qquad
V_p=\frac{p(1-p)\Delta^2}{1-r^2}.
\tag{5}
\]
At \(p_0=a/(a+b)\), expanding the numerator over the common denominator \((1+ha)(1+hb)\) gives
\[
p_0C_a+(1-p_0)C_b=(1-r)\frac{au+bv}{a+b}.
\]
It follows that \(m_p-x_\star=\Delta(p-p_0)/(1-r)\); because \(\Delta\ne0\), no other \(p\) yields an unbiased stationary endpoint. The identity \(\mathbb E(X-x_\star)^2=\operatorname{Var}X+(\mathbb EX-x_\star)^2\) now proves (1).

**Step 3: global sharp minimizer and transition.** The second derivative of the brace in (1) is
\[
\frac{2}{(1-r)^2}-\frac{2}{1-r^2}
=\frac{4r}{(1-r)^2(1+r)}>0.
\]
Thus the risk is strictly convex in \(p\), and its unique real unconstrained minimizer is
\[
p^\circ=\frac12+\frac{1+r}{2r}\left(p_0-\frac12\right)
=\frac a{a+b}+\frac{a-b}4h+\frac{ab(a-b)}{4(a+b)}h^2.
\]
For \(a>b\), this lies strictly above \(p_0>1/2\), so the only possible active interval constraint is \(p\le1\). Consequently (2) follows by projecting onto \([0,1]\). Equality \(p^\circ=1\) is equivalent to \(r=(a-b)/(a+3b)\), proving (3) and the uniqueness of \(h_c>0\), because \((1+ha)(1+hb)\) strictly increases from \(1\) to infinity, while \((a+3b)/(a-b)>1\). The risk remains strictly convex at the threshold, proving uniqueness also there.

**Step 4: limiting error orders.** As \(h\downarrow0\),
\[
r=1-(a+b)h+O(h^2),\qquad \Delta=ab(u-v)h^2+O(h^3).
\]
The first term in (1), evaluated at \(p=1/2\), has positive \(h^2\) coefficient \(a^2b^2(a-b)^2(u-v)^2/[4(a+b)^4]\); the variance term is only \(O(h^3)\). At \(p=p_0\) the bias term vanishes exactly and the variance term has the displayed \(h^3\) coefficient. Moreover \(p_\star(h)=p_0+(a-b)h/4+O(h^2)\), whose displacement contributes only \(O(h^4)\) to risk. This proves (4) and its optimal-policy counterpart.

## Verification

A standalone standard-library exact-rational verifier, `verify.py`, evaluates the two composed proximal offsets, stationary first and second moment recurrences, strict convexity, the unconstrained and clipped risk minimizers, and equality of the moment formula to (1). It performs 15,624 exact-rational assertions across curvature ratios, distinct minimizers, stepsizes, and order probabilities. Run `python verify.py`; expected output is in `verification_output.txt`. The finite tests check transcription and sample cases; the proof above supplies the universal parameter quantifiers.

An explicit comparison takes \(a=3\), \(b=1\), \(u=1\), \(v=-1\), \(h=1/4\). Then \(r=16/35\), \(p_0=3/4\), \(p_\star=115/128\) and
\[
\mathcal E_h(1/2)=381/24548,\quad
\mathcal E_h(3/4)=9/1292,\quad
\mathcal E_h(115/128)=231/41344,\quad
\mathcal E_h(1)=9/1444.
\]
For the same quadratics at \(h=1\), \(r=1/8\) and \(p_\star=1\), with \(\mathcal E_h(1)=9/196\) versus \(\mathcal E_h(3/4)=3/28\). All values are exact rational consequences of (1).

## Relationship to prior work

Das, Schölkopf and Muehlebach (2022, arXiv:2206.02953) define a componentwise implicit proximal point algorithm with uniform random reshuffling, shuffle once, and adversarial orders. Their main contributions are general finite-epoch convergence bounds, including for implicit updates, rather than optimization of stationary risk over continuously biased two-order distributions. In particular, their specified RR permutation law is uniform and their adversarial bounds cannot imply the exact optimum (2) by a change of notation.

Traoré, Apidopoulos, Salzo and Villa (2023, arXiv:2308.09310) provide a broad variance-reduced stochastic proximal point framework and convergence rates, not the two-order curvature-weighted stationary-mean and stationary-risk classification here. Rajput, Lee and Papailiopoulos (2021, arXiv:2102.09718) show that permutation choice matters substantially for explicit-gradient SGD, including scalar strongly convex settings, but their update differs from the implicit componentwise proximal maps studied here; their rate and permutation results do not imply (1)–(4). Mishchenko, Khaled and Richtárik (2021, arXiv:2102.06704) propose an algorithm also named ProxRR, whose component operations are explicit gradient steps and whose regularizer proximal call is once per epoch; this distinct operator structure does not yield the present formulas. The more general observation that the ordering of noncommuting maps matters is not asserted to be new. The novelty claim is limited to the exact sharp implicit two-map stationarity, unbiased-order law, risk optimizer, and its phase transition and small-stepsize consequence.

## Limitations

This is a small, analytically tractable model. It does not apply directly to vector-valued, noncommuting component Hessians, unequal numbers of component visits, unequal proximal stepsizes, state-adaptive order choices, noisy or inexact component proximal solves, or fixed-duration performance. For constant \(p\), the best mean-square risk does not require the stationary mean to equal the full-objective minimizer. A different algorithm, e.g. a full objective proximal call, may outperform every considered two-component ordering law. Independent validation and an exhaustive specialist-literature precedence check are not supplied; some earlier work on random affine iterations may contain equivalent formulas.

## References

- Aniket Das, Bernhard Schölkopf, Michael Muehlebach, *Sampling without Replacement Leads to Faster Rates in Finite-Sum Minimax Optimization*, arXiv:2206.02953 (first public 2022-06-07), https://arxiv.org/abs/2206.02953.
- Cheik Traoré, Vassilis Apidopoulos, Saverio Salzo, Silvia Villa, *Variance reduction techniques for stochastic proximal point algorithms*, arXiv:2308.09310 (first public 2023-08-18), https://arxiv.org/abs/2308.09310.
- Shashank Rajput, Kangwook Lee, Dimitris Papailiopoulos, *Permutation-Based SGD: Is Random Optimal?*, arXiv:2102.09718 (first public 2021-02-19), https://arxiv.org/abs/2102.09718.
- Konstantin Mishchenko, Ahmed Khaled, Peter Richtárik, *Proximal and Federated Random Reshuffling*, arXiv:2102.06704 (first public 2021-02-12), https://arxiv.org/abs/2102.06704.
