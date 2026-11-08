# Near-complete phylogenetic rarefaction distinguishes cherries and pitchforks and reverses variance rankings

## Finding
Let \(T\) be any rooted full-binary phylogenetic tree with \(n\ge4\) leaves, every edge of length one, and no stem above its root. Let \(Y_r(T)\) denote rooted phylogenetic diversity when exactly \(r\) leaves are uniformly deleted without replacement (the root is always retained). Write \(c(T)\) for the number of cherry clades with exactly two descendant leaves and \(t(T)\) for the number of pitchfork clades with exactly three descendant leaves. For \(N_2=\binom n2\), \(N_3=\binom n3\), and \(a=c(T)(n-2)\), the exact variances are

\[
\operatorname{Var}Y_2(T)=\frac{c(T)}{N_2}\left(1-\frac{c(T)}{N_2}\right),
\qquad
\operatorname{Var}Y_3(T)=\frac{a+3t(T)}{N_3}-\left(\frac{a+t(T)}{N_3}\right)^2.
\]

For each fixed \(n\ge4\), the ordered pair \((\operatorname{Var}Y_2,\operatorname{Var}Y_3)\) uniquely determines \((c(T),t(T))\), although it need not identify the entire tree. The ranking of two trees by these variances can reverse: there are trees \(A_m,B_m\) with \(6m\) leaves, for **every integer \(m\ge1\)**, such that

\[
\operatorname{Var}Y_2(A_m)>\operatorname{Var}Y_2(B_m),
\qquad
\operatorname{Var}Y_3(A_m)<\operatorname{Var}Y_3(B_m).
\]

Thus increasing the fixed deletion budget from two to three taxa can reverse a comparative uncertainty ranking even in arbitrarily large equal-edge trees.

## Assumptions and scope
A rooted full-binary tree means every nonleaf vertex has exactly two children and every leaf has none; unlabeled tree shapes are allowed and labels affect only the uniform choice of deleted leaves. There are \(2n-2\) edges, each of unit length, and no incoming edge to the root. Rooted phylogenetic diversity of surviving leaves is the number of edges belonging to the union of root-to-survivor paths. The uniform deletion set is sampled among all \(\binom nr\) subsets for \(r=2,3\); these are fixed-size, negatively dependent extinctions, **not** independent Bernoulli extinctions. A cherry is a rooted two-leaf clade; a pitchfork is a rooted three-leaf clade. The definition of \(Y_3\) requires at least one survivor, hence \(n\ge4\). No phylogenetic ultrametric assumption is imposed.

## Proof
**1. Edge-loss representation.** The root-to-survivor union omits exactly the edges whose descendant leaf sets are contained in the deleted set. With two deleted leaves, precisely the two pendant edges are missing, together with the incoming edge of a cherry if the deleted pair is a cherry. Distinct cherries are disjoint, so a random pair is a cherry with probability \(c/N_2\). If \(A_2\) indicates that event, then \(Y_2=2n-4-A_2\), proving the first variance formula.

With three deleted leaves, precisely three pendant edges are always missing. An additional incoming edge is missing for each cherry contained in the deleted triple; there can be at most one such cherry because different cherries have disjoint leaf pairs. One more edge is missing exactly when the deleted triple itself is a three-leaf clade. Write \(A_3\) for the cherry-containing event and \(B_3\) for the pitchfork event. Every three-leaf clade contains a cherry, so \(B_3\) implies \(A_3\). Consequently \(Y_3=2n-5-A_3-B_3\) and \((A_3+B_3)^2=A_3+3B_3\). Each cherry belongs to exactly \(n-2\) triples, giving

\[
\mathbb E A_3=\frac{c(n-2)}{N_3},\quad
\mathbb E B_3=\frac{t}{N_3},\quad
\mathbb E(A_3+B_3)^2=\frac{c(n-2)+3t}{N_3}.
\]

Subtracting the square of \(\mathbb E(A_3+B_3)\) proves the second formula.

**2. Recovery of two shape indices.** Cherries are pairwise disjoint, hence \(1\le c\le\lfloor n/2\rfloor\) and \(0<c/N_2\le1/(n-1)<1/2\). Because \(x(1-x)\) is strictly increasing for \(0<x<1/2\), \(\operatorname{Var}Y_2\) determines \(c\). With \(c\) fixed, put \(a=c(n-2)\). Increasing \(t\) by one changes the second displayed variance by

\[
\frac{3N_3-2(a+t)-1}{N_3^2}.
\]

This is positive throughout feasible counts. Indeed \(a+t\le N_3\): for \(n\ge5\) the bounds \(c\le n/2\) and \(t\le n/3\) imply
\(a+t\le n(n-2)/2+n/3\le\binom n3\); the last inequality is \(n^2-6n+6\ge0\), true at every integer \(n\ge5\). For \(n=4\), the only shapes have \((c,t)=(2,0)\) or \((1,1)\), satisfying the same inequality. Therefore \(3N_3-2(a+t)-1\ge N_3-1>0\), so \(\operatorname{Var}Y_3\) determines \(t\) after \(c\) is known.

**3. An infinite reversal family.** Fix integer \(m\ge1\) and set \(n=6m\). To construct \(A_m\), combine the roots of \(2m+1\) disjoint two-leaf cherries with an arbitrary full-binary connecting skeleton. This gives \(4m+2\) leaves. Attach a new leaf above the current root, making a new binary root, exactly \(2m-2\) times. No new two- or three-leaf clades are created by either operation, so \((c(A_m),t(A_m))=(2m+1,0)\). To construct \(B_m\), combine \(2m\) disjoint three-leaf pitchfork blocks with a full-binary skeleton. Its count is \((c(B_m),t(B_m))=(2m,2m)\). Both trees have \(n\) leaves and unit edges.

As \(c(A_m)>c(B_m)\), step 2 gives \(\operatorname{Var}Y_2(A_m)>\operatorname{Var}Y_2(B_m)\). Put \(N=N_3\) and \(u_A=(2m+1)(n-2)\), \(u_B=2m(n-2)+2m\). Their two event-sum means are \(u_A/N\) and \(u_B/N\), so \(u_A-u_B=4m-2>0\). Their second-moment difference (\(B_m\) minus \(A_m\)) is

\[
\frac{2m(n-2)+6m-(2m+1)(n-2)}{N}=\frac2N>0.
\]

It follows exactly that

\[
\operatorname{Var}Y_3(B_m)-\operatorname{Var}Y_3(A_m)
=\frac2N+\frac{(4m-2)(u_A+u_B)}{N^2}>0,
\]

establishing the reversal for every integer \(m\ge1\).

**4. Smallest admissible witness.** For four leaves, compare the balanced rooted shape \(A=((a,b),(c,d))\) with the caterpillar \(B=(a,(b,(c,d)))\). Their shape counts are \((2,0)\) and \((1,1)\), giving

\[
\operatorname{Var}Y_2(A)=\frac29>\frac5{36}=\operatorname{Var}Y_2(B),
\qquad
\operatorname{Var}Y_3(A)=0<\frac{11}{16}=\operatorname{Var}Y_3(B).
\]

Four is the first size at which both nonempty retained sample sizes \(n-2\) and \(n-3\) exist. The infinite family above ensures that the phenomenon does not depend on this one-survivor small case.

## Verification
The standard-library Python program `verify.py` independently enumerates all deleted two- and three-leaf sets of every nonplane rooted full-binary tree shape on \(4\) through \(11\) leaves (\(792\) shape/budget comparisons). It calculates rooted diversity by actual descendant-edge inclusion rather than by the cherry/pitchfork formulas, and matches the two symbolic variance expressions exactly as rational numbers. It also independently enumerates the four-leaf example and the explicitly constructed \(6m\)-leaf family for \(m=1,2,3,5\). Run with `python verify.py`; no external packages are needed. These finite checks are not offered as proofs of the all-size formulas or infinite family; steps 1–3 are those proofs.

## Relationship to prior work
Nipperess and Matsen derived general exact mean and variance formulas for rooted and unrooted phylogenetic diversity under uniform rarefaction. Their exact rooted formula is a broader computational identity from which the two near-complete formulas here can be specialized; this finding does **not** claim a new generic rarefaction moment method. Disanto and Wiehe studied cherry and pitchfork distributions for coalescent-ranked tree models, and later Choi, Thompson and Wu studied their joint distributions for random rooted and unrooted tree models. Those treatments supply established shape-statistic context, not a proof of the present deterministic-tree variance-index recovery or its infinite ranking reversal. The new claim is the combination of explicit near-complete shape-index recovery and the universal-size structural counterfamily; finding a known general formula or known shape counts alone would not constitute priority for that claim.

## Limitations
The theorem concerns **rooted** diversity, equal unit edge lengths, full-binary trees, one observation per leaf, and uniform fixed-budget deletion. It does not assert reversal under independent survival, for arbitrary positive branch lengths, or for unrooted diversity. The variance pair identifies only the two clade counts, not an entire tree topology, and it is not an estimator from noisy observed rarefaction variances. The result is a theoretical benchmark, not an empirical conservation recommendation. Historical priority is conditional on the inspected literature, not independently certified.

## References
- D. A. Nipperess and F. A. Matsen IV, *The mean and variance of phylogenetic diversity under rarefaction*, arXiv:1208.6552 (first posted 2012-08-31); *Methods in Ecology and Evolution* 4 (2013), 566–572, DOI: 10.1111/2041-210X.12042. Full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC3699894/ .
- F. Disanto and T. Wiehe, *Exact enumeration of cherries and pitchforks in ranked trees under the coalescent model*, arXiv:1112.1295 (first posted 2011-12-06); *Mathematical Biosciences* 242 (2013), 195–200, DOI: 10.1016/j.mbs.2013.01.010.
- K. P. Choi, A. Thompson and T. Wu, *On cherry and pitchfork distributions of random rooted and unrooted phylogenetic trees*, arXiv:2002.12643 (first posted 2020-02-28); *Theoretical Population Biology* 132 (2020), 92–104, DOI: 10.1016/j.tpb.2020.02.001.
