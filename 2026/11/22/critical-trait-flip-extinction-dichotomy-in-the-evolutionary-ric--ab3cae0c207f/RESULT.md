# Critical trait-flip extinction dichotomy in the evolutionary Ricker map

## Finding

The evolutionary Ricker map of Luís and Ryals has a sharp, global contrast at the **simultaneous zero-intrinsic-growth and neutral trait-flip boundary**. Set \(\beta>0\), \(x_0>0\), \(y_0\in\mathbb R\), and iterate
\[
x_{n+1}=x_n\exp(-x_n-\beta y_n^2),\qquad
 y_{n+1}=(1-s)y_n+s x_n. \tag{1}
\]
For every \(0<s<2\), all such trajectories satisfy
\[
\frac1{x_n}=n+(\beta+\tfrac12)\log n+C+o(1),
\qquad \lim_{n\to\infty}n^2(y_n-x_n)=\frac1s. \tag{2}
\]
Here and below, \(C\in\mathbb R\) depends on the initial state and parameters.

At the exact boundary \(s=2\), the alternating amplitude
\[
A=y_0-2\sum_{j=0}^{\infty}(-1)^j x_j \tag{3}
\]
exists for **every** real initial trait. Its defining series is absolutely convergent when \(A\ne0\) and conditionally convergent when \(A=0\). There are exactly two alternatives:

* If \(A\ne0\), then \((-1)^n y_n\to A\) and a constant \(K\in(0,\infty)\) exists such that
\[
\lim_{n\to\infty}e^{\beta A^2 n}x_n=K. \tag{4}
\]
* If \(A=0\), then \(0<y_n<2x_n\) for every \(n\), and (2) holds with \(s=2\), notably
\[
\frac1{x_n}=n+(\beta+\tfrac12)\log n+C+o(1),
\qquad \lim_{n\to\infty}n^2(y_n-x_n)=\tfrac12. \tag{5}
\]

For each fixed \(x_0>0\), \(\beta>0\), there exists at least one \(y_0\in(0,2x_0)\) giving \(A=0\). Uniqueness of such an initial trait is **not** claimed. Thus at \(s=2\) both exponential extinction with persistent alternating phenotype and algebraic extinction with logarithmic clock occur, whereas at any fixed \(0<s<2\) every positive-population trajectory obeys the algebraic clock.

## Assumptions and scope

All statements concern the mathematically defined map (1) with zero growth exponent, \(\beta>0\), \(x_0>0\), \(y_0\in\mathbb R\), and \(0<s\le2\). No positivity assumption is imposed on the trait, which is allowed to change sign. The exponential rate in (4) is \(\beta A^2\); the prefactor \(K\) is strictly positive. The amplitude is a trajectory-defined quantity, not an independently specified model parameter. At \(s=2\), amplitude zero is an existentially nonempty slice, not a proved unique graph. The original 2024 article investigates positive intrinsic growth and a different range of adaptation rates, so the theorem is a boundary extension rather than a corollary of its stability theorems.

## Proof

**1. Monotone population, uniform bound.** Put \(\eta_n=x_n+\beta y_n^2>0\) and \(w_n=1/x_n\). By (1), \(x_{n+1}=x_ne^{-\eta_n}\in(0,x_n)\) and
\[
w_{n+1}-w_n=(e^{\eta_n}-1)/x_n\ge1.
\]
Consequently \(0<x_n\le (n+1/x_0)^{-1}\), which proves \(x_n\downarrow0\) and ensures convergence of every alternating series of the decreasing positive \(x_n\).

**2. Interior relaxation.** If \(0<s<2\), write \(q=1-s\), \(|q|<1\). The second equation is the contracting convolution
\[
y_n=q^ny_0+s\sum_{j=0}^{n-1}q^j x_{n-1-j}.
\]
Since \(x_n\to0\), it follows that \(y_n\to0\), so \(x_{n+1}/x_n\to1\). The latter ratio is subexponential in \(n\); splitting the convolution into indices \(j\le n/2\) and \(j>n/2\), with a geometric majorant on the first block and the uniform \(x_0\) bound on the second, yields \(y_n/x_n\to s\sum_{j\ge0}q^j=1\). To spell out the domination, for every small \(\epsilon>0\), eventually \(x_{k+1}\ge e^{-\epsilon}x_k\); take \(\epsilon\) with \(|q|e^\epsilon<1\). The finitely many early terms of the convolution are exponentially small relative to \(x_n\), since \(\log(1/x_n)=o(n)\).

It follows that \(\eta_n=x_n+O(x_n^2)\) and
\[
w_{n+1}-w_n=1+O(x_n).
\]
Combining this estimate with \(x_n\le(n+1/x_0)^{-1}\) gives \(w_n=n+O(\log n)\), hence \(x_n=n^{-1}+O(\log n/n^2)\). Set \(d_n=y_n-x_n\), so exactly
\[
d_{n+1}=q d_n+(x_n-x_{n+1}). \tag{6}
\]
As \(x_n-x_{n+1}=x_n^2+O(x_n^3)\), the contracting convolution in (6) yields \(d_n/x_n^2\to\sum_{j\ge0}q^j=1/s\), in particular \(y_n=x_n+O(x_n^2)\). Expanding the reciprocal increment one order further now gives
\[
w_{n+1}-w_n=1+(\beta+\tfrac12)x_n+O(x_n^2).
\]
The difference between this increment and \(1+(\beta+1/2)/(n+1)\) is summable, because \(x_n-(n+1)^{-1}=O(\log n/n^2)\). Summation and the harmonic-number asymptotic prove (2), including existence of a finite renormalized constant.

**3. Alternating amplitude at the flip boundary.** For \(s=2\), telescoping the trait equation gives
\[
(-1)^n y_n=y_0-2\sum_{j=0}^{n-1}(-1)^j x_j.
\]
The monotone alternating-series test and Step 1 prove (3). The exact tail identity is
\[
y_n=(-1)^n A+2\sum_{j=0}^{\infty}(-1)^j x_{n+j}. \tag{7}
\]
The positive alternating tail lies strictly between \(0\) and \(x_n\). This strictness follows from strict decrease of \(x_n\), grouping adjacent positive differences, and the fact that all terms are positive. Therefore \(|y_n-(-1)^nA|\le2x_n\). The convergence of (3) is **uniform** in \(y_0\) at fixed \(x_0\), since the tail is bounded by \(x_N\le(N+1/x_0)^{-1}\) uniformly in the initial trait. Each finite partial sum is continuous in \(y_0\); hence \(A\) is continuous. At \(y_0=0\) the alternating sum is strictly positive, so \(A<0\), while at \(y_0=2x_0\) that sum is strictly less than \(x_0\), so \(A>0\). The intermediate-value theorem proves existence of a zero in \((0,2x_0)\).

**4. Off-critical exponential branch.** If \(A\ne0\), (7) gives \(y_n=(-1)^nA+O(x_n)\). Thus \(x_{n+1}/x_n\to e^{-\beta A^2}<1\) and \(\sum_n x_n<\infty\). Also \(y_n^2-A^2=O(x_n)\), hence \(\sum_n|\eta_n-\beta A^2|<\infty\). Summing the exact identity \(\log x_{n+1}-\log x_n=-\eta_n\) proves (4) with \(K=x_0\exp[-\sum_n(\eta_n-\beta A^2)]>0\).

**5. The zero-amplitude critical branch.** If \(A=0\), the strict alternating bounds in (7) yield \(0<y_n<2x_n\). Consequently \(\eta_n=x_n+O(x_n^2)\), and the reciprocal argument in Step 2 gives \(x_n=n^{-1}+O(\log n/n^2)\). Define the bounded normalized trait mismatch \(p_n=y_n/x_n-1\in(-1,1)\). The exact recurrence and its two-step iterate are
\[
p_{n+1}=e^{\eta_n}(1-p_n)-1,\qquad
p_{n+2}=\frac{x_n}{x_{n+2}}p_n+b_n,
\quad b_n=e^{\eta_{n+1}}(2-e^{\eta_n})-1. \tag{8}
\]
Initially, \(y_n=O(x_n)\) implies \(\eta_{n+1}-\eta_n=O(x_n^2)\), so \(b_n=O(x_n^2)\). Iterating (8) *backwards* to time infinity is justified because \(|p_{n+2k}|<1\) while \(x_{n+2k}\to0\); it gives the convergent exact identity
\[
p_n=-\frac1{x_n}\sum_{j=0}^{\infty}x_{n+2j+2}b_{n+2j}. \tag{9}
\]
Since \(x_n\asymp1/n\), (9) implies \(p_n=O(1/n)\), so \(y_n=x_n+O(x_n^2)\). In particular, expanding (8) with \(x_{n+1}=x_n-x_n^2+O(x_n^3)\) gives
\[
b_n=-2x_n^2+O(x_n^3). \tag{10}
\]
The asymptotic sum \(\sum_{j\ge0}(n+2j)^{-3}\sim1/(4n^2)\) in (9) therefore yields \(np_n\to1/2\), equivalently \(n^2(y_n-x_n)\to1/2\). Finally \(y_n=x_n+O(x_n^2)\) reproduces exactly the summable reciprocal increment of Step 2, proving the finite logarithmically renormalized limit in (5). In this branch \(x_n\sim1/n\), so the alternating amplitude series converges only conditionally. In the nonzero-amplitude branch its absolute convergence follows from the geometric bound in Step 4. \(\square\)

## Verification

The accompanying `check.py` tests finite-step identities and reciprocal estimates on sample trajectories, including the two-step mismatch equation (8) and a finite-time approximation of the amplitude sign bracket. It is a diagnostic only. The strict alternating-tail bounds and infinite-time conclusions follow from the analytical argument above.

## Relationship to prior work

Luís and Ryals (2024) define the exact evolutionary Ricker map with the growth parameter \(\alpha>0\) and emphasize \(0<s<1\); their introduction cites positive-growth results for \(1<s<2\). The present theorem concerns \(\alpha=0\) and the critical trait flip \(s=2\), which are outside their stated theorem hypotheses. Classical alternating-series arguments, stable linear filters, and reciprocal-growth expansions are proof ingredients, not claims of novelty. Related results on symmetric Ricker competition, Ricker–Kolmogorov predator–prey dynamics, and Ricker–Beverton–Holt systems involve different nonlinear state equations and do not imply the critical-amplitude partition (3)–(5) for this evolutionary trait map.

## Limitations

The theorem is about the ideal deterministic map at zero intrinsic growth; it does not assert the biological validity of nonpositive intrinsic growth or the endpoint evolutionary response. The critical set \(A=0\) is proved nonempty, but its uniqueness, regularity and basin geometry are not classified. The result makes no statements about \(s>2\), perturbations, positive intrinsic growth, or finite-precision simulation. No independent mathematical audit has been performed. General-purpose methods are classical, so independently rediscovered or unindexed equivalent specializations remain a publication-priority risk.

## References

1. R. Luís and B. Ryals, *Invariant Sets, Global Dynamics, and the Neimark–Sacker Bifurcation in the Evolutionary Ricker Model*, Symmetry **16** (2024), 1139, published 2024-09-02, https://doi.org/10.3390/sym16091139.
2. *Discrete evolutionary population models: a new approach*, Journal of Biological Dynamics (2020), https://doi.org/10.1080/17513758.2020.1772997.
3. Related mathematical literature: recent analyses of neutral symmetric Ricker competition and Ricker–Kolmogorov predator–prey maps, whose different state equations do not cover the result above.
