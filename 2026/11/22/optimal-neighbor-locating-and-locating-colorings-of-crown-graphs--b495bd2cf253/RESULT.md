# Optimal neighbor-locating and locating colorings of crown graphs

## Finding
For every integer \(n\ge3\), the crown graph \(\operatorname{Cr}_n=K_{n,n}-M\) satisfies
\[
\chi_{NL}(\operatorname{Cr}_n)=\chi_L(\operatorname{Cr}_n)=n+1.
\]
In fact **every** proper vertex coloring of \(\operatorname{Cr}_n\) is neighbor-locating precisely when it is locating in the metric color-code sense. Among partitions into exactly \(n+1\) **unnamed** nonempty color classes, the total number is
\[
N_n=n3^{n-1}-(n-2)2^n-2.
\]
At orders \(n=3,4,5,6,7,8\) the respective counts are \(17,74,307,1200,4461,15958\).

All optimal color partitions have the following unique form. First choose a nonempty index subset \(U\subseteq[n]\) and, for every \(i\in[n]\setminus U\), form the two-vertex mixed class \(\{L_i,R_i\}\). On \(U\) choose exactly one of:

1. If \(|U|=1\), place its two vertices in separate singleton classes.
2. If \(|U|\ge2\), choose a shore: its \(|U|\) vertices form one class; the opposite shore has \(|U|\) singleton classes.
3. If \(|U|\ge3\), choose subsets \(A,B\subseteq U\), with \(A\cup B=U\), \(|A\cap B|=1\), and \(|A|,|B|\ge2\). The class \(\{L_i:i\in A\}\) and the class \(\{R_i:i\in B\}\) are the only non-singleton pure-shore classes, and all other vertices over \(U\) are singleton classes.

There are no other optimal partitions. The shore orientation is part of the partition, but color *names* are not.

## Assumptions and scope
Write \(L_1,\ldots,L_n\) and \(R_1,\ldots,R_n\) for two independent shores. Edges are precisely \(L_iR_j\) with \(i\ne j\). A **proper coloring** means a partition into nonempty independent vertex classes, without counting permutations of color names separately.

For a color class \(C\) and vertex \(v\), let \(d(v,C)=\min_{w\in C}d(v,w)\). A proper coloring is **locating** when the vectors \((d(v,C))_C\) distinguish every two vertices; because vertices of different colors have different zero coordinates, it suffices to test same-colored pairs. A proper coloring is **neighbor-locating** when any two same-colored vertices see different sets of colors in their open neighborhoods. All graphs considered are finite, undirected, simple, and the theorem uses \(n\ge3\), when the crown graph is connected and all distances below are finite.

## Proof
**Step 1: proper-color normal form.** If an independent color class contains vertices from both shores, then it must be the pair \(\{L_i,R_i\}\), since any cross-shore pair with different indices is adjacent. Thus a proper partition consists of \(p\) disjoint paired classes, \(a\) classes contained wholly in the left shore, and \(b\) wholly in the right shore. Let \(U\) be the residual indices and \(m=|U|=n-p\). If \(m=0\), all classes are matched pairs and \(L_i,R_i\) have identical neighbor-color sets and identical distance vectors; such a partition is not locating of either kind. Hence \(m\ge1\) and \(a,b\ge1\).

**Step 2: neighborhood-color and distance tests coincide.** Consider two same-colored vertices \(L_i,L_j\) in a pure-left class (so \(i,j\in U\)). Every pure-left class other than their own is at distance \(2\) from each; paired classes are at distance \(1\) from each. For a pure-right class \(C\), both vertices have distance \(1\) to \(C\) unless \(C=\{R_i\}\) or \(C=\{R_j\}\): the corresponding matched left vertex has distance \(3\), whereas the other has distance \(1\). Equivalently, the color of a singleton \(R_i\) (or \(R_j\)) is omitted from exactly one open-neighborhood color set. Thus \(L_i,L_j\) are distinguished by either scheme exactly when at least one of \(R_i,R_j\) is a singleton pure-right class. The right-shore statement is symmetric.

For two same-colored matched vertices \(L_i,R_i\), a nonempty residual set \(U\) gives a pure-left class at distance \(2\) from \(L_i\) but distance \(1\) from \(R_i\), as well as an open-neighborhood color present only at \(R_i\). If \(U=\varnothing\), neither scheme distinguishes them. There are no other same-colored pair types. Consequently locating and neighbor-locating colorings coincide for every proper coloring of \(\operatorname{Cr}_n\).

**Step 3: the lower bound.** Let \(r\) denote the number of singleton pure-right classes and \(t\) the number of non-singleton pure-right classes, so \(b=r+t\). There are exactly \(m-r\) residual indices whose right endpoints lie in non-singleton right classes. By Step 2, each pure-left class contains at most one of these indices; hence \(a\ge m-r\). If \(t\ge1\), then
\[
p+a+b=p+a+r+t\ge p+m+t\ge n+1.
\]
If \(t=0\), then \(b=m\) and \(a\ge1\), again giving \(p+a+b\ge n+1\). Taking \(U=[n]\), a single left class and \(n\) singleton right classes gives a valid coloring using exactly \(n+1\) classes. Therefore both minima equal \(n+1\).

**Step 4: rigidity at equality.** With exactly \(n+1\) classes, if \(t=0\) then \(a=1\): all residual left vertices make one class and all residual right vertices are singletons. If \(t\ge1\), equality forces \(t=1\), \(a=m-r\), and every pure-left class contains exactly one index of the unique non-singleton pure-right block \(B\), which has size \(m-r\ge2\). The symmetric Step 2 condition says that at most one of the indices in \(B\) lies in a non-singleton pure-left class. Every index in \(U\setminus B\) must join that one class (there is no other pure-left class without a representative from \(B\)). If \(U=B\), all left classes are singleton and the right shore consists of one class, giving the opposite orientation of case 2. Otherwise there is precisely one left non-singleton class \(A=(U\setminus B)\cup\{x\}\) for a unique \(x\in B\). Consequently \(A\cup B=U\), \(A\cap B=\{x\}\) and both have size at least two. Conversely the listed forms obey Step 2 and have exactly \(n+1\) classes. Their structural descriptions are disjoint and their parameters are recoverable from the partition.

**Step 5: exact enumeration.** For a fixed residual index set \(U\) of size \(m\), there is one optimum when \(m=1\); when \(m\ge2\), two oriented one-block configurations; and when \(m\ge3\), there are \(m(2^{m-1}-2)\) configurations with two non-singleton blocks: choose their sole shared index, then assign the remaining \(m-1\) indices nontrivially to the two shores. Thus for all \(m\ge1\), the count is
\[
F(m)=m2^{m-1}-2m+2.
\]
Summing over the \(\binom nm\) choices of \(U\) yields
\[
\begin{aligned}
N_n&=\sum_{m=1}^n\binom nm F(m)\\
&=n3^{n-1}-n2^n+2(2^n-1)\\
&=n3^{n-1}-(n-2)2^n-2,
\end{aligned}
\]
using the binomial theorem and its first derivative. This completes the proof.

## Verification
The standalone `verify_exhaustive.cpp` recursively enumerates every unlabelled set partition of the \(2n\) labelled vertices for \(2\le n\le6\), pruning partitions that are already improper. For each proper partition, it calculates independently the sets of neighbor colors and the distance-to-class vectors from the explicit crown-graph distance table. It checks their equivalence, the minimum class count, and the number of optimal partitions. At \(n=3,4,5,6\), respectively, it inspected \(41,354,4125,61375\) proper partitions and recovered \(17,74,307,1200\) optima.

The independent `verify_constructive.py` generates the three normal-form families on every fixed labelled crown graph for \(2\le n\le8\), directly checks properness and neighbor-color separation, rejects duplicate partitions, and compares the counts with the formula. Both programs return successful completion. These finite tests corroborate, rather than replace, the all-\(n\) argument above.

## Relationship to prior work
Alcón, Gutiérrez, Hernando, Mora and Pelayo [1] introduced neighbor-locating colorings in the relevant formulation and proved for twin-free graphs of order \(v\) the upper bound \(\chi_{NL}\le v-\alpha+1\). For the crown graphs, \(v=2n\) and \(\alpha=n\), giving the already implied **upper bound** \(n+1\). Their inspected general results do not give the matching lower bound, the equivalence with locating colorings, or the exact count and rigidity classification.

Chakraborty, Foucaud, Nandi, Sen and Supraja [2] study sparsity bounds, complexity and separations between locating and neighbor-locating chromatic numbers. The product-graph study [3] treats Cartesian, lexicographic and corona products. Their inspected statements do not imply the present classification on complete bipartite graphs after deletion of a perfect matching. No definitive exhaustive historical-priority claim is made.

## Limitations
The theorem is about the specific complete bipartite minus perfect matching graph family with \(n\ge3\); it does not classify arbitrary matching-deleted bicliques or general bipartite graphs. The counts are of partitions with color names forgotten, on graphs whose \(2n\) vertices retain fixed labels. The conclusions are not independent audits of historical priority or external mathematics.

## References
[1] L. Alcón, M. Gutiérrez, C. Hernando, M. Mora, I. M. Pelayo, *Neighbor-Locating Colorings in Graphs*, arXiv:1806.11465 (first public 2018-06-29), https://arxiv.org/abs/1806.11465.

[2] D. Chakraborty, F. Foucaud, S. Nandi, S. Sen, D. K. Supraja, *On locating and neighbor-locating colorings of sparse graphs*, arXiv:2301.13557 (first public 2023-01-31), https://arxiv.org/abs/2301.13557.

[3] *Neighbor Locating Coloring on Graphs: Three Products*, Journal of Combinatorial Mathematics and Combinatorial Computing 122 (2024), 73–89, DOI:10.61091/jcmcc122-06, https://doi.org/10.61091/jcmcc122-06.
