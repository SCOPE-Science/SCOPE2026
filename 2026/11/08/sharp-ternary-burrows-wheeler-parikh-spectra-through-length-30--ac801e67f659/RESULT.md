# Sharp ternary Burrows–Wheeler Parikh spectra through length 30

## Finding
Let the ordered alphabet be \(\Sigma=\{0,1,2\}\). For a word \(L\in\Sigma^n\), let \(F\) be its nondecreasing rearrangement. Let \(\pi_L\) be the stable occurrence-rank permutation: the \(r\)-th appearance of a letter \(a\) in \(L\), numbered from zero, is mapped to position \(\sum_{b<a}|L|_b+r\) in \(F\). Call \(L\) *sharp* if it has unequal adjacent symbols, \(\pi_L\) is one \(n\)-cycle, and its Hamming distance from \(F\) is \(\lceil n/2\rceil\).

For every integer \(13\le n\le30\), and every sorted triple \(\lambda=(\lambda_1,\lambda_2,\lambda_3)\) of nonnegative integers summing to \(n\), the accompanying `data/parikh_profiles.csv` gives the **exact** number \(T_n(\lambda)\) of sharp last columns \(L\) with sorted Parikh vector \(\lambda\). All triples absent from the file have count zero. Each present triple has an explicit witnessing last column.

The aggregate counts are:

| \(n\) | sharp last columns | realized sorted Parikh triples |
|---:|---:|---:|
|13|28|4|
|14|4|1|
|15|88|4|
|16|22|3|
|17|120|5|
|18|30|3|
|19|256|6|
|20|61|4|
|21|540|8|
|22|94|4|
|23|1084|9|
|24|180|6|
|25|2148|11|
|26|330|5|
|27|3956|12|
|28|595|8|
|29|8322|16|
|30|1072|6|

In particular, every \(n\) in this range realizes the sharp input cyclic-run bound \(U_3(n)=\lceil n/2\rceil\). A notable compositional obstruction occurs at length \(14\): the only realized sorted triple is \((4,4,6)\), with precisely four sharp last columns; the even, balanced triple \((2,6,6)\) is not realized, despite satisfying the previously known parity restriction.

## Assumptions and scope
The BWT is defined by lexicographically sorting all cyclic rotations of a **primitive** word and taking their last column, without a sentinel. Its input is a necklace, so the cyclic-run count \(\rho^\circ\) is well defined. The ordinary run count of \(L\) is \(n\) precisely when \(L_i\ne L_{i+1}\) for all \(0\le i<n-1\); equality of the first and last letters is allowed. The Parikh triple in the table is sorted solely for grouping: labels \(0<1<2\) remain fixed in the enumeration, and the count includes all label assignments that actually occur, without asserting every assignment is realizable. The scope is exactly the eighteen lengths \(13\) through \(30\), inclusive, and alphabet \(\Sigma\).

## Proof
**Reduction.** For a proposed last column \(L\), the standard LF correspondence maps its position \(i\) to \(\pi_L(i)\). If \(\pi_L\) is a single cycle, its orbit reconstructs a primitive word, uniquely up to cyclic rotation, whose BWT last column is \(L\). Conversely every BWT of a primitive necklace gives a single cycle. Along this cycle, consecutive letters of the reconstructed word differ exactly at positions where \(L_i\ne F_i\), so
\[
\rho^\circ(\operatorname{BWT}^{-1}(L))=d_H(L,F).
\]
This standard characterization is recalled in the cited BWT literature. The previously proved factor-two bound \(\rho(\operatorname{BWT}(u))\le2\rho^\circ(u)\) gives \(\rho^\circ(u)\ge\lceil n/2\rceil\) when the BWT has \(n\) ordinary runs.

**Exhaustive finite calculation.** The provided C++17 program `tools/checker.cpp` traverses *all* last columns with \(n\) ordinary runs. The first position has three choices; each later position has exactly two choices, giving exactly \(3\cdot2^{n-1}\) candidates, with no omissions or duplicate words. It computes each letter count, the stable occurrence-rank map, its cycle through position zero, and the exact Hamming distance to sorted \(F\). An \(n\)-cycle is detected if and only if zero returns for the first time after exactly \(n\) iterations. A necessary parity restriction from Kumallagov (2026), requiring all three counts even for even sharp lengths and exactly one odd count for odd sharp lengths, is used only to prune provably ineligible candidates. Unpruned checks were separately run through length \(24\).

For each \(n=13,\ldots,30\), the program accumulates counts by the sorted triple and requires equality to *every* CSV entry and absence of unlisted entries. These are finite exact integer comparisons, not statistical samples. Hence the CSV is exhaustive and every asserted number is exact. The file includes a literal witness for each of the 115 realized length/Parikh-type combinations. The independent script `tools/check_witness.py` directly reconstructs a primitive word from each witness, sorts all of its cyclic rotations, checks that the resulting BWT is the proposed \(L\), and checks its cyclic-run count. At least one verified sharp witness exists at every tested length; the universal lower bound therefore establishes the claimed eighteen values of \(U_3(n)\).

## Verification
With a C++17 compiler and Python 3, run from the package root:

```sh
g++ -std=c++17 -O3 tools/checker.cpp -o bwt_checker
./bwt_checker data/parikh_profiles.csv 13 28
./bwt_checker data/parikh_profiles.csv 29 29
./bwt_checker data/parikh_profiles.csv 30 30
python3 tools/check_witness.py data/parikh_profiles.csv
```

The three C++ invocations together independently recompute every claimed profile over the complete stated range; the Python invocation verifies all 115 direct-BWT witness identities. Splitting the C++ calculation only limits per-process runtime, not the search domain. No randomness, external data files or third-party computational packages are needed.

## Relationship to prior work
Kumallagov, *An extremal problem for completely unclustered Burrows–Wheeler images* (arXiv:2606.01267, first public version May 31, 2026), supplies the lower bound, the parity obstruction and a conjectural general sharpness statement, with its reported small-length results and special infinite families. Fici, Gabory, Romana and Sciortino, *Totally Unclustered BWT Images of Any Length over Non-Binary Alphabets* (CPM 2026), prove existence of unclustered BWT images for all lengths and give lower counting bounds; they do not provide the present exact sharp Parikh-profile census. Earlier work also treats the special \((m,m,1)\) Parikh slice, so the mere existence of that slice and its known individual classification are not claimed as new. The new result is the full range of exact class counts and exclusions for lengths \(13\)–\(30\), including the missing sharp Parikh class \((2,6,6)\) at length \(14\).

## Limitations
The cutoff \(30\) is a genuine finite cutoff: the data do not prove the conjectured sharpness for every larger length or classify all possible Parikh vectors asymptotically. The exact counts enumerate ternary last columns (equivalently primitive necklaces), not all cyclic rotations separately and not alphabets with four or more letters. The preprint of Kumallagov was accessible here through its abstract and detailed secondary synopsis, but not through a complete primary-text inspection; an unindexed equivalent or a table in inaccessible supplementary material remains a historical-priority risk. Independent external validation has not been performed.

## References
1. David Kumallagov, *An extremal problem for completely unclustered Burrows–Wheeler images*, arXiv:2606.01267 (2026), https://arxiv.org/abs/2606.01267.
2. Gabriele Fici, Estéban Gabory, Giuseppe Romana, Marinella Sciortino, *Totally Unclustered BWT Images of Any Length over Non-Binary Alphabets*, CPM 2026, DOI:10.4230/LIPIcs.CPM.2026.13, https://drops.dagstuhl.de/storage/00lipics/lipics-vol369-cpm2026/html/LIPIcs.CPM.2026.13/LIPIcs.CPM.2026.13.html.
3. S. Mantaci, A. Restivo, M. Sciortino, *Burrows–Wheeler transform and Sturmian words*, Information Processing Letters 86 (2003), 241–246, DOI:10.1016/S0020-0190(02)00512-4.
