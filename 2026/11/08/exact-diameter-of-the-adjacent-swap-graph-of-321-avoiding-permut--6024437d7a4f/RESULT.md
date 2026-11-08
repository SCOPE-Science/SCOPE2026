# Exact diameter of the adjacent-swap graph of \(321\)-avoiding permutations

## Finding

For every integer \(n\geq1\), define \(\mathcal A_n\) to be the permutations of \(\{1,\ldots,n\}\) with no indices \(i<j<k\) satisfying \(\pi_i>\pi_j>\pi_k\). Let \(G_n\) have vertex set \(\mathcal A_n\), with two permutations adjacent if one is obtained from the other by exchanging the entries at exactly two consecutive positions. In particular, both endpoints of each edge must avoid the pattern \(321\). Then \(G_n\) is connected, and its exact diameter is

\[
\operatorname{diam}(G_n)=
\begin{cases}
(n^2-1)/2,&n\text{ odd},\\
n^2/2-1,&n\text{ even}.
\end{cases}
\]

When \(n\) is odd and at least three, exactly one unordered pair of vertices realizes the diameter: the two maximum-inversion \(321\)-avoiders. This last assertion is proved below, not extrapolated from the finite checks.

The shortest path in \(G_3\) between the distinct permutations \((2,3,1)\) and \((3,1,2)\) has length four, although their unrestricted adjacent-transposition distance is two. Thus the induced-subgraph metric is genuinely different from the ambient Kendall distance.

## Assumptions and scope

The labels are distinct and individually named. An allowed operation swaps **adjacent positions** and is forbidden whenever its resulting permutation contains a decreasing subsequence of length three. No intermediate permutations violating avoidance are allowed. Graph distance counts the minimum number of such swaps. The statement is for all integers \(n\geq1\), with the one-vertex case \(n=1\) assigned diameter zero. It is not a claim about rotations, arbitrary transpositions, permutation-pattern Gray codes of bounded Hamming distance, or the graph of reduced expressions of a fixed Coxeter-group element.

Let \(\operatorname{inv}(\pi)\) count pairs of positions \(i<j\) with \(\pi_i>\pi_j\). A **left-to-right maximum** is a letter exceeding all letters that precede it.

## Proof

**Lemma 1 (monotone paths to the identity).** Swapping an adjacent inversion, say consecutive entries \(a>b\), changes the inversion number by minus one. It cannot create an occurrence of \(321\), because such a new occurrence would require three inverted value-pairs and no new inverted value-pair was created. Hence every bubble-sort descent can be removed while staying in \(\mathcal A_n\). It takes exactly \(\operatorname{inv}(\pi)\) moves to reach the identity. Reversing another such path gives

\[
d_{G_n}(\pi,\sigma)\leq\operatorname{inv}(\pi)+\operatorname{inv}(\sigma).
\]

This also proves connectivity.

**Lemma 2 (maximum inversions).** Partition the letters of a \(321\)-avoiding permutation into \(A\), its left-to-right maxima, and \(B\), the remaining letters. Both subsequences are increasing: the first by definition; if two letters \(x>y\) of \(B\) occurred in that order, an earlier letter \(z>x\) would exist because \(x\) was not a left-to-right maximum, and \(z,x,y\) would be forbidden. Every inversion therefore crosses the two subsequences. Consequently

\[
\operatorname{inv}(\pi)\leq |A||B|\leq\lfloor n^2/4\rfloor.
\]

If equality holds in the first inequality, **every** cross-subsequence pair must be inverted. A letter of \(B\) preceding a letter of \(A\) cannot be inverted, because a later left-to-right maximum exceeds every preceding letter. Therefore all of \(A\) precedes all of \(B\), with every value in \(A\) exceeding every value in \(B\). Since each subsequence increases, for fixed \(b=|B|\) the only such permutation is

\[
(b+1,b+2,\ldots,n,1,2,\ldots,b).
\]

Equality in the second inequality requires \(b\) to be a nearest integer to \(n/2\). Thus, when \(n=2m\), the maximum \(m^2\) inversions occur at exactly one permutation, and when \(n=2m+1\), the maximum \(m(m+1)\) inversions occur at exactly two permutations.

**Upper bound.** For odd \(n=2m+1\), Lemmas 1 and 2 imply \(d\leq2m(m+1)=(n^2-1)/2\). For even \(n=2m\), two **distinct** vertices cannot both have \(m^2\) inversions because the maximizer is unique. Their inversion sum is therefore at most \(2m^2-1=n^2/2-1\). The distance from a vertex to itself is zero, so this also bounds all pairs.

**Lower bound (a forced double crossing).** For \(n\geq2\), put \(\ell=\lfloor(n-1)/2\rfloor\), \(h=n-\ell-1\), and \(c=\ell+1\). Let \(L=(1,\ldots,\ell)\) and \(H=(c+1,\ldots,n)\), listed increasingly. Both of the following two-block permutations avoid \(321\):

\[
\pi=(c,H,L),\qquad \sigma=(H,L,c).
\]

Take any legal path from \(\pi\) to \(\sigma\). At some step the letter \(c\) must first exchange places with a letter \(x\in H\), changing their order from \(c,x\) to \(x,c\). Before this **first** crossing, all letters of \(H\) still follow \(c\). Just after the crossing, if some \(y\in L\) were still later than \(c\), then \(x,c,y\) would be a decreasing subsequence of length three. Hence every letter of \(L\) has already moved before \(c\), and immediately before the crossing every letter of \(L\) precedes every letter of \(H\).

Initially and finally every letter of \(H\) precedes every letter of \(L\). Thus each of the \(h\ell\) pairs consisting of one \(H\)-letter and one \(L\)-letter must exchange relative order at least twice along any path (once going to the forced intermediate order, once on return). Independently, \(c\) starts before every other letter and finishes after every other letter; it must exchange relative order at least once with each of the \(h+\ell\) other letters. Each adjacent-position swap exchanges the relative order of exactly one value-pair. These requirements are disjoint, so every path has at least

\[
2h\ell+h+\ell
=\begin{cases}(n^2-1)/2,&n\text{ odd},\\n^2/2-1,&n\text{ even}.
\end{cases}
\]

legal moves. The upper bound supplies a path of this length, proving the sharp diameter for all \(n\geq2\). At \(n=1\), both sides are zero.

**Odd-order uniqueness.** Any pair at distance \(2m(m+1)\) for odd \(n=2m+1\geq3\) must have both inversion numbers equal to their maximum \(m(m+1)\), by Lemma 1. Lemma 2 identifies exactly two such permutations, so only their unordered pair can be diametral. The witness above for odd \(n\) is precisely that pair.

## Verification

`verify_enumerate.py` checks all \(321\)-avoiding permutations and **all-source** distances for \(1\leq n\leq8\), using a direct three-index forbidden-pattern test. `verify_prefix.cpp` independently constructs permutations by rejecting forbidden decreasing triples in prefixes, tests all-source distances for \(n\leq8\), and checks the claimed extremal pair by graph traversal for \(n=9,10\). Both programs independently generate all legal adjacent transpositions, compare the Catalan state counts, and require exact agreement with the formula. In their respective environments run:

```sh
python3 verify_enumerate.py
c++ -std=c++17 -O2 -Wall -Wextra verify_prefix.cpp -o verify_prefix
./verify_prefix
```

The finite programs are cross-checks, not substitutes for the preceding all-order proof. Examples of checked values: orders \(3,4,5,6,7,8\) have respective diameters \(4,7,12,17,24,31\); the constructive witness for orders \(9,10\) has distance \(40,49\).

## Relationship to prior work

Pattern-avoiding permutations, their Catalan enumerations, Coxeter interpretations as fully commutative permutations, and inversion statistics are established topics; see Reifegerste, Biagioli–Jouhet–Nadeau, and Chen–Mei–Wang. The bound on the maximum inversion count is included explicitly here as a proof ingredient, not claimed to be independently new. Dukes–Flanagan–Mansour–Vajnovszki construct generation Gray codes with bounded Hamming changes or rotations, rather than computing all-pairs shortest paths inside the adjacency-restricted subgraph. An apparently close paper about a graph of \(312\)-avoiders uses an overlap-window digraph, not adjacent positional swaps. The claimed new result is the exact **geodesic diameter of the induced adjacent-swap graph on all \(321\)-avoiders**, including the forced-double-crossing lower-bound construction and the odd-order diametral-pair uniqueness.

## Limitations

The all-order result concerns **one specific** avoidance class and one specific elementary move. It does not classify all extremal pairs for even orders, compute average distances, or establish analogous formulas for avoidance of a different length-three pattern under arbitrary other moves. Scientific priority is subject to the possibility of older equivalent statements under weak-order or Catalan/permutahedral terminology; source inspection and record searches did not establish exhaustive priority. The verification files cover only the stated finite ranges; the general proof does not depend on their outputs. No independent scholarly audit has been carried out.

## References

1. Astrid Reifegerste, *On the diagram of 132-avoiding permutations*, arXiv:math/0208006, first public posting 2002-08-01. https://arxiv.org/abs/math/0208006
2. W. M. B. Dukes, M. F. Flanagan, T. Mansour and V. Vajnovszki, *Combinatorial Gray codes for classes of pattern avoiding permutations*, arXiv:0704.2048. https://arxiv.org/abs/0704.2048
3. R. Biagioli, F. Jouhet and P. Nadeau, *Fully commutative elements in finite and affine Coxeter groups*, arXiv:1402.2166. https://arxiv.org/abs/1402.2166
4. P. Chen, Z. Mei and S. Wang, *Inversion Formulae on Permutations Avoiding 321*, Electronic Journal of Combinatorics 22(4) (2015), P4.28. https://doi.org/10.37236/5451
5. R. Ehrenborg, S. Kitaev and E. Steingrímsson, *Number of cycles in graph of 312-avoiding permutations* (overlap-window digraph; distinct adjacency notion).
