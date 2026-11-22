# Entropy-tight adaptive assignment shattering of valley permutations and the eight-letter gap

## Finding
Let \(\mathcal V_n=\operatorname{Av}_n(132,231)\) be the permutations of \([n]\) avoiding both classical three-letter patterns. For a position \(i\) and a value \(v\), the assignment query \(q_{i,v}\) asks whether \(\pi(i)=v\). A query support is shattered when all of its Boolean answer assignments occur among these permutations. The following statements hold.

1. **All-order adaptive theorem:** for every \(n\ge1\), \(\operatorname{Ldim}(\mathcal V_n)=n-1\) under assignment queries, attained by a concrete adaptive decision tree which recovers one independently chosen left/right bit for every value \(v\ge2\).
2. **All-order static bounds:** for every \(n\ge2\), \(\operatorname{VCdim}(\mathcal V_n)\ge\lceil n/2\rceil\). For every \(n\ge4\), \(\operatorname{VCdim}(\mathcal V_n)\le n-2\). Thus the adaptive dimension is strictly larger than the static dimension at all \(n\ge4\).
3. **Complete exact small-order census:** for \(1\le n\le8\), the complete shattered-support face polynomials are displayed below. At the eight-letter boundary,
\[
\Phi_8(z)=1+52z+510z^2+1238z^3+560z^4,
\quad\operatorname{VCdim}(\mathcal V_8)=4,
\quad\operatorname{Ldim}(\mathcal V_8)=7.
\]
This is the first order with a three-unit adaptive-minus-static gap (the previous gaps at orders \(1\) through \(7\) are respectively \(0,0,0,1,1,2,2\)). The entire finite census, including every absence of larger shattered supports, is certified by exhaustive enumeration of query traces and two independently implemented programs.

| \(n\) | \(\Phi_n(z)\) | VC | Littlestone |
|---:|---|---:|---:|
|1|\(1\)|0|0|
|2|\(1+4z\)|1|1|
|3|\(1+8z+4z^2\)|2|2|
|4|\(1+14z+22z^2\)|2|3|
|5|\(1+21z+68z^2+16z^3\)|3|4|
|6|\(1+30z+150z^2+116z^3\)|3|5|
|7|\(1+40z+294z^2+440z^3+64z^4\)|4|6|
|8|\(1+52z+510z^2+1238z^3+560z^4\)|4|7|

## Assumptions and scope
Positions and values are labeled \(1,\dots,n\); a query is one matrix cell, **not** a pairwise preference comparison, a relative ordering of subsets, or a query asking whether a value lies to one side of another. Queries in supports are distinct. At a node of an adaptive tree the next cell may depend on previous answers, and every complete root-to-leaf binary word must be realized by some permutation.

A permutation avoids both \(132\) and \(231\) exactly when all entries preceding its unique minimum \(1\) decrease strictly, and all entries following \(1\) increase strictly. Indeed, the minimum cannot be the last member of a nonmonotone triple; any ascent to its left gives \(231\), and any descent to its right gives \(132\). Conversely, every possible forbidden triple includes a nonmonotone pair on the appropriate side of its minimum. Thus every hypothesis is uniquely encoded by independent bits \(b_v\in\{0,1\}\), \(2\le v\le n\): put \(v\) to the left of \(1\) iff \(b_v=1\), decreasing to its left and increasing to its right. There are \(2^{n-1}\) hypotheses. For \(v\ge2\) the position of \(v\) is
\[
\operatorname{pos}(v)=
\begin{cases}
1+\displaystyle\sum_{w>v}b_w,&b_v=1,\\
v+\displaystyle\sum_{w>v}b_w,&b_v=0,
\end{cases}
\]
and \(\operatorname{pos}(1)=1+\sum_{w=2}^n b_w\). These equations fix all normalizations used in the proof and checker.

## Proof
**1. The exact online depth.** Query values in decreasing order \(v=n,n-1,\ldots,2\). Once the answers for values larger than \(v\) are known, write \(s=\sum_{w>v}b_w\). Query the assignment cell \((s+1,v)\). If \(b_v=1\), the position formula gives \(\operatorname{pos}(v)=s+1\) and the answer is positive; if \(b_v=0\), its position is \(s+v>s+1\) and the answer is negative. Thus each stage determines the next independent bit and every answer word of length \(n-1\) occurs. Conversely, a complete binary tree of depth \(d\) requires at least \(2^d\) different hypotheses, while the class has exactly \(2^{n-1}\). This proves the online formula, including \(n=1\).

**2. A uniform static lower bound.** First let \(n=2k-1\) with \(k\ge2\). Select the \(k\) assignment queries
\[
S_k=\{(i,2k+1-2i):1\le i\le k\}
=\{(1,2k-1),(2,2k-3),\ldots,(k-1,3),(k,1)\}.
\]
Given arbitrary prescribed answers, for each consecutive pair of values \((2j+1,2j)\) with \(2\le j\le k-1\), place exactly one member on the left. Choose the odd member on the left iff the query for that odd member is prescribed positive. For every one of these \(k-2\) odd queried values \(v\ge5\), exactly one of each higher consecutive pair is left, so its selected queried position is exactly \(1+(k-1)-(v-1)/2\) when \(b_v=1\), and strictly later when \(b_v=0\). This realizes those answers independently. Now choose \(b_3\) to equal the desired answer to \((k-1,3)\): there are exactly \(k-2\) larger values on the left, hence \(\operatorname{pos}(3)=k-1\) iff \(b_3=1\). Finally select \(b_2\) to make \(b_3+b_2=1\) if the query \((k,1)\) is required positive, and to make \(b_3+b_2\ne1\) otherwise (take \(b_2=b_3\) in the negative case). The minimum is at position \(k\) exactly in the first case, so all \(2^k\) answer vectors occur. This proves \(\operatorname{VCdim}\ge k\) for odd \(n\ge3\). For even \(n=2k\), append the new maximum \(2k\) to the right of each permutation on \(2k-1\) elements. This preserves avoidance and all queried positions of the above \(k\) support. At \(n=2\), either of its two hypotheses shatters a singleton coordinate. Hence \(\operatorname{VCdim}\ge\lceil n/2\rceil\) for all \(n\ge2\).

**3. Static dimension cannot reach the cardinality bound for \(n\ge4\).** If a support of size \(n-1\) were shattered, its \(2^{n-1}\) distinct answer words would require every one of the \(2^{n-1}\) hypotheses exactly once. Consequently each of its constituent queries must have marginal positive probability exactly \(1/2\) under the uniform hypothesis distribution.

Let \(B\sim\operatorname{Bin}(n-v,1/2)\). For \(2\le v<n\), the position formula and independence show
\[
\mathbb P(q_{i,v}=1)=\tfrac12\bigl(\mathbb P(B=i-1)+\mathbb P(B=i-v)\bigr).
\]
The two binomial indices differ by \(v-1\ge1\). When \(n-v\ge1\), the sum of their probabilities is **strictly less than one** for \(n\ge4\): the binomial support has at least two indices, and the only way two distinct atoms could exhaust the distribution is the two-point case \(n-v=1\) with adjacent indices, which forces \(v=2,n=3\), excluded. Thus these queries have marginal strictly below one half. For \(v=1\), \(\operatorname{pos}(1)=1+\operatorname{Bin}(n-1,1/2)\), and its largest atom is strictly below one half for \(n\ge4\). The only assignment queries with marginal exactly one half are therefore \((1,n)\) and \((n,n)\), since the maximum is necessarily at one of these endpoints. The two cannot simultaneously be positive, so they cannot form a shattered pair. In particular, a support of \(n-1\ge3\) queries cannot be shattered. Therefore \(\operatorname{VCdim}\le n-2\).

**4. The exact eight-letter finite claim.** For each \(1\le n\le8\), construct all \(2^{n-1}\) permutations by the left/right bits and all nonconstant assignment queries. Starting with the singleton trace \(\{0,1\}\), process a candidate query support by splitting each current hypothesis-class trace on that query. If every one of the \(2^k\) possible Boolean traces survives, the \(k\)-support is shattered. Enumerate only extensions of already shattered supports; this is exhaustive because every subset of a shattered support is shattered. Both independent implementations explicitly enumerate all support extensions, retain every distinct sorted support exactly once, and produce the complete coefficient table above. Their common output gives \(560\) shattered four-cell supports and no shattered five-cell support at \(n=8\); similarly every smaller order is fully classified. The code and outputs are supplied as the finite proof certificate. This is a complete finite enumeration, not a claim about all larger orders.

## Verification
Place `verify_valley.py` and `verify_valley.cpp` in a directory and run `python3 verify_valley.py`, then `c++ -std=c++17 -O2 verify_valley.cpp -o verify_valley_bin && ./verify_valley_bin`. The Python implementation also constructs all permutations directly for \(n\le7\) and verifies that the left/right-bit class equals the classical pattern-avoiders. The C++ implementation constructs the same hypothesis family by a separate insertion recursion and uses fixed-width bitsets for query traces. Both independently certify all face-polynomial coefficients and maximal dimensions through \(n=8\). `checks.txt` records the actual replay output. The all-order parts are proved independently in Steps 1–3; finite experiments do not establish unstated formulas for larger \(n\).

## Relationship to prior work
The classical bit encoding of permutations avoiding both \(132\) and \(231\), equivalent by reversing values to the \(213,312\) family, belongs to the standard enumerative theory of double pattern avoidance. Bukata and coauthors (2018) study such avoidance classes under ascent, descent and peak statistics; that work is not asserted to provide assignment-query learning dimensions. Zhan's (2022) sign representation of single-peaked preferences gives another equivalent left/right encoding, but does not state the fixed-position, fixed-value assignment shattering complex. The previously published *Nested comparison shattering and a continuous-domain VC counterexample for single-peaked preferences* derives the very different polynomial \(\sum_{k}\binom n{2k}z^k\) for **pairwise preference-comparison** queries, not position-value equality tests. The published *Exact online ranks for permutation assignments avoiding a matching* proves a general \(n-1\) online upper bound for permutation-matrix subfamilies and computes it for a differently constrained family, but not the present adaptive construction or exact finite shattering profile. Johnson and Wickes's permutation shattering uses all relative orders of a chosen value subset (\(k!\) possibilities), not Boolean assignment-cell traces.

## Limitations
No closed form or exact VC dimension is claimed for \(n>8\); only the proven all-order static bounds and exact online dimension apply there. The eight-letter polynomial is a reproducible complete finite computation, not an extrapolated theorem. No complexity bounds for learning under other types of preference queries are asserted. Unindexed or differently phrased prior work may imply some or all of the new statement, and historical priority requires independent assessment. No independent mathematical audit has been conducted.

## References
1. M. Bukata, R. Kulwicki, N. Lewandowski, L. Pudwell, J. Roth, T. Wheeland, *Distributions of Statistics over Pattern-Avoiding Permutations*, arXiv:1812.07112, first publicly posted 2018-12-18. https://arxiv.org/abs/1812.07112
2. P. Zhan, *Sign representation of single-peaked preferences and Bruhat orders*, arXiv:2202.11352, first publicly posted 2022-02-23. https://arxiv.org/abs/2202.11352
3. J. R. Johnson, B. Wickes, *Shattering k-sets with Permutations*, arXiv:2112.01946, first publicly posted 2021-12-03. https://arxiv.org/abs/2112.01946
4. *Nested comparison shattering and a continuous-domain VC counterexample for single-peaked preferences*, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-nested-comparison-shattering-and-a-continuous-domain-vc-countere--c8a8ba074d20/RESULT.md
5. *Exact online ranks for permutation assignments avoiding a matching*, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-online-ranks-for-permutation-assignments-avoiding-a-matchi--bbd7533ba4ae/RESULT.md
6. *Comparison shattering of stack-sortable permutations and a linear online gap*, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-comparison-shattering-of-stack-sortable-permutations-and-a-linea--88a936fca69a/RESULT.md
