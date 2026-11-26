# A nonvanishing crossing-covariance footprint of rare isolated chords

## Finding

In a uniformly random chord diagram with \(n\ge2\) chords, let \(X_n\) count crossing pairs, \(Y_n\) count chords crossed by no other chord, \(S_n\) count chords joining two cyclically consecutive endpoints, and \(Z_n=Y_n-S_n\) count isolated chords that are not cyclically consecutive. Define \((-1)!!=1\), and for \(0\le r\le n-1\) put
\[
w_{n,r}=\frac{(2r-1)!!(2n-2r-3)!!}{(2n-1)!!}.
\]
Then the *joint crossing–isolation covariance law* is exact for every integer \(n\ge2\):
\[
\begin{aligned}
\mathbb E Z_n&=n\sum_{r=1}^{n-2}w_{n,r},\\
\operatorname{Cov}(X_n,Z_n)&=-\frac n3\sum_{r=1}^{n-2}w_{n,r}\bigl(n-1+r(n-1-r)\bigr),\\
\operatorname{Cov}(X_n,S_n)&=-\frac{2n(n-1)}{3(2n-1)},\\
\operatorname{Cov}(X_n,Y_n)&=-\frac n3\sum_{r=0}^{n-1}w_{n,r}\bigl(n-1+r(n-1-r)\bigr).
\end{aligned}
\]
Empty sums are zero. In particular, \(\operatorname{Cov}(X_n,Y_n)<0\) for every \(n\ge2\), and \(\operatorname{Cov}(X_n,Z_n)<0\) for \(n\ge3\). The rare non-simple isolates have the asymptotics
\[
\boxed{\mathbb E Z_n=\frac1{2n}+O(n^{-2}),\qquad
\operatorname{Cov}(X_n,Z_n)=-\frac13+O(n^{-1}).}
\]
Consequently, despite \(Z_n\to0\) in probability,
\[
\boxed{\operatorname{Cov}(X_n,Y_n)=-\frac n3-\frac16+O(n^{-1}).}
\]
The constant-order covariance contribution \(-1/3\) of the vanishingly rare nonsimple isolates distinguishes the total-isolate statistic from the count of simple chords.

## Assumptions and scope

Take \(2n\) distinct points labelled \(0,1,\ldots,2n-1\) clockwise on a circle, and choose a perfect matching uniformly among \((2n-1)!!\) matchings. Each matched pair is a chord. Two chords cross if their endpoints alternate in cyclic order. A chord is *isolated* if it crosses no other chord; a *simple* chord joins cyclically consecutive labels. Every simple chord is isolated, so \(Z_n\) is a nonnegative integer. The claims hold without conditioning and without restrictions on diagram connectivity. The probability model and the word *isolated* refer to the intersection graph, not to an independently sampled set of geometric line segments.

## Proof

**Conditioning on one isolated chord.** Fix a possible chord joining endpoints \(a<b\). The open arc from \(a\) to \(b\) contains \(b-a-1\) points. This chord is present and isolated precisely when those points and the points on the complementary open arc are separately perfectly matched. Consequently, the event is impossible unless \(b-a-1=2r\) for some \(0\le r\le n-1\). Writing \(s=n-1-r\), its probability is \(w_{n,r}\). Conditioned on the event, the two arc matchings are independent and uniform, containing \(r\) and \(s\) chords respectively. No crossing can involve two distinct arcs or the distinguished isolated chord.

For any two chords of a uniform matching, their four cyclically ordered endpoints admit three equiprobable pairings and exactly one pairing crosses. Thus the unconditional mean crossing count is
\[
\mathbb E X_n=\frac13\binom n2=\frac{n(n-1)}6.
\]
The conditional mean under the specified isolated chord is
\[
\mathbb E[X_n\mid (a,b)\text{ is isolated}]
=\frac13\left(\binom r2+\binom s2\right).
\]
The exact deficit relative to the unconditional mean is
\[
\frac13\left(\binom r2+\binom s2-\binom n2\right)
=-\frac{n-1+rs}{3}.
\]

**Summing all possible isolated chords.** For a fixed \(r\), the number of pairs \(a<b\) with \(b-a-1=2r\) is \(2(n-1-r)+1=2s+1\). Every summand used below is symmetric under \(r\leftrightarrow s\), while
\[
(2s+1)+(2r+1)=2n.
\]
Thus summing the expected isolated-chord indicator, or its covariance with \(X_n\), is equivalent to replacing the multiplicity \(2s+1\) with \(n\) and summing over \(r=0,\ldots,n-1\). Linearity of covariance yields the stated formulas for \(Y_n\). The simple-chord cases are exactly \(r=0\) and \(r=n-1\); their probabilities equal \(1/(2n-1)\). Removing them yields the formulas for \(Z_n\) and the displayed formula for \(S_n\). Every nonzero summand in the covariance formulas is strictly negative, proving the sign statements.

**Sharp sparse-isolate contribution.** For \(n\ge4\), the two first nonsimple terms, \(r=1\) and \(r=n-2\), each have
\[
w_{n,1}=\frac1{(2n-1)(2n-3)}.
\]
Their total contributions to \(\mathbb E Z_n\) and \(\operatorname{Cov}(X_n,Z_n)\) are respectively
\[
\frac{2n}{(2n-1)(2n-3)}\quad\text{and}\quad
-\frac{2n}{3(2n-1)}.
\]
We show that all remaining terms contribute only \(O(n^{-2})\) to the mean and \(O(n^{-1})\) to the covariance. In the notation \(L=n-1\), the symmetric weights satisfy
\[
\frac{w_{n,r+1}}{w_{n,r}}=\frac{2r+1}{2(L-r)-1}.
\]
For large \(L\), this ratio is at most \(1/2\) when \(2\le r\le\lfloor L/4\rfloor\), and the weights decrease until the middle of the range. Since
\[
w_{n,2}=\frac3{(2n-1)(2n-3)(2n-5)}=O(n^{-3}),
\]
the geometric bound near each endpoint and the exponentially small middle establish
\[
\sum_{r=2}^{n-3}w_{n,r}=O(n^{-3}),\qquad
\sum_{r=2}^{n-3}r(n-1-r)w_{n,r}=O(n^{-2}).
\]
For completeness, the first bound follows by summing a geometric series up to \(L/4\), bounding the next \(O(L)\) weights by \(w_{n,2}2^{-\lfloor L/4\rfloor+2}\), and reflecting. For the second bound, multiply near-endpoint terms by at most \(Lr\) and use \(\sum_{r\ge2}r2^{-(r-2)}<\infty\); middle terms remain negligible after multiplication by \(O(L^3)\). The finitely many small values of \(n\) affect none of these asymptotic estimates.

Substitution proves \(\mathbb E Z_n=(2n)/((2n-1)(2n-3))+O(n^{-2})\) and \(\operatorname{Cov}(X_n,Z_n)=-2n/(3(2n-1))+O(n^{-1})\). Finally the exact simple-chord formula gives
\[
\operatorname{Cov}(X_n,S_n)=-\frac n3+\frac16+O(n^{-1}),
\]
so adding the \(Z_n\) contribution proves the stated asymptotic for \(\operatorname{Cov}(X_n,Y_n)\).

## Verification

The standalone standard-library Python script `chord_cov_verify.py` enumerates every perfect matching of \(2n\) labelled cyclic endpoints for \(n=2,\ldots,7\), independently computes crossings, zero-crossing chords and simple chords, and compares exact rational moments and covariances with the formulas above. All \(146598\) diagrams across these six sizes were checked. These finite checks corroborate the formulas but do not prove them outside the enumerated range; the complete proof is the combinatorial conditioning and asymptotic argument above.

## Relationship to prior work

Flajolet and Noy (2000) derived the marginal component and crossing laws for random chord diagrams. Acan (first posted January 2015, primary MSC \(60\mathrm C05\)) analyzed random chord degrees and the emergence of monolithic diagrams, in which isolated components become asymptotically simple. Courtiel–Yeats–Zeilberger (first posted November 2016), in their Theorem 50, refined crossing-count generating functions by top-chord counts for connected or indecomposable diagrams; a top chord is not an isolated vertex of the intersection graph. Paguyo (first posted April 2021) established quantitative marginal normal approximation for crossings and Poisson approximation for simple chords. The present statement concerns instead the **exact mixed covariance** between all isolated chords and crossings and identifies the finite order-of-one contribution of the exceptional nonsimple isolates. The cited marginal results do not, as stated, imply this correction constant. The underlying combinatorial decomposition is compatible with those papers.

## Limitations

The result concerns uniform perfect matchings of fixed cyclic endpoints only; it does not address biased matchings, intersections of independently selected geometric chords, or a joint Poisson–Gaussian convergence rate. The asymptotic error terms are stated with implicit constants, not optimized explicit error bounds. Computations are finite corroboration, not external proof certification. An equivalent mixed-moment identity may be implicit in a multivariate enumeration not identified here; the literature comparison cannot establish absolute novelty or independent verification.

## References

- P. Flajolet and M. Noy, *Analytic Combinatorics of Chord Diagrams*, INRIA RR-3914 (March 2000), Sections 1–2. https://algo.inria.fr/flajolet/Publications/FlNo00.pdf
- H. Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489, posted 2015-01-07; in particular Sections 2–3. https://arxiv.org/abs/1501.01489
- J. Courtiel, K. Yeats and N. Zeilberger, *Connected chord diagrams and bridgeless maps*, arXiv:1611.04611, first posted 2016-11-14; Section 6.2, Theorem 50. https://arxiv.org/abs/1611.04611
- J. E. Paguyo, *Convergence rates of limit theorems in random chord diagrams*, arXiv:2104.01134, first posted 2021-04-02; Sections 2–3. https://arxiv.org/abs/2104.01134
