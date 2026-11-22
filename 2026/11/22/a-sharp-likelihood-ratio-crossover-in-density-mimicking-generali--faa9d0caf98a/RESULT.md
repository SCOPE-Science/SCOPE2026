# A sharp likelihood-ratio crossover in density-mimicking generalized half-logistic counts

## Finding

Consider the density-mimicking generalized half-logistic count family introduced in §5 of Barbiero and Hitaj (2024). With shape \(\alpha>0\), rate \(\theta>0\), and integer \(n\ge0\), its mass is
\[
p_{\alpha,\theta}(n)=\frac{w_{\alpha,\theta}(n)}{Z_{\alpha,\theta}},\qquad
w_{\alpha,\theta}(n)=\frac{e^{-\alpha\theta n}}{(1+e^{-\theta n})^{\alpha+1}},\qquad
Z_{\alpha,\theta}=\sum_{j=0}^{\infty}w_{\alpha,\theta}(j).
\]

**Theorem (complete rate-likelihood-ratio phase diagram).** Fix \(\alpha>0\) and two rates \(0<a<b\). Define
\[
H_{a,b}=\log\frac{1+e^{-a}}{1+e^{-b}},\qquad
c(a,b)=\frac{H_{a,b}}{b-a-H_{a,b}}\in(0,1).
\]
The ratio \(R_n=p_{\alpha,b}(n)/p_{\alpha,a}(n)\) is nonincreasing for every nonnegative integer \(n\) **if and only if** \(\alpha\ge c(a,b)\). It decreases strictly at every step for \(\alpha>c(a,b)\). At equality the first two values tie, \(R_0=R_1\), and every later step decreases strictly. For \(0<\alpha<c(a,b)\), the sequence of likelihood ratios rises strictly from index zero and thereafter has **one and only one transition** from rising to falling; at that transition, two adjacent maxima may tie, but there is no second increase. Thus failure of monotone likelihood ratio does not permit multiple separate ratio peaks.

More precisely, the rate phase diagram at fixed shape is:

* If \(\alpha\ge1\), every pair \(0<a<b\) has decreasing likelihood ratio.
* If \(0<\alpha<1\) and \(a\ge\log(1/\alpha)\), every \(b>a\) has decreasing likelihood ratio.
* If \(0<\alpha<1\) and \(0<a<\log(1/\alpha)\), there is a **unique** \(b_*(a,\alpha)>a\) solving
  \[
  \log\frac{1+e^{-a}}{1+e^{-b_*}}=
  \frac{\alpha}{1+\alpha}(b_*-a).
  \]
  For \(a<b<b_*\) the ratio has the single interior peak described above, at \(b=b_*\) it has the initial tie, and for \(b>b_*\) it decreases strictly. In particular, a small rate increase can fail likelihood-ratio order, while a larger rate increase restores it.

The same family has an exact modal staircase. For \(\theta>0\), set
\[
h_n(\theta)=\log\frac{1+e^{-\theta n}}{1+e^{-\theta(n+1)}},\qquad
A_n(\theta)=\frac{h_n(\theta)}{\theta-h_n(\theta)}\quad(n\ge0).
\]
Then \(A_0>A_1>\cdots>0\) and \(A_n\downarrow0\). Its unique mode is at zero when \(\alpha>A_0\); for each integer \(k\ge1\) its unique mode is \(k\) exactly when \(A_k<\alpha<A_{k-1}\). At \(\alpha=A_k\) the only modes are \(k,k+1\). All masses are strictly log-concave for every admissible \(\alpha,\theta\). These modal statements are included to give the full shape interpretation of the same likelihood-ratio crossover.

For an exact witness, take \(\alpha=1/4\), \(a=\log2\), \(b=\log4\). Then the normalization-free ratio satisfies
\[
\left(\frac{R_1}{R_0}\right)^4=\frac{(6/5)^5}{2}>1,\qquad
\left(\frac{R_2}{R_1}\right)^4=\frac{(50/51)^5}{2}<1.
\]
It is nonmonotone with its unique maximum at index one; with the same shape and first rate, every second rate \(b>b_*\approx2.1900927766\) instead gives strictly decreasing likelihood ratio.

## Assumptions and scope

All rates and shapes are strictly positive and finite; the support is the entire \(\mathbb N_0\). Rate is the reciprocal of the conventional scale, so the order in the theorem is specifically the decreasing likelihood ratio of the higher-**rate** law relative to the lower-rate law. A likelihood-ratio order means that \(p_{\alpha,b}(n)/p_{\alpha,a}(n)\) is nonincreasing over **every** nonnegative integer, not only over an observed or truncated range. The two-rate theorem keeps \(\alpha\) fixed. The modal theorem keeps \(\theta\) fixed. No claims are made for mixed simultaneous variation of both parameters, for a survival-preserving discretization, or for the continuous generalized half-logistic model.

Normalization is well-defined: \(0<w_{\alpha,\theta}(n)\le e^{-\alpha\theta n}\), hence \(0<Z_{\alpha,\theta}<\infty\). Strict positivity of the mass makes every likelihood ratio well-defined.

## Proof

**Step 1: exact adjacent ratios.** Put \(\ell_\theta(x)=\log(1+e^{-\theta x})\). Direct cancellation of the common normalizer gives
\[
\log\frac{p_{\alpha,\theta}(n+1)}{p_{\alpha,\theta}(n)}=
-\alpha\theta+(\alpha+1)[\ell_\theta(n)-\ell_\theta(n+1)]
=-\alpha\theta+(\alpha+1)h_n(\theta).
\tag{1}
\]
Since \(\ell_\theta''(x)=\theta^2e^{\theta x}/(1+e^{\theta x})^2>0\), its unit-step decrements \(h_n\) decrease strictly with \(n\). Also \(0<h_n<\theta\) and \(h_n\to0\). The increments in (1) therefore strictly decrease to \(-\alpha\theta\), proving strict discrete log-concavity and the stated exact modal thresholds, with the tie convention following from a zero adjacent log ratio. This proves the modal part including every boundary and integer index.

**Step 2: the rate comparison.** Let \(a<b\), \(\Delta=b-a\), and for \(x\ge0\) define
\[
F(x)=\ell_a(x)-\ell_b(x)
=\log\frac{1+e^{-ax}}{1+e^{-bx}}.
\]
Then \(F(0)=0\), \(F(x)>0\) for \(x>0\), \(F(x)\to0\) as \(x\to\infty\), and
\[
F(x)=\int_a^b\frac{x}{1+e^{tx}}\,dt,
\qquad
\log\frac{R_{n+1}}{R_n}
=-\alpha\Delta+(\alpha+1)[F(n+1)-F(n)].
\tag{2}
\]
Write \(d(x)=F(x+1)-F(x)\), and \(t_\alpha=\alpha\Delta/(1+\alpha)>0\). Then (2) has the sign of \(d(n)-t_\alpha\). In particular \(d(0)=F(1)=H_{a,b}>0\).

**Step 3: a one-crossing lemma for positive forward increments.** Differentiation gives
\[
F''(x)=\frac{a^2}{4\cosh^2(ax/2)}-\frac{b^2}{4\cosh^2(bx/2)}.
\tag{3}
\]
The ratio \(\cosh(bx/2)/\cosh(ax/2)\) increases strictly from one to infinity for \(x>0\), because the derivative of its logarithm is \([b\tanh(bx/2)-a\tanh(ax/2)]/2>0\). Thus (3) changes sign exactly once, from negative to positive, at a point \(x_0>0\). Since \(F'(0)=\Delta/2>0\) and \(F'(x)\to0\) from below, \(F'\) has precisely one zero \(m\in(0,x_0)\): it is strictly decreasing until \(x_0\), strictly increasing thereafter, with a negative minimum. Consequently \(F\) strictly increases up to \(m\) and strictly decreases thereafter.

Now whenever \(d(x)>0\), the strict decrease of \(F\) on \([m,\infty)\) forces \(x<m\), hence \(F'(x)>0\). If \(x+1\le x_0\), strict decrease of \(F'\) yields \(F'(x+1)<F'(x)\). If \(x+1>x_0\), then \(F'(x+1)<0<F'(x)\). In both cases
\[
d'(x)=F'(x+1)-F'(x)<0\quad\text{whenever }d(x)>0.
\tag{4}
\]
For clarity, the second case includes \(x+1>x_0\) because \(F'(y)<0\) holds for all \(y>m\), and \(x_0>m\). Since \(d(0)>0\), while \(d(x)<0\) for all \(x\ge m\), continuity and (4) imply that each level \(t>0\) strictly below \(d(0)\) is crossed exactly once, downward. The special level \(d(0)\) is attained at the initial point only. At all integer steps following the crossing, \(d(n)<t\). This is an infinite-index argument, not a finite numerical sign scan.

**Step 4: sharpness and tie behavior.** The first step in (2) is nonpositive exactly when
\[
(1+\alpha)H_{a,b}\le\alpha\Delta
\iff\alpha\ge c(a,b)=\frac{H_{a,b}}{\Delta-H_{a,b}}.
\]
By the one-crossing lemma, this condition is **sufficient for every later step**; if it fails, the very first likelihood-ratio step increases, so it is also necessary. If equality holds, (4) and strict decrease from the positive starting value give \(d(n)<d(0)\) for all \(n\ge1\), hence strict later decrease. When \(\alpha<c(a,b)\), the level \(t_\alpha\in(0,d(0))\) is crossed exactly once. Therefore the positive steps form a nonempty initial consecutive segment and all later steps are negative, with at most one zero step at the transition. The likelihood-ratio sequence has precisely the asserted single-peaked pattern, including a possible adjacent tie. As \(n\to\infty\), (2) tends to \(-\alpha\Delta<0\), so the declining segment is nonempty.

**Step 5: the unique two-rate crossover.** At \(x=1\), the integral in step 2 reads
\[
\frac{H_{a,b}}{\Delta}=\frac{1}{b-a}\int_a^b g(t)\,dt,
\qquad g(t)=\frac1{1+e^t}.
\tag{5}
\]
Since \(g\) decreases strictly and lies strictly between zero and one half for \(t>0\), this average lies in \((0,1/2)\). This proves \(0<c(a,b)<1\). For fixed \(a\), its average over \([a,b]\) decreases strictly with \(b\), with limits \(g(a)\) as \(b\downarrow a\) and zero as \(b\to\infty\) (the integral to infinity converges). As \(c=s/(1-s)\), it follows that \(c(a,b)\) decreases strictly from \(e^{-a}\) to zero. Therefore at fixed \(0<\alpha<1\), if \(a\ge\log(1/\alpha)\), every \(b>a\) has \(c(a,b)<\alpha\); otherwise \(c(a,b)=\alpha\) has exactly one root \(b_*>a\) and the three claimed phases follow. If \(\alpha\ge1\), the strict bound \(c(a,b)<1\) applies to every pair. This completes the proof.

**Step 6: exact witness.** For \(a=\log2,b=\log4\), one has \(\Delta=\log2\), \(F(1)=\log(6/5)\), and \(F(2)-F(1)=\log(50/51)\). Substituting \(\alpha=1/4\) in (2) and raising the positive ratios to the fourth power yields the two rational inequalities displayed in the finding. In particular, there is no appeal to floating-point signs or unknown normalizing constants. The unique rate \(b_*\) is the exact implicit solution of the equation in the theorem; its decimal is for orientation only.

## Verification

The package includes `verification/check.py`. It is a standalone, standard-library Python program checking: (a) exact rational likelihood-ratio steps at the specified witness; (b) the location of modes, strict log-concavity at numerically safe indices, and positive normalizers with explicit geometric tail bounds on selected parameter slices; (c) sign patterns of adjacent likelihood ratios on a finite grid; and (d) the claimed restoration of likelihood-ratio monotonicity at larger rate. The program was executed successfully in the delivered package. Its finite checks corroborate, but do **not** replace, the all-index proofs in Steps 1–5.

To reproduce, extract all embedded files preserving their paths and run:

```sh
python3 verification/check.py
```

## Relationship to prior work

Barbiero and Hitaj (2024a, first public 6 April 2024), §5, **defines** this density-mimicking two-parameter law and notes that its mode need not be at zero. It does not provide the rate likelihood-ratio threshold, the one-turn property, the unique restoration rate, or the exact modal-cutoff formulas derived here. Its §2–4 theorems concern the **one-parameter** model. Barbiero and Hitaj (2024b, 19 January 2024), §4, studies a distinct **survival-preserving** type-I generalized discrete half-logistic law, whose probabilities are differences of exponentiated half-logistic cdf values rather than density samples; its modal and log-concavity findings do not imply the present claims. Classical likelihood-ratio order and its implication for stochastic order are standard and not asserted to be new. Searches of relevant distribution, likelihood-ratio, and generalized half-logistic literature found no statement dominating the sharp rate-dependent phase diagram; this is a best-knowledge priority statement rather than a proof of uniqueness in all literature.

## Limitations

The theorem addresses fixed-shape changes in **rate** only, not simultaneous changes of shape and rate. The sharp phase condition describes monotone likelihood-ratio ordering; its failure does not by itself imply the failure of ordinary stochastic ordering. The generalized density-sampling law differs from the survival-preserving type-I law and from the continuous parent. The mode and likelihood-ratio conclusions hold for all admissible positive real parameters analytically; reported decimal values and finite checker grids are not substitutes for the proof. Historical priority is provisional pending broader independent scholarly review. Independent verification and external mathematical audit have not been performed.

## References

1. A. Barbiero and A. Hitaj, *A Discrete Version of the Half-Logistic Distribution Based on the Mimicking of the Probability Density Function*, Journal of the Indian Society for Probability and Statistics 25 (2024), 373–394, first published 6 April 2024, §5. https://doi.org/10.1007/s41096-024-00185-w ; open full article: https://link.springer.com/article/10.1007/s41096-024-00185-w .
2. A. Barbiero and A. Hitaj, *Discrete half-logistic distributions with applications in reliability and risk analysis*, Annals of Operations Research 340 (2024), 27–57, first published 19 January 2024, §4 (different survival-preserving type-I generalized law). https://doi.org/10.1007/s10479-023-05807-3 ; open full article: https://link.springer.com/article/10.1007/s10479-023-05807-3 .
3. M. Shaked and J. G. Shanthikumar, *Stochastic Orders*, Springer, 2007 (background definitions of likelihood-ratio order; no family-specific priority claim). https://doi.org/10.1007/978-0-387-34675-5 .
