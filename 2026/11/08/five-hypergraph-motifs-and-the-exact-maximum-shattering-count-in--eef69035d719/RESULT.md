# Five hypergraph motifs and the exact maximum-shattering count in rank-three Johnson graphs

## Finding

For every integer \(n\ge3\), let \(J(n,3)\) be the graph whose vertices are the three-element subsets of \([n]\). Two vertices are adjacent when their intersection has exactly two elements. Write \(\mathcal N_{n,3}=\{N(C):C\in\binom{[n]}3\}\) for its **open** neighborhood concept family, and let \(s_4(n)\) count the unordered four-vertex supports shattered by this family.

The exact answer is
\[
\boxed{s_4(n)=
\begin{cases}
0,&3\le n\le5,\\
720,&n=6,\\
\displaystyle\frac{(n)_5(6n^2-17n-41)}{48},&n\ge7,
\end{cases}}
\]
where \((n)_j=n(n-1)\cdots(n-j+1)\). In particular, \(s_4(7)=7035\), \(s_4(8)=28980\), and \(s_4(9)=91980\).

More precisely, **every** shattered four-support, viewed as a simple three-uniform hypergraph on its union of coordinate labels, is isomorphic to one of exactly five types in the table below. An entry \(abc\) denotes the triple \(\{a,b,c\}\). The last column is the minimum ambient \(n\) needed for that type to be shattered.

| Type | Four support triples | Union size \(u\) | Automorphism order | Minimum \(n\) |
|---|---|---:|---:|---:|
| A | 234, 124, 125, 345 | 5 | 2 | 6 |
| B | 156, 136, 236, 456 | 6 | 2 | 6 |
| C | 356, 136, 236, 456 | 6 | 2 | 7 |
| D | 156, 256, 356, 456 | 6 | 48 | 7 |
| E | 167, 247, 347, 567 | 7 | 8 | 7 |

Consequently the counts by type, for \(n\ge7\), are respectively
\[
\frac{(n)_5}{2},\quad\frac{(n)_6}{2},\quad
\frac{(n)_6}{2},\quad\frac{(n)_6}{48},\quad
\frac{(n)_7}{8}.
\]
For \(n=6\) only types A and B occur. Thus among uniformly chosen unordered four-vertex supports in \(J(n,3)\), the probability of shattering is
\[
\frac{s_4(n)}{\binom{\binom n3}{4}}
=\frac{3888}{n^5}+O(n^{-6})\qquad(n\to\infty).
\]
The established VC-dimension bound of four for all Johnson graphs is prior work; the contribution here is the exact rank-three maximum-support census, its five unrooted types, and its asymptotic frequency.

## Assumptions and scope

The graph and query family are finite, with ordinary **open** adjacency: a center does not label itself positive. A support \(S=\{A_1,A_2,A_3,A_4\}\) is shattered if for each subset \(T\subseteq S\) some center \(C\in\binom{[n]}3\) satisfies \(N(C)\cap S=T\). The four triples are distinct. Isomorphism of support hypergraphs permits relabeling the underlying coordinate symbols and reordering the four support triples. No result about closed neighborhoods, other Johnson ranks, online dimension, or induced subgraphs is asserted.

## Proof

**1. A finite, exact incidence encoding.** Temporarily order the support as \(A_1,\ldots,A_4\). Each coordinate symbol \(v\) in its union has a nonempty membership type \(t(v)\in\{1,\ldots,15\}\), whose \(i\)th binary bit records \(v\in A_i\). Let \(m_t\) be the number of coordinates of type \(t\). Each triple has size three if and only if
\[
\sum_{t:\,t_i=1}m_t=3\quad(i=1,2,3,4),
\qquad m_t\in\mathbb Z_{\ge0}.
\tag{1}
\]
Their union size is \(u=\sum_{t=1}^{15}m_t\le12\). The four rows are distinct precisely when, for every \(i<j\), some occupied type has differing \(i\)th and \(j\)th bits. Conditions (1), plus this distinctness test, enumerate **every** ordered four-support up to relabeling of its coordinate symbols; no geometric case is omitted.

**2. All possible traces in each incidence type.** A center \(C\) is another three-element subset. Put \(k_t=|C\cap\{v:t(v)=t\}|\), and let \(k_0\) count its coordinates outside the union. These choices are feasible exactly when
\[
0\le k_t\le m_t,\qquad 0\le k_0\le n-u,
\qquad k_0+\sum_{t=1}^{15}k_t=3.
\tag{2}
\]
The center traces positively on \(A_i\) exactly when
\[
\sum_{t:\,t_i=1}k_t=2.\tag{3}
\]
Hence the vector \(m\) is shattered in an ambient set of size \(n\) **if and only if** the feasible integer vectors in (2) produce all sixteen four-bit patterns by (3). No further combinatorial assumption enters. Since centers have size three, at most three outside coordinates can be used: for a fixed \(m\), scanning \(n-u=0,1,2,3\) settles every ambient size, and shattering is monotone in the number of unused coordinates.

**3. Complete bounded classification.** The standalone `verify.py` enumerates all nonnegative solutions of (1) by recursion on the fifteen membership types, rejecting repeated support rows. For each vector it enumerates all size-three centers on the represented union together with up to three external symbols, applies (3), and records the smallest sufficient number of outsiders. It exhausts exactly \(862\) integer vectors before the row-distinctness filter and finds exactly \(40\) accepted ordered membership vectors. The complete accepted distribution, in the format (union size, minimum outsiders, accepted ordered vectors), is
\[
(5,1,12),\qquad(6,0,12),\qquad(6,1,13),\qquad(7,0,3).
\tag{4}
\]
Quotienting these forty vectors by all twenty-four permutations of the four support-row labels produces exactly five orbits, represented by A–E in the table. Their orbit sizes are \(12,12,12,1,3\), and their minimum-outside requirements are respectively \(1,0,1,1,0\). The executable's enumeration is a finite exhaustive proof: its search space is exactly all solutions of (1), with no parameter cutoff on \(n\) because of the three-outsider reduction. The five displayed representatives, independently checked by the same exact trace equations, provide positive witnesses for all their asserted admissible ambient sizes.

**4. Labeling the motifs.** For one ordered membership vector \(m\) with union size \(u\), the number of realizations on \([n]\) equals
\[
\frac{(n)_u}{\prod_{t=1}^{15}m_t!}.
\]
Every unordered four-support has exactly \(4!\) orderings. Thus the total count is the sum of this quantity divided by \(24\) over the forty accepted vectors with \(n-u\) at least their minimum outsider number. Collecting according to (4) yields
\[
\begin{aligned}
 s_4(n)&=\tfrac12(n)_5+\tfrac12(n)_6&&\text{if }n=6,\\
 s_4(n)&=\tfrac12(n)_5+\tfrac{49}{48}(n)_6+\tfrac18(n)_7&&\text{if }n\ge7.
\end{aligned}
\]
For \(n\le5\) no motif has enough ambient coordinates and the count is zero. Algebraic simplification of the second line gives the boxed formula. The automorphism orders in the table are the reciprocals of the corresponding unlabelled pattern weights. The asymptotic statement follows from \(s_4(n)=n^7/8+O(n^6)\) and \(\binom{\binom n3}{4}=n^{12}/31104+O(n^{11})\).

## Verification

Run `python3 verify.py` in an ordinary Python 3 environment. The exhaustive membership-cell certificate confirms all \(862\) solutions, the \(40\) accepted vectors, the five row-permutation orbits, the four weighted coefficients, and agreement with the closed formula for ambient sizes \(3\) through \(18\).

An independently implemented checker, `direct_check.cpp`, constructs all three-subsets, enumerates **every four-subset** of graph vertices for sizes \(4\le n\le9\), and tests its full sixteen trace masks directly by scanning centers. Compile with `g++ -O3 -std=c++17 direct_check.cpp -o direct_check`, then execute `./direct_check`. It returns the exact counts \(0,0,720,7035,28980,91980\). The second computation does not use motif data or the membership-vector recursion.

The finite certificate establishes the universal formula only in conjunction with Steps 1–2, which prove that its search domain covers all cases. Direct small-size experiments alone would not establish the unrestricted theorem.

## Relationship to prior work

Adler, Benediktsson, and Macpherson (first publicly posted July 31, 2020) proved the general VC-dimension bound four for open neighborhoods on Johnson graphs and analyzed sixteen local configurations around a fixed center, eight of which are shattered. Thus maximum support size and much of the underlying local geometry are already known. This result changes the enumeration problem: it removes the distinguished center, identifies exactly five global rank-three support-hypergraph isomorphism types including their minimum embedding sizes, and computes their exact label multiplicities and asymptotic frequency. The general bound and its existing examples are **not** claimed as new.

Coudert, Csikós, Ducoffe, and Viennot (2024) address algorithms for graph VC dimension, not an explicit rank-three Johnson maximum-support census in the material inspected. Other graph-neighborhood or Johnson rank-two enumerations are related context but do not imply this exact rank-three coefficient without a separate incidence classification and count.

## Limitations

The statement is restricted to the fourth coefficient of the shattered-support polynomial of **open** neighborhoods of rank-three Johnson graphs. The remaining coefficients are not determined. Historical priority remains uncertain, especially if the earlier local Johnson-graph case analysis has been independently converted into an equivalent global enumeration. The finite certificate and its arithmetic have been checked within this package; there has been no independent mathematical audit or comprehensive literature-priority review. The result does not assert a new VC-dimension bound.

## References

1. I. Adler, B. G. Benediktsson, and D. Macpherson, *Vapnik–Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042, first posted 2020-07-31; *Discrete Applied Mathematics* 312 (2022), 29–44. https://arxiv.org/abs/2007.16042 ; https://doi.org/10.1016/j.dam.2021.09.017 . Accepted manuscript: https://eprints.whiterose.ac.uk/id/eprint/178584/ .
2. D. Coudert, M. Csikós, G. Ducoffe, and L. Viennot, *Practical Computation of Graph VC-Dimension*, SEA 2024, DOI:10.4230/LIPIcs.SEA.2024.8. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SEA.2024.8 .
