# Weight–length universality and sharp covariance zeros for composition patterns

## Finding

Choose uniformly an ordered positive-integer composition of \(N\ge1\). Let \(K_N\) be its number of parts. Fix an **exact** finite word \(b=(b_1,\ldots,b_r)\) of positive integers, with \(r\ge2\) and total weight \(w=\sum_{j=1}^r b_j\). For \(N\ge w\), let \(Y_{N,b}\) count all consecutive occurrences of that exact word, **including overlapping occurrences**. Write \(t=N-w\). Then

\[
\operatorname{Cov}(K_N,Y_{N,b})=
\begin{cases}
\dfrac{2r-w-1}{2^w},&t=0,\\[4pt]
\dfrac{(2r-w+1)t+6r-3w-1}{2^{w+2}},&t\ge1.
\end{cases}
\]

Thus the covariance depends only on the pair \((r,w)\), not on the word order, repetitions, or autocorrelation. Its **complete sign classification** is:

- If \(w<2r-1\), the covariance is strictly positive for all \(N\ge w\).
- If \(w=2r-1\), the covariance is zero at \(N=w\) and positive for all \(N>w\).
- If \(w=2r\), it is negative at \(N=w\), zero at \(N=w+1\), and positive for \(N\ge w+2\).
- If \(w>2r\), it is strictly negative for all \(N\ge w\).

The two zero-covariance cases are **not independence**: in both, the event \(Y_{N,b}>0\) fixes \(K_N\) at its unconditional mean, while \(K_N\) is nonconstant. In particular, the covariance is exactly \(-2^{-w}\), independent of \(N\), whenever \(w=2r+1\) and \(N>w\). For each fixed word,

\[
\lim_{N\to\infty}\frac{\operatorname{Cov}(K_N,Y_{N,b})}{N}
=\frac{2r-w+1}{2^{w+2}}.
\]

## Assumptions and scope

An ordered positive-integer composition of \(N\) is a finite tuple of positive integers summing to \(N\). Each of the \(2^{N-1}\) such tuples is equally likely; there are no restrictions on available part values. The word \(b\) is fixed, not an order-isomorphism class or an arbitrary subsequence. Its occurrences must use consecutive parts, and each start position contributes one even if occurrences overlap. The theorem is asserted for every integer \(r\ge2\), every such word, and every integer \(N\ge w\). When \(N<w\), the count is identically zero and so is its covariance; this trivial regime is excluded from the sign classification.

## Proof

Write \(A(z)=z/(1-z)\) for the ordinary part-weight generating function. Marking the number of parts by \(u\), the generating function of all compositions including the empty composition is

\[
C(z,u)=\frac1{1-uA(z)}=\frac{1-z}{1-(1+u)z}.
\]

Mark exactly one occurrence of \(b\). Removing its \(r\) parts partitions the rest uniquely into a left and a right composition. Conversely, any such two compositions and the inserted word give a marked occurrence. This bijection counts **occurrences** (not compositions containing at least one), so it is valid even for self-overlapping words. Consequently,

\[
\sum_{N\ge0}z^N\sum_{c\in\mathcal C_N}u^{K(c)}Y_{N,b}(c)
=u^r z^w C(z,u)^2.
\]

At \(u=1\), put \(C(z)=(1-z)/(1-2z)\). Differentiating at \(u=1\), with \(t=N-w\), gives

\[
\mathbb E[Y_{N,b}]
=\frac{[z^t]C(z)^2}{2^{N-1}},\qquad
\mathbb E[K_NY_{N,b}]
=\frac{[z^t]\bigl(rC(z)^2+2C(z)^3A(z)\bigr)}{2^{N-1}}.
\]

The independent-cut representation gives \(K_N\overset{d}=1+\operatorname{Bin}(N-1,1/2)\), hence \(\mathbb E[K_N]=(N+1)/2\). For \(t=0\), the two relevant coefficients are \(1\) and \(0\). For every integer \(t\ge1\), direct expansion of the two rational functions yields

\[
[z^t]C(z)^2=2^{t-2}(t+3),\qquad
[z^t]\,2C(z)^3A(z)=2^{t-3}(t^2+5t+2).
\]

Substituting these coefficients into \(\mathbb E[K_NY_{N,b}]-\mathbb E[K_N]\mathbb E[Y_{N,b}]\), and using \(N=w+t\), proves the displayed piecewise covariance identity. It also gives \(\mathbb E[Y_{N,b}]=2^{1-w}\) at \(t=0\), and \((t+3)/2^{w+1}\) at \(t\ge1\).

For the signs, put \(d=2r-w\). The numerator in the \(t=0\) case is \(d-1\); for \(t\ge1\) it is \((d+1)t+3d-1\). Since \(d\) is integral, considering \(d\ge2\), \(d=1\), \(d=0\), and \(d\le-1\) gives precisely the four cases above, with no other zeros. When \(d=1,t=0\), an occurrence occupies all the weight and forces \(K_N=r=(N+1)/2\). When \(d=0,t=1\), it leaves exactly one extra part of size one and forces \(K_N=r+1=(N+1)/2\). These events have positive probability, but \(K_N\) is nondegenerate for the relevant \(N\ge3\), proving non-independence. The fixed-covariance and limiting-slope assertions follow by substitution.

## Verification

The standalone file `checker.py` uses only Python's standard library. Running `python3 checker.py` enumerates every positive-integer composition of \(N=1,\ldots,12\), every consecutive exact word occurring in each, and checks the means, covariance identity, and sign cases with exact rational arithmetic. It executes 24,558 exact assertions. This enumeration separately checks finite cases; the rational generating-function coefficient proof above establishes the unrestricted integer ranges.

## Relationship to prior work

Heubach and Kitaev (2009) derive bivariate weight-and-part-length generating functions for *avoiding* fixed substrings, and Wilf (2009) and Gafni (2009) study longest equal-part runs. Bender and Canfield (2009) establish general asymptotic normality for local-event counts in restricted compositions. Shabani and Gjergji (2016) study order-isomorphic three-letter pattern statistics with repeated letters. These works motivate the local-occurrence setting, but the inspected statements do not give the exact all-word mixed covariance, its weight–length universality, the exhaustive sign phase diagram, or the zero-covariance/non-independence distinction. More general generating-function techniques may allow a derivation, so absence of an explicitly identified theorem is not proof of historical novelty. The single-part \(r=1\) case is excluded from the new claim and can be approached using standard part-frequency moments.

## Limitations

The theorem addresses **uniform, unrestricted** compositions and the mixed covariance of an exact consecutive-word count with the total part count; it does not determine the pattern-count variance, distribution, higher-order dependencies, or covariance for nonuniform/composition-conditioned laws. Independence is ruled out only at the characterized zero-covariance cases. The assessed novelty concerns the explicit combined classification and must be considered provisional pending independent historical review.

## References

- Silvia Heubach and Sergey Kitaev, *Avoiding substrings in compositons*, arXiv:0903.5135, first submitted March 30, 2009. https://arxiv.org/abs/0903.5135
- Herbert S. Wilf, *The distribution of longest run lengths in integer compositions*, arXiv:0906.5196, first submitted June 29, 2009. https://arxiv.org/abs/0906.5196
- Ayla Gafni, *Longest Run of Equal Parts in a Random Integer Composition*, arXiv:0907.5553, first submitted July 31, 2009. https://arxiv.org/abs/0907.5553
- Edward A. Bender and E. Rodney Canfield, *Locally Restricted Compositions II. General Restrictions and Infinite Matrices*, Electronic Journal of Combinatorics 16 (2009), R108. https://doi.org/10.37236/197
- Armend Shabani and Rexhep Gjergji, *Statistics for 3-letter patterns with repetitions in compositions*, Discrete Mathematics & Theoretical Computer Science 17 (2016), 147–166. https://doi.org/10.46298/dmtcs.2156
