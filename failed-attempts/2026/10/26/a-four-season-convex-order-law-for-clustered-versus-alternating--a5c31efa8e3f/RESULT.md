# A four-season convex-order law for clustered versus alternating carrying capacities

## Finding
Fix \(R>1\) and two environmental carrying capacities \(0<K_L<K_H\). In a four-season periodic Beverton–Holt population, suppose each capacity occurs exactly twice. Cyclically inequivalent schedules are the **alternating** order \((K_H,K_L,K_H,K_L)\) and the **clustered** order \((K_H,K_H,K_L,K_L)\). Let \(X^A_0,\ldots,X^A_3\) and \(X^C_0,\ldots,X^C_3\) denote their globally attracting positive periodic populations, with superscripts \(A\) and \(C\) for alternating and clustered, respectively.

**Theorem.** Their inverse-population vectors obey strict majorization: after decreasing rearrangement, every leading partial sum of \((1/X^C_t)_{t=0}^3\) at indices \(1,2,3\) strictly exceeds the corresponding sum of \((1/X^A_t)_{t=0}^3\), while both total sums agree. Thus for any strictly convex function \(\varphi:(0,\infty)\to\mathbb R\),
\[
 \sum_{t=0}^{3}\varphi(1/X^C_t)>\sum_{t=0}^{3}\varphi(1/X^A_t).
\]
For convex, not strictly convex, functions the comparison is nonstrict. In particular, clustering **strictly increases arithmetic mean population yet strictly decreases minimum population**, while preserving its harmonic mean:
\[
 \frac14\sum_t X^C_t>\frac14\sum_t X^A_t,
 \qquad \min_t X^C_t<\min_t X^A_t,
 \qquad \operatorname{HM}(X^C)=\operatorname{HM}(X^A).
\]
The clustered schedule also strictly increases maximum population. The inverse-population variance ratio is exactly
\[
 \frac{\operatorname{Var}(1/X^C)}{\operatorname{Var}(1/X^A)}=
 \frac{(1+R^{-1})^2}{1+R^{-2}}>1.
\]
Four seasons are the shortest binary-capacity period with two copies of each capacity that permits two cyclically inequivalent orders.

## Assumptions and scope
At integer time \(t\), abundance \(x_t>0\) obeys
\[
 x_{t+1}=\frac{R K_t x_t}{K_t+(R-1)x_t},\qquad R>1,
\]
where \((K_t)\) is repeated every four seasons, each of \(K_H\) and \(K_L\) appearing twice. A phase shift merely cyclically permutes periodic-orbit coordinates and does not affect the claims. There is no harvesting, randomness, density-independent immigration, or species interaction. Means, extrema and variances are across the four phases of the unique attracting periodic orbit, with variance normalized by \(1/4\).

Write
\[
 a=R^{-1},\quad u=K_H^{-1},\quad v=K_L^{-1},\quad
 c=\frac{u+v}{2},\quad d=\frac{v-u}{2}>0,
\]
\[
 D=\frac{1-a}{1+a},\qquad B=\frac{1-a^2}{1+a^2},\qquad
 E=\frac{(1-a)^2}{1+a^2}.
\]
For \(0<a<1\), all denominators are positive and \(c>d>0\).

## Proof
**Existence and global attraction.** With \(y_t=1/x_t\), the Beverton–Holt recurrence becomes the affine contraction
\[
 y_{t+1}=a y_t+(1-a)K_t^{-1}.
\]
The four-step map is affine with derivative \(a^4\in(0,1)\), yielding a unique positive periodic orbit. Every initial \(y_0>0\) converges to it, and consequently so does the positive population orbit.

**Exact inverse-population vectors.** Solving the recurrence over the alternating schedule and sorting in decreasing order gives
\[
 (1/X^A)^{\downarrow}=(c+Dd,\ c+Dd,\ c-Dd,\ c-Dd).
\]
For the clustered schedule one obtains
\[
 (1/X^C)^{\downarrow}=(c+Bd,\ c+Ed,\ c-Ed,\ c-Bd).
\]
To verify the order in the second vector, observe \(B>E>0\). The first vector is likewise sorted because \(D>0\). Both vectors sum to \(4c\).

**Strict majorization.** Direct algebra yields
\[
 B-D=\frac{2a(1-a)}{(1+a)(1+a^2)}>0,
 \qquad
 B+E-2D=\frac{2a(1-a)^2}{(1+a)(1+a^2)}>0.
\]
The differences of the first, second and third leading partial sums, clustered minus alternating, are respectively \(d(B-D)>0\), \(d(B+E-2D)>0\) and \(d(B-D)>0\). The total sums coincide. By the finite-vector majorization theorem (or successive two-coordinate averaging), every convex sum is no smaller for the clustered vector; if the function is strictly convex, the non-permutation and strict partial sums make the inequality strict.

**Population consequences.** The function \(y\mapsto1/y\) is strictly convex on positive reals, giving the strict mean-population comparison. The largest inverse population is \(c+Bd\) for clustering versus \(c+Dd\) for alternation, so taking reciprocals gives a strictly smaller clustered minimum population. Conversely, \(c-Bd<c-Dd\) gives a strictly larger clustered maximum population. Since both inverse-population vectors sum to \(4c\), their population harmonic means both equal \(1/c\).

The inverse-population variances are \(D^2d^2\) for alternation and \((B^2+E^2)d^2/2\) for clustering. Substituting the definitions gives
\[
 \frac{B^2+E^2}{2D^2}=\frac{(1+a)^2}{1+a^2}>1.
\]
Finally, among six labeled placements of the two high seasons, two are alternating and four clustered; every pattern of length less than four with two occurrences of each state is impossible. This proves the claimed minimal scheduling distinction. \(\square\)

## Verification
Run the included standalone, Python-standard-library script from the directory containing the package files:

```sh
python verify.py > recomputed_certificate.json
```

The accompanying `certificate.json` was generated by running that script. It uses `fractions.Fraction` exclusively to calculate four rational parameter instances, proves by direct exact arithmetic that their two sorted inverse-population vectors obey all three strict partial-sum inequalities, verifies the claimed extrema, mean and variance identities, and checks all six four-season placements. Its finite cases independently stress-test the algebra, but only the preceding symbolic proof establishes the theorem for every admissible real parameter.

## Relationship to prior work
AlSharawi and Ben Haj Rhouma (2010), especially Section 3, Theorems 3.3 and 3.5, and Example 3.4, investigate effects of carrying-capacity permutations on maximum sustainable harvesting and provide examples in which ordering affects mean population without harvesting. The present claim concerns neither optimal harvesting nor merely the possibility of an order effect; it gives a strict **all-parameter convex-order comparison** for the first nontrivial repeated binary four-season multiset and simultaneously resolves the mean-versus-minimum ecological tradeoff.

Yang and Sacker (with Haskell's appendix, 2012 online/2013 journal) derive general formulas for periodic Beverton–Holt orbits and state averages, so the construction of particular periodic orbits is established background. Their general formulas allow the quantities used here to be computed but the inspected article does not state or prove the claimed uniform, strictly ordered convex-function inequalities for the two binary seasonal arrangements.

Zhang, Shi, Xi and Chen (2018) address majorization for cyclic moving averages. That comparison varies a moving-average window for a fixed data sequence rather than permuting a four-season environmental sequence under an exponentially weighted recurrence.

## Limitations
The result is deterministic and concerns homogeneous growth factor \(R\) and exactly two high and two low capacity seasons. Convex order refers to **inverse** populations, not untransformed populations. It does not assert a stochastic extinction probability, a corresponding order for arbitrary multiseason multisets, or ecological optimality when both mean abundance and bottleneck abundance matter. Strict inequalities can disappear at degenerate boundary limits such as \(K_H=K_L\), \(R\to1\) or \(R\to\infty\). Bibliographic equivalence to a differently formulated historical rearrangement result is a residual risk; independent review has not been performed.

## References
1. Z. AlSharawi and M. Ben Haj Rhouma, “The Discrete Beverton-Holt Model with Periodic Harvesting in a Periodically Fluctuating Environment,” *Advances in Difference Equations*, 2010, article 215875. Published online 2010-03-08. DOI: 10.1155/2010/215875. https://doi.org/10.1155/2010/215875
2. Y. Yang and R. J. Sacker, with an appendix by C. Haskell, “Resonance and attenuation in the n-periodic Beverton–Holt equation,” *Journal of Difference Equations and Applications*, 19 (2013), 1174–1191. First published online 2012-10-09. DOI: 10.1080/10236198.2012.726988. https://dornsife.usc.edu/robert-sacker/wp-content/uploads/sites/256/2023/06/Yang-Sacker-BH.pdf
3. T. Zhang, H.-N. Shi, B.-Y. Xi and A. Chen, “Majorization involving the cyclic moving average,” *Journal of Inequalities and Applications*, 2018, article 152. DOI: 10.1186/s13660-018-1737-4. https://doi.org/10.1186/s13660-018-1737-4
