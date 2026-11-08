# Exact return–maximum anticorrelation in tied-down simple random walks

## Finding

For every integer \(n\ge1\), let \((S_t)_{0\le t\le2n}\) be a uniformly chosen nearest-neighbor walk on the integers with \(S_0=S_{2n}=0\): precisely, choose uniformly among the \(\binom{2n}{n}\) sequences with \(n\) increments \(+1\) and \(n\) increments \(-1\). Define the number of completed excursions (positive-time returns to the origin) and the one-sided maximum by
\[
K_n=\#\{t\in\{1,\ldots,2n\}:S_t=0\},\qquad
M_n=\max_{0\le t\le2n}S_t.
\]
Put \(R_n=4^n/\binom{2n}{n}\). The mixed and marginal moments are **exactly**
\[
\begin{aligned}
\mathbb E K_n&=R_n-1,& \mathbb E M_n&=(R_n-1)/2,\\
\mathbb E(K_nM_n)&=3n/2+1-R_n,\\
\operatorname{Var}(K_n)&=4n+2-R_n-R_n^2,\\
\operatorname{Var}(M_n)&=(4n+1-R_n^2)/4.
\end{aligned}
\]
Consequently
\[
\boxed{\operatorname{Cov}(K_n,M_n)=\frac{3n+1-R_n^2}{2}.}
\]
The covariance vanishes at \(n=1\), is **strictly negative for every \(n\ge2\)**, and obeys
\[
\lim_{n\to\infty}\frac{\operatorname{Cov}(K_n,M_n)}n=\frac{3-\pi}{2},
\quad
\lim_{n\to\infty}\operatorname{Corr}(K_n,M_n)=\frac{3-\pi}{4-\pi}.
\]
The correlation is defined in the second limit for \(n\ge2\). The maximum is **one-sided**, not the absolute maximum, and the endpoint is counted in \(K_n\).

## Assumptions and scope

All paths have even length \(2n\) and are conditioned to return to the origin; \(n\) is an arbitrary positive integer. There is no continuous-time interpolation or nonzero drift. The conditioning makes all \(\binom{2n}{n}\) bridge paths equally likely. Every exact identity is finite and requires no limiting probability theorem. The terminal return at time \(2n\) contributes one to \(K_n\).

## Proof

**1. Maximum-capped bridge generating functions.** Use the formal variable \(z\) for semilength. Write
\[
s=\sqrt{1-4z},\qquad B(z)=\frac1s,
\qquad q(z)=\frac{1-s}{1+s}.
\]
Thus \([z^n]B=\binom{2n}{n}\). For an integer \(h\ge0\), let \(B_h(z)\) count bridges whose maximum is at most \(h\). Reflect a bridge from its first arrival at \(h+1\) about level \(h+1\). This bijection sends a path with endpoint zero and maximum greater than \(h\) to a path ending at \(2(h+1)\). Accordingly,
\[
[z^n](B-B_h)=\binom{2n}{n+h+1},
\qquad B_h=B(1-q^{h+1}). \tag{1}
\]
The last equality follows by the Catalan generating-function identity \([z^n]Bq^r=\binom{2n}{n+r}\) for \(r\ge1\), interpreted as zero when \(r>n\).

**2. Marking complete excursions.** A bridge with maximum at most \(h\) is a unique ordered concatenation of nonempty first-return excursions, each also capped at \(h\). Their generating function is \(E_h=1-B_h^{-1}\), and the bivariate generating function with each completed excursion marked by \(u\) is
\[
F_h(z,u)=\frac1{1-uE_h(z)}.
\]
At \(u=1\), differentiate to obtain
\[
\partial_u F_h(z,1)=B_h^2-B_h. \tag{2}
\]
In the uncapped case \(B_h\to B\), so
\[
[z^n]\mathbb E K_n\binom{2n}{n}
=[z^n](B^2-B)=4^n-\binom{2n}{n}.
\]

**3. The maximum and the mixed moment.** For any nonnegative integer-valued maximum, sum its level-exceedance indicators. From (1),
\[
\mathbb E M_n\binom{2n}{n}
=[z^n]\sum_{r\ge1}(B-B_{r-1})
=[z^n]\frac{Bq}{1-q}.
\]
The rationalized expression is \(Bq/(1-q)=1/(2s^2)-1/(2s)\), giving \(\mathbb E M_n=(R_n-1)/2\).

Similarly, by (2), the generating function of \(K_n\mathbf1_{\{M_n\ge r\}}\) is the difference between uncapped and capped marked-bridge derivatives. Summing \(r\ge1\) gives
\[
\begin{aligned}
\mathbb E(K_nM_n)\binom{2n}{n}
&=[z^n]\sum_{r\ge1}\bigl[(B^2-B)-(B_{r-1}^2-B_{r-1})\bigr]\\
&=[z^n]\left(\frac{2B^2q}{1-q}-\frac{B^2q^2}{1-q^2}-\frac{Bq}{1-q}\right)\\
&=[z^n]\left(\frac3{4s^3}-\frac1{s^2}+\frac1{4s}\right).
\end{aligned}
\]
Since \([z^n]s^{-3}=(2n+1)\binom{2n}{n}\), this is \(\mathbb E(K_nM_n)=3n/2+1-R_n\).

**4. Marginal second moments.** Twice differentiating \(F(z,u)=1/(1-u(1-1/B))\) yields the factorial-second-moment generating function \(2(B^3-2B^2+B)\). Coefficient extraction and the previously calculated mean give
\[
\mathbb E K_n^2=4n+3-3R_n.
\]
For the maximum, the tail-square identity and (1) give
\[
\mathbb E M_n^2=\frac1{\binom{2n}{n}}
\sum_{r=1}^{n}(2r-1)\binom{2n}{n+r}=n+\frac12-\frac{R_n}2.
\]
Here the sum uses \(\sum_{r=1}^{n}r\binom{2n}{n+r}=n\binom{2n}{n}/2\) and \(\sum_{r=1}^{n}\binom{2n}{n+r}=(4^n-\binom{2n}{n})/2\). Subtracting squared means proves the variance and covariance formulas.

**5. Strict sign and limits.** At \(n=1\), \(R_1^2=4=3(1)+1\). For every \(n\ge1\),
\[
\frac{R_{n+1}^2/(3n+4)}{R_n^2/(3n+1)}
=1+\frac{n}{(2n+1)^2(3n+4)}>1.
\]
Thus \(R_n^2>3n+1\) for all \(n\ge2\). Finally \(R_n\sim\sqrt{\pi n}\) by Stirling's formula, so the covariance divided by \(n\) tends to \((3-\pi)/2\). The variances divided by \(n\) tend to \(4-\pi\) and \((4-\pi)/4\), respectively, which establishes the correlation limit.

## Verification

The standalone `verify.py` requires Python 3.9+ and only the standard library. Run `python verify.py` in the directory containing this result. It independently computes exact bridge moments by dynamic programming for every \(1\le n\le40\) and by enumerating all \(\binom{2n}{n}\) bridge sequences for \(1\le n\le9\), comparing all eight displayed moment/covariance/variance identities as exact rational numbers. It tests the finite sign classification separately. The checks are independent corroboration; the coefficient-extraction and induction arguments above prove the infinite statements.

## Relationship to prior work

Pitman (1998) develops the Brownian-bridge local-time distribution and relevant Lévy/reflection identities; these describe limiting objects but do not give the finite discrete mixed moment or the stated finite sign law in the inspected report. Lindell and Holst (2007) analyze ranked **excursion durations** in tied-down random walks, not the **spatial height maximum** jointly with the number of returns. Voss (2007) treats the return-count distribution of random-walk bridges. The new result combines the two distinct bridge observables and identifies their exact covariance at every length, including the nontrivial negative correlation limit. General renewal and reflection methods underlie the proof and create a residual risk of implicit coverage by earlier broad enumerative identities.

## Limitations

The theorem concerns nearest-neighbor symmetric bridges and the one-sided maximum only. It does not assert negative association for all increasing functions of the two statistics, or independence/monotone regression; a negative covariance is strictly weaker. The finite formulas do not directly extend to biased conditioned bridges, higher-dimensional walks, or absolute maxima. The continuous asymptotic correlation is a consequence of finite moments here, not a claim of a new Brownian limit theorem. Historical originality is a best-knowledge literature assessment, not proof of first discovery; an older general bivariate path enumeration could imply the formula without explicitly naming this covariance.

## References

1. J. Pitman, *The distribution of local times of a Brownian bridge*, UC Berkeley Department of Statistics Technical Report 539, November 3, 1998. https://live-statistics.pantheon.berkeley.edu/sites/default/files/tech-reports/539.pdf
2. A. Lindell and L. Holst, *Distributions of the longest excursions in a tied down simple random walk and in a Brownian bridge*, Journal of Applied Probability 44 (2007), 1056–1067. https://doi.org/10.1239/jap/1197908824
3. J. Voss, *Random walk bridges*, October 17, 2007. https://www.seehuhn.de/blog/6.html
