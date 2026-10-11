# Lengyel orbit profile of the universal homogeneous two-sorted ultrametric space

## Finding

Let \(\mathbb U\) be the countable universal homogeneous two-sorted ultrametric space of Bartoš, Kubiś, Kwiatkowska, and Malicki, and let \(G=\operatorname{Aut}(\mathbb U)\) be its full group of dc-automorphisms. We consider the induced action of \(G\) on the point sort.

For every \(n\ge 1\), the \(G\)-orbits on injective ordered \(n\)-tuples of points are in canonical bijection with strict chains from the minimum to the maximum of the partition lattice \(\Pi_n\). Hence their number is the Lengyel number
\[
a_n=A005121(n),
\]
with initial values
\[
1,1,4,32,436,9012,262760,10270696,\ldots.
\]
Equivalently, \(a_n\) is the number of ultradissimilarity relations on an \(n\)-element labeled set.

If repetitions are allowed, the number \(b_n\) of orbits on all ordered \(n\)-tuples is
\[
b_n=\sum_{k=1}^n {n\brace k}a_k,
\]
where \({n\brace k}\) is a Stirling number of the second kind. The classical Lengyel recurrence
\[
a_n=\sum_{k=1}^{n-1}{n\brace k}a_k\qquad(n\ge2)
\]
therefore gives the unexpectedly simple identity
\[
\boxed{\ b_1=1,\qquad b_n=2a_n\quad(n\ge2).\ }
\]
Thus the full point-tuple orbit profile begins
\[
1,2,8,64,872,18024,525520,20541392,\ldots.
\]
In particular, the Babai--Lengyel asymptotic for \(a_n\) immediately yields
\[
b_n\sim 2C_L (n!)^2(2\log 2)^{-n}n^{-1-(\log 2)/3},
\]
where \(C_L\approx1.0986858055\).

## Assumptions and scope

The action here is the point-sort action of the **full dc-automorphism group**, not the isometry group. A dc-map may move numerical distance values as long as their linear order is preserved. That distinction is essential: an injective tuple remembers only the equality and order pattern among its pairwise distances, rather than their particular rational values.

The result concerns finite ordered tuples of points. No assertion is made here about conjugacy classes of automorphisms, orbit equivalence relations on infinite sequences, or the completion of \(\mathbb U\).

## Proof

Take an injective ordered tuple \(\bar x=(x_1,\ldots,x_n)\). List the distinct positive distances occurring among its coordinates as
\[
r_1<r_2<\cdots<r_m.
\]
For \(j=0,1,\ldots,m\), define a partition \(\pi_j\) of \([n]\) by
\[
i\equiv_{\pi_j}k
\quad\Longleftrightarrow\quad
\begin{cases}
i=k,&j=0,\\
d(x_i,x_k)\le r_j,&j\ge1.
\end{cases}
\]
Because \(d\) is an ultrametric, each relation \(d(x_i,x_k)\le r_j\) is an equivalence relation. Since every \(r_j\) is actually attained, each step is strict. Injectivity gives the discrete partition at the bottom, and the largest occurring distance merges all coordinates at the top. Hence
\[
\pi_0<\pi_1<\cdots<\pi_m
\]
is a strict chain from the minimum to the maximum of \(\Pi_n\).

Conversely, given any strict chain
\[
\hat0=\pi_0<\pi_1<\cdots<\pi_m=\hat1,
\]
choose formal levels \(0<r_1<\cdots<r_m\) and set, for \(i\ne k\),
\[
d(i,k)=r_{\min\{j:i\equiv_{\pi_j}k\}}.
\]
Nested equivalence relations make this an ultrametric. Thus strict partition chains are exactly the order types of finite labeled ultrametrics with distinct points.

Two injective tuples yield the same chain exactly when the coordinatewise bijection between their generated point sets extends to an order-preserving bijection between the finite sets of distances. In other words, their generated finite two-sorted substructures are dc-isomorphic. The cited 2026 paper proves that all finite two-sorted ultrametric spaces form a Fraïssé class and that \(\mathbb U\) is its dc-homogeneous limit. Therefore such a finite dc-isomorphism extends to a global element of \(G\), while different chains cannot be merged by a dc-automorphism. This proves the orbit-chain bijection.

OEIS A005121 records that the number of chains from minimum to maximum in \(\Pi_n\) is exactly the number of ultradissimilarity relations on an \(n\)-set and gives the displayed sequence. It also records the Lengyel recurrence above.

For a general ordered \(n\)-tuple, first record its equality partition. If it has \(k\) blocks, the quotient tuple has \(k\) distinct points and hence \(a_k\) possible dc-orbits. There are \({n\brace k}\) equality partitions with \(k\) blocks, so
\[
b_n=\sum_{k=1}^n {n\brace k}a_k.
\]
For \(n\ge2\), separating the \(k=n\) term and applying the Lengyel recurrence gives
\[
b_n=a_n+\sum_{k=1}^{n-1}{n\brace k}a_k=2a_n.
\]

## Verification

The structural proof is independent of computation. The bundled `verify.py` supplies an exact finite replay of its combinatorial side. It enumerates set partitions as restricted-growth strings, counts every strict chain from the discrete to the indiscrete partition through \(n=7\), and obtains
\[
1,1,4,32,436,9012,262760.
\]
It independently checks these against the Stirling recurrence for A005121. It then explicitly enumerates every partition chain through \(n=5\), converts first-merge levels into distance ranks, and verifies the ultrametric inequality on every ordered triple. Finally it computes the repeated-coordinate Stirling transform and confirms
\[
1,2,8,64,872,18024,525520
\]
and \(b_n=2a_n\) for every tested \(n\ge2\). The script returns `VERIFY_OK`.

## Relationship to prior work

Bartoš--Kubiś--Kwiatkowska--Malicki introduce the two-sorted/dc framework, prove that all finite two-sorted ultrametric spaces form a Fraïssé class, identify its countable limit with the rational Urysohn ultrametric space, and prove dc-homogeneity. Their paper also studies the full automorphism group. A follow-up paper studies generic dc-automorphisms and individual automorphism trajectories. In the checked versions, neither paper states an all-arity finite point-tuple orbit profile, a partition-lattice enumeration, or the doubling identity for tuples with repetitions.

The sequence itself is classical. Schader counted ordinal ultradissimilarity structures; Lengyel studied its Stirling recurrence; Babai--Lengyel obtained its asymptotic; and OEIS A005121 explicitly identifies it with chains from minimum to maximum in the partition lattice. None of that combinatorial enumeration is claimed as new here.

The accepted contribution is the **Fraïssé-orbit identification for the 2026 universal homogeneous two-sorted ultrametric space**, together with the full-tuple Stirling transform and its exact factor-two collapse. Targeted exact web searches, full-text term searches in both 2026 papers, and three semantic-index queries did not locate that statement. Because the deduction is short once the dc-Fraïssé framework and classical ultradissimilarity enumeration are juxtaposed, unindexed folklore remains a priority risk.

## Limitations

The originality assessment is literature-search based and cannot exclude unpublished notes, talks, or folklore. In particular, the injective count is a natural corollary of dc-homogeneity plus the classical enumeration of ordinal ultrametrics.

The verification program checks the finite combinatorics and the chain-to-ultrametric encoding only. The all-arity orbit theorem rests on the source-supported Fraïssé homogeneity argument, not on extrapolation from finite data.

The result is for the full dc-automorphism group acting on the point sort. The isometry group has a much finer orbit decomposition because it fixes actual rational distance values.

## References

A. Bartoš, W. Kubiś, A. Kwiatkowska, M. Malicki, *Universal homogeneous two-sorted ultrametric spaces*, arXiv:2605.13608. First public version: 2026-05-13. MSC: 54E35, 03C50, 20B27, 18A22.

A. Bartoš, W. Kubiś, A. Kwiatkowska, M. Malicki, *Generic dc-automorphisms of two-sorted ultrametric spaces*, arXiv:2606.11498.

OEIS A005121, *Number of ultradissimilarity relations on an n-set*; includes the partition-chain interpretation, Lengyel recurrence, and Babai--Lengyel asymptotic.
