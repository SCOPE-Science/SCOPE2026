# Gaussian fluctuations and cubic variance of one-point type counts over uniform weak orders

## Finding

Let \(\mathbb U\) be the countable homogeneous universal strict partial order, and let \(P_n\) be a uniformly random weak order (ordered partition into antichain levels) on the labelled set \(\{1,\ldots,n\}\), embedded as individually named parameters in \(\mathbb U\). Write \(T_n\) for the number of complete **nonalgebraic** one-point types over this base, with all named parameters fixed pointwise. Put \(\rho=\log 2\). Then

\[
\boxed{\frac{\rho^2}{n^{3/2}}\left(T_n-\frac{n^2}{2\rho^2}\right)\ \xrightarrow{\,d\,}\ N(0,1),\qquad
\operatorname{Var}(T_n)\sim\frac{n^3}{\rho^4}.}
\]

In particular, \(T_n/n^2\to1/(2\rho^2)\) in probability and its relative fluctuations have order \(n^{-1/2}\). The first-order mean \(\mathbb E T_n=n^2/(2\rho^2)+O(n)\) was previously known; the claimed contributions are the normal limit and the sharp variance coefficient, not that mean or the deterministic finite-base formula.

## Assumptions and scope

Every parameter is individually named, the new point is distinct from the parameters, and the random object is **uniform among labelled weak orders**, not among all posets or among unlabelled weak orders. Write the levels of a particular base as \(A_1\oplus\cdots\oplus A_h\), with \(k_i=|A_i|\ge1\), \(b_i=2^{k_i}-1\), \(S=\sum_i b_i\), and \(Q=\sum_i b_i^2\). The elementary, previously established finite-base extension formula is

\[
T=1+2S+\sum_{i<j} b_i b_j=1+2S+\tfrac12(S^2-Q).
\]

It counts the admissible downset/upset pairs defining a new point's order comparisons in the generic poset. The new theorem concerns the distribution of this integer statistic when the level sizes themselves are sampled from the uniform labelled ordered-partition measure. All limits are for integer \(n\to\infty\), and \(\sim\) means ratio tending to one.

## Proof

**1. Exact renewal representation.** For a given ordered composition \((k_1,\ldots,k_h)\) of \(n\), there are \(n!/\prod_i k_i!\) labelled weak orders with those ordered level sizes. Set \(\rho=\log2\) and let \(K\) be a positive-integer random variable with
\[
\Pr(K=k)=p_k=\frac{\rho^k}{k!}\quad(k\ge1).
\]
The probabilities sum to \(e^\rho-1=1\). For independent copies \(K_1,K_2,\ldots\), the distribution of the sequence up to an exact renewal hit of \(n\), conditional on that event, assigns each composition a weight proportional to \(\prod_i p_{k_i}=\rho^n/\prod_i k_i!\). It is therefore exactly the uniform-labelled-weak-order level-size distribution. Put \(B=2^K-1\) and \(S_n=\sum B_i\) over the renewal blocks to \(n\).

Direct differentiation of exponential series gives
\[
\begin{aligned}
\mathbb E K&=2\rho,&\mathbb E B&=2,\\
\mathbb E K^2&=2\rho+2\rho^2,&\mathbb E(KB)&=6\rho,&\mathbb E B^2&=10.
\end{aligned}
\]
For \(Y=B-K/\rho\), one obtains \(\mathbb EY=0\) and \(\mathbb EY^2=2/\rho\). The renewal-reward variance per unit total size is thus \(\mathbb EY^2/\mathbb EK=1/\rho^2\).

**2. Conditional lattice central limit theorem.** We give a direct proof, since the exact-sum renewal conditioning and the fast-growing reward warrant care. For real \(t\), define
\[
f(z,t)=\sum_{k\ge1}p_k z^k\exp\left(it(2^k-1-k/\rho)\right),
\qquad F(z,t)=\frac1{1-f(z,t)}.
\]
For each real \(t\), \(f(\cdot,t)\) is entire, by factorial decay; near \(t=0\), the function and its first two \(t\)-derivatives converge uniformly on every fixed compact \(z\)-disk. At \(t=0\), \(f(z,0)=e^{\rho z}-1\), and the zeros of \(1-f(z,0)\) are \(1+2\pi i j/\rho\), \(j\in\mathbb Z\). Choose a circle of radius \(R>1\) smaller than the modulus of any nonreal zero. For small real \(|t|\), exactly one simple zero \(z(t)\) lies inside this circle, near \(1\); it follows by uniform perturbation on the contour and the implicit-function theorem in \(z\).

Differentiating \(f(z(t),t)=1\) twice at zero and using \(f_z(1,0)=\mathbb EK=2\rho\), \(f_t(1,0)=i\mathbb EY=0\), and \(f_{tt}(1,0)=-\mathbb EY^2\), gives
\[
z(t)=1+\frac{\mathbb EY^2}{2\mathbb EK}t^2+o(t^2)
=1+\frac{t^2}{2\rho^2}+o(t^2).
\]
Cauchy's coefficient formula, taking the residue at this single pole and bounding the remaining contour uniformly, gives
\[
[z^n]F(z,t)=\frac{z(t)^{-n}}{z(t)f_z(z(t),t)}+O(R^{-n}).
\]
The coefficient ratio \([z^n]F(z,t/\sqrt n)/[z^n]F(z,0)\) is the characteristic function of \((S_n-n/\rho)/\sqrt n\) under the conditional renewal law. It tends to \(\exp(-t^2/(2\rho^2))\). Hence
\[
\frac{\rho}{\sqrt n}\left(S_n-\frac n\rho\right)\xrightarrow{d}N(0,1).
\]

**3. Moment control and the sharp variance.** The reward \(B\) has finite moments of every fixed order, but **does not have a positive exponential moment**. We therefore use only fixed formal derivatives rather than asserting a complex moment-generating function near zero. Let
\[
A_j(z)=\sum_{k\ge1}p_k(2^k-1)^jz^k,\qquad W(z)=\frac1{1-A_0(z)}.
\]
Each \(A_j\) is entire for fixed integer \(j\ge0\). Formally marking blocks by \(\exp(uB)\), differentiation to each fixed order yields meromorphic functions with their unique nearest singularity at \(z=1\). The standard simple-pole coefficient expansion, applied coefficientwise to this *finite-order formal perturbation*, yields for every fixed \(j\) the cumulant bound \(\kappa_j(S_n)=O(n)\); specifically \(\mathbb ES_n=n/\rho+O(1)\), \(\operatorname{Var}(S_n)=n/\rho^2+O(1)\), and \(\mathbb E(S_n-\mathbb ES_n)^4=O(n^2)\). To see the leading variance coefficient directly, the formal pole location has logarithmic second derivative \(\mathbb EY^2/\mathbb EK=1/\rho^2\), exactly as in Step 2. The fixed-order argument is legitimate because only the finitely many entire functions \(A_0,\ldots,A_j\) enter each derivative.

The statistic \(Q_n=\sum_i B_i^2\) has first and second moments \(O(n)\) and \(O(n^2)\): its renewal-weighted generating functions are respectively \(A_2W^2\) and \(A_4W^2+2A_2^2W^3\); dividing the coefficient at size \(n\) by \([z^n]W\) gives these orders by pole orders two and three.

Write \(\Delta_n=S_n-n/\rho\). The deterministic identity in the assumptions becomes
\[
T_n=\frac{n^2}{2\rho^2}+\frac n\rho\Delta_n+R_n,
\qquad R_n=1+2S_n+\frac12\Delta_n^2-\frac12Q_n.
\]
The established moments imply \(\mathbb E R_n^2=O(n^2)\). Consequently \(R_n/n^{3/2}\to0\) in \(L^2\). Slutsky's theorem and Step 2 prove the stated normal limit. Moreover, the variance of the leading random term is
\[
\operatorname{Var}\left(\frac n\rho\Delta_n\right)
=\frac{n^2}{\rho^2}\left(\frac n{\rho^2}+O(1)\right)
=\frac{n^3}{\rho^4}+O(n^2).
\]
The covariance with \(R_n\) is bounded by Cauchy–Schwarz by \(O(n^{5/2})=o(n^3)\), and \(\operatorname{Var}(R_n)=O(n^2)\). This proves the sharp cubic-variance asymptotic. The first-order mean follows likewise from the decomposition (and was already known).

## Verification

The accompanying `verify.py` is a standalone Python 3 standard-library program. It checks the weak-order type formula by direct enumeration of all ternary new-point comparison patterns for 127 ordered compositions with up to seven elements. It uses an independent labelled-block recurrence to compute exact integer moments of \(S_n\) and \(T_n\), cross-checks the second moment against explicit ordered compositions for sizes up to seven, and compares finite-size normalized means and variances through size 200. The accompanying `verification_output.txt` contains the exact output. These finite calculations do **not** prove the Gaussian limit or the infinite variance asymptotic; Steps 2 and 3 provide their proofs.

## Relationship to prior work

The finite-poset ideal/filter type parametrization is classical and appears in Dolinka and Mašulović (2010), Lemma 4.3. Elder et al. (2023), Theorem 3.3, give the closely related interval-closed-set count for ordinal sums of antichains. The indexed result **Quadratic average one-point type growth over random finite weak orders** (2026) establishes the exact finite-base formula, random weak-order expectation generating functions, and \(\mathbb E T_n=n^2/(2(\log2)^2)+O(n)\); its limitations expressly withhold any variance, concentration, or distributional assertion. All those inputs are credited. The present claim gives the previously unaddressed sharp \(n^3\) variance and a central limit theorem for that particular model-theoretic statistic. The general renewal-reward limit theory in Patch–Nazarathy–Taimre (2014) is also relevant; its nonlattice/spread-out formulation is not directly an exact-sum conditioned lattice theorem and does not state the transformed weak-order result or its constant.

## Limitations

The theorem is about uniformly chosen **labelled** finite weak orders and individually named parameter types. It does not give a local limit theorem, large deviations, a rate of Gaussian convergence, or the analogous law for unrestricted uniformly random posets. Positive exponential moments of the block reward do not exist, so a naive analytic moment-generating-function argument would be unjustified; the proof deliberately uses a real-characteristic-function perturbation and finite-order formal moment derivatives. The originality assessment does not rule out an unlocated published specialization of a more general conditional renewal theorem. Independent mathematical audit has not yet been performed.

## References

1. I. Dolinka and D. Mašulović, *A universality result for endomorphism monoids of some ultrahomogeneous structures*, arXiv:1009.2892, first posted 2010-09-15, Lemma 4.3, https://arxiv.org/abs/1009.2892.
2. J. Elder, N. Lafrenière, E. McNicholas, J. Striker, and A. Welch, *Toggling, rowmotion, and homomesy on interval-closed sets*, arXiv:2307.08520, first posted 2023-07-17, Theorem 3.3, https://arxiv.org/abs/2307.08520.
3. *Quadratic average one-point type growth over random finite weak orders*, publicly indexed research finding (2026), identifier `2026/10/18/SCOPE-quadratic-average-one-point-type-growth-over-random-finite-weak--a2d26ced4e39`, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-quadratic-average-one-point-type-growth-over-random-finite-weak--a2d26ced4e39.
4. B. Patch, Y. Nazarathy and T. Taimre, *A correction term for the covariance of renewal-reward processes with multivariate rewards*, arXiv:1408.1530, 2014, https://arxiv.org/abs/1408.1530.
