# A sharp square-root crossover for fractional maximal perturbations on finite stars

## Finding

Let \(S_m=K_{1,m}\) be the unweighted graph with hub \(0\) and leaves \(1,\ldots,m\), where \(m\ge2\). For \(0<\alpha<1\) and complex vertex data define the centered fractional Hardy--Littlewood maximal map
\[
(M_\alpha f)(v)=\max_{r\ge0}|B(v,r)|^{\alpha-1}\sum_{w\in B(v,r)}|f(w)|.
\]
Write \(V_2(g)=(\sum_{i=1}^m|g(i)-g(0)|^2)^{1/2}\), with each edge counted once and unnormalized counting measure on vertices. Its two-input Euclidean-to-edge modulus is
\[
L_{m,\alpha}=\sup_{f\ne g}\frac{V_2(M_\alpha f-M_\alpha g)}{\|f-g\|_{\ell^2(\{0,\ldots,m\})}}.
\]
Put \(h=(m+1)^{\alpha-1}\). Then, uniformly for every integer \(m\ge2\) and real \(0<\alpha<1\),
\[
\boxed{\sqrt{m\big((1-h)^2+mh^2\big)}\ \le\ L_{m,\alpha}\ \le\ 1+\sqrt{m+m^2h^2}.}\tag{1}
\]
The lower bound is an exact two-input quotient for two strictly positive real signals. Consequently, for fixed \(\alpha\in(0,1)\),
\[
\boxed{\displaystyle L_{m,\alpha}\sim\sqrt{m+m^2(m+1)^{2\alpha-2}}}\qquad(m\to\infty).
\]
This gives the *sharp square-root phase transition*
\[
\lim_{m\to\infty}\frac{L_{m,\alpha}}{m^{1/2}}=1\quad(0<\alpha<1/2),\qquad
\lim_{m\to\infty}\frac{L_{m,1/2}}{m^{1/2}}=\sqrt2,
\]
\[
\lim_{m\to\infty}\frac{L_{m,\alpha}}{m^\alpha}=1\quad(1/2<\alpha<1).
\]
Moreover the transition has a *universal logarithmic critical window*: for each fixed \(s\in\mathbb R\) and sufficiently large \(m\) let \(\alpha_m=\tfrac12+s/\log m\). Then
\[
\boxed{\displaystyle\lim_{m\to\infty}\frac{L_{m,\alpha_m}}{\sqrt m}=\sqrt{1+e^{2s}}.}\tag{2}
\]

## Assumptions and scope

The balls are graph-distance balls and their weights are their cardinalities raised to \(\alpha-1\); the full star ball has \(m+1\) vertices and a radius-one leaf ball has two vertices. The operator averages the pointwise absolute value before taking a supremum. Vertex and edge Euclidean norms are both *unnormalized*. The two-input supremum runs over all distinct complex vertex signals; the theorem is therefore also valid for real and nonnegative inputs. The finite-parameter claim is a two-sided sharp-asymptotic enclosure, **not** the exact finite-\(m\) modulus. The index \(m\) counts leaves, not total vertices. The critical-window parameter \(s\) is fixed as \(m\) varies; the formula for \(\alpha_m\) is used only when \(0<\alpha_m<1\).

## Proof

**1. The three ball averages.** Since the coordinatewise absolute-value map is nonexpansive in \(\ell^2\), it is enough for the upper bound to consider nonnegative vectors \(x=(x_0,x_1,\ldots,x_m)\). Set
\[
b=2^{\alpha-1},\quad h=(m+1)^{\alpha-1},\quad T=x_0+\sum_{j=1}^m x_j.
\]
Then \(0<h<b<1\), and direct examination of the distinct graph balls gives
\[
(M_\alpha x)_0=\max\{x_0,hT\},\qquad
(M_\alpha x)_i=\max\{x_i,b(x_0+x_i),hT\}.
\]
Let \(F_i(x)=(M_\alpha x)_i-(M_\alpha x)_0\). The map \(F:\mathbb R^{m+1}\to\mathbb R^m\) is continuous and piecewise linear, and its Euclidean Lipschitz coefficient controls \(L_{m,\alpha}\).

**2. Uniform global upper bound.** On every open cell on which each maximum has a unique active branch, the \(i\)-th row of the Jacobian of \(F\), with the hub column written first, has the form
\[
J_{i,0}=c_i,\qquad J_{i,j}=d_i\mathbf 1_{\{i=j\}}+r_i\quad(1\le j\le m),
\]
where \(|c_i|\le1\), \(|d_i|\le1\) and \(r_i\in\{-h,0,h\}\). These are consequences of subtracting either the hub singleton branch or the hub global branch from one of the three leaf branches. Thus \(J=D+R\), where \(D\) has only the diagonal leaf entries \(d_i\) and a zero hub column, while \(R\) has hub entries \(c_i\) and constant entries \(r_i\) across the leaf columns. Hence
\[
\|D\|_{2\to2}\le1,\qquad
\|R\|_{2\to2}\le\|R\|_F\le\sqrt{m+m^2h^2},
\]
so \(\|J\|_{2\to2}\le1+\sqrt{m+m^2h^2}\). Partition a line segment into its finitely many active pieces (or approximate a segment lying on a cell wall by generic segments) and integrate the piecewise-constant derivative. Continuity gives the global Lipschitz estimate on the positive orthant. Finally, \(\||f|-|g|\|_2\le\|f-g\|_2\) extends it to arbitrary complex signals. This proves the upper inequality in (1).

**3. A full-dimensional hub-versus-leaves cell.** Fix \(m,\alpha\), normalize \(x_0=1\), and introduce
\[
U=\frac{(m+1)^{1-\alpha}-1}{m}=\frac{h^{-1}-1}{m}.
\]
Write \(\beta=1-\alpha\in(0,1)\). The strict concavity of \(t^\beta\) for positive \(t\) implies
\[
(m+1)^\beta-1<m(2^\beta-1),
\]
so \(U<b^{-1}-1\). Also \(0<U<1\), since \(1<(m+1)^\beta<m+1\). At the equal-leaf vector \((1,U,\ldots,U)\), the global average equals \(h(1+mU)=1\), yet \(1>U\) and \(1>b(1+U)\). Choosing a slightly smaller \(u<U\), still positive, preserves both strict leaf inequalities while making the hub singleton branch strictly dominant: \(1>h(1+mu)>\max\{u,b(1+u)\}\). By continuity these inequalities hold on a nonempty open neighborhood of \((1,u,\ldots,u)\). There the center output is \(x_0\) and every leaf output is \(hT\), giving
\[
F(x)=(hT-x_0)\mathbf1_m.
\]
Its constant Jacobian has each row
\[
w=(h-1,h,h,\ldots,h)\in\mathbb R^{m+1},
\]
and exact operator norm \(\sqrt m\|w\|_2=\sqrt{m[(1-h)^2+mh^2]}\). The two strictly positive signals \(x\) and \(x+\varepsilon w/\|w\|_2\) remain inside this open cell for sufficiently small \(\varepsilon>0\); their quotient equals that norm exactly. This proves the lower inequality and its stated attainment. This step uses no asymptotic estimate or finite computation.

**4. Sharp fixed-parameter and moving-parameter limits.** Divide (1) by \(A_m=\sqrt{m+m^2h^2}=\sqrt m\sqrt{1+mh^2}\). The lower ratio equals \(\sqrt{1-2h/(1+mh^2)}\), and the upper ratio equals \(1+1/A_m\). For every sequence \(m\to\infty\) and \(\alpha_m\in(0,1)\) with \(h_m=(m+1)^{\alpha_m-1}\to0\), both ratios tend to one. This yields the sharp common asymptotic. In particular, for fixed \(\alpha\), \(mh_m^2\sim m^{2\alpha-1}\), proving the three fixed-parameter limits.

For the logarithmic window, \(\alpha_m=1/2+s/\log m\) gives
\[
\log(mh_m^2)=\log m+2(\alpha_m-1)\log(m+1)\longrightarrow2s,
\]
so \(mh_m^2\to e^{2s}\) and \(h_m\to0\). Dividing (1) by \(\sqrt m\) gives (2). The argument treats every fixed real \(s\) and therefore shows that the transition window has scale \(1/\log m\), not a discontinuity at a finite \(m\).

## Verification

The standalone `check_star_fractional_crossover.py` uses Python's standard library only. Run `python check_star_fractional_crossover.py`. It verifies the distinct graph-ball formulas, constructs strictly positive local lower-bound witnesses, evaluates their exact active branch and sharp local quotient numerically, checks the global estimate on seeded random real and complex pairs, and checks the predicted limiting profiles on increasing star sizes. All general assertions follow from the analytic four-part proof rather than finite testing; floating-point comparisons are diagnostics and are not mathematical certificates for an infinite assertion.

## Relationship to prior work

Liu, Lian and Wang (first public 2026-11-11) study sharp one-input and \(\ell^p\) inequalities for graph maximal operators and their fractional versions, including stars. Lu and Zhao (first public 2026-11-18) analyze sharp one-input fractional edge-variation inequalities on finite graphs. These are genuine background results, but neither yields the two-input map modulus from vertex Euclidean perturbations to graph-edge Euclidean differences. In particular a single-input variation estimate does not imply an estimate for \(M_\alpha f-M_\alpha g\), and the two-input modulus need not share the single-input contraction behavior.

A related published finite-star computation determines the two-input *total-variation to total-variation* coefficient for the **ordinary** centered maximal operator, with \(\alpha=0\). Its output/input seminorm pair and exponent are distinct from those here. Another published finite-star degree--smoothing result concerns the **linear** spectral multiplier \(BL^{-s}\), not nonlinear ball maxima, even though both exhibit an exponent threshold. No assertion of a new fractional maximal-function definition or novelty of the standard star graph reduction is made.

## Limitations

The estimates do not determine the exact finite-\(m\) value of \(L_{m,\alpha}\), nor all extremizing pairs. The star is unweighted and counting measure is unnormalized. The limiting laws use \(m\to\infty\), fixed \(\alpha\) or the stated fixed-\(s\) critical window; extensions to general trees, weighted stars, uncentered maximal operators and other input/output norms are unproved. A historical result formulated as a general nonlinear star-Jacobian comparison might imply these estimates without using the same terminology; absolute bibliographic priority is not certified.

## References

1. F. Liu, Y. Lian and Y. Wang, *Sharp \(L^p\) and variation inequalities for maximal operators on finite connected graphs*, arXiv:2611.15377v1, first posted 2026-11-11, https://arxiv.org/abs/2611.15377 .
2. S. Lu and F. Zhao, *Variational Estimates for the Fractional Maximal Operator on Finite Graphs*, arXiv:2611.24189v1, first posted 2026-11-18, https://arxiv.org/abs/2611.24189 .
3. C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs*, arXiv:2005.03146v1, first posted 2020-05-06, https://arxiv.org/abs/2005.03146 .
