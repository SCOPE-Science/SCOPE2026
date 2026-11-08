# Sharp quadratic decay for triangle-free Pareto stick samples

## Finding

For integer \(n\ge3\), let \(X_1,\ldots,X_n\) be independent Pareto type-I lengths with scale \(s>0\) and shape \(\alpha>0\):
\[
\Pr(X_i>x)=(s/x)^\alpha\quad(x\ge s).
\]
Write \(A_n\) for the event that no three distinct sampled lengths form a nondegenerate triangle. Let \(\varphi=(1+\sqrt5)/2\), \(c=\log\varphi\) and \(b_n=c(n-1)(n-2)/2\). Then the following explicit two-sided bounds hold for every \(n\ge3\):
\[
\boxed{e^{-\alpha c n(n-1)/2}\le\Pr(A_n)\le e^{-\alpha b_n}\sum_{j=0}^{n-2}\frac{(\alpha b_n)^j}{j!}.}
\]
In particular, for each fixed \(\alpha>0\),
\[
\boxed{\lim_{n\to\infty}-\frac{2}{n^2}\log\Pr(A_n)=\alpha\log\varphi.}
\]
Equivalently, \(\log\Pr(A_n)=-\alpha(\log\varphi)n^2/2+O_\alpha(n\log n)\). Neither the bounds nor the limit depend on scale \(s\).

## Assumptions and scope

The result concerns exactly independent, identically distributed continuous Pareto type-I samples with the fixed (in \(n\)) parameters \(s,\alpha>0\). Any triple of positive lengths forms a nondegenerate triangle exactly when its largest length is strictly less than the sum of the other two. Tangential equality has probability zero under the sample law, but the event \(A_n\) is defined including the possible equality case in the *nontriangle* relation. The asymptotic takes \(n\to\infty\) with fixed \(\alpha\), not with a varying tail index. All finite-sample bounds hold for every \(n\ge3\).

## Proof

**1. Reduction to consecutive order statistics.** Write the ordered sample as \(X_{(1)}\le\cdots\le X_{(n)}\). The absence of a triangular triple is equivalent to
\[
X_{(i)}+X_{(i+1)}\le X_{(i+2)}\qquad(1\le i\le n-2).
\]
Necessity is immediate. For sufficiency, consider any indices \(i<j<k\). The sum of its two smaller lengths is at most \(X_{(k-2)}+X_{(k-1)}\), which is no larger than \(X_{(k)}\). Thus no such triple is triangular.

**2. Independent exponential logarithmic gaps.** Since \(\log(X_j/s)\) has exponential law of rate \(\alpha\), standard exponential order-statistic spacings imply that
\[
Y_i=\log\frac{X_{(i+1)}}{X_{(i)}}\quad(1\le i\le n-1)
\]
are independent with \(Y_i\sim\operatorname{Exp}(\alpha(n-i))\). The inequalities in Step 1 are therefore equivalent to
\[
Y_{i+1}\ge h(Y_i),\qquad h(y)=\log(1+e^{-y}),\qquad1\le i\le n-2.
\]
The map \(h\) is decreasing and strictly convex on the nonnegative half-line. It has the positive fixed point \(c=\log\varphi\), since \(1+1/\varphi=\varphi\), and \(h'(c)=-q\) for \(q=\varphi^{-2}\in(0,1)\).

**3. Deterministic weighted-energy lower bound on the event.** The tangent inequality for convex \(h\), together with Step 2, gives
\[
Y_{i+1}\ge h(Y_i)\ge c-q(Y_i-c),\qquad\text{or}\qquad Y_{i+1}+qY_i\ge(1+q)c.
\]
Summing the first \(m-1\) inequalities for any \(2\le m\le n-1\) yields
\[
(1+q)\sum_{i=1}^{m}Y_i-Y_1-qY_m\ge (m-1)(1+q)c.
\]
Since the gaps are nonnegative, \(\sum_{i=1}^mY_i\ge(m-1)c\); the same inequality is trivial for \(m=1\). Consequently, on \(A_n\), the weighted energy
\[
W_n=\sum_{i=1}^{n-1}(n-i)Y_i=\sum_{m=1}^{n-1}\sum_{i=1}^mY_i
\]
obeys
\[
W_n\ge c\sum_{m=1}^{n-1}(m-1)=\frac{c(n-1)(n-2)}2=b_n.
\]
The random variables \((n-i)Y_i\), \(1\le i\le n-1\), are independent rate-\(\alpha\) exponentials. Therefore \(W_n\) is gamma with integer shape \(n-1\) and rate \(\alpha\), and its exact survival function gives
\[
\Pr(A_n)\le\Pr(W_n\ge b_n)=e^{-\alpha b_n}\sum_{j=0}^{n-2}\frac{(\alpha b_n)^j}{j!}.
\]

**4. Explicit feasible subevent.** If every gap \(Y_i\ge c\), then, because \(h\) is decreasing, \(h(Y_i)\le h(c)=c\le Y_{i+1}\). This whole subevent is contained in \(A_n\). By independence,
\[
\Pr(A_n)\ge\prod_{i=1}^{n-1}\Pr(Y_i\ge c)=\exp\!\left[-\alpha c\sum_{i=1}^{n-1}(n-i)\right]
=e^{-\alpha c n(n-1)/2}.
\]

**5. Limiting sharp exponent.** With fixed \(\alpha,c>0\), \(b_n=\Theta(n^2)\). The elementary bound
\[
\sum_{j=0}^{n-2}\frac{(\alpha b_n)^j}{j!}\le(n-1)(1+\alpha b_n)^{n-2}
\]
shows that the logarithm of the gamma-tail polynomial is \(O_\alpha(n\log n)\). Thus the upper bound from Step 3 implies
\[
\log\Pr(A_n)\le-\alpha c(n-1)(n-2)/2+O_\alpha(n\log n).
\]
Step 4 supplies \(\log\Pr(A_n)\ge-\alpha c n(n-1)/2\). Divide both inequalities by \(-n^2/2\), reversing inequalities where necessary, and pass to the limit to obtain the stated \(\alpha\log\varphi\).

## Verification

The standalone standard-library program `CHECK.py` verifies the tangent relation on a finite grid, exhaustively checks the consecutive-triple equivalence on all nondecreasing integer multisets of lengths \(3\) through \(7\) with entries \(1\) through \(8\), tests weighted energy inequalities on constructed feasible gap paths, and checks finite-n bounds. It also computes two independent integral representations for the shape-one, \(n=3\) and \(n=4\) cases and compares them against direct Pareto Monte Carlo. It finishes with `PASS 23666 independent finite checks`. An independent symbolic integration gives
\[
\Pr(A_3)=2(1-\log 2),\qquad
\Pr(A_4)=2+26\log 2-18\log 3\qquad(\alpha=1).
\]
These finite checks establish no infinite-n limit on their own; the proof in Steps 1–5 does.

## Relationship to prior work

Sudbury, Sun, Treeby and Wang (2025, arXiv:2504.19911) give a Fibonacci-product **exact** probability for independently sampled **uniform** stick lengths. Brennan, Callow and Lin (2026, arXiv:2604.27573) extend the uniform polygon probabilities and provide integrals for arbitrary sampling laws, including unbounded distributions; their published integral framework contains the Pareto finite-n problem as a special case but does not evaluate its fixed-index large-n logarithmic rate. Barczy and Lovas (2026, arXiv:2611.04436v1, first posted November 3) give exact multidimensional integral representations for the Pareto case, using the same exponential-spacing or Beta-ratio representation; their Theorem 3.2 therefore already covers the **finite-n probability as an integral**. They give shape-index-specific n=3 evaluations. The distinct statement established here is the **explicit all-\(\alpha\) quadratic-rate constant** and **finite gamma-tail / feasible-subevent bounds**, which require a separate convex-geometric inequality and asymptotic squeeze. The earlier full-n integral expressions are acknowledged as significant stronger background coverage of the underlying distribution, not misrepresented as unrelated. A prior equivalent rate evaluation outside the checked literature remains possible.

## Limitations

The logarithmic-rate result gives a leading \(n^2\) exponent and an \(O_\alpha(n\log n)\) remainder, not an exact finite-n formula, a sharp subleading term, or a limit uniform over changing \(\alpha\). It does not cover other regularly varying distributions, dependent lengths, or avoidance of larger polygons. The exact integral formulas in recent papers provide additional finite-n information not claimed here. Historical novelty has only been assessed against the cited primary texts and the recorded searches and awaits independent assessment.

## References

1. A. Sudbury, A. Sun, D. Treeby, E. Wang, *Pick-up Sticks and the Fibonacci Factorial*, arXiv:2504.19911v1 (public April 28, 2025). https://arxiv.org/abs/2504.19911
2. M. Brennan, N. Callow, T. C. Lin, *Fibonacci numbers and the probability of polygon formation using random length sticks*, arXiv:2604.27573v1 (public April 30, 2026). https://arxiv.org/abs/2604.27573
3. M. Barczy, R. L. Lovas, *Pick-up sticks problems for exponential and Pareto distributions*, arXiv:2611.04436v1 (public November 3, 2026). https://arxiv.org/html/2611.04436v1
