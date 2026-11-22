# The only quadratic Walsh blind spots of maximal independent sets on cycles

## Finding
Let \(n\ge3\), and identify every subset \(I\) of the labelled cycle \(C_n\) with its binary vertex-incidence vector in \(G_n=(\mathbb Z/2\mathbb Z)^n\). Let \(f_n\) be the indicator of **inclusion-maximal independent sets** (equivalently, independent dominating sets). Define the unnormalized Walsh transform
\[
\widehat f_n(S)=\sum_{I\text{ maximal independent in }C_n}(-1)^{|I\cap S|},\qquad S\subseteq\{0,\ldots,n-1\}.
\]
Then among all Walsh frequencies with \(|S|\le2\), precisely the following have zero multiplier:

- At \(n=4\), the four singleton frequencies \(S=\{i\}\).
- At \(n=9\), the eighteen two-vertex frequencies \(S=\{i,j\}\) whose cyclic distance is \(3\) or \(4\).

There are **no other zeros of degree at most two, at any cycle length**. Equivalently, counting convolution by \(f_n\) is injective on Walsh polynomials of degree at most two for every \(n\ge3\) except \(n=4,9\); its restricted kernel dimensions at those two lengths are, respectively, \(4\) and \(18\). In particular, all linear and quadratic Walsh modes survive at every \(n\ge10\), irrespective of possible zeros at higher degrees.

## Assumptions and scope
The cycle is simple, with distinct cyclically labelled vertices \(0,\ldots,n-1\), and maximality means inclusion-maximality, not maximum cardinality. The operator \(T_n g=f_n*g\) uses ordinary unnormalized convolution on \(G_n\), so \(\widehat{T_ng}(S)=\widehat f_n(S)\widehat g(S)\). A Walsh polynomial of degree at most two is a linear combination of characters \(\chi_S(x)=(-1)^{\sum_{i\in S}x_i}\) with \(|S|\le2\). Thus the dimension of its convolution kernel is the number of vanishing multipliers within that frequency band.

Define \(b_0=1\), \(b_1=0\), \(b_2=1\), and \(b_k=b_{k-2}+b_{k-3}\) for every integer \(k\ge3\). This is the number of ordered compositions of \(k\) into parts \(2\) and \(3\). Write \(P_n\) for the number of maximal independent sets of \(C_n\), with \(P_0=3\), \(P_1=0\), \(P_2=2\), and \(P_n=P_{n-2}+P_{n-3}\) for \(n\ge3\), the classical Perrin count. Values at \(n=0,1,2\) are recurrence seeds only, not counts for simple cycles of those orders.

## Proof
**1. Cyclic gaps and exact two-point transform.** Every maximal independent set of a cycle has successive selected vertices separated clockwise by \(2\) or \(3\) edges: independence forbids consecutive selected vertices, and domination forbids three consecutive unselected vertices. Fixing vertex \(0\) to be selected bijects these configurations with ordered \(2,3\)-compositions of \(n\), so exactly \(b_n\) maximal independent sets contain a specified vertex. If vertices \(0,d\) are both selected, the two complementary arcs give independent ordered compositions of lengths \(d\) and \(n-d\). Hence exactly \(b_d b_{n-d}\) maximal independent sets contain both.

The Perrin recurrence, or a direct cyclic-gap count, gives \(P_n=2b_n+b_{n-3}\) for every \(n\ge3\): both sides obey the same recurrence, with agreeing values \(3,2,5\) at lengths \(3,4,5\). Expanding the Walsh signs therefore yields
\[
\widehat f_n(\varnothing)=P_n,\qquad
\widehat f_n(\{i\})=P_n-2b_n=b_{n-3},
\]
and for \(i\ne j\) at directed clockwise distance \(d\in\{1,\ldots,n-1\}\),
\[
\widehat f_n(\{i,j\})
=P_n-4b_n+4b_d b_{n-d}
=H(n,d),\qquad
H(n,d):=4b_d b_{n-d}-2b_{n-2}-b_{n-3}.
\]
This also proves \(H(n,d)=H(n,n-d)\). Since \(b_k\) is zero only at \(k=1\) for nonnegative \(k\), singleton zeros occur precisely at \(n=4\). For adjacent vertices, \(d=1\) gives \(H(n,1)=-2b_{n-2}-b_{n-3}<0\).

**2. Fixed small distances.** By the recurrence of \(b\), for each fixed \(d\) the integer sequence \(H(n,d)\) obeys
\[
H(n,d)=H(n-2,d)+H(n-3,d)\qquad(n\ge\max\{6,d+3\}).
\]
Consequently, three consecutive strictly positive values propagate strict positivity; three consecutive strictly negative values propagate strict negativity. The following complete integer seed certificates cover \(2\le d\le9\). Each row gives \((H(N,d),H(N+1,d),H(N+2,d))\), where \(N\) is the displayed starting length:

| \(d\) | \(N\) | Three exact values | Consequence for \(n\ge N\) |
|---|---:|---|---|
| 2 | 4 | \((2,1,1)\) | Positive |
| 3 | 10 | \((1,2,1)\) | Positive |
| 4 | 10 | \((-3,-2,-3)\) | Negative |
| 5 | 10 | \((5,2,5)\) | Positive |
| 6 | 12 | \((-3,-1,-1)\) | Negative |
| 7 | 14 | \((3,4,2)\) | Positive |
| 8 | 16 | \((6,3,10)\) | Positive |
| 9 | 19 | \((5,1,3)\) | Positive |

The remaining feasible lengths \(2d\le n<N\) occur only for \(d=3,4,9\): they are
\[
(H(6,3),H(7,3),H(8,3),H(9,3))=(1,-1,2,0),
\]
\[
(H(8,4),H(9,4))=(-2,0),\qquad H(18,9)=-2.
\]
Thus for every \(d\le9\), the only pair-frequency zeros arise at \(n=9\), distances \(3\) and \(4\).

**3. Uniform exclusion of all larger distances.** Let \(\lambda\) be the unique real root greater than one of \(\lambda^3=\lambda+1\). The rational interval
\[
\frac{1324717957}{10^9}<\lambda<\frac{132471796}{10^8}
\]
is certified by the opposite signs of \(t^3-t-1\) at its endpoints. Direct rational inequalities at \(k=10,11,12\) establish
\[
\frac{51}{125}\lambda^k<b_k<\frac{421}{1000}\lambda^k.
\]
Because \(\lambda^{-2}+\lambda^{-3}=1\), the ratios \(b_k/\lambda^k\) satisfy a convex-combination recurrence; these strict bounds propagate to **every** \(k\ge10\).

Now suppose both cyclic arcs have length at least ten, namely \(d\ge10\) and \(n-d\ge10\). Then \(n\ge20\), so \(n-2,n-3\ge10\), and
\[
\frac{H(n,d)}{\lambda^n}>
4\left(\frac{51}{125}\right)^2
-\frac{421}{1000}\left(2\lambda^{-2}+\lambda^{-3}\right)>0.
\]
The last strict inequality follows already from the lower rational endpoint \(\lambda>1324717957/10^9\): the positive term equals \(0.665856\) and the subtracted term is below \(0.661\). This excludes all larger distances. By symmetry it suffices to take \(d\le n/2\), so the small-distance table and this bound exhaust every pair frequency.

**4. Exact kernel dimensions.** At \(n=4\) every one of the four singleton frequencies vanishes, and no two-vertex frequency does. At \(n=9\), for each cyclic distance \(3\) or \(4\) there are nine unordered vertex pairs (neither distance equals \(n/2\)), giving \(9+9=18\) zeros. No constant coefficient vanishes because \(P_n>0\). Walsh diagonalization gives the asserted kernel dimensions and injectivity classification.

## Verification
The standalone `verify_low_degree.py` uses direct Boolean nonadjacency and domination tests (independent of the composition formula) and an integer Walsh–Hadamard transform at all \(3\le n\le17\), checking every character of degree at most two against the formulas and predicted zero set. It also verifies the rational plastic-constant bounds exactly, all finite propagation seeds, and the nonzero pair classification through \(n=600\) by integer recurrence. Executing the embedded program with Python 3.9 or later gives `PASSED: 92597 exact assertions`. The infinite conclusion follows from the preceding proof, not the finite checks.

## Relationship to prior work
Bisdorff and Marichal (first arXiv version 2007) establish and exploit the cyclic \(2,3\)-gap representation and Perrin/Padovan counting for maximal independent sets on cycles, primarily to enumerate rotational and dihedral orbits. Those foundational results are used here. They neither define the Walsh convolution operator nor classify its pair-character zeros. A published cycle maximal-independent-set implication-basis result concerns logical closures and Boolean trace dimension; a published greedy-sampling result concerns nonuniform probabilities of randomly produced maximal independent sets. Neither implies the signed pair-multiplier classification. Prior Fourier results for **all** independent sets, including the empty/nonmaximal sets, concern a different counting measure. The present contribution is the all-length exclusion of zero multipliers outside the two stated low-degree exceptions.

## Limitations
This theorem classifies only the Walsh band of degree at most two; it does not claim that convolution is invertible on the **full** function space at other lengths or determine the higher-degree nullity. It depends on the unweighted uniform indicator of maximal independent sets, not the distribution produced by a greedy algorithm. The novelty judgment rests on the cited primary material and available searchable records; an older unindexed signed-enumerator identity with an explicit all-length quadratic zero classification would supersede it. No independent external audit has been performed.

## References
1. R. Bisdorff and J.-L. Marichal, *Counting non-isomorphic maximal independent sets of the n-cycle graph*, arXiv:math/0701647v1, first posted 2007-01-23; *Journal of Integer Sequences* 11 (2008), Article 08.5.7. https://arxiv.org/abs/math/0701647 ; full text https://arxiv.org/html/math/0701647v2
2. *Minimal one-pass implications and exact Boolean trace rank for cycle maximal-independent-set contexts* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-minimal-one-pass-implications-and-exact-boolean-trace-rank-for-c--5aa3700acbcd
3. *Exact uniformity and a local likelihood-ratio obstruction for greedy independent sets on cycles* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-uniformity-and-a-local-likelihood-ratio-obstruction-for-gr--9a6d94e819c5
