# Jacobi zeros and Gaussian lengths for two-prime ordered factorizations

## Finding

Let \(p\ne q\) be primes and let \(a,b\ge1\). Write \(c_k(p^a q^b)\) for the number of ordered sequences of **exactly** \(k\) integers greater than one whose product is \(p^a q^b\). Set
\[
P_{a,b}(t)=\sum_{k=1}^{a+b}c_k(p^a q^b)t^k,\quad M=\max(a,b),\quad m=\min(a,b).
\]
Then the **entire factor-length polynomial** has the Jacobi factorization
\[
\boxed{P_{a,b}(t)=t(1+t)^{M-1}P_m^{(0,M-m)}(1+2t),}
\]
where \(P_m^{(\alpha,\beta)}\) denotes the standard Jacobi polynomial normalized by \(P_m^{(\alpha,\beta)}(1)=\binom{m+\alpha}{m}\).

Consequently, its zeros consist of one simple zero at \(0\), exactly \(M-1\) zeros at \(-1\), and exactly \(m\) distinct simple zeros strictly between \(-1\) and \(0\). Every zero is real. Newton's inequalities additionally show that the normalized length-count sequence \(c_k(p^a q^b)/\binom{a+b-1}{k-1}\) is log-concave for \(1\le k\le a+b\). The root description applies without exception, including \(a=b=1\).

For a uniformly selected ordered factorization of \(p^a q^b\), let \(L_{a,b}\) denote its number of factors. If \(x_1,\ldots,x_m\) are the zeros of \(P_m^{(0,M-m)}\), then there is an equality in distribution
\[
\boxed{L_{a,b}\ \overset{d}=\ 1+\sum_{i=1}^{M-1}U_i+\sum_{j=1}^{m}V_j,}
\]
where all summands are independent, \(U_i\sim\operatorname{Bernoulli}(1/2)\), and \(V_j\sim\operatorname{Bernoulli}(2/(3-x_j))\). The \(V_j\) success probabilities lie strictly between \(1/2\) and \(1\). If \(a+b\to\infty\) along *any* sequence of positive integer exponent pairs, then
\[
\frac{L_{a,b}-\mathbb E L_{a,b}}{\sqrt{\operatorname{Var}(L_{a,b})}}
\ \xrightarrow{d}\ \mathcal N(0,1).
\]
This is a fixed-integer factorization-ensemble central limit statement, rather than a result averaging over integers in a growing interval.

## Assumptions and scope

Primes \(p\) and \(q\) are distinct but otherwise arbitrary; the polynomial depends only on the positive exponents \(a,b\). Factorization order matters, equal factor sequences are counted once, and factors equal to one are excluded. For example, \(P_{2,2}(t)=t+7t^2+12t^3+6t^4=t(1+t)(1+6t+6t^2)\). The Gaussian conclusion concerns uniform sampling from the finite set of all such factorizations for each exponent pair.

The polynomial itself and the individual coefficient counts are established objects in prior work. The claims here concern the Jacobi identity **as a polynomial in the factor-length marker**, the complete two-prime root structure, the independent-Bernoulli representation and the resulting fixed-integer Gaussian limit.

## Proof

**1. Ordered-factorization generating function.** Fix formal variables \(x,y,t\). A single factor \(p^i q^j>1\) has weight \(x^i y^j\) with \(i,j\ge0\), not both zero; hence its bivariate series is
\[
B(x,y)=\frac1{(1-x)(1-y)}-1.
\]
An ordered sequence of exactly \(k\) such factors has series \(B(x,y)^k\), including all repetitions without an additional factorial. Therefore, for \(a+b>0\), the coefficient of \(x^a y^b\) in \((1-tB)^{-1}\) is exactly \(P_{a,b}(t)\). Formal power series suffice, so no analytic convergence assumption is involved.

**2. An exact bivariate coefficient identity.** Put \(s=1+t\), and define the formal series
\[
G(x,y;t)=\frac1{1-s(x+y)+sxy}.
\]
By a geometric-series expansion in the mixed term (equivalently, the elementary bivariate binomial identity),
\[
[x^a y^b]G=s^{a+b}\sum_{j=0}^{\min(a,b)}\binom aj\binom bj(t/s)^j.
\]
For completeness, this follows by summing the identity
\[
\sum_{a\ge j}\binom aj X^a=\frac{X^j}{(1-X)^{j+1}}
\]
independently in the two indices and then summing \(j\) with weight \(t/s\), where \(X=sx\) and \(Y=sy\). The rational generating function is
\[
\sum_{a,b\ge0}\sum_{j\le\min(a,b)}\binom aj\binom bj(t/s)^j X^a Y^b
=\frac1{(1-X)(1-Y)-(t/s)XY}=G.
\]
The original factorization generating function satisfies
\[
\frac1{1-tB}=(1-x)(1-y)G=\frac1s+\frac tsG.
\]
The constant term \(1/s\) affects only \(a=b=0\). Thus for every \(a+b>0\),
\[
P_{a,b}(t)=t(1+t)^{a+b-1}\sum_{j=0}^{\min(a,b)}\binom aj\binom bj\left(\frac t{1+t}\right)^j.
\]
This identity is a polynomial identity despite its intermediate rational notation.

**3. Jacobi identification.** By symmetry assume \(a=M\) and \(b=m\). Rearranging the finite sum gives
\[
P_{a,b}(t)=t(1+t)^{M-1}\sum_{j=0}^{m}\binom Mj\binom mj t^j(1+t)^{m-j}.
\]
The standard binomial representation of the Jacobi polynomial is
\[
P_m^{(0,M-m)}(1+2t)
=\sum_{j=0}^{m}\binom mj\binom Mj t^j(1+t)^{m-j}.
\]
It is the same polynomial, giving the asserted factorization with exactly the stated normalization. Its degree is \(m\), its value at \(t=0\) is \(1\), and its value at \(t=-1\) is \((-1)^m\binom Mm\ne0\). Consequently no endpoint root multiplicities are hidden in the Jacobi factor.

**4. Zeros and probability law.** For \(\alpha=0\) and \(\beta=M-m\ge0\), Jacobi orthogonality with the strictly positive weight \((1+x)^\beta\) on \((-1,1)\) gives exactly \(m\) distinct real zeros \(x_j\in(-1,1)\). Their transforms \((x_j-1)/2\) lie strictly in \((-1,0)\). This proves the exact zero census, with \(0\) and \(-1\) accounted for by the other factors.

Define \(\theta_j=(1-x_j)/2\in(0,1)\). Dividing \(P_{a,b}(t)\) by its positive value at \(t=1\) yields the probability generating function of \(L_{a,b}\):
\[
\mathbb E[t^{L_{a,b}}]=t\left(\frac{1+t}{2}\right)^{M-1}
\prod_{j=1}^{m}\frac{\theta_j+t}{\theta_j+1}.
\]
Each normalized linear factor \((\theta_j+t)/(\theta_j+1)\) is the generating function of a Bernoulli variable with success probability \(1/(1+\theta_j)=2/(3-x_j)\). Multiplication of these generating functions proves the independent-summand representation. In particular,
\[
\frac{M-1}{4}\le\operatorname{Var}(L_{a,b})\le\frac{a+b-1}{4}.
\]
As \(a+b\to\infty\), necessarily \(M\to\infty\), so the variance diverges. Every centered Bernoulli summand is bounded in absolute value by one; hence the Lindeberg condition holds for the resulting triangular array, and the normalized sum converges to a standard normal random variable.

## Verification

The standalone `verify.py` reconstructs ordered-factorization length profiles independently by recursively choosing the first nontrivial factor. It compares their exact coefficient vectors with the finite Jacobi/binomial expression for all \(144\) pairs \(1\le a,b\le12\), including four explicitly specified sample vectors. Execution with Python 3 standard library produces the line `PASS: 144 pairs of exponents, 4 illustrative coefficient vectors`. These finite checks corroborate the algebra; the identity and limit theorem are proved above for all exponent pairs.

## Relationship to prior work

MacMahon's classical inclusion-exclusion formula gives every fixed-length factorization count. Sprittulla (2016, equation (1.1)) reviews that formula. Kinder (2012, Theorem 4) expresses the **total** count at two-prime exponent shapes as a Jacobi polynomial evaluated at a fixed argument; this is a one-point evaluation, not a factor-length generating-polynomial identity. Huxley, Lettington and Schmidt (arXiv:2610.13864, first public version October 9, 2026, Sections 3–4) define the full divisor-function polynomial and establish its Dirichlet generating function and squarefree specializations, but the relevant inspected discussion does not provide the two-prime Jacobi root classification or the fixed-integer Bernoulli/Gaussian law. Law, Lettington and Schmidt (2025, Theorem 1.5) focus on related joint ordered multifactorizations and divisor-function sums. These known formulas and objects are inputs, not claimed inventions.

## Limitations

No claim is made about the nontrivial-factor length-polynomial zero set for integers having three or more distinct prime factors. This result concerns two-prime exponent shapes and does not classify joint multifactorization polynomials. The exact Jacobi representation is a new formulation of previously defined polynomials; its novelty is subject to possible implicit prior derivation from MacMahon's formulas, from special-function identities, or from general results about zeros of combinatorial rank polynomials. The Gaussian law is asymptotic with mean and variance taken from the exact finite distribution; no local limit theorem or explicit Berry–Esseen constant is asserted.

## References

- M. N. Huxley, M. C. Lettington, K. M. Schmidt, *On Divisor Function Polynomials and Dirichlet Series*, arXiv:2610.13864 (2026), https://arxiv.org/abs/2610.13864.
- A. D. Law, M. C. Lettington, K. M. Schmidt, *Multifactorisations and divisor functions*, Utilitas Mathematica 125 (2025), 43–60, https://doi.org/10.61091/um125-03.
- J. Sprittulla, *Ordered Factorizations with \(k\) Factors*, arXiv:1610.04826 (2016), https://arxiv.org/abs/1610.04826.
- M. I. Kinder, *On perfect partitions of integers* (2012), https://s.science-education.ru/pdf/2012/5/98.pdf.
- P. A. MacMahon, *Memoir on the Theory of the Compositions of Numbers*, Philosophical Transactions of the Royal Society of London A 184 (1893), 835–901 (historical coefficient formula).
