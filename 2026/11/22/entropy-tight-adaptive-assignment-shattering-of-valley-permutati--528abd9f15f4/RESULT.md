# Entropy-tight adaptive assignment shattering of valley permutations and the eight-letter gap

## Finding

Let \(\mathcal V_n=\operatorname{Av}_n(132,231)\). An assignment query \(q_{i,v}\) asks whether \(\pi(i)=v\). A set of these queries is shattered if every Boolean assignment on that set is realized by some \(\pi\in\mathcal V_n\). Define \(\Phi_n(z)=\sum_S z^{|S|}\), where the sum is over shattered sets of assignment cells.

1. For \(n\ge2\), \(\operatorname{VCdim}(\mathcal V_n)\ge\lceil n/2\rceil\). For \(n\ge4\), \(\operatorname{VCdim}(\mathcal V_n)\le n-2\). In particular, static assignment queries have strictly smaller dimension than the adaptive benchmark at every \(n\ge4\).
2. The complete assignment-cell face polynomials at \(1\le n\le8\) are given below. At \(n=8\), the VC dimension is four and the adaptive-minus-static gap is three for the first time **in this query model**.

For comparison the Littlestone dimension is \(n-1\) at all orders. The adaptive construction is the assignment-cell translation of the known endpoint-deletion tree for single-peaked comparisons, credited below. The claims here concern the **static assignment-cell** bounds and finite census, and the gap they imply against that benchmark.

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

Positions and values lie in \([n]\); each query is one matrix cell, not a pairwise preference comparison. Supports are sets of distinct cells. A complete adaptive tree may choose its next cell based on previous answers; every binary root-to-leaf path must be realized by a hypothesis.

The two forbidden patterns are exactly the three-entry patterns with the largest entry in the middle. In an avoider the entries to the left of the minimum \(1\) must decrease, since any ascent there makes a forbidden triple ending at \(1\); the entries to its right must increase, since a descent there makes a forbidden triple starting at \(1\). Conversely, a middle entry left of \(1\) cannot exceed an earlier entry, and a middle entry right of \(1\) cannot exceed a later entry. The minimum itself cannot be largest. Thus the class consists exactly of these valley permutations, with each value \(v\ge2\) independently placed on the left (\(b_v=1\)) or the right (\(b_v=0\)). In particular, \(|\mathcal V_n|=2^{n-1}\). For \(v\ge2\),
\[
\operatorname{pos}(v)=
\begin{cases}
1+\sum_{w>v}b_w,& b_v=1,\\
v+\sum_{w>v}b_w,& b_v=0,
\end{cases}
\qquad
\operatorname{pos}(1)=1+\sum_{w=2}^n b_w.
\]

## Proof

**1. The adaptive benchmark.** View the position indices as alternatives on an axis and each \(\pi(i)\) as a rank, with rank \(1\) most preferred. Removing the worst remaining alternative from a single-peaked order leaves a smaller interval; the worst remaining alternative is one of its endpoints. After ranks \(n,n-1,\ldots,v+1\) have been decoded, let \(s=\sum_{w>v}b_w\). The interval of unassigned positions is \([s+1,s+v]\). On this node's restricted hypothesis class, the comparison asking whether its left endpoint is less preferred than its right endpoint has exactly the same answers as \(q_{s+1,v}\): the worse endpoint is the position of rank \(v\). Thus the known endpoint-comparison tree can be used without changing its splits, by relabeling each node with this cell. Equivalently, the position formula says the query reads \(b_v\), and all independent strings of these bits occur. This gives a complete tree of depth \(n-1\). The cardinality bound \(2^d\le2^{n-1}\) for any depth-\(d\) tree proves the matching upper bound, including \(n=1\).

**2. A uniform static lower bound.** Let \(n=2k-1\) with \(k\ge2\). Select the fixed support
\[
S_k=\{(i,2k+1-2i):1\le i\le k\}
 =\{(1,2k-1),(2,2k-3),\ldots,(k-1,3),(k,1)\}.
\]
For each pair \((2j+1,2j)\) with \(2\le j\le k-1\), put exactly one member on the left, choosing the odd member exactly when its query is prescribed positive. For such an odd member \(v=2j+1\), there are \(k-1-j\) higher values on the left. Its position is therefore the queried position \(k-j\) exactly when \(b_v=1\). There are \(k-2\) higher values on the left when deciding \(b_3\), so choosing \(b_3=1\) makes the query \((k-1,3)\) positive and choosing \(b_3=0\) makes it negative. Finally the query \((k,1)\) has a positive answer exactly when \(b_3+b_2=1\). Choose \(b_2=1-b_3\) for a positive answer and \(b_2=b_3\) otherwise. This realizes every answer vector on \(S_k\), including for \(k=2\) when the higher pairs are absent. For \(n=2k\) with \(k\ge2\), append the new maximum on the right of each odd-size witness; this preserves avoidance and all queried cells. At \(n=2\), the class \(\{12,21\}\) shatters a singleton cell. Hence the lower bound holds for all \(n\ge2\).

**3. Static dimension cannot reach the cardinality bound for \(n\ge4\).** If a support of size \(n-1\) were shattered, its \(2^{n-1}\) answer vectors would use each hypothesis exactly once. Every constituent query would have positive probability \(1/2\) under the uniform distribution on hypotheses. For \(2\le v<n\), putting \(B\sim\operatorname{Bin}(n-v,1/2)\), the position formula gives
\[
\mathbb P(q_{i,v}=1)=\tfrac12\bigl[\mathbb P(B=i-1)+\mathbb P(B=i-v)\bigr].
\]
The two indices differ by \(v-1\). They can exhaust the binomial support only if the support has two points and the indices are adjacent. That would require \(n-v=1\) and \(v=2\), hence \(n=3\). For \(v=1\), the largest atom of \(1+\operatorname{Bin}(n-1,1/2)\) is strictly less than \(1/2\) at \(n\ge4\) (it is \(3/8\) at \(n=4\) and binomial convolution by a fair bit cannot increase the maximum atom). For \(v=n\), the two half-marginal queries are \((1,n)\) and \((n,n)\), which cannot both be positive. This precludes a shattered support of size \(n-1\ge3\), giving the upper bound.

**4. The finite census.** Construct all \(2^{n-1}\) valley permutations and the nonconstant cell queries. The empty support has one trace class, the entire hypothesis class. When adding a query to a support, intersect each current trace class both with that query's positive set and with its complement. The enlarged support is shattered if and only if all these intersections are nonempty. The supplied programs extend sorted supports only to later nonconstant queries and discard a support as soon as it is not shattered. This counts each shattered support once, and loses none because every subset of a shattered support is shattered. The first empty size layer certifies the absence of all larger faces. The exact enumeration yields the table; subtracting its VC ranks from \(n-1\) at orders one through eight gives \(0,0,0,1,1,2,2,3\).

## Verification

With the supplied files alongside this document, run `python3 verify_valley.py`, and run `c++ -std=c++17 -O2 verify_valley.cpp -o verify_valley_bin && ./verify_valley_bin`. The Python implementation generates left/right bit choices and cross-checks the hypothesis class by direct pattern filtering through \(n=7\); the C++ implementation uses insertion at the two ends and fixed-width bitsets for the traces. `checks.txt` records the outputs for both implementations. The finite census is exact through \(n=8\); the arbitrary-order static bounds use the arguments in §§2–3, not extrapolation from the table.

## Relationship to prior work

The binary coding is standard; see Bukata et al. for the value-complement avoidance class and Zhan for the sign representation of single-peaked rankings. The prior *Nested comparison shattering* result gives the exact endpoint-deletion adaptive tree used in §1. Although the two query domains differ globally, its adaptive splits at the current endpoints are exactly the appropriate assignment-cell splits, so the adaptive value is a credited corollary. Its nested comparison cubes also provide the even-size static lower-bound idea: delete the current endpoints as a two-element block, then repeat, choosing the deletion order within each block independently. At a chosen position of a block, this toggles the cell for the worse rank of that block. Here the odd-size bound uses two independent cell answers on the final three positions, including a query for the minimum.

The comparison-support polynomial \(\sum_k\binom n{2k}z^k\) in that prior result answers a different static question: its degree is \(\lfloor n/2\rfloor\) and at \(n=8\) its coefficients are \(1,28,70,28,1\), not the assignment-cell census. Its three-unit gap first occurs at seven, which does not contradict the assignment-cell cutoff of eight. *Exact online ranks for permutation assignments avoiding a matching* provides a general permutation-matrix upper bound and computes ranks for a different class; its static conclusions do not give the valley support obstruction or census. Johnson–Wickes study traces of all relative orders on a selected value set (\(k!\) orders), not Boolean answers on cells.

## Limitations

No exact VC dimension or coefficient formula is claimed for \(n>8\). The census and gap cutoff are specific to static assignment cells on the valley class. The novelty of the static conclusions is subject to unindexed or differently formulated prior work.

## References

1. M. Bukata, R. Kulwicki, N. Lewandowski, L. Pudwell, J. Roth, T. Wheeland, *Distributions of Statistics over Pattern-Avoiding Permutations*, [arXiv:1812.07112](https://arxiv.org/abs/1812.07112).
2. P. Zhan, *Sign representation of single-peaked preferences and Bruhat orders*, [arXiv:2202.11352](https://arxiv.org/abs/2202.11352).
3. J. R. Johnson, B. Wickes, *Shattering k-sets with Permutations*, [arXiv:2112.01946](https://arxiv.org/abs/2112.01946).
4. [*Nested comparison shattering and a continuous-domain VC counterexample for single-peaked preferences*](https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-nested-comparison-shattering-and-a-continuous-domain-vc-countere--c8a8ba074d20/RESULT.md), particularly Proof §§2 and 4.
5. [*Exact online ranks for permutation assignments avoiding a matching*](https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-exact-online-ranks-for-permutation-assignments-avoiding-a-matchi--bbd7533ba4ae/RESULT.md).
