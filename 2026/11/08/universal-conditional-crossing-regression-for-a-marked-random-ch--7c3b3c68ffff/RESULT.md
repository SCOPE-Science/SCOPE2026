# Universal conditional crossing regression for a marked random chord

## Finding

Fix a chord in a uniformly random circular pairing. Conditional on the number of other chords crossing that marked chord, the expected number of crossings *among the other chords* is exactly affine. Its slope is universal: it depends on the total number of chords and **not** on the geometric position of the marked chord.

For every feasible degree \(t\),
\[
\mathbb{E}[Y\mid e\text{ present},D=t]
=\frac{a(a-2)+b(b-2)}{24}+\frac{2n-3}{12}t.
\]
Consequently, for the total crossing count \(K=Y+D\),
\[
\mathbb{E}[K\mid e\text{ present},D=t]
=\frac{a(a-2)+b(b-2)}{24}+\frac{2n+9}{12}t.
\]
The second equality is the same structural statement expressed as the edge count of the full intersection graph.

## Assumptions and scope

Let \(n\ge3\) be an integer. A chord diagram is a perfect matching of \(2n\) distinctly labeled, cyclically ordered points, sampled uniformly over all \((2n-1)!!\) matchings. Let \(e\) be a specified pair of endpoints and condition on its inclusion. There are \(a\) points strictly between the endpoints of \(e\) in one open circle arc and \(b=2n-2-a\) in the other. The conditional law on the remaining \(2n-2\) points is uniform.

Let \(D\) count other chords with one endpoint on each open arc, \(Y\) count pairs of *remaining* chords whose endpoints alternate cyclically, and \(K=D+Y\). Exactly the values \(t\in\{0,1,\ldots,\min(a,b)\}\) satisfying \(t\equiv a\pmod 2\) are feasible and have positive conditional probability. All expectations are conditional on the presence of \(e\) unless indicated otherwise. At \(a\le1\) or \(b\le1\), the degree is deterministic but the regression statement still holds at its attainable value.

## Proof

**1. Conditioning splits the remaining chords into three classes.** Conditional on \(D=t\), precisely \(t\) chords bridge the arcs. The remaining internal chord counts are \(p=(a-t)/2\) and \(q=(b-t)/2\) on the respective sides. Every matching with these counts is equiprobable, and the endpoints of each type are exchangeable within their arc.

**2. Pairwise crossing probabilities.** Consider a pair of remaining chords, classified by their endpoint types. Two internal chords lying on the same arc cross with probability \(1/3\): for four endpoints in increasing order, precisely one of the three pairings crosses. An internal chord and a bridge chord cross with probability \(1/3\), because among their three endpoints on the same arc the bridge endpoint lies between the internal endpoints in exactly two of the six possible orders. Two bridge chords cross with probability \(1/2\), because after choosing their two endpoints in each arc, their two possible endpoint bijections are equiprobable and exactly one alternates cyclically. Internal chords on opposite arcs never cross. These probabilities remain valid when conditioning on the class counts: randomly permuting the labels within each arc preserves the conditional uniform law and the class counts.

**3. The finite regression identity.** Linearity of expectation across unordered chord pairs therefore gives
\[
\mathbb{E}[Y\mid D=t]
=\frac13\left\{\binom p2+\binom q2+t(p+q)\right\}+\frac12\binom t2.
\]
Substituting \(p=(a-t)/2\), \(q=(b-t)/2\) and collecting terms yields
\[
\mathbb{E}[Y\mid D=t]
=\frac{a(a-2)+b(b-2)+2t(a+b-1)}{24}
=\frac{a(a-2)+b(b-2)}{24}+\frac{2n-3}{12}t.
\]
This simplification cancels every quadratic term in \(t\); in particular the slope is independent of the arc imbalance. Since \(K=Y+D\), the claimed total-crossing regression follows.

**4. Covariance as a consequence, not a substitute for the regression.** For distinct endpoints on opposite arcs, the probability they are paired is \(1/(2n-3)\); for two ordered, disjoint opposite-arc pairs it is \(1/((2n-3)(2n-5))\). Thus
\[
\mathbb E[D]=\frac{ab}{2n-3},\qquad
\mathbb E[D(D-1)]=\frac{a(a-1)b(b-1)}{(2n-3)(2n-5)},
\]
whence direct simplification gives
\[
\operatorname{Var}(D)=\frac{2a(a-1)b(b-1)}{(2n-5)(2n-3)^2}.
\]
The law of total covariance and the conditional affine identity give
\[
\operatorname{Cov}(D,Y)=\operatorname{Cov}(D,\mathbb E[Y\mid D])
=\frac{2n-3}{12}\operatorname{Var}(D).
\]
For \(a,b\ge2\) the variance is positive; for the other arc lengths \(D\) is deterministic and the last formula vanishes. The proof is valid for every integer \(n\ge3\), not only in an asymptotic regime.

## Verification

The standalone \(\texttt{verify.py}\) enumerates every residual perfect matching for \(n=3,4,5,6,7\) and each distinct arc size \(0\le a\le n-1\), exploiting exchange of the two arcs. It separately computes the marked crossing count and every crossing among the other chords, groups diagrams by feasible \(t\), and compares all conditional means as exact rational numbers with the stated formulas. It independently confirms the feasible support, bridge-count distribution, variance, covariance and total expectation. The observed execution passed 291 exact assertions across 25 arc cases and 79,029 full residual matching enumerations. Run with \(\texttt{python3 verify.py}\). These finite checks corroborate the combinatorial all-size proof; they are not an exhaustive check for unbounded \(n\).

## Relationship to prior work

Acan [1, Section 2] studies the degree of a chord in a uniform chord diagram conditional on its shorter-arc length, obtaining its mean and variance and an asymptotic law; the joint pointwise conditional expectation of total crossings given that degree is not stated there. Flajolet and Noy [2] derive global crossing-count enumeration and asymptotics without identifying this marked-chord conditional regression. Paguyo [3] develops distributional approximation for global crossing statistics; its statements do not give this exact conditional identity. The pointwise identity here is stronger than the separate marginal crossing moments or a single mixed covariance, since the latter only constrain a weighted average of possible conditional means.

## Limitations

This result determines the conditional first moment only. It does not claim an exact conditional distribution, conditional variance, concentration inequality, or uniqueness relative to all historical chord-diagram enumerations. The classical joint generating-function literature may contain a more general formula from which this identity follows without matching words; the accessible primary sources examined did not identify that implication. A fresh independent literature review remains appropriate.

## References

[1] Hüseyin Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489v1, publicly posted January 7, 2015. https://arxiv.org/pdf/1501.01489

[2] Philippe Flajolet and Marc Noy, *Analytic Combinatorics of Chord Diagrams*, INRIA research report RR-3914 (2000). https://algo.inria.fr/flajolet/Publications/FlNo00.pdf

[3] Adrianne E. Paguyo, *Convergence rates of limit theorems in random chord diagrams*, arXiv:2104.01134 (2021). https://arxiv.org/pdf/2104.01134
