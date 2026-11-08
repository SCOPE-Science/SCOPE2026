# First stochastic-order crossing for Quicksort root splits at nine keys

## Finding

In standard randomized Quicksort on \(n\) distinct keys, let \(C_n\) be the number of key comparisons and let \(J\in\{0,\ldots,n-1\}\) be the number of keys smaller than the first pivot. Write \(C_{n,j}\) for the conditional law of \(C_n\) given \(J=j\). The same law counts total internal path length of a binary search tree built from a uniformly random permutation with first inserted rank \(j+1\).

A natural first-order stochastic hypothesis says that moving the pivot one place toward the center cannot increase the comparison cost in stochastic order: \(C_{n,j}\succeq_{\mathrm{st}} C_{n,j+1}\) for \(0\le j<(n-1)/2\), where \(X\succeq_{\mathrm{st}}Y\) means \(\Pr(X\le t)\le\Pr(Y\le t)\) for every real \(t\).

**Sharp finite cutoff.** This stochastic hypothesis holds for every \(2\le n\le8\) and every applicable split, and first fails for \(n=9\), comparing the zero-based first-pivot ranks \(j=3\) and \(j+1=4\). The conditional cumulative probabilities at two adjacent attainable costs are

\[
\begin{aligned}
\Pr(C_9\le16\mid J=3)&=\frac19,&
\Pr(C_9\le16\mid J=4)&=\frac14,\\
\Pr(C_9\le17\mid J=3)&=\frac{19}{45},&
\Pr(C_9\le17\mid J=4)&=\frac5{12}.
\end{aligned}
\]

Thus the two conditional distribution functions cross; neither conditional law stochastically dominates the other. This contrasts with their strictly ordered means:
\[
\mathbb E(C_9\mid J=3)=\frac{271}{15}>\frac{53}{3}=\mathbb E(C_9\mid J=4),
\]
whose difference is \(2/5\). The sign reversal in the CDF comparison between thresholds 16 and 17 is not numerical noise: at threshold 17 its rational margin is exactly \(1/180\).

## Assumptions and scope

The input consists of \(n\) distinct totally ordered keys in uniform random order, or equivalently independent uniform pivot selection in each Quicksort subproblem. Each pivot is compared exactly once with every other key in its current subproblem; no comparisons for pivot selection, swaps, or loop overhead are included. A single comparison costs one unit. The integer \(J\) counts smaller keys than the first pivot, hence is a zero-based rank. All claims are finite and exact; no asymptotic stochastic comparison is asserted.

When \(0\le j<(n-1)/2\) the partition with \(j+1\) smaller keys is one step closer to balance. Reflection identifies \(C_{n,j}\) and \(C_{n,n-1-j}\), so checking adjacent pairs on the left side covers every adjacent move toward the center and, by transitivity, all pairs ordered by split balance through size eight.

## Proof

Let \(a_m(t)\) be the number of permutations of \(m\) distinct keys for which ordinary first-element-pivot Quicksort makes exactly \(t\) comparisons. Use \(a_0(0)=a_1(0)=1\) and zero counts at all other costs. The initial pivot has \(i\) smaller and \(m-1-i\) larger keys, contributing exactly \(m-1\) comparisons. There are \(\binom{m-1}{i}\) ways to interleave the remaining relative orders of the two sublists, and their recursive costs are independent under conditional uniformity. Therefore, for every integer \(m\ge2\),
\[
 a_m(t)=\sum_{i=0}^{m-1}\binom{m-1}{i}
          \sum_{u+v=t-(m-1)}a_i(u)a_{m-1-i}(v).
\]
For a specified zero-based root rank \(j\), the conditional numerator is
\[
 A_{n,j}(t)=\binom{n-1}{j}
      \sum_{u+v=t-(n-1)}a_j(u)a_{n-1-j}(v),
 \qquad \sum_t A_{n,j}(t)=(n-1)!.
\]
Consequently the cumulative difference in favor of the more balanced root is the integer
\[
 G_{n,j}(t)=\sum_{s\le t}\bigl(A_{n,j+1}(s)-A_{n,j}(s)\bigr).
\]
The desired stochastic order holds if and only if \(G_{n,j}(t)\ge0\) for all integer \(t\). Values outside the finite common support are zero. The recurrence uniquely determines every coefficient by induction, so calculating its finitely many coefficients is an exhaustive exact proof, not a sample or a finite experiment extrapolated to infinity.

The following table gives **every nonzero** value of \(G_{n,j}(t)\), beginning at the listed cost and proceeding through consecutive integer costs. Omitted values at other costs, including both tails, are zero. The listed entries are the unnormalized integer numerators with common denominator \((n-1)!\).

| \(n\) | \(j\) | Starting cost | Consecutive nonzero gaps |
|---:|---:|---:|---|
| 3 | 0 | 2 | 2 |
| 4 | 0 | 4 | 6, 4 |
| 5 | 0 | 6 | 8, 24, 12, 8 |
| 5 | 1 | 6 | 16 |
| 6 | 0 | 9 | 60, 80, 80, 48, 24, 16 |
| 6 | 1 | 8 | 40, 60, 40 |
| 7 | 0 | 12 | 240, 432, 496, 264, 320, 160, 96, 48, 32 |
| 7 | 1 | 11 | 360, 240, 288, 144, 96 |
| 7 | 2 | 10 | 80, 40, 240 |
| 8 | 0 | 15 | 560, 2520, 2720, 2800, 2208, 1680, 1344, 912, 640, 320, 192, 96, 64 |
| 8 | 1 | 14 | 1680, 2464, 1512, 1568, 1120, 672, 336, 224 |
| 8 | 2 | 13 | 840, 1120, 896, 1008, 672 |

For \(n=2\) the two root splits have identical laws by reflection, so there is no distinct adjacent move toward the center. The table is exhaustive for all distinct adjacent splits toward the center at \(3\le n\le8\). Every listed number is nonnegative, proving all required orders in this range.

At \(n=9,j=3\), the same recurrence yields the exact CDF numerators out of \(8!=40320\): at threshold \(16\), the pair is \((4480,10080)\), and at threshold \(17\), it is \((17024,16800)\). This gives \(G_{9,3}(16)=5600>0\) but \(G_{9,3}(17)=-224<0\), proving the crossing and the failure at the first possible sample size. Moreover the other three adjacent comparisons at \(n=9\) remain ordered; only the last move into the center crosses.

For context, the classical mean formula \(\mu_m=\mathbb E(C_m)=2(m+1)H_m-4m\), with \(H_m=\sum_{i=1}^m1/i\), gives
\[
\mathbb E(C_{n,j})-\mathbb E(C_{n,j+1})=
2(H_{n-1-j}-H_{j+1})>0
\]
whenever \(j<(n-2)/2\). Therefore the crossing shows precisely why positive ordered conditional means do not imply first-order stochastic dominance.

## Verification

The self-contained Python 3 program `checker.py` implements the integer recurrence, checks each row of the finite certificate against a separately embedded expected vector, checks that each conditional distribution sums to \((n-1)!\), and independently enumerates all \(2\cdot8!=80640\) nine-key input permutations whose first pivots have ranks four or five. Its distinct insertion-tree computation gives exactly the same conditional histograms and CDFs. The companion `cdf_certificate.json` records the finite cutoff table and the four rational CDF values. Execute `python checker.py` in the directory containing the package.

The exact checker reports 109 internal assertions or vector comparisons and 80,640 independently generated permutation outcomes. The induction recurrence plus the displayed exhaustive coefficient table constitute the finite proof; the second algorithm is a corroborating check. The checker does not claim to establish novelty or anything for all sample sizes beyond the stated cutoff.

## Relationship to prior work

Fill and Janson (2001) analyze the limiting distribution of Quicksort comparisons and recall the random-pivot distributional recurrence; Iliopoulos and Penman (2010) give a full moment analysis. These sources establish the model and available recurrence, **not** the stated sharp failure of a first-order stochastic comparison between adjacent fixed root ranks. Dennert and Grübel (2010) study a different joint statistic, the binary-search-tree fringe-size profile. Known mean or covariance comparisons for a root-split statistic and total path length do not imply a stochastic ordering: the two CDF inequalities above provide a counterexample to that possible inference.

The claim of contribution is strictly the smallest-size all-split stochastic boundary and its exact crossing witness, not the recurrence, the classical mean formula, or any general algorithmic improvement. A generic known recurrence from which finite coefficients can in principle be extracted is explicitly acknowledged; unknown previous evaluations of the same sharp cutoff remain a historical-priority risk.

## Limitations

The theorem addresses classical key-comparison counts under uniform input or independent uniform pivots, not wall-clock running time, pivot sampling, duplicates, optimized partition implementations, or input distributions with dependencies. It gives a sharp cutoff through size nine but does not classify all further stochastic-order failures for larger sizes. No claim of an independent review or formal proof-assistant certification is made. The enumeration is finite and exact but its historical novelty cannot be guaranteed by search results alone.

## References

- J. A. Fill and S. Janson, *Approximating the limiting Quicksort distribution*, arXiv:math/0105246 (public preprint May 29, 2001); *Random Structures & Algorithms* 19 (2001), 376–406. https://arxiv.org/abs/math/0105246
- V. Iliopoulos and D. Penman, *Variance of the number of Comparisons of Randomized Quicksort*, arXiv:1006.4063 (June 21, 2010). https://arxiv.org/abs/1006.4063
- F. Dennert and R. Grübel, *On the Subtree Size Profile of Binary Search Trees*, *Combinatorics, Probability and Computing* 19 (2010), 561–578, first online January 22, 2010. https://doi.org/10.1017/S0963548309990630
