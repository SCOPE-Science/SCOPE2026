# Later first collisions favor rarer labels: a strict likelihood-ratio law

## Finding

In the nonuniform birthday problem, the type causing the *first* repeated observation systematically shifts toward rarer types as that first repeat is delayed. This holds for every finite strictly positive probability vector, with a strict monotone likelihood-ratio (MLR) comparison between all consecutive possible collision times.

**Theorem.** Let \(m\ge2\), let \(p_1,\ldots,p_m>0\) with \(\sum_i p_i=1\), and independently sample \(Y_1,Y_2,\ldots\) with \(\Pr(Y_t=i)=p_i\). Write
\[
T=\min\{t\ge2:Y_t\in\{Y_1,\ldots,Y_{t-1}\}\},\qquad J=Y_T.
\]
For each index \(i\), let \(p_{-i}\) denote the list of all probabilities except \(p_i\), and write \(e_s\) for its degree-\(s\) elementary symmetric polynomial. Then, for every \(2\le t\le m+1\),
\[
\Pr(T=t,J=i)=(t-1)!p_i^2 e_{t-2}(p_{-i}).
\]
For every pair of labels with \(p_i>p_j\) and every \(2\le t\le m\),
\[
\frac{\Pr(J=i\mid T=t+1)}{\Pr(J=j\mid T=t+1)}
<\frac{\Pr(J=i\mid T=t)}{\Pr(J=j\mid T=t)}.
\]
Equality holds in the pairwise comparison if \(p_i=p_j\). Accordingly, when category labels are ordered by their probabilities, the conditional collision-label law strictly shifts toward rarer categories in MLR order as the collision time grows.

For every strictly increasing real function \(f\) on collision times and every strictly increasing real function \(g\) on the distinct probability values, a nonuniform probability vector satisfies
\[
\operatorname{Cov}(f(T),g(p_J))<0.
\]
If all probabilities are equal, \(T\) and \(J\) are independent and these covariances are zero. In fact, \(T\) and \(J\) are independent *only* for the uniform vector. The two extreme conditional laws illustrate the full-order transition:
\[
\Pr(J=i\mid T=2)=\frac{p_i^2}{\sum_j p_j^2},\qquad
\Pr(J=i\mid T=m+1)=p_i.
\]

## Assumptions and scope

This theorem concerns i.i.d. sampling with replacement from a **finite** support of at least two categories, each having strictly positive mass. \(T\) is the draw *on which the first duplicate occurs* (not the number of distinct categories before it), and \(J\) denotes the type repeated on that draw (not the preceding distinct type). Since the support has size \(m\), \(T\in\{2,\ldots,m+1\}\); each value and each joint cell \(\{T=t,J=i\}\) has positive probability. We use \(e_0=1\), \(e_s=0\) when \(s<0\) or \(s\) exceeds the number of variables. The MLR assertion concerns the ordered values of \(p_i\), allowing tied probabilities.

## Proof

**1. Exact joint law.** On \(\{T=t,J=i\}\), the first \(t-1\) draws are distinct and contain \(i\) exactly once; the final draw equals \(i\). Choose the remaining \(t-2\) distinct labels from the other \(m-1\) labels and order the \(t-1\) distinct labels arbitrarily. The resulting total probability is
\[
(t-1)!\,p_i^2\sum_{B\subseteq\{1,\ldots,m\}\setminus\{i\},\,|B|=t-2}\prod_{j\in B}p_j
=(t-1)!p_i^2e_{t-2}(p_{-i}).
\]

**2. Strict pairwise MLR comparison.** Fix \(i\ne j\) with \(p_i>p_j\), and remove both masses to form a list \(q\) with \(r=m-2\) positive entries. Put \(a_s=e_s(q)\), with \(a_{-1}=a_{r+1}=0\). For \(s=t-2\),
\[
\frac{\Pr(T=t,J=i)}{\Pr(T=t,J=j)}
=\frac{p_i^2}{p_j^2}
\frac{a_s+p_ja_{s-1}}{a_s+p_ia_{s-1}},
\qquad 0\le s\le r+1.
\]
All denominators are positive. For adjacent \(s\) the cross-product difference of the two fractions on the right (the earlier fraction minus the later one after cross multiplication) is precisely
\[
(p_i-p_j)(a_s^2-a_{s-1}a_{s+1})>0.
\]
For \(s=0\) and \(s=r\), this is immediate from the positive endpoint elementary symmetric polynomials and the zero conventions. For \(1\le s\le r-1\), Newton's inequalities for positive variables yield \(a_s^2>a_{s-1}a_{s+1}\). In more detail, the normalized sequence \(a_s/\binom rs\) is log-concave, and \(\binom rs^2>\binom r{s-1}\binom r{s+1}\), with all interior \(a_s\) positive. This proves the strict comparison for every consecutive time. For \(p_i=p_j\), symmetry makes the ratio equal to one at every time.

**3. Increasing-transform covariance and uniformity.** The preceding pairwise comparison is the finite ordered-support MLR condition: for later \(t\), the distribution of the scalar \(p_J\) shifts toward smaller values. It implies that \(h(t)=\mathbb E[g(p_J)\mid T=t]\) is strictly decreasing when the vector is not uniform and \(g\) strictly increases on its distinct masses. For an independent copy \(T'\),
\[
2\operatorname{Cov}(f(T),g(p_J))
=\mathbb E\big[(f(T)-f(T'))(h(T)-h(T'))\big]<0,
\]
because \(T\) has every support point with positive probability. If the masses are uniform, label exchangeability gives independence of \(J\) and \(T\). Conversely the extreme conditional distributions follow by setting \(t=2\) and \(t=m+1\) in the joint formula. If \(J\) were independent of \(T\), they would coincide, forcing \(p_i^2/\sum_jp_j^2=p_i\) for every \(i\); positivity forces all \(p_i\) equal. This completes the proof.

## Verification

The attached self-contained Python 3 program `verify.py` independently enumerates all ordered distinct prefixes before a first repeat, and separately computes the elementary-symmetric formula. It checks every exact joint cell, normalization, both endpoint distributions, strict pairwise MLR minors including equal-mass cases, strict conditional mean decay, and the negative covariance law. In the packaged execution, **2,235 exact rational assertions passed** across **25 positive probability vectors** with support sizes two through six. These finite checks are corroborative only; all-size statements follow from the proof and Newton's inequalities.

For example, at probabilities \((1/2,1/3,1/6)\), the conditional collision-label law changes from \((9/14,4/14,1/14)\) at \(T=2\), through \((27/48,16/48,5/48)\) at \(T=3\), to \((1/2,1/3,1/6)\) at \(T=4\).

## Relationship to prior work

The exact symmetric-polynomial machinery underlying the first-repeat waiting time is classical. Camarri and Pitman [1] give the nonuniform first-repeat distribution and the set-valued first-repeat law (equations (1) and (13)); marking the repeated element yields the present elementary joint formula. Flajolet, Gardy and Thimonier [2] give a general birthday/coupon framework and derive expectations by elementary symmetric functions. Fadnavis [3] studies nonuniform noncollision probabilities and Schur-concavity. None of the inspected portions provides the **pairwise strict conditional likelihood-ratio order** in the *identity* of the first repeated category, or the consequent independence characterization; those are the distinct claims assessed here. A source that records only waiting times or observed sets does not itself state these conditional ordering consequences.

## Limitations

The result does not cover zero-mass labels, dependent draws, countably infinite support, or repeat thresholds greater than two. Although the exact identity is elementary and follows from earlier nonuniform birthday machinery, priority for the MLR ordering cannot be certified exhaustively from the literature accessible for this assessment. The full text of Holst's 1995 article [4] was inaccessible; its abstract concerns waiting-time distribution rather than the collision-label order. Some other older recurrence and birthday literature might implicitly contain a related inequality. No claim of independent external validation is made.

## References

1. Michael Camarri and Jim Pitman, *Limit distributions and random trees derived from the birthday problem with unequal probabilities*, University of California, Berkeley, Statistics Technical Report 523, dated June 1, 1998; *Electronic Journal of Probability* 5 (2000), paper 2. https://statistics.berkeley.edu/tech-reports/523; open PDF https://www.maths.tcd.ie/EMIS/journals/EJP-ECP/article/download/58/58-115-1-PB.pdf.
2. Philippe Flajolet, Danièle Gardy and Loys Thimonier, *Birthday paradox, coupon collectors, caching algorithms and self-organizing search*, INRIA Research Report RR-0720 (1987); later journal version *Discrete Applied Mathematics* 39 (1992), 207–229. https://inria.hal.science/inria-00075832v1; scanned full report https://ftpmirror.your.org/pub/misc/bitsavers/pdf/stanford/Stanford_CS_TR_Collection_2025-12-12/PDF/pdf/RR-0720-ocr.pdf.
3. Sukhada Fadnavis, *A generalization of the birthday problem and the chromatic polynomial*, arXiv:1105.0698 (first submitted May 3, 2011). https://arxiv.org/abs/1105.0698.
4. Lars Holst, *The general birthday problem*, *Random Structures & Algorithms* 6 (1995), 201–208. https://doi.org/10.1002/rsa.3240060207.
