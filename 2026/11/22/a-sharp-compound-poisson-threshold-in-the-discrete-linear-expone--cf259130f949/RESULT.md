# A sharp compound-Poisson threshold in the discrete linear-exponential count law

## Finding

Let \(X_\sigma\) be the nonnegative-integer-valued discrete linear-exponential law of El-Morshedy (2022), with \(\sigma>0\) and survival function
\[
\Pr(X_\sigma\ge k)=e^{-\sigma k}\left(1+\frac{\sigma k}{1+\sigma^3}\right),\qquad k=0,1,2,\ldots.
\]
There exists a **unique** \(\sigma_*\in(0,\infty)\) such that \(X_\sigma\) is infinitely divisible under ordinary addition of nonnegative integer-valued variables **if and only if** \(\sigma\ge\sigma_*\). The threshold is characterized exactly by
\[
\boxed{\ \sigma_*^3=\frac{\sigma_*}{2}\coth\left(\frac{\sigma_*}{2}\right)-1\ },
\qquad 0.08332369209698<\sigma_*<0.08332369209699.
\]
For all \(\sigma>0\), the probability sequence is strictly log-concave, so this provides a natural class whose log-concavity does not ensure infinite divisibility. Whenever \(\sigma\ge\sigma_*\), the distribution has an explicit compound-Poisson representation with jump intensities given below. At \(\sigma=1/20\), the coefficient of degree \(104\) in the logarithm of the probability-generating function is strictly negative; hence this member is *not* infinitely divisible.

## Assumptions and scope

All statements concern the one-parameter family on \(\mathbb Z_{\ge0}\), with \(\sigma\in(0,\infty)\), and ordinary convolution of probability measures on the nonnegative integers. They do not concern infinite divisibility under binomial thinning, nor other models sometimes described by the generic phrase “discrete linear-exponential.” The survival-discretization convention is \(\Pr(X_\sigma\ge k)=\Pr(T_\sigma\ge k)\) at nonnegative integer \(k\). The source law has \(\Pr(T_\sigma\ge t)=(1+\sigma t/(1+\sigma^3))e^{-\sigma t}\) for \(t\ge0\).

Write
\[
q=e^{-\sigma},\qquad a=\frac{\sigma}{1+\sigma^3},\qquad
A=1-q-qa,\qquad B=(1-q)a,\qquad c=q\left(\frac BA-1\right).
\]
Since \(0<a<\sigma<e^\sigma-1\), \(A>0\) and \(B>0\). All statements below hold for every positive \(\sigma\), including equality at the threshold.

## Proof

**1. Probability masses and log-concavity.** Taking consecutive differences of the survival function yields
\[
p_j=\Pr(X_\sigma=j)=q^j(A+Bj),\qquad j\in\mathbb Z_{\ge0}.
\]
The sequence is normalized because it telescopes from survival one to survival zero. Since \(A,B>0\), all masses are positive, and for every integer \(j\ge1\),
\[
p_j^2-p_{j-1}p_{j+1}=q^{2j}B^2>0.
\]
Thus the mass sequence is strictly log-concave for **every** \(\sigma>0\).

**2. The exact generating-function obstruction.** The probability-generating function is
\[
P_\sigma(z)=\sum_{j=0}^\infty p_jz^j
=\frac{A+(B-A)qz}{(1-qz)^2}
=A\frac{1+cz}{(1-qz)^2}.
\]
For sufficiently small complex \(z\), its logarithm has the convergent series
\[
\log P_\sigma(z)=\log A+\sum_{n=1}^\infty \nu_nz^n,\qquad
\nu_n=\frac{2q^n+(-1)^{n+1}c^n}{n}.
\]
A probability distribution supported on \(\mathbb Z_{\ge0}\) with strictly positive mass at zero is infinitely divisible under ordinary addition **if and only if** it is compound Poisson; equivalently, the nonconstant Taylor coefficients of its log-PGF are all nonnegative, with finite sum (the discrete compound-Poisson characterization). Here \(c/q=B/A-1>-1\), so \(c>-q\). If \(c\le q\), then \(|c|\le q\), whence for odd \(n\) the coefficient \(\nu_n\) is strictly positive and for even \(n\) it is at least \(q^n/n>0\). Also \(|c|\le q<1\), so the series is summable, and normalization gives \(\sum_{n\ge1}\nu_n=-\log A\). The compound-Poisson representation follows: take Poisson rate \(-\log A\) and a strictly positive integer-valued jump law with probabilities \(\nu_n/(-\log A)\). Conversely, if \(c>q\), all sufficiently large even coefficients satisfy \(\nu_{2m}=(2q^{2m}-c^{2m})/(2m)<0\), so the law cannot be infinitely divisible. Consequently
\[
X_\sigma\ \text{is infinitely divisible}\quad\Longleftrightarrow\quad
c\le q\quad\Longleftrightarrow\quad B\le2A\quad\Longleftrightarrow\quad
\frac{\sigma}{1+\sigma^3}\le2\tanh\frac\sigma2.
\]
The last inequality is equivalent to \(\sigma^3\ge(\sigma/2)\coth(\sigma/2)-1\).

**3. Uniqueness of the parameter transition.** Put \(x=\sigma/2\), and let \(f(x)=(x\coth x-1)/x^2\). Direct differentiation shows that the sign of \(-f'(x)\), for \(x>0\), is the sign of
\[
D(x)=x^2+x\sinh x\cosh x-2\sinh^2x.
\]
Writing \(2\sinh^2x=\cosh(2x)-1\) and \(\sinh x\cosh x=\sinh(2x)/2\), cancellation of the quadratic and quartic coefficients gives the positive series
\[
D(x)=\sum_{n=3}^\infty
\frac{2^{2n-2}(n-2)}{n(2n-1)!}\,x^{2n}>0.
\]
Thus \(f\) is strictly decreasing and positive. Hence
\[
\frac{(\sigma/2)\coth(\sigma/2)-1}{\sigma^3}
=\frac{f(\sigma/2)}{4\sigma}
\]
is strictly decreasing, from \(+\infty\) as \(\sigma\downarrow0\) to zero as \(\sigma\to\infty\). Here the small-parameter numerator is \(\sigma^2/12+O(\sigma^4)\), and the large-parameter numerator is \(\sigma/2-1+o(1)\). There is exactly one crossing with value one, proving the theorem and direction of the inequality.

**4. A finite exact certificate outside the compound-Poisson region.** At \(\sigma=1/20\), set \(a=\sigma/(1+\sigma^3)\). The ratio \(c/q\) can be written without an exponential in the denominator as
\[
\frac cq=\frac{(e^\sigma-1)a}{e^\sigma-1-a}-1.
\]
The bundled exact-rational checker bounds \(e^{1/20}\) between the degree-20 Taylor polynomial and its explicit geometric remainder upper bound. Substitution and rational comparison prove
\[
1<\frac cq,\qquad \left(\frac cq\right)^{102}<2<\left(\frac cq\right)^{104}.
\]
Therefore \(\nu_{104}=q^{104}[2-(c/q)^{104}]/104<0\). The checker also proves opposite signs of the defining transition equation at \(0.08332369209698\) and \(0.08332369209699\). Uniqueness from Step 3 converts those two exact rational inequalities into the stated rigorous enclosure.

## Verification

The included standalone script `check_exact.py` uses exact rational fractions and symbolic algebra (Python 3 and SymPy). Run `python3 check_exact.py` in the directory containing this file and the script. It verifies five symbolic formulas; two sign evaluations for the root enclosure using rational exponential bounds; the strict negative sign of the degree-104 log-PGF coefficient at \(\sigma=1/20\); and hundreds of supporting finite rational coefficient checks. These computations are **not** substituted for the infinite-support proof: the compound-Poisson characterization and the all-positive power series for \(D(x)\) supply the infinite arguments. The threshold and negative-degree certificates rely on exact arithmetic, not floating point.

## Relationship to prior work

El-Morshedy (2022) introduces the specific one-parameter discrete linear-exponential law and derives distributional features, including its survival and count formulas. Al-Harbi et al. (2024) revisit this family and its inference and descriptive properties. The classical discrete compound-Poisson characterization supplies the general method but does not, by itself, state the sharp boundary for this constrained one-parameter family.

A particularly close later comparison is Das et al. (2025), whose more general discretized two-parameter Lindley survival function includes the present model under continuous rate \(\theta=\sigma\) and continuous second parameter \(\alpha=\sigma^{-2}\), because \(\alpha\theta/(\alpha+\theta)=\sigma/(1+\sigma^3)\). Their Theorem 3.3 asserts broad infinite divisibility using two *necessary*, rather than sufficient, conditions. The exact negative degree-104 coefficient above demonstrates that such an unconditional conclusion does not hold for this included parameter point. This comparison is about the mathematical implication of that theorem, not a claim about their software or numerical experiments. Related published findings on geometric maxima, two-Poisson mixtures, and zero-inflated negative-binomial laws study different probability-generating functions and do not imply this threshold.

## Limitations

The theorem classifies only this one-parameter survival-discretized family. It does not classify the entire two-parameter Lindley family or more general linear-geometric laws. The literature comparison covers accessible material; further historical work on algebraic or rational generating functions may contain equivalent general criteria. The presented mathematical review is not independent validation. No inference or empirical performance results are claimed.

## References

1. M. El-Morshedy (2022), “A Discrete Linear-Exponential Model: Synthesis and Analysis with Inference to Model Extreme Count Data,” *Axioms* **11**, 531. https://doi.org/10.3390/axioms11100531 (publicly published 4 October 2022).
2. K. Al-Harbi, A. Fayomi, H. Baaqeel and A. Alsuraihi (2024), “A Novel Discrete Linear-Exponential Distribution for Modeling Physical and Medical Data,” *Symmetry* **16**, 1123. https://doi.org/10.3390/sym16091123.
3. D. Das et al. (2025), “A Discrete Expansion of the Lindley Distribution: Mathematical and Statistical Characterizations with Estimation Techniques, Simulation, and Goodness-of-Fit Analysis,” *Computational Journal of Mathematical and Statistical Sciences* **4**, 622–645. https://doi.org/10.21608/cjmss.2025.373562.1146.
4. F. W. Steutel and K. van Harn, *Infinite Divisibility of Probability Distributions on the Real Line*, Marcel Dekker, 2004, discrete compound-Poisson characterization.
