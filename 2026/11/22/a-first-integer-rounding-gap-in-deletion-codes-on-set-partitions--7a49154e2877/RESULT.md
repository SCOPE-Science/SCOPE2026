# A first integer-rounding gap in deletion codes on set partitions

## Finding

Let \(\Pi_n\) denote the set of unordered set partitions of \([n]=\{1,\ldots,n\}\), with the ground-set order retained but block labels disregarded. For a partition \(P\), let \(\Delta(P)\) be the **set of distinct** partitions of \([n-1]\) obtained by deleting exactly one unknown element and then order-standardizing the survivors. Write \(M_n\) for the maximum number of partitions that can be selected from \(\Pi_n\) with pairwise disjoint deletion sets.

For \(1\le n\le6\),

\[
(M_1,M_2,M_3,M_4,M_5,M_6)=(1,1,2,3,6,14).
\]

Define the fractional shadow-packing optimum

\[
P_n=\max\left\{\sum_{X\in\Pi_n}z_X:\ z_X\ge0,\quad
\sum_{X:Y\in\Delta(X)}z_X\le1\quad(Y\in\Pi_{n-1})\right\}.
\]

**The first failure of integer rounding occurs at size six:** for every \(n\le5\), \(M_n=\lfloor P_n\rfloor\), but

\[
\boxed{M_6=14<15<\frac{243}{16}\le P_6.}
\]

In particular, the natural fractional deletion-packing relaxation cannot certify the exact six-point zero-error capacity, even after rounding down.

## Assumptions and scope

A set partition has unlabelled blocks. Its canonical restricted-growth word \(r_1\cdots r_n\) is obtained by numbering blocks \(0,1,\ldots\) in order of their smallest elements; equivalently, \(r_1=0\) and \(0\le r_i\le1+\max_{j<i}r_j\). Deleting position \(i\) means removing its entry and renumbering remaining block labels by **first occurrence**, not preserving the numerical labels of blocks that may have disappeared. A deletion output is a single partition, not an entire observed deck. Distinct repeated outputs of one source count only once.

This is a finite theorem for \(1\le n\le6\), not a proposed general sequence law. Its source set has \(B_6=203\) members, and its receiver set has \(B_5=52\) members.

## Proof

**1. Exact reduction to a finite conflict graph.** List all canonical restricted-growth words of length \(n\) recursively: from a valid word with \(b\) distinct blocks, append one of its \(b\) existing labels or the new label \(b\). This exhausts \(\Pi_n\), once each, by induction. For each listed source form the set of all canonical words obtained by deleting one position. Construct a graph with one vertex per source and an edge between two vertices if and only if their sets of deletion outputs are disjoint. Thus a code is exactly a clique, and \(M_n\) is the clique number. The complete, deterministic enumeration and bounding search are in `verify.py`.

**2. Exact integer upper bound.** The checker uses a recursive maximum-clique algorithm with a correct coloring bound. At a search node, greedily color the induced graph on candidate vertices, using successive independent color classes. A clique has at most one vertex of each color. Explore candidates in reverse color order, branching on the inclusion of each vertex, and eliminate a branch only if its already-selected cardinality plus its color bound cannot exceed the best attained cardinality. Every possible clique is either visited or safely bounded by this inequality. This exhaustive finite argument returns maxima \(1,2,3,6,14\) for lengths \(2,3,4,5,6\), using respectively \(2,3,4,16,452972\) visited recursion nodes. For length one the bound is immediate. The base recurrence and color-bound induction are entirely combinatorial; there is no numerical optimization tolerance.

**3. Attaining the six-point upper bound.** `CERTIFICATES.json` contains fourteen explicit six-digit restricted-growth words, namely

```
000000 000011 000123 001110 001122 001200 010020
010101 010232 012123 012201 012310 012333 012345
```

The checker regenerates every deletion output of each word, verifies that all fourteen words are distinct eligible sources, and tests that their received-output sets are pairwise disjoint. They cover 45 of the 52 possible received partitions. This supplies the matching lower bound \(M_6\ge14\).

**4. A rational fractional witness beyond fifteen.** Number the 203 length-six restricted-growth words in the lexicographic recursion of Step 1. The list `fractional_6` in `CERTIFICATES.json` gives 41 nonzero integer numerators \(a_j\), with all other numerators zero. Its denominator is 64. Direct integer verification gives

\[
\sum_{j=0}^{202}a_j=972,
\qquad
\sum_{j:Y\in\Delta(X_j)}a_j\le64\quad\text{for every }Y\in\Pi_5.
\]

Consequently \(z_{X_j}=a_j/64\) is feasible and has total weight \(972/64=243/16>15\). This proves the strict rounding failure without needing the exact value of \(P_6\).

**5. Why size six is the first.** For length five, a dual fractional output cover on the 15 canonical length-four partitions, indexed as above, is stored as `cover_5`. Every source deletion set has covering numerator sum at least 4, while the total numerator sum is 25. Summing the covering inequalities against any fractional packing proves \(P_5\le25/4<7\). Since a six-word code exists, \(6\le P_5<7\), so \(\lfloor P_5\rfloor=M_5=6\). For length four the three unit-weight outputs indexed \(0,1,4\) in `cover_4` hit every source deletion set, proving \(P_4\le3=M_4\). For lengths one through three, the receiver-count bounds \(B_0=1\), \(B_1=1\), and \(B_2=2\) equal the attained code sizes. Therefore all shorter lengths have integer-rounding equality.

## Verification

Run `python3 verify.py` in the same directory as `CERTIFICATES.json`. The script uses only the Python standard library and checks every listed rational certificate with exact integers. It separately generates source partitions by inserting a largest ground-set element into unordered blocks, and verifies agreement with the restricted-growth recursion; it also regenerates the size-six deletion relation by **inverse insertion** from all receivers and compares every incidence with forward deletion.

Its complete exhaustive clique search returns `MAX 6 ... capacity 14 nodes 452972`, checks the 14-word code and \(972/64\) witness, and ends with `VERIFY_OK`. The verification counts are part of the reproducible finite proof, not inferences from an experimental sample.

## Relationship to prior work

Chee, Ge, and Ling (2010) study perfect ordinary \(q\)-ary deletion-correcting codes and characterize the size spectrum for specified very short unrestricted word lengths; they do not classify codes over set partitions under block restandardization. Kulkarni and Kiyavash (2012) develop the hypergraph matching and fractional-transversal method, including constrained ordinary word sources, but do not provide the 203-source / 52-output set-partition channel or its integer-rounding threshold. Campbell et al. (first preprint 2016) study standardized restricted-growth patterns and statistics, not disjoint single-deletion shadows; their discussion explicitly distinguishes two notions of pattern containment for partitions. The present receiver operation is standardized *set-partition restriction*, rather than ordinary symbol-preserving word deletion.

An earlier result describing coincidences among deletion outputs **of the same source partition** does not bound the maximum family of sources with mutually disjoint output sets, and does not supply the fractional witness. Published-result and claim/parameter searches did not locate equivalent numerical coverage; this is a qualified literature comparison, not an absolute claim of priority.

## Limitations

No result is claimed for length seven or more; the exact optimum \(P_6\) of the fractional program is not asserted. This theorem depends on exact finite enumeration, with the full source generation, independent incidence construction, pruned-search proof method, explicit code, and rational certificates supplied for replay. Further external indexing or older unindexed work could alter historical priority. No independent mathematical audit has been performed.

## References

1. Y. M. Chee, G. Ge and A. C. H. Ling, *Spectrum of Sizes for Perfect Deletion-Correcting Codes*, SIAM J. Discrete Math. 24 (2010), 33–55. DOI: https://doi.org/10.1137/090751311 ; open preprint https://arxiv.org/abs/1008.1343 (journal first online February 5, 2010).
2. A. A. Kulkarni and N. Kiyavash, *Non-asymptotic Upper Bounds for Deletion Correcting Codes*, preprint first public November 13, 2012, https://arxiv.org/abs/1211.3128 .
3. L. R. Campbell et al., *Restricted growth function patterns and statistics*, preprint first public May 16, 2016, https://arxiv.org/abs/1605.04807 .
4. NIST Digital Library of Mathematical Functions, §26.7, *Set Partitions: Bell Numbers*, https://dlmf.nist.gov/26.7 .
