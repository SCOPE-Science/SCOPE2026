# Exact dual containment-frontier means for random intervals

## Finding

Consider independent intervals formed by pairing independently sampled real endpoints from the same continuous distribution. Inclusion defines two natural irredundant frontiers: an interval is **minimal** if it contains none of its peers, and **maximal** if it is contained in none. Despite being the two opposite frontiers of one containment relation, their expected sizes have different growth scales.

For every integer \(n\ge1\), let \(A_n\) and \(B_n\) be the numbers of inclusion-minimal and inclusion-maximal intervals, respectively. Their exact means are
\[
\mathbb E A_n=\sqrt\pi\,\frac{\Gamma(n+1)}{\Gamma(n+\tfrac12)}-1,
\qquad
\mathbb E B_n=\sum_{j=0}^{n-1}\frac{1}{2^j}\sum_{k=0}^j\frac{\binom jk}{2k+1}.
\]
The integrals and these sums are valid for every continuous parent distribution, not just the uniform law. Moreover,
\[
\begin{aligned}
\mathbb E A_n&=\sqrt{\pi n}-1+O(n^{-1/2}),\\
\mathbb E B_n&=\log n+\gamma+\log2+O(n^{-1}),
\end{aligned}
\]
and consequently
\[
\frac{\mathbb E A_n}{\mathbb E B_n}\sim\frac{\sqrt{\pi n}}{\log n}.
\]
Here \(\gamma\) denotes Euler's constant. This is a sharp contrast between the two expected frontier sizes; the theorem does not claim a corresponding ratio for realized random counts.

## Assumptions and scope

Let \(n\ge1\) and let \(X_1,Y_1,\ldots,X_n,Y_n\) be independent with a common continuous cumulative distribution function \(F\) on the real line. Define \(I_i=[\min(X_i,Y_i),\max(X_i,Y_i)]\). Almost surely all endpoints are distinct. Interval \(I_i\) is inclusion-minimal if there is no \(j\ne i\) with \(I_j\subsetneq I_i\), and inclusion-maximal if no \(j\ne i\) has \(I_i\subsetneq I_j\). No independence between the two frontier counts is assumed. The primary mathematical classification is geometric probability, MSC2020 60D05.

The probability integral transform \(F\) preserves all sampled strict endpoint orders almost surely. Consequently it suffices to take the endpoints independent and uniform on \((0,1)\). Sorting the \(2n\) endpoints also identifies this model with a uniformly random matching of \(2n\) ordered points; nested matching arcs represent interval containment.

## Proof

Write \(U=\min(X,Y)\) and \(V=\max(X,Y)\) after transforming to uniform endpoints. Their joint density is \(2\) on the triangle \(0<u<v<1\). Conditional on \((U,V)=(u,v)\), the probability that a fresh interval lies properly **inside** \([u,v]\) equals \((v-u)^2\), and that it properly **contains** \([u,v]\) equals \(2u(1-v)\). Conditioning on one interval and using linearity of expectation yields the exact integral identities
\[
\begin{aligned}
\mathbb E A_n&=2n\int_0^1\!\int_u^1(1-(v-u)^2)^{n-1}\,dv\,du,\\
\mathbb E B_n&=2n\int_0^1\!\int_u^1(1-2u(1-v))^{n-1}\,dv\,du.
\end{aligned}
\]
For the first, substitute \(d=v-u\) and exchange integration order:
\[
\mathbb E A_n=2n\int_0^1(1-d)(1-d^2)^{n-1}\,dd=n\,\mathrm B(\tfrac12,n)-1
=\sqrt\pi\,\frac{\Gamma(n+1)}{\Gamma(n+\tfrac12)}-1.
\]
The beta–gamma identity and standard gamma-ratio asymptotics give the first asymptotic expansion.

For the second, integrating in \(v\) gives
\[
\mathbb E B_n=\int_0^1\frac{1-[1-2u(1-u)]^n}{u}\,du.
\]
The numerator is symmetric in \(u\) and \(1-u\). Set \(s=1-2u\) on the first half, and \(Q(s)=(1+s^2)/2\). Then
\[
\mathbb E B_n=\int_0^1\frac{2(1-Q(s)^n)}{1-s^2}\,ds
=\int_0^1\sum_{j=0}^{n-1}Q(s)^j\,ds
=\sum_{j=0}^{n-1}\frac1{2^j}\sum_{k=0}^j\frac{\binom jk}{2k+1}.
\]
All terms are finite, so the interchange of sums and integration is immediate.

For its asymptotic constant, use the exact splitting \(2/(1-s^2)=1/(1-s)+1/(1+s)\). With \(H_n=\int_0^1(1-s^n)/(1-s)\,ds\),
\[
\mathbb E B_n-H_n
=-\int_0^1\frac{Q(s)^n-s^n}{1-s}\,ds
+\int_0^1\frac{1-Q(s)^n}{1+s}\,ds.
\]
Since \(Q(s)-s=(1-s)^2/2\), \(Q(s)\le e^{-(1-s)/2}\), and \(Q(s)\ge s\), the first integral in absolute value is at most
\[
\frac n2\int_0^1(1-s)e^{-(n-1)(1-s)/2}\,ds=O(n^{-1}).
\]
The second integral equals \(\log2+O(n^{-1})\), because the omitted term is bounded by \(\int_0^1e^{-n(1-s)/2}\,ds\). Finally \(H_n=\log n+\gamma+O(n^{-1})\). This proves the second expansion and their ratio.

## Verification

The included standard-library script `verify.py` enumerates every perfect matching on \(2n\) ordered endpoints for \(1\le n\le7\), counts both kinds of arcs and compares the exact rational averages with the two formulas. It also tests the rational values through \(n=20\). Its finite computations illustrate and check the formulas but do not replace the proof of the all-size identities or asymptotic estimates. For instance the expected minimal and maximal counts are both \(5/3\) at \(n=2\), and are respectively \(11/5\) and \(32/15\) at \(n=3\).

Run `python verify.py` from a directory containing that file.

## Relationship to prior work

Justicz, Scheinerman, and Winkler (1990) introduce the same independent-endpoint random-interval model and study maximum collections of pairwise **disjoint** intervals and the event that one interval meets every other. Those properties concern intersection/disjointness rather than the number of intervals irredundant under inclusion. Its abstract was inspected; complete text access was unavailable, so an unrecognized contained-interval consequence remains possible.

Chen, Deng, Du, Stanley, and Yan (2005) study the largest *depth* of crossing and nesting systems of arcs in random matchings and partitions. Their notion of minimal/maximal **block elements** refers to endpoint labels, not inclusion-minimal/maximal arcs. Their full text was inspected via an openly displayed author manuscript. Neither its explicit crossing–nesting distribution symmetry nor its maximal nesting-size statistics give the present two expected numbers directly. The change of viewpoint from nesting depth to the sizes of the outer and inner nesting **frontiers** is essential.

Under \([u,v]\mapsto(-u,v)\), inclusion-maximal intervals become Pareto-maximal points, but their underlying two-coordinate law is supported on a triangle and is not a product distribution. Thus the familiar independent-coordinate square-record mean is not an immediate equivalent of the formula here.

## Limitations

Only the exact means and their asymptotic scales are established. No variance bound, concentration theorem, distributional limit, stochastic domination, or strict all-size comparison between the two random counts is asserted. The simultaneous-frontier comparison has not been independently audited. The older 1990 primary paper was inspected only at the abstract level; historical priority beyond the sources inspected remains uncertain.

## References

1. J. Justicz, E. R. Scheinerman, and P. M. Winkler, *Random Intervals*, American Mathematical Monthly 97 (1990), 881–889. DOI: https://doi.org/10.1080/00029890.1990.11995679
2. W. Y. C. Chen, E. Y. P. Deng, R. R. X. Du, R. P. Stanley, and C. H. Yan, *Crossings and Nestings of Matchings and Partitions*, arXiv:math/0501230 (first public arXiv version 2005-01-14), https://arxiv.org/abs/math/0501230
