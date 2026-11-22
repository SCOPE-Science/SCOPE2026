# Two Pareto shape-index endpoints for triangle-free sticks: Fibonacci localization and a marked rare-triangle law

## Finding

Fix an integer \(n\ge3\). Let \(X_1,\ldots,X_n\) be independent Pareto type-I lengths of scale one and shape \(\alpha>0\), so \(\Pr(X_i>x)=x^{-\alpha}\) for \(x\ge1\). Let \(A_{n,\alpha}\) denote the event that no three lengths form a nondegenerate triangle, and write the ordered sample as \(x_1<\cdots<x_n\) (almost surely).

Let \(F_1=F_2=1\) and \(F_i=F_{i-1}+F_{i-2}\) for \(i\ge3\). Define the **constraint slacks**
\[
u_1=x_1-1,\qquad u_2=x_2-x_1,\qquad u_i=x_i-x_{i-1}-x_{i-2}\quad(3\le i\le n).
\]
On \(A_{n,\alpha}\), all the slacks are nonnegative. Put \(b_{i1}=F_i\); for \(i\ge2\), put \(b_{i2}=F_{i-1}\); for \(3\le j\le i\), put \(b_{ij}=F_{i-j+1}\); and put \(b_{ij}=0\) otherwise. Define the strictly positive rational numbers
\[
c_j=\sum_{i=j}^n\frac{b_{ij}}{F_i}\qquad(1\le j\le n),
\quad C_n=\frac{n!}{\displaystyle\prod_{i=1}^n F_i\prod_{j=1}^n c_j}.
\]

**Two-endpoint theorem.** As \(\alpha\to\infty\) with fixed \(n\),
\[
\Pr(A_{n,\alpha})\sim C_n\left(\prod_{i=1}^nF_i\right)^{-\alpha},
\qquad
\mathcal L\big((\alpha u_j)_{j=1}^n\mid A_{n,\alpha}\big)
\xrightarrow{\mathrm{TV}}\bigotimes_{j=1}^n\operatorname{Exp}(c_j).
\]
Thus, conditioned on the rare triangle-free event, the ordered stick lengths converge to the Fibonacci vector and the appropriately scaled constraint slacks become independent with explicitly unequal exponential rates. In particular, \(C_3=4/3\), \(C_4=108/65\), so the first two probability equivalents are \((4/3)2^{-\alpha}\) and \((108/65)6^{-\alpha}\).

At the opposite endpoint, as \(\alpha\downarrow0\) with fixed \(n\),
\[
\Pr(A_{n,\alpha})
=1-\frac{\pi^2}{36}n(n-1)(n-2)\alpha^2+O_n(\alpha^3).
\]
There is a **marked** version of this law. Set \(Y_i=\log(x_{i+1}/x_i)\) and \(h(y)=\log(1+e^{-y})\). Let \(E_i=\{Y_{i+1}<h(Y_i)\}\), \(1\le i\le n-2\). Conditional on the complementary event \(A_{n,\alpha}^{\mathrm c}\), with probability tending to one exactly one of the \(E_i\) occurs. Its index \(J\) converges to the discrete law
\[
\Pr(J=j\mid A_{n,\alpha}^{\mathrm c})\longrightarrow
\frac{3(n-j)(n-j-1)}{n(n-1)(n-2)},\quad 1\le j\le n-2.
\]
Given this index, the corresponding adjacent logarithmic gaps converge in total variation to the joint density
\[
\frac{12}{\pi^2}\mathbf 1\{y\ge0,\ 0\le z<h(y)\}\,dy\,dz.
\]
This limiting marked-pair law is independent of the selected index.

## Assumptions and scope

The sample size \(n\) is any **fixed** integer at least three; the shape parameter approaches either zero or infinity. Neither asymptotic is asserted to be uniform in increasing \(n\). The scale-one normalization is without loss for the probability, since multiplying all stick lengths by the same constant preserves triangle formation; for scale \(s>0\), define the slacks using lengths divided by \(s\). Ties and exact triangle equalities are null events for this continuous law. The total-variation convergence refers to laws on the full nonnegative orthant, not merely marginal weak limits.

## Proof

**1. Event and triangular coordinates.** Absence of triangles is equivalent to \(x_{i-2}+x_{i-1}\le x_i\) for every \(3\le i\le n\): any pair of smaller elements of a triple with largest member \(x_k\) is bounded above by \(x_{k-2}+x_{k-1}\). The conditions \(1\le x_1\le x_2\) and the successive inequalities are exactly \(u_j\ge0\). Conversely, the recursion \(x_1=1+u_1\), \(x_2=x_1+u_2\), and \(x_i=x_{i-1}+x_{i-2}+u_i\) reconstructs every permitted ordered vector. It has a triangular unit Jacobian. Solving this recursion gives
\[
x_i=F_i+\sum_{j=1}^i b_{ij}u_j,
\]
with the stated coefficients. In particular, \(x_i\ge F_i+u_i\).

**2. Density and large-shape local limit.** The ordered Pareto density is
\[
n!\alpha^n\prod_{i=1}^n x_i^{-\alpha-1}\,dx_1\cdots dx_n.
\]
Apply the unit-Jacobian slack transform and set \(v_j=\alpha u_j\). The exact probability becomes
\[
\Pr(A_{n,\alpha})=
 n!\Big(\prod_{i=1}^n F_i\Big)^{-\alpha-1}
 \int_{\mathbb R_+^n}
 \prod_{i=1}^n\left(1+\frac{\sum_{j\le i}b_{ij}v_j}{\alpha F_i}\right)^{-\alpha-1}dv.
\]
For each fixed nonnegative vector \(v\), the integrand converges to
\(\exp(-\sum_i\sum_{j\le i}b_{ij}v_j/F_i)=\exp(-\sum_jc_jv_j)\). It is dominated **uniformly for \(\alpha\ge2\)** by the integrable product
\[
\prod_{i=1}^n(1+v_i/(2F_i))^{-2}.
\]
Indeed, the \(i\)-th bracket has argument at least \(1+v_i/(\alpha F_i)\), and \((1+t/\alpha)^{\alpha+1}\ge(1+t/2)^2\) for \(\alpha\ge2,t\ge0\). Dominated convergence yields the integral limit \(\prod_jc_j^{-1}\), establishing the claimed probability equivalent. Dividing the integrand by its integral identifies the conditional density of \((\alpha u_j)\). This density converges almost everywhere to \(\prod_jc_je^{-c_jv_j}\); both integrate to one, so Scheffé's lemma gives **total variation**, not just weak, convergence. The limiting Fibonacci configuration is the unique coordinatewise minimal configuration in this feasible cone.

**3. Independent logarithmic spacings and small-shape expansion.** Since \(\log X_i\) has exponential law of rate \(\alpha\), the successive ascending log-gaps \(Y_i=\log(x_{i+1}/x_i)\), \(1\le i\le n-1\), are independent exponential variables with rates \(r_i=(n-i)\alpha\). The exact triangle condition becomes \(Y_{i+1}\ge h(Y_i)\). Thus its failure is the union of \(E_i=\{Y_{i+1}<h(Y_i)\}\). Independence gives
\[
\Pr(E_i)=r_i\int_0^\infty e^{-r_iy}\bigl(1-e^{-r_{i+1}h(y)}\bigr)dy
=r_ir_{i+1}\int_0^\infty h(y)dy+O_n(\alpha^3).
\]
The uniform remainder follows from \(1-e^{-t}=t+O(t^2)\), \(e^{-r_iy}=1+O(r_i y)\), and integrability of \(yh(y)+h(y)^2\). Expanding \(\log(1+e^{-y})\) into its alternating exponential series and integrating gives
\[
\int_0^\infty h(y)dy=\sum_{k\ge1}\frac{(-1)^{k+1}}{k^2}=\frac{\pi^2}{12}.
\]
For \(|i-j|\ge2\) the events \(E_i,E_j\) involve disjoint pairs of gaps, so their intersection is \(O_n(\alpha^4)\). For adjacent indices, \(E_i\cap E_{i+1}\subset E_i\cap\{Y_{i+2}<\log2\}\), an intersection of independent events of probability \(O_n(\alpha^3)\). The union therefore has probability
\[
\sum_{i=1}^{n-2}\Pr(E_i)+O_n(\alpha^3)
=\frac{\pi^2\alpha^2}{12}\sum_{i=1}^{n-2}(n-i)(n-i-1)+O_n(\alpha^3).
\]
The finite sum is \(n(n-1)(n-2)/3\). Subtracting the union probability from one proves the small-shape formula.

**4. Marked rare triangle.** The preceding intersection bounds show that, conditioned on at least one \(E_i\), the chance of more than one \(E_i\) is \(O_n(\alpha)\). The normalized leading probabilities \(r_ir_{i+1}(\pi^2/12)\) give the displayed index weights. Conditional on \(E_i\), the joint density of \((Y_i,Y_{i+1})\) is proportional to
\[
r_ir_{i+1}e^{-r_iy-r_{i+1}z}\mathbf1\{y\ge0,0\le z<h(y)\}.
\]
After normalization it converges pointwise to the constant \(12/\pi^2\) on that integrable domain. Scheffé's lemma proves convergence in total variation. Changing the conditioning from \(E_i\) to a unique failure on \(A_{n,\alpha}^{\mathrm c}\) changes conditional probabilities by \(O_n(\alpha)\), completing the marked assertion.

## Verification

Run `python3 CHECK.py` from a directory containing the embedded file. The program uses **only the Python standard library** and verifies the exact Fibonacci slack reconstruction for sample sizes 3 through 11, the positive rates, all finite-difference coefficients, and the explicit cases \(C_3=4/3,C_4=108/65\). Deterministic Simpson quadrature checks the integral \(\pi^2/12\), the paper's exact three-stick formula at \(\alpha=1\), and the approach to both derived asymptotics for selected positive parameter values. It prints `PASS 4421 finite exact or deterministic quadrature assertions`. The quadrature and finite enumeration do not establish either asymptotic; the uniform dominating function, independent exponential gaps, intersection bounds and Scheffé arguments above do.

## Relationship to prior work

Barczy and Lovas (2026, arXiv:2611.04436v1, Theorem 3.2) derive exact finite-sample Pareto integral representations for every positive shape parameter, and their Corollary 3.3 treats three sticks explicitly. Their Remark 3.5 gives qualitative endpoint limits for three sticks, not the all-\(n\) sharp constants or either conditional marked law above. Thus their exact integral framework **contains** the problem but does not directly state the two sharp endpoint descriptions. These earlier representations are acknowledged, rather than treated as independent new probability laws.

A previously published result entitled *Sharp quadratic decay for triangle-free Pareto stick samples* establishes the large-\(n\) quadratic logarithmic rate for fixed \(\alpha>0\); its own scope explicitly excludes a changing shape index. Its limit takes a **different parameter** to infinity and does not imply the fixed-\(n\), \(\alpha\to\infty\) Fibonacci prefactor or conditional total-variation law. Sudbury, Sun, Treeby and Wang (2026) treat **uniform** sampled sticks and derive a Fibonacci-product probability; that sampling distribution is distinct. All cited exact finite-\(n\) formulas are credited. A theorem expressing an equivalent asymptotic in other variables elsewhere in the literature remains possible.

## Limitations

Both results are pointwise in a **fixed** sample size \(n\). They do not offer uniform two-parameter limits, rates of total-variation convergence, or analogous formulae for other stick distributions and larger polygons. The endpoint event includes degenerate triangles only on a null set. Total-variation convergence of *scaled slacks* is not convergence of the unconditioned joint stick distribution. The finite integral is known from earlier work; the present statements are its shape-endpoint asymptotics and conditional rare-event geometry. Historical priority beyond the inspected sources has not been independently certified.

## References

1. M. Barczy and R. L. Lovas, *Pick-up sticks problems for exponential and Pareto distributions*, arXiv:2611.04436v1, first public November 3, 2026. Theorem 3.2, Corollary 3.3, Remark 3.5. https://arxiv.org/html/2611.04436v1
2. *Sharp quadratic decay for triangle-free Pareto stick samples*, public mathematical research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-quadratic-decay-for-triangle-free-pareto-stick-samples--8d0ac1d44459
3. A. Sudbury, A. Sun, D. Treeby and E. Wang, *Pick-up Sticks and the Fibonacci Factorial*, Fibonacci Quarterly (published online July 16, 2026), arXiv:2504.19911. https://www.tandfonline.com/doi/full/10.1080/00150517.2026.2663981
4. M. Brennan, N. Callow and T. C. Lin, *Fibonacci numbers and the probability of polygon formation using random length sticks*, arXiv:2604.27573 (2026). https://arxiv.org/abs/2604.27573
