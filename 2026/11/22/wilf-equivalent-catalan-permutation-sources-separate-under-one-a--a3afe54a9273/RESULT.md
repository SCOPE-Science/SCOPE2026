# Wilf-equivalent Catalan permutation sources separate under one adjacent-swap correction

## Finding
Let \(\operatorname{Av}_n(\tau)\subseteq S_n\) be the one-line permutations of \([n]\) avoiding the classical three-letter pattern \(\tau\in S_3\). A transmission is allowed either no change or a swap of one pair of adjacent *positions*; the receiver is any permutation in \(S_n\), without an avoidance restriction. Let \(M_n(\tau)\) be the largest size of a zero-error source code, \(N_n(\tau)\) the number of labeled maximizing codebooks (subsets, not ordered lists), and \(P_n(\tau)\) the optimal fractional packing weight subject to at most one unit of mass at each received permutation.

For **every** \(\tau\in S_3\) and **every** \(1\le n\le5\), the complete exact table is:

| \(n\) | \(M_n\) for \(\tau=123,321\) | \(N_n\) for \(\tau=123,321\) | \(P_n\) for \(\tau=123,321\) | \(M_n\) for other four patterns | \(N_n\) for other four patterns | \(P_n\) for other four patterns |
|---|---:|---:|---:|---:|---:|---:|
|1|1|1|1|1|1|1|
|2|1|2|1|1|2|1|
|3|2|2|2|2|2|2|
|4|5|2|5|4|17|\(23/5\)|
|5|12|40|12|11|96|\(227/18\)|

Thus the equally numerous Catalan sources first separate in single-adjacent-transposition capacity at \(n=4\):
\[
M_4(123)=5>4=M_4(132).
\]
The nonmonotone family first violates the **integer-rounded** fractional output-packing bound at \(n=5\), while the monotone family remains integral throughout the proved range:
\[
M_5(132)=11<\lfloor P_5(132)\rfloor=12,
\qquad M_5(123)=P_5(123)=12.
\]
There is a fractional (but not integer-rounded) gap at \(n=4\), since \(P_4(132)=23/5\).

## Assumptions and scope
Classical avoidance excludes every three *not necessarily consecutive* positions whose relative order is \(\tau\). All six forbidden patterns yield the Catalan count \(|\operatorname{Av}_n(\tau)|=C_n\), equal to \(1,2,5,14,42\) for \(1\le n\le5\). An adjacent swap exchanges positions \(i,i+1\) of a received full permutation, with no other errors. Every source permutation is labeled and ordinary sequence order matters.

For \(w\in\operatorname{Av}_n(\tau)\), write \(B(w)\) for its unchanged-plus-one-swap output set. The integer feasible families satisfy \(B(u)\cap B(v)=\varnothing\) for distinct codewords. The fractional program has nonnegative variables \(x_w\) and constraints \(\sum_{w:r\in B(w)}x_w\le1\) at every \(r\in S_n\), maximizing \(\sum_w x_w\). Its dual has \(y_r\ge0\), \(\sum_{r\in B(w)}y_r\ge1\), and minimizes \(\sum_r y_r\). The exact certificates supply both vectors for all nontrivial cases.

## Proof
**1. Two orbit types.** Reversing positions preserves the one-swap channel (an index \(i\) becomes \(n-i\)); complementing every value also preserves it. These operations bijectively map avoiding classes and their output sets. Acting on length-three forbidden patterns, their two orbits are \(\{123,321\}\) and \(\{132,213,231,312\}\). They preserve integer capacities, all codebook counts, and the fractional primal/dual optimum, so it suffices to prove the table for \(123\) and \(132\).

**2. Exact confusability.** For two permutations, their unchanged-plus-one-swap balls meet if and only if their Kendall \(\tau\) distance is at most two. In one direction a shared output gives a path of at most two adjacent swaps; in the other direction any shortest path of length zero, one, or two has an intermediate permutation within one swap of both endpoints. Consequently the compatibility graph has one vertex per avoiding source and connects precisely pairs at Kendall distance at least three. Its cliques are exactly the correcting codebooks.

**3. Exhaustive integer capacity and equality counts.** `verify.py` enumerates all \(n!\) permutations and tests all \(\binom n3\) selected triples, so no avoiding input is omitted. It constructs each unchanged-plus-one-swap output set and, independently, recomputes the ordinary Kendall distance as a pair-inversion count; every edge passes this independent equality test. A complete Bron–Kerbosch maximal-clique traversal with exact pivoting enumerates every maximal clique once, giving the maximum size and the exact number of maximum labeled subsets. A separate increasing-index recursion exhaustively counts all cliques of the reported maximum size and verifies that none of the next larger size exists. The two enumerations agree on all cases, including 40 monotone and 96 nonmonotone optima at length five.

For concrete size-five witnesses, a twelve-word \(123\)-avoiding code is

`15432 21543 25431 31542 32154 35241 42153 43152 43251 45132 45231 53412`.

An eleven-word \(132\)-avoiding code is

`12345 23451 32145 34125 34521 41235 45231 51234 52341 53412 54123`.

The verifier regenerates and tests these maxima; they are not being inferred from solver claims or from incomplete samples.

**4. Exact fractional optima.** `certificates.json` stores sparse lists of numerator/denominator pairs for both a feasible fractional packing \(x\) and a feasible output cover \(y\) for each representative at \(n=3,4,5\). Source indices are in lexicographic avoiding-permutation order; output indices are in lexicographic order of the union of the received sets. `verify.py` reconstructs every rational exactly and checks \(x\ge0\), \(y\ge0\), every input and output inequality, and equality of the two objective sums. Weak duality then proves the values \(2,5,12\) in the monotone type and \(2,23/5,227/18\) in the other. For lengths one and two, respectively one input/output and two sources with the same full two-output ball give optimum one directly.

No probabilistic inference or numerical tolerance is used in these claims.

## Verification
Place `verify.py` and `certificates.json` together and run `python3 verify.py` using Python 3. The script uses only the Python standard library, rederives all source words and complete error balls, checks the independent distance computation and two exact clique enumerations for all six forbidden patterns, and validates every rational primal/dual certificate. Expected final line: `VERIFY_OK`. For \(n=5\), the certificate covers 42 source permutations and respectively 84 or 83 distinct observed permutations for the two orbit representatives.

## Relationship to prior work
Dukes, Flanagan, Mansour and Vajnovszki (2007) explicitly generate every classical single-three-pattern-avoiding Catalan family by Gray-code orderings; their distance-four/five figures are **Hamming distances between consecutive words of a full listing**, not a minimum Kendall distance among all pairs in a correcting subcode. Their generating algorithms do not give maximum independent-set packings or fractional incidence optima. Lewis (2008) develops classical \(132\)-avoidance and Catalan enumeration, including relations with alternating avoiding permutations. Buzaglo, Etzion, Yaakobi and Bruck (2013) construct systematic Kendall-metric codes in the full symmetric group; Buzaglo and Etzion (2014, subsequent versions) give sharp unrestricted permutation-code bounds, anticodes and small unrestricted constructions. Those bounds are not equalities for the restricted Catalan source, and do not give the counts of maximizing constrained codes or their fractional output incidence program. The published exact \(S_5\) unrestricted minimum-Kendall-distance-three code theorem gives capacity \(20\) and \(3192\) full-alphabet optimizers, but an upper bound for every subset does not determine induced pattern-avoiding maxima \(11,12\). A published comparison-class study establishes that Wilf-equivalent three-pattern avoidance classes can have different *online comparison-shattering dimensions*; its query-tree parameter does not control adjacent-swap packing or give the table here.

The commonality of Catalan cardinality does not imply equality of local Kendall error neighborhoods. The source restriction and the unrestricted received alphabet are both essential: neither a rank-standardized deletion channel nor a restricted-output channel has the same confusability relation.

## Limitations
The exact capacities, optimizer populations and fractional values are proved **only through \(n=5\)**. No eventual formula, monotonicity claim, or asymptotic gap is asserted. The result does not extend the general all-permutation bounds, and no equalities beyond the two stated pattern orbits are implied. This is an internally checked finite mathematical result, not an independently audited theorem; unindexed historical treatment of equivalent constrained Kendall tables remains a residual novelty risk.

## References
1. W. M. B. Dukes, Mark F. Flanagan, Toufik Mansour and Vincent Vajnovszki, *Combinatorial Gray codes for classes of pattern avoiding permutations*, arXiv:0704.2048, first posted 2007-04-16; Sections 1–2 and the stated Hamming metric and four-position rotation result, https://arxiv.org/abs/0704.2048.
2. Joel Brewster Lewis, *Alternating, pattern-avoiding permutations*, arXiv:0805.1964, first posted 2008-05-14; especially Section 2 on \(132\)-avoidance and Catalan enumeration, https://arxiv.org/abs/0805.1964.
3. Sarit Buzaglo, Eitan Yaakobi, Tuvi Etzion and Jehoshua Bruck, *Systematic Codes for Rank Modulation*, arXiv:1311.7113, first posted 2013-11-27; Sections II–IV, https://arxiv.org/abs/1311.7113.
4. Sarit Buzaglo and Tuvi Etzion, *Bounds on the Size of Permutation Codes with the Kendall \(\tau\)-Metric*, arXiv:1408.4963, first posted 2014-08-21; Sections II–V, https://arxiv.org/abs/1408.4963.
5. *Wilf-equivalent length-three avoidance classes separate in adaptive comparison dimension*, publicly indexed result, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-wilf-equivalent-length-three-avoidance-classes-separate-in-adapt--8a37d59fa16f.
6. *Equality census for optimal \(S_5\) Kendall-\(\tau\) codes at distance \(3\)*, publicly indexed result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-equality-census-for-optimal-s-5-kendall-tau-codes-at-distance-3--01233b6e774d.
