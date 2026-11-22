# Two-tail triangle-free stick samples: a sharp rare-event exponent and a conditional rank large-deviation law

## Finding

Let \(X_1,X_2,\ldots\) be independent, identically distributed positive lengths and suppose \(Y=\log X_1\) has a continuous density \(f:\mathbb R\to(0,\infty)\) with two finite, positive logarithmic tail slopes:
\[
\lim_{y\to+\infty}\frac{-\log f(y)}{y}=\alpha>0,
\qquad
\lim_{y\to-\infty}\frac{-\log f(y)}{|y|}=\beta>0.
\]
Let \(A_n\) be the event that **none** of the \(\binom n3\) triples of lengths form a nondegenerate triangle. For any fixed threshold \(t>0\), define \(M_n(t)=\#\{1\le j\le n:X_j\le t\}\), and write \(\varphi=(1+\sqrt5)/2\) and \(c=\log\varphi\).

**Theorem.** For any sequence of integers \(0\le m_n\le n\) satisfying \(m_n/n\to u\in[0,1]\),
\[
\lim_{n\to\infty}\frac{1}{n^2}\log\mathbb P\bigl(A_n,\,M_n(t)=m_n\bigr)
=-\frac c2\left[\beta u^2+\alpha(1-u)^2\right].\tag{1}
\]
Consequently,
\[
\lim_{n\to\infty}\frac{1}{n^2}\log\mathbb P(A_n)
=-\frac{c\alpha\beta}{2(\alpha+\beta)}.\tag{2}
\]
Conditionally on \(A_n\), the fractions \(M_n(t)/n\) satisfy a large-deviation principle on \([0,1]\) with speed \(n^2\) and good rate function
\[
I(u)=\frac{c(\alpha+\beta)}2\left(u-\frac{\alpha}{\alpha+\beta}\right)^2,\qquad 0\le u\le1.\tag{3}
\]
In particular, simultaneously for **every fixed** positive threshold,
\[
\frac{M_n(t)}n\ \xrightarrow[n\to\infty]{\mathbb P(\,\cdot\mid A_n)}\
\frac{\alpha}{\alpha+\beta}.\tag{4}
\]
The assertion is about each fixed threshold, not a uniform claim over thresholds that vary with \(n\).

For the concrete two-sided power-law family whose logarithm has asymmetric Laplace density
\[
f(y)=\frac{\alpha\beta}{\alpha+\beta}
\begin{cases}e^{-\alpha y},&y\ge0,\\e^{\beta y},&y<0,\end{cases}
\]
(2)–(4) hold without any smoothness condition on the derivatives of \(f\). In the symmetric case \(\alpha=\beta=1\), the no-triangle logarithmic exponent equals \(-\log\varphi/4\), and half the sticks are below each fixed \(t>0\) under the rare-event conditioning.

## Assumptions and scope

The density is required to be continuous and strictly positive at every finite real argument; the two displayed limits are limits of the **log density**, not just regular variation in probability tails. No finite mean or variance of \(X_1\) is assumed. All limits are as \(n\to\infty\), with \(\alpha,\beta,t\) held fixed. Intervals with exactly equal lengths and exactly degenerate triangles have probability zero, so the choice of strict versus non-strict inequality at equality does not alter probabilities.

We use the Fibonacci numbers \(F_1=F_2=1\), \(F_{j+2}=F_{j+1}+F_j\). Their elementary exponential bound \(F_{d+1}\ge\varphi^{d-1}\) is valid for every integer \(d\ge1\) by induction.

## Proof

### 1. Reduction to a constrained sorted sequence

Write the order statistics as \(x_1<\cdots<x_n\). Since the lengths are positive, no triple forms a nondegenerate triangle exactly when
\[
x_{i+2}\ge x_i+x_{i+1},\qquad 1\le i\le n-2.\tag{5}
\]
Indeed, if (5) holds, every triple \(a<b<d\) obeys \(x_a+x_b\le x_{d-2}+x_{d-1}\le x_d\); the converse follows by choosing consecutive triples. Combining monotonicity, (5) and induction yields
\[
x_j\ge F_{j-i+1}x_i,\qquad 1\le i<j\le n.\tag{6}
\]
Fix \(t>0\) and let \(z_i=\log(x_i/t)\). Let \(m=\#\{i:z_i\le0\}\) and \(k=n-m\). For \(i\le m\), (6) with \(j=m\) and \(x_m\le t\) yields \(-z_i\ge \log F_{m-i+1}\) (when \(m\ge1\)). For \(i\ge m+1\), (6) with the first point above the threshold gives \(z_i\ge\log F_{i-m}\) (when \(k\ge1\)). Consequently, with \(a_+=\max(a,0)\),
\[
\begin{aligned}
E_{\alpha,\beta}(z)&:=\alpha\sum_{i=1}^n(z_i)_+
+\beta\sum_{i=1}^n(-z_i)_+\\
&\ge \frac c2\Bigl[\beta(m-1)_+(m-2)_+
+\alpha(k-1)_+(k-2)_+\Bigr]\\
&=\frac c2[\beta m^2+\alpha k^2]-O_{\alpha,\beta}(n).
\end{aligned}\tag{7}
\]
The cases \(m=0\) and \(m=n\) use only the nonempty side of the same bound and are included. The error bound is uniform over \(0\le m\le n\).

### 2. Upper bound for an exact threshold count

For every sufficiently small \(\varepsilon>0\), the two log-density hypotheses, positivity, and continuity imply global constants \(0<c_{\varepsilon,t}\le C_{\varepsilon,t}<\infty\) such that, writing \(f_t(z)=f(z+\log t)\),
\[
c_{\varepsilon,t}\,e^{-E_{\alpha+\varepsilon,\beta+\varepsilon}(z)}
\le f_t(z)\le
C_{\varepsilon,t}\,e^{-E_{\alpha-\varepsilon,\beta-\varepsilon}(z)}.\tag{8}
\]
For any \(\eta\in(0,1)\), write the product of the upper densities as a \((1-\eta)\)-fraction used for the constrained cost and an \(\eta\)-fraction used for integration. The integral of \(e^{-\eta E_{\alpha-\varepsilon,\beta-\varepsilon}(z)}\) on \(\mathbb R\) is the finite constant
\[
K_{\varepsilon,\eta}
=\frac1{\eta(\alpha-\varepsilon)}
+\frac1{\eta(\beta-\varepsilon)}.
\]
Using the order-statistic density \(n!\prod f_t(z_i)\), (7), and discarding the ordering restrictions only in the remaining integrable factor, we get for every \(m\in\{0,\ldots,n\}\)
\[
\begin{aligned}
\mathbb P(A_n,M_n(t)=m)
&\le n!\bigl(C_{\varepsilon,t}K_{\varepsilon,\eta}\bigr)^n\\
&\quad\cdot \exp\left\{-\frac{(1-\eta)c}{2}
\bigl[(\beta-\varepsilon)m^2+(\alpha-\varepsilon)(n-m)^2\bigr]
+O_{\alpha,\beta,\varepsilon}(n)\right\}.
\end{aligned}\tag{9}
\]
Since \(\log n!=o(n^2)\), if \(m_n/n\to u\), (9) gives the corresponding upper bound in (1), after \(\eta\downarrow0\) and \(\varepsilon\downarrow0\).

### 3. A matching positive-probability rectangle

Fix any rational \(q>\varphi\). Choose \(h>0\) small enough that
\[
(1+h)(1+q)<q^2,\qquad 1+h<q.\tag{10}
\]
For each \(m\in\{0,\ldots,n\}\), prescribe a separated interval for the \(i\)-th ordered length:
\[
J_i=\left[tq^{i-m-1},\,t(1+h)q^{i-m-1}\right],\qquad1\le i\le n.\tag{11}
\]
Every choice \(x_i\in J_i\) is strictly increasing and satisfies \(x_i+x_{i+1}<x_{i+2}\). Exactly the first \(m\) choices lie below \(t\), apart from a probability-zero endpoint. Therefore the disjoint-permutation event that exactly one sample belongs to each \(J_i\) is contained in \(A_n\cap\{M_n(t)=m\}\), and its probability is
\[
n!\prod_{i=1}^n\int_{\log(J_i/t)}f_t(z)\,dz.\tag{12}
\]
The logarithmic intervals all have fixed width \(\log(1+h)>0\). By the lower inequality in (8), and the Lipschitz property of the piecewise-linear energy,
\[
\begin{aligned}
\log\mathbb P(A_n,M_n(t)=m)
&\ge -\frac{\log q}{2}
\left[(\beta+\varepsilon)m^2+(\alpha+\varepsilon)(n-m)^2\right]
-O_{\varepsilon,t,q,h}(n)+\log n!.
\end{aligned}\tag{13}
\]
For clarity, the leading quadratic terms arise from the exact arithmetic sums of exponents: \(\sum_{i=1}^{m}(m+1-i)=m(m+1)/2\) below the pivot and \(\sum_{i=m+1}^{n}(i-m-1)=k(k-1)/2\) above it. Both differ from the displayed squares only by linear terms. Here \(\log q\downarrow \log\varphi\) as \(q\downarrow\varphi\), while \(h\) may depend on \(q\) but is fixed **before** letting \(n\) increase. Dividing (13) by \(n^2\) and then taking \(\varepsilon\downarrow0\), \(q\downarrow\varphi\) proves the lower bound in (1).

### 4. Marginal exponent and conditional large deviations

Complete the square:
\[
\beta u^2+\alpha(1-u)^2
=\frac{\alpha\beta}{\alpha+\beta}
+(\alpha+\beta)\left(u-\frac\alpha{\alpha+\beta}\right)^2.\tag{14}
\]
Summing (9) over the at most \(n+1\) occupancy counts and using the lower bound (13) with \(m/n\to\alpha/(\alpha+\beta)\) establishes (2). Dividing (1) by (2) establishes the exact conditional logarithmic point probabilities:
\[
\lim_{n\to\infty}\frac1{n^2}\log\mathbb P(M_n(t)=m_n\mid A_n)
=-I(u),\qquad m_n/n\to u.\tag{15}
\]
The uniform bound (9) and compactness of \([0,1]\) imply the closed-set upper bound for the conditional large-deviation principle. For an open set, choose any \(u\) in it and a sequence \(m_n/n\to u\); (15) supplies the matching open-set lower bound. Thus (3) follows with a continuous good rate function on a compact space. Its unique minimizer gives (4).

## Verification

The standalone `check_two_tail.py` uses only the Python standard library. It checks the independent finite combinatorial consequences of (5), the occupancy-preserving ordered rational rectangles of (11), Fibonacci pair domination, and (14). It uses exact `fractions.Fraction` arithmetic for the certificate inequalities at \(q=13/8\) and \(h=1/1000\), across all \(3\le n\le37\), \(0\le m\le n\) and three rational pairs of tail slopes. Four further rational-probability lower-event calculations for an asymmetric log-Laplace model show convergence of the rectangular lower rate toward the predicted fixed-\(q\) coefficient. See `VERIFICATION.md` and replay with `python3 check_two_tail.py`.

The complete infinite-\(n\) result rests on the analytical bounds (7)–(15), not on finite enumeration, the diagnostic output, or numerical fitting.

## Relationship to prior work

Barczy and Lovas (2026) analyze the same no-three-triangles question for exponential and **one-sided Pareto type I** lengths, including exact finite-sample integral formulas. Their Pareto log-length distribution has no lower exponential log tail, so no finite positive \(\beta\) or two-sided conditional rank law is included. Brennan, Callow and Lin (2026) give a general-density integral representation and Fibonacci polygon formulas, but their general representation is not an evaluated two-tail quadratic large-deviation rate and has no conditional threshold-occupancy limit. Sudbury, Sun, Treeby and Wang (2026) derive a uniform-bounded finite-sample Fibonacci product. An indexed 2026 companion finding derives the \(-\alpha(\log\varphi)/2\) quadratic rate for **one-sided** Pareto samples; its full text could not be retrieved in the available access path, and it is compared at the level of its explicit published theorem summary. The finite-two-tail formula and the full conditional occupancy rate function are not implied by the published one-sided rate alone.

The shared Fibonacci obstruction and general integration identity are acknowledged as prior results. The asserted contribution is precisely the two-tail harmonic-mean sharp exponent together with the conditional rank large-deviation law; it is **not** the general reduction (5) or the Fibonacci growth bound.

## Limitations

The hypothesis is on the pointwise log-density slopes, a stronger requirement than merely asymptotic probability-tail exponents. The law is at logarithmic \(n^2\) accuracy: no finite-\(n\) exact probability, \(O(n\log n)\) remainder, prefactor, or local fluctuation central limit theorem is asserted. The conditioning statement holds for each fixed threshold independently; no uniformity in thresholds growing or shrinking with \(n\) is claimed. Beyond the inspected sources, a previously unlocated equivalent two-tail treatment remains a possible priority risk. Independent mathematical review has not been performed.

## References

1. M. Barczy and R. L. Lovas, *Pick-up sticks problems for exponential and Pareto distributions*, arXiv:2611.04436v1, first available 2026-11-03. https://arxiv.org/html/2611.04436v1
2. M. Brennan, N. Callow, and T. Cao Lin, *Fibonacci numbers and the probability of polygon formation using random length sticks*, arXiv:2604.27573v1, first available 2026-04-30; especially Section 3.3. https://arxiv.org/html/2604.27573v1
3. E. Sudbury, S. Sun, D. Treeby, and W. Wang, *Pick-up Sticks and the Fibonacci Factorial* (2026), DOI 10.1080/00150517.2026.2663981. https://doi.org/10.1080/00150517.2026.2663981
4. *Sharp quadratic decay for triangle-free Pareto stick samples* (indexed published theorem summary, first indexed 2026-11-08); a one-sided Pareto rate result, with full-text inspection unavailable.
