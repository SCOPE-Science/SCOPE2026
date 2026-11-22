# Positive dependence and exact covariance of common-phase Kummer carry indicators

## Finding

For every integer \(d\ge3\), every pair \(1\le j,k<d\), and a single uniformly distributed phase \(X\in[0,1)\), define
\[
F_j(X)=\lfloor dX\rfloor-\lfloor jX\rfloor-\lfloor(d-j)X\rfloor.
\]
Each \(F_j\) is a fair Bernoulli variable. Let \(K(a,b)=\gcd(a,b)^2/(ab)\) for positive integers \(a,b\). Then the complete pair covariance is the explicitly rational number
\[
12\operatorname{Cov}(F_j,F_k)=1+K(j,k)+K(j,d-k)+K(d-j,k)+K(d-j,d-k)
-K(j,d)-K(d-j,d)-K(k,d)-K(d-k,d).
\]
In particular all pair covariances are nonnegative; **if neither index equals \(d/2\)**, then the covariance is strictly positive. Consequently, when \(d\) is odd, every pair of carry indicators, including pairs of different lower-index ratios, is strictly positively correlated. When \(d\) is even, the central coordinate is the only coordinate that can participate in zero covariance; the previously studied central-coordinate boundary is not claimed as new here.

The exact binary joint distribution follows from the covariance: for \(a,b\in\{0,1\}\),
\[
\Pr(F_j=a,F_k=b)=\tfrac14+(2a-1)(2b-1)\operatorname{Cov}(F_j,F_k).
\]
Thus all *noncentral* pairs satisfy strict positive quadrant dependence, without assuming or claiming independence of the complete family.

## Assumptions and scope

Here \(d,j,k\) are integers and all floors are ordinary real floors; the only random variable is the **shared** continuously uniform real phase \(X\). Endpoints of the finitely many discontinuity intervals have measure zero, so the Fourier identities below are asserted almost everywhere. The result does not concern independently sampled phases. In the binomial setting the function has the exact Kummer–Legendre interpretation
\[
\nu_p\!\left(\binom{dm}{jm}\right)=\sum_{r\ge1}F_j\!\left(\left\{\frac m{p^r}\right\}\right),
\]
for primes \(p\) and positive integers \(m\). This identity motivates the family but does **not** identify the joint distribution of actual integer-indexed prime-adic valuation sums with the continuous-phase law proved here.

## Proof

1. For a real \(t\), the addition-of-fractional-parts identity gives \(F_j(t)=\{jt\}+\{(d-j)t\}-\{dt\}\), taking values in \(\{0,1\}\). Let \(B(t)=\{t\}-\tfrac12\), with arbitrary values at integers. For almost every \(t\),
\[
F_j(t)-\tfrac12=B(jt)+B((d-j)t)-B(dt).
\]
Since every \(B(at)\) has integral zero on \([0,1]\), \(\mathbb EF_j=1/2\).

2. The classical Fourier coefficients are \(\widehat B(n)=-1/(2\pi i n)\) for \(n\ne0\). For a positive integer \(a\), \(\widehat{B(a\cdot)}(n)=-a\mathbf1_{a\mid n}/(2\pi i n)\). Therefore if
\[
W_j(n)=j\mathbf1_{j\mid n}+(d-j)\mathbf1_{d-j\mid n}-d\mathbf1_{d\mid n},
\]
Parseval's identity in \(L^2[0,1]\) yields the absolutely convergent series
\[
\operatorname{Cov}(F_j,F_k)=\frac1{2\pi^2}\sum_{n\ge1}\frac{W_j(n)W_k(n)}{n^2}.
\]
For \(d\nmid n\), both \(W_j(n)\) and \(W_k(n)\) are nonnegative. For \(d\mid n\), each lies between \(-d\) and \(0\). Consequently every summand is nonnegative, proving the universal nonnegative-covariance assertion.

3. At the particular frequency \(n=d\),
\[
W_j(d)=-\delta_d(j),\qquad
\delta_d(j)=d-j\mathbf1_{j\mid d}-(d-j)\mathbf1_{d-j\mid d}.
\]
If \(\delta_d(j)=0\), both positive summands in its definition must appear, so \(j\mid d\) and \(d-j\mid d\). Setting \(a=d/j\) and \(b=d/(d-j)\) gives integers \(a,b\ge2\) with \(1/a+1/b=1\). Therefore \(a=b=2\), and \(j=d/2\). Conversely this central index gives \(\delta_d(j)=0\). Thus \(\delta_d(j)\ge1\) for every noncentral integer index, and for noncentral \(j,k\) the \(n=d\) summand proves the explicit strict bound
\[
\operatorname{Cov}(F_j,F_k)\ge\frac{\delta_d(j)\delta_d(k)}{2\pi^2d^2}>0.
\]
No finite truncation of the Fourier sum is used in the inequality.

4. Finally, the standard Bernoulli–sawtooth correlation identity (derivable from the same Fourier expansion) is
\[
\int_0^1B(at)B(bt)\,dt=\frac{\gcd(a,b)^2}{12ab}=\frac{K(a,b)}{12}.
\]
Expanding the three-term expressions for \(F_j-1/2\) and \(F_k-1/2\) gives the displayed eight-term \(K\)-formula. For the joint distribution, write \(q=\Pr(F_j=1,F_k=1)\); since both marginals are \(1/2\), one has \(q=1/4+\operatorname{Cov}\), the off-diagonal probabilities are \(1/2-q\), and the other diagonal probability is \(q\). This establishes the claim in full.

## Verification

The companion Python program `check.py` performs exact rational integration by partitioning \([0,1]\) at **all** discontinuities of the two carry functions. It independently evaluates the stated gcd formula and compares values for every unordered pair \(1\le j\le k<d\) across all \(3\le d\le35\): **7,139 exact pair checks**; 86 observed zero values all involve the central index. Sample values: \(\operatorname{Cov}(F_1,F_2)=1/6\) at \(d=5\), \(1/10\) at \(d=6\), and \(\operatorname{Cov}(F_6,F_{10})=1/30\) at \(d=30\). These finite checks detect arithmetic errors; the Fourier proof handles every integer parameter.

Run with Python 3 using `python check.py`; only the standard library is required.

## Relationship to prior work

Wu's June 18, 2026 binomial-GCD paper (arXiv:2606.20940) and Guo–Qiu–Cao–Feng–Gao's June 22, 2026 gcd criterion (arXiv:2606.22997; primary MSC 11B65) motivate arithmetic questions about multiple binomial indices. Neither paper states a shared-continuous-phase pair-covariance law. The classical sawtooth correlation \(K(a,b)/12\) is explicitly given in Proposition 3.1 of Lemke Oliver–Soundararajan's paper on consecutive-prime biases; it is **not** claimed new here. The new assertion is the carry-vector sign structure derived from a common Fourier sign certificate for every pair of noncentral ratios, with its exact combined kernel.

A later relevant preprint by Cui and Yang (arXiv:2611.25794, first posted November 19, 2026) defines the same individual function in Lemma 2.2 and proves a half-measure zero-set property, using conditions at varying prime phases to derive binomial-GCD asymptotics. Its inspected statements do not give the common-phase pair covariance or the strict universal sign law. It is a literature comparison, not the eligible motivating source for this result. A separate preceding result already treats independence involving the central coordinate; the present theorem deliberately claims only the general all-pairs kernel and strict positivity away from that coordinate.

## Limitations

This is a pairwise statement. Strict positive covariance does not imply mutual independence, positive association for arbitrary increasing functions, or any corresponding inequality between full arithmetic valuations on integer samples. The proof uses ordinary Fourier analysis of periodic sawtooth functions and the previously known two-function gcd identity; earlier unindexed equivalent formulations remain a priority risk. No independent audit is claimed.

## References

- Chai Wah Wu, *Computing the Greatest Common Divisor of Binomial Coefficients*, arXiv:2606.20940v1, submitted June 18, 2026. https://arxiv.org/abs/2606.20940
- Dakai Guo, Ruichen Qiu, Yichuan Cao, Ruyong Feng, Xiao-Shan Gao, *A Greatest Common Divisor Criterion of Certain Binomial Coefficients*, arXiv:2606.22997v1, submitted June 22, 2026. https://arxiv.org/abs/2606.22997
- Robert J. Lemke Oliver and Kannan Soundararajan, *The Distribution of Consecutive Prime Biases and Sums of Sawtooth Random Variables*, Proposition 3.1. https://rlemke01.math.tufts.edu/papers/18-DistributionSawtooth.pdf
- Zhoulin Cui and Zhishan Yang, *The distribution of greatest common divisors of binomial coefficients and their upper indices*, arXiv:2611.25794v1, submitted November 19, 2026, consulted only for overlap. https://arxiv.org/abs/2611.25794
