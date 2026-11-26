# Parity-sensitive likelihood-ratio ordering of crossing counts in random chord diagrams

## Finding

Let \(n\ge3\). Condition a uniformly random perfect matching of \(2n\) cyclically ordered endpoints to contain one prescribed chord. The chord splits the remaining \(m=2n-2\) endpoints into two arcs. For \(0\le a\le n-1\), let \(X_a\) count residual matching edges joining the arc of \(a\) endpoints to the other arc of \(b=m-a\) endpoints; these are precisely the chords crossing the prescribed chord.

The entire law is
\[
\Pr(X_a=k)=\frac{a!b!}{k!\,2^{(m-2k)/2}\,((a-k)/2)!\,((b-k)/2)!\,(m-1)!!},
\]
where \(0\le k\le a\), \(k\equiv a\pmod 2\); all other masses vanish. The mean \(\mathbb E[X_a]=a(m-a)/(m-1)\) increases strictly for \(0\le a<n-1\). Yet **adjacent lengths are stochastically incomparable**: for every \(1\le a<n-1\), neither \(X_a\le_{\mathrm{st}}X_{a+1}\) nor its reverse holds.

For every \(0\le a\le n-3\), the two-step comparison instead satisfies the strict *likelihood-ratio order* \(X_a<_{\mathrm{lr}}X_{a+2}\). On the support of \(X_a\),
\[
\frac{\Pr(X_{a+2}=k)}{\Pr(X_a=k)}=
\frac{(a+2)(a+1)(b-k)}{b(b-1)(a+2-k)},
\]
which is strictly increasing with \(k\); the larger law additionally assigns positive probability to \(a+2\). Thus the even-length and odd-length crossing-count families each increase strictly in likelihood-ratio order as their arc split moves toward balance.

## Assumptions and scope

The endpoints are distinct and cyclically ordered; the conditioned distinguished chord must be present. All matchings of the other \(m\) points are equally likely. Each cut is determined by a fixed subset of size \(a\); exchangeability makes the physical position of the cut irrelevant. We restrict \(a\) to the smaller arc, so \(a\le m/2=n-1\). Stochastic order means comparison of all upper-tail probabilities; likelihood-ratio order means an increasing ratio of point masses, with zero masses beyond the smaller support interpreted in the standard extended sense. The assertions concern finite exact laws, not only their limits.

## Proof

**1. The exact mass function.** For a crossing count \(k\), choose \(k\) endpoints from each arc, pair them bijectively, and match the \(a-k\) and \(b-k\) remaining endpoints internally. The count is \(\binom ak\binom bk k!(a-k-1)!!(b-k-1)!!\), divided by the total \((m-1)!!\) matchings. Factorial simplification gives the displayed mass formula, including the boundary convention \((-1)!!=1\).

**2. Increasing means.** Every ordered pair consisting of one endpoint in either arc has matching probability \(1/(m-1)\). Hence \(\mathbb E X_a=ab/(m-1)\), whose one-step difference is \((m-2a-1)/(m-1)>0\) for \(0\le a<n-1\).

**3. Adjacent cuts are incomparable.** Take a single uniform random matching and an independent uniformly random order of its \(m\) endpoints. Let the first \(a\) endpoints form the smaller side. Conditional on \(X_a=x\), among the \(m-a\) outside endpoints exactly \(x\) are matched to the inside. Thus
\[
\Pr(X_{a+1}=x-1\mid X_a=x)=\frac{x}{m-a},\quad
\Pr(X_{a+1}=x+1\mid X_a=x)=\frac{m-a-x}{m-a}.
\]
These marginals coincide with the fixed-cut laws by exchangeability. For odd \(a\), put \(t=1\); for even \(a\ge2\), put \(t=2\). Since \(X_a\) has the parity of \(a\), the difference of upper tails at threshold \(t\) equals \(-t\Pr(X_a=t)/(m-a)<0\), while at threshold \(t+1\) it equals \((m-a-t)\Pr(X_a=t)/(m-a)>0\). The strict inequalities hold for all \(1\le a<n-1\), proving incomparability.

**4. Two-step likelihood-ratio order.** For \(0\le a\le n-3\), write \(b=m-a\). Dividing the exact masses at the same admissible \(k\) gives
\[
R(k)=\frac{(a+2)(a+1)(b-k)}{b(b-1)(a+2-k)}.
\]
Since \(b>a+2\), the elementary difference \((b-k)/(a+2-k)\) is strictly increasing with \(k\). Meanwhile \(X_{a+2}\) has the new maximal attainable value \(a+2\), with positive probability. Thus it strictly dominates \(X_a\) in likelihood-ratio order. Repeating the two-step comparison proves the stated ordering along each parity class.

## Verification

A standalone standard-library checker `verify.py` independently enumerates every perfect matching of up to 12 residual endpoints and matches its exact crossing-count histogram to the factorial law. It then checks normalization, means, upper-tail incomparability, strict common-support likelihood ratios, the closed ratio formula, and dominance along two-step comparisons for every even residual size through 40. All computations use exact rational arithmetic; the all-size conclusions follow from the combinatorial and algebraic proof rather than the finite checks.

## Relationship to prior work

H. Acan, *On a uniformly random chord diagram and its intersection graph* (arXiv:1501.01489, initially public January 7, 2015), studies the same random diagram and in Section 2 calculates the first two moments of the number of internal pairs at a fixed chord length, then derives an asymptotic degree law. If that number is \(J_a\), the crossing count here is \(X_a=a-2J_a\). The cited paper does not state the parity-dependent finite stochastic incomparability or the two-step likelihood-ratio ordering. Existing exact crossing enumerators for the entire diagram concern a different aggregate variable, not these conditional cut distributions. Factorial matching counts are classical and not claimed as new.

## Limitations

The theorem compares adjacent arc lengths in first-order stochastic order and distances two apart in likelihood-ratio order. It does not purport to classify arbitrary pairs of opposite parity at widely separated lengths, nor the joint behavior of two or more marked chords. Historical matching-enumeration literature may implicitly encode the factorial mass function; the new assessed content is the sharp order dichotomy. No independent external audit has been performed.

## References

- H. Acan (2015), *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489, https://arxiv.org/abs/1501.01489 (Section 2, initial version January 7, 2015).
- P. Flajolet and M. Noy (2000), *Analytic combinatorics of chord diagrams*, cited for the established aggregate-diagram context in Acan (2015).
