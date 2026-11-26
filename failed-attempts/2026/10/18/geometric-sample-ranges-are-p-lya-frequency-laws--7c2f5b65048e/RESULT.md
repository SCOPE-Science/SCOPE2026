# Geometric sample ranges are Pólya-frequency laws

## Finding
For an integer \(n\ge 2\) and \(0<q<1\), let \(X_1,\ldots,X_n\) be independent with \(\Pr(X_i=k)=(1-q)q^k\) for integers \(k\ge0\), and put \(R_n=\max_iX_i-\min_iX_i\). For a permutation \(\pi\in\mathfrak S_n\), let \(D(\pi)=\{j:1\le j<n,\ \pi_j>\pi_{j+1}\}\), \(d(\pi)=|D(\pi)|\) and \(c(\pi)=\sum_{j\in D(\pi)}(n-j)\). Define the explicit \(q\)-Eulerian polynomial
\[
 A_n(z,q)=\sum_{\pi\in\mathfrak S_n}z^{d(\pi)}q^{c(\pi)}.
\]
Then for \(|z|<1/q\),
\[
 \boxed{\quad\mathbb E[z^{R_n}]=\frac{(1-q)^n A_n(z,q)}{(1-q^n)\prod_{j=1}^{n-1}(1-q^jz)}.\quad}
\]
All \(n-1\) roots of \(A_n(\cdot,q)\), counted with multiplicity, are strictly negative. Consequently there exist \(\lambda_1,\ldots,\lambda_{n-1}>0\) such that \(A_n(z,q)=\prod_{j=1}^{n-1}(1+\lambda_jz)\), and an exact equality in distribution holds:
\[
 \boxed{\quad R_n\ \stackrel{d}{=}\ \sum_{j=1}^{n-1}B_j+\sum_{j=1}^{n-1}G_j,\quad}
\]
where the \(2(n-1)\) summands are mutually independent, \(B_j\) is Bernoulli with success probability \(\lambda_j/(1+\lambda_j)\), and \(\Pr(G_j=k)=(1-q^j)(q^j)^k\) for \(k\ge0\). Therefore the probability sequence \((\Pr(R_n=k))_{k\ge0}\) is Pólya-frequency of every order (PF\(\infty\)): all minors of its infinite lower-triangular Toeplitz matrix are nonnegative. In particular, it is log-concave and has no internal zeros.

## Assumptions and scope
The variables are identically distributed, independent, integer-valued, and geometric on the nonnegative integers. The sample size is a fixed finite integer \(n\ge2\); there is no random-sample-size or heterogeneous-parameter assertion. The open restriction \(0<q<1\) ensures a nondegenerate full-support parent. The formula and factorization concern ordinary probability generating functions, not formal analytic continuation beyond poles.

## Proof
**1. Sort each outcome with deterministic tie-breaking.** For each vector of observed values, order its indices as \(\pi_1,\ldots,\pi_n\) so that the values increase, breaking any tie by increasing index. Set \(a_0=X_{\pi_1}\) and \(a_j=X_{\pi_{j+1}}-X_{\pi_j}\) for \(1\le j<n\). The tie rule forces \(a_j\ge1\) whenever \(j\in D(\pi)\), and \(a_j\ge0\) otherwise. Conversely, every permutation and every such sequence of gap integers gives precisely one outcome vector, since a zero gap is possible only when the two adjacent labels are increasing. The total observed value and sample range are
\[
 \sum_{i=1}^nX_i=na_0+\sum_{j=1}^{n-1}(n-j)a_j,\qquad R_n=\sum_{j=1}^{n-1}a_j.
\]
For a fixed permutation, the probability generating sum is the product of elementary geometric series:
\[
 \begin{aligned}
 &(1-q)^n\sum_{a_0\ge0}\!q^{na_0}\prod_{j=1}^{n-1}\sum_{a_j\ge\mathbf 1_{\{j\in D(\pi)\}}}\!(q^{n-j}z)^{a_j}\\
 &\hspace{10mm}=\frac{(1-q)^n}{(1-q^n)\prod_{j=1}^{n-1}(1-q^{n-j}z)}\,q^{c(\pi)}z^{d(\pi)}.
 \end{aligned}
\]
Summing over permutations proves the displayed probability generating function. The series converge absolutely for \(|z|<1/q\).

**2. Real zeros and normalization.** Savage and Visontai, Theorem 5.4, prove for all positive \(q\) that the \(q\)-Eulerian polynomial defined by exactly the descent and comajor-index statistics above has only real roots. Our polynomial has constant coefficient \(1\), positive coefficients in every degree up to \(n-1\), and positive leading coefficient \(q^{n(n-1)/2}\). Hence none of its real roots is zero or positive: write \(A_n(z,q)=\prod_{j=1}^{n-1}(1+\lambda_jz)\) with \(\lambda_j>0\). The generating function has value \(1\) at \(z=1\), since the disjoint sorted-tuple classes exhaust all outcomes. Equivalently,
\[
 A_n(1,q)=\frac{(1-q^n)\prod_{j=1}^{n-1}(1-q^j)}{(1-q)^n}.
\]
Insert this identity and the root factorization into the first formula:
\[
 \mathbb E[z^{R_n}]=\prod_{j=1}^{n-1}\frac{1+\lambda_jz}{1+\lambda_j}\ \prod_{j=1}^{n-1}\frac{1-q^j}{1-q^jz}.
\]
Each factor is a normalized probability generating function of the Bernoulli or geometric variable specified in the finding, proving the independent-summand representation.

**3. Pólya-frequency conclusion.** The Toeplitz matrix of the two-point sequence with generating polynomial \(1+\lambda z\) (after normalization) is a nonnegative lower-bidiagonal matrix: all its minors are nonnegative. The Toeplitz matrix of \(((1-t)t^k)_{k\ge0}\), \(0<t<1\), has entries \((1-t)t^{i-j}\mathbf1_{\{i\ge j\}}\) and is totally nonnegative (the elementary one-sided geometric Toeplitz kernel). Convolution of sequences corresponds to multiplication of their lower-triangular Toeplitz matrices, and Cauchy–Binet preserves nonnegativity of every finite minor. The preceding independent-summand factorization therefore makes the range sequence PF\(\infty\). Its distribution has positive mass at every nonnegative integer, so the adjacent \(2\times2\) minors give ordinary log-concavity with no internal zeros.

## Verification
A separate exact-rational checker, `geometric_range_check.py`, computes the permutation polynomial from its defining sum, evaluates the rational generating-function coefficients, and compares them against a second expression obtained by summing over the sample minimum:
\[
 \Pr(R_n\le r)=\frac{(1-q^{r+1})^n-q^n(1-q^r)^n}{1-q^n}\quad(r=0,1,2,\ldots).
\]
For every \(2\le n\le7\), at \(q\in\{1/2,1/3,2/5,4/5\}\), it checks 11 initial probabilities and exact normalization, totaling 288 rational comparisons. The program printed `PASS 288 exact coefficient/normalization checks; counterexample discriminant -15`. This finite test is corroboration only; the proof of the theorem is the general sorted-tuple bijection together with Savage–Visontai real-rootedness and Toeplitz closure.

The special assumption on the geometric parent is substantive. For example, if \(X_1,X_2\) are iid \(\operatorname{Bin}(3,1/2)\), their range has the polynomial
\[
 \mathbb E[z^{|X_1-X_2|}]=\frac{10+15z+6z^2+z^3}{32}=\frac{(1+z)(10+5z+z^2)}{32}.
\]
The quadratic factor has discriminant \(-15\); thus, although the binomial parent itself is PF\(\infty\), its two-observation range is not. In particular the theorem is not an unqualified preservation principle for ranges of arbitrary PF\(\infty\) parents.

## Relationship to prior work
Badiella, del Castillo, and Puig (2023), Theorem 2, establish log-concavity and ultra-log-concavity of **order statistics**, not total positivity of the **difference of the extreme order statistics**. Savage and Visontai (2013 preprint version, Theorem 5.4) establish the real-rootedness of the comajor-index \(q\)-Eulerian numerator as a combinatorial theorem; that ingredient is used here as a published theorem, not claimed as new. The new identification is the exact law of the geometric sample **range** with this numerator and the ensuing Bernoulli–geometric convolution and PF\(\infty\) distributional conclusion. Pitman and Yakubovich (2017) examine geometric gaps for samples from a random GEM environment; their random-environment model is not the fixed geometric iid parent used here.

## Limitations
The positivity and factorization conclusions use Savage–Visontai's known real-rootedness theorem and do not independently reprove it. They do not imply that arbitrary discrete-order-statistic differences, non-geometric ranges, or geometric-parent ranges under dependence are PF\(\infty\). Numeric checks cover finitely many instances, not the proof's infinite quantifiers. A previously unlocated explicit sample-range version of the Eulerian/P-partition identity remains a bibliographic possibility; independent external validation has not been performed.

## References
1. L. Badiella, J. del Castillo, P. Puig, *Ultra log-concavity of discrete order statistics*, Statistics & Probability Letters **201** (2023), 109900; DOI 10.1016/j.spl.2023.109900 (first online 26 June 2023), especially Theorem 2.
2. C. D. Savage, M. Visontai, *The s-Eulerian polynomials have only real roots*, arXiv:1208.3831v3, §5.1, Theorem 5.4 (real-rootedness of the comajor-index q-Eulerian polynomial).
3. J. Pitman, Y. Yakubovich, *Extremes and gaps in sampling from a GEM random discrete distribution*, arXiv:1701.06294, Theorem 1.1 (distinct random-environment sampling model).
