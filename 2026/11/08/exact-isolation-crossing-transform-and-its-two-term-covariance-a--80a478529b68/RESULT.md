# Exact isolation–crossing transform and its two-term covariance asymptotic in random chord diagrams

## Finding

Let \(\mathcal M_n\) be the set of perfect matchings of \(2n\) clockwise-labelled points on a circle, uniformly sampled, and let \(X_n\) be the number of unordered pairs of crossing chords. Let \(J_n\) be the number of isolated chords: a chord is isolated precisely when no other chord crosses it (equivalently, it is an isolated vertex of the intersection graph). Define the unnormalized crossing polynomial
\[
Q_m(z)=\sum_{\pi\in\mathcal M_m}z^{X_m(\pi)},\qquad Q_0(z)=1.
\]
For every integer \(n\ge1\) and every complex \(z\), the complete mixed first-moment transform is
\[
\boxed{\mathbb E[J_nz^{X_n}]=\frac{n}{(2n-1)!!}\sum_{a=0}^{n-1}Q_a(z)Q_{n-1-a}(z).}\tag{1}
\]
Set \(b=n-1-a\) and \(p_{n,a}=(2a-1)!!(2b-1)!!/(2n-1)!!\), with \((-1)!!=1\). Differentiating at \(z=1\) gives
\[
\boxed{\operatorname{Cov}(J_n,X_n)=-\frac n3\sum_{a=0}^{n-1}p_{n,a}\bigl(n-1+a(n-1-a)\bigr).}\tag{2}
\]
Consequently the covariance vanishes for \(n=1\), is strictly negative for every integer \(n\ge2\), and obeys the two-term expansion
\[
\boxed{\operatorname{Cov}(J_n,X_n)=-\frac n3-\frac16+O(n^{-1})\qquad(n\to\infty).}\tag{3}
\]
Equation (1) also determines all mixed moments \(\mathbb E[J_n(X_n)_{\underline r}]\) through derivatives of the known crossing polynomials, not only the covariance.

## Assumptions and scope

Endpoints are distinguishable and have a fixed cyclic order; each perfect matching is equally likely. Crossing is strict cyclic alternation of chord endpoints. An isolated chord need not have adjacent endpoints. In particular, the isolated count \(J_n\) is not the simple-chord count. The formulas are exact for all finite integers \(n\ge1\); the expansion concerns the limit along integers. The polynomial variable \(z\) may be arbitrary complex; formulas follow by finite polynomial identities. Acan (2015), first publicly posted on January 7, 2015, is a probabilistic study of the model and explicitly lists primary MSC 60C05. Earlier graph-theoretic literature supplies additional scientific context.

## Proof

**1. Circular isolated-chord decomposition.** A specified chord cuts the remaining \(2n-2\) endpoints into two open arcs. An isolated chord must enclose an even number \(2a\) of endpoints on one arc and \(2b\) on the other, with \(a+b=n-1\); otherwise some chord would cross it. On the isolation event, the two sets are matched internally, independently and uniformly; no cross-arc crossing occurs. Therefore, if \(\mathcal E_{i,a}\) denotes the event that endpoints \(i\) and \(i+2a+1\) (cyclic indices) form an isolated chord, then
\[
\sum_{\pi:\mathcal E_{i,a}}z^{X_n(\pi)}=Q_a(z)Q_b(z).
\]
Each undirected chord is indexed exactly twice among the \(2n\) choices of \(i\) and the \(n\) choices of \(a\): once in either orientation. Thus summing and dividing by two gives the weighted matching identity
\[
\sum_{\pi\in\mathcal M_n}J_n(\pi)z^{X_n(\pi)}
=n\sum_{a=0}^{n-1}Q_a(z)Q_{n-1-a}(z),
\]
and (1) follows by the total matching count \((2n-1)!!\). This is a finite identity of polynomials, with no convergence assumption.

**2. Exact covariance.** Among any four labelled points in cyclic order, the event that their two crossing pairs occur has probability \(1/((2n-1)(2n-3))\). Summation over all four-point sets yields \(\mathbb E X_n=n(n-1)/6\), including the empty- and one-chord cases. Given any particular isolated chord with \(2a\) and \(2b\) endpoints on its two sides, the independent residual diagrams contribute
\[
\mathbb E[X_n\mid\mathcal E_{i,a}]
=\frac{a(a-1)+b(b-1)}6,
\]
so that
\[
\mathbb E[X_n\mid\mathcal E_{i,a}]-\mathbb E X_n
=-\frac{n-1+ab}{3}.
\]
The isolation event has probability \(p_{n,a}\). Since \(J_n\) sums the indicators of all distinct isolated chords, the covariance is the sum of these weighted conditional differences. The same double-counting yields (2). Every summand is positive before its leading negative sign whenever \(n\ge2\), proving strict negativity. At \(n=1\), both \(X_n\) and the covariance are zero.

**3. Controlled two-term expansion.** Write
\[
U_n=\sum_{a=0}^{n-1}p_{n,a},\qquad V_n=\sum_{a=0}^{n-1}a(n-1-a)p_{n,a}.
\]
The terms are symmetric in \(a\) and \(n-1-a\), and
\[
p_{n,0}=\frac1{2n-1},\quad p_{n,1}=\frac1{(2n-1)(2n-3)},\quad
p_{n,2}=\frac3{(2n-1)(2n-3)(2n-5)}.
\]
For \(0\le a<(n-1)/2\),
\[
\frac{p_{n,a+1}}{p_{n,a}}=\frac{2a+1}{2(n-1-a)-1}.
\]
This ratio is at most \(1/2\) throughout \(2\le a\le\lfloor n/4\rfloor-1\) for all sufficiently large \(n\). Up to that index the tail starting at \(a=2\) is geometrically bounded by a constant times \(p_{n,2}=O(n^{-3})\), even after multiplication by \(a\). From \(\lfloor n/4\rfloor\) to the midpoint, the terms are decreasing and bounded by an exponentially small multiple of \(p_{n,2}\), so the remaining (polynomially many and polynomially weighted) terms are negligible. Symmetry therefore proves, with genuine uniform error bounds,
\[
U_n=2p_{n,0}+2p_{n,1}+O(n^{-3}),\qquad
V_n=2(n-2)p_{n,1}+O(n^{-2}).
\]
The leading part of \((n-1)U_n\) simplifies exactly:
\[
(n-1)\bigl(2p_{n,0}+2p_{n,1}\bigr)
=\frac{4(n-1)^2}{4(n-1)^2-1}=1+O(n^{-2}).
\]
Also \(V_n=1/(2n)+O(n^{-2})\). Inserting these expansions into (2) yields (3).

## Verification

The standalone `verify.py` enumerates **all** perfect matchings with up to seven chords (there are \(135135\) matchings at seven chords), counts isolated chords and crossings directly, and compares the exact weighted polynomial coefficient-by-coefficient against (1). It independently checks (2) using exact rational arithmetic and tests the sign through \(n=249\). The recorded local replay passed 339 exact assertions. Enumeration is finite validation of the implementation, not a substitute for the preceding all-order proof. Reproduce with `python3 verify.py` using only the Python standard library.

## Relationship to prior work

Flajolet and Noy (2000) derive the component-count generating function in their Section 1 and the marginal Touchard–Riordan crossing polynomial and its moments in Section 2. Their displayed formulas do not combine the isolated-component count with the crossing polynomial. Acan and Pittel (2014) study a sparse-crossing conditioning and giant-component questions; that conditioning does not supply the unconditional isolation-weighted polynomial (1). Acan (2015), particularly Sections 2 and 3, treats the degree distribution and the limiting behavior of chord lengths and simple components, rather than the displayed cross-statistic. Paguyo (2021, revision 2023) studies separate quantitative limits for crossings and simple chords, not the mixed isolated-chord transform. This is a statement-level comparison, not an assertion of absolute priority. A broader, unlocated multivariate generating-function treatment could implicitly cover (1), and should be checked independently.

## Limitations

The result concerns one isolation-weighted factor: it does not establish the full joint distribution of \((J_n,X_n)\), nor asymptotic independence or a central limit theorem for a bivariate normalization. The expansion has an unspecified but rigorously bounded \(O(n^{-1})\) remainder. No independent audit or historical-priority certification has been performed. Full-text searches and inspected passages cannot exclude every equivalent formulation in the wider literature.

## References

1. P. Flajolet and M. Noy, *Analytic Combinatorics of Chord Diagrams*, INRIA RR3914, March 2000 (publicly accessible text; the document date is not asserted to be the exact day of first public availability). https://algo.inria.fr/flajolet/Publications/FlNo00.pdf
2. H. Acan and B. Pittel, *Formation of a giant component in the intersection graph of a random chord diagram*, arXiv:1406.2867, first posted June 11, 2014. https://arxiv.org/abs/1406.2867
3. H. Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489, first posted January 7, 2015. https://arxiv.org/abs/1501.01489
4. J. E. Paguyo, *Convergence rates of limit theorems in random chord diagrams*, arXiv:2104.01134, first posted April 2, 2021. https://arxiv.org/abs/2104.01134
