# A sharp three-periodic diameter for restricted pattern-avoiding permutation swaps

## Finding

For every integer \(n\ge 2\), let \(\mathcal P_n=\operatorname{Av}_n(321,312,2341)\) consist of the permutations of \(\{1,\ldots,n\}\) avoiding the three listed ordinary (not consecutive) patterns. Form a graph \(G_n\) on \(\mathcal P_n\) by joining two permutations when one is obtained from the other by exchanging two entries in adjacent **positions** and both endpoints are in \(\mathcal P_n\). Then \(G_n\) is connected and its sharp diameter is

\[
\operatorname{diam}(G_n)=n-1+\left\lfloor\frac n3\right\rfloor.
\]

There is also an exact shortest-path formula for every ordered pair. Write \(m=n-1\), and for \(\pi\in\mathcal P_n\) define its positional inversion vector \(b(\pi)=(b_1,\ldots,b_m)\), where \(b_i=\#\{j>i:\pi_i>\pi_j\}\). It is binary and avoids the contiguous factor \(111\). For two such vectors \(x,y\), let \(M=\{i:x_i\ne y_i\}\). Define \(F\), the *forced shared-one set*, by sweeping \(i=1,\ldots,m-1\): initially \(F=\varnothing\); whenever \(i\in M\cup F\) and \(x_{i+1}=y_{i+1}=1\), insert \(i+1\) into \(F\). Then

\[
\operatorname{dist}_{G_n}(\pi,\sigma)=|M|+2|F|.
\]

In particular, every pair has a shortest path using only one flip at each disagreeing inversion coordinate and a remove–restore pair at each forced shared-one coordinate. The three-periodic diameter comes from the sharp packing of those forced coordinates.

## Assumptions and scope

The alphabet is the labeled set \(\{1,\ldots,n\}\). Pattern avoidance means the usual subsequence pattern order type, not avoidance of adjacent factors. A graph edge exchanges entries in adjacent positions, not arbitrary values. All lengths \(n\ge2\) are included; no asymptotic, random model, or infinite-graph conclusion is asserted. An ordinary permutation's positional inversion vector has entries from zero through the remaining suffix length, but the three pattern restrictions force precisely the binary vectors avoiding \(111\) (see the cited 2022 source).

The proof also establishes the forced-coordinate distance lemma in any coordinatewise downward-closed family of binary strings under the rule that bit \(i\) can change only if bit \(i+1\) is zero, with an always-changeable last coordinate. The exact optimized diameter is claimed here for the specific \(111\)-avoiding family, not for every downward-closed family or every forbidden-run length.

## Proof

**1. Bijection and allowed moves.** Barcucci, Bernini and Pinzani (2022), Proposition 5.1, show that the positional inversion vectors of \(\operatorname{Av}_n(321,312,2341)\) are exactly the length-\(m\) binary strings avoiding \(111\). For completeness, the binary part can be seen directly: an entry with two smaller entries to its right would create either \(321\) or \(312\). Conversely, a Lehmer inversion code all of whose digits are zero or one yields a permutation avoiding both. The cited proposition identifies consecutive ones with the additional increasing-then-smallest pattern \(2341\). Reconstruct a permutation from such a vector by repeatedly choosing the smallest remaining value when the next digit is zero, and the second smallest when it is one; the final value is forced.

Set \(b_{m+1}=0\) as a sentinel. When \(b_{i+1}=0\), the values at adjacent positions \(i,i+1\) are the two smallest values available at step \(i\), in one order or the other. Swapping these two entries changes exactly \(b_i\) from zero to one or vice versa, leaving all other inversion digits unchanged. If \(b_{i+1}=1\), the second of the two entries is the third-smallest remaining value if the first is the smallest or second-smallest; swapping puts this third-smallest value first, giving an inversion digit at least two, so the swapped permutation does not avoid \(321,312\). Consequently, the legal edges under the coding are exactly

\[
 x\longleftrightarrow x\oplus e_i\quad\Longleftrightarrow\quad x_{i+1}=0\ \text{and both strings avoid }111,
\]

with \(x_{m+1}=0\). This is the right-facilitated flip graph on the \(111\)-free language.

**2. Exact distances.** Fix legal endpoint strings \(x,y\). Every coordinate of \(M\) must be flipped at least once. If coordinate \(i\) must be flipped while the right neighbor \(i+1\) is one at both endpoints, that neighbor must be changed from one to zero and back, costing at least two moves. Inductively, the forced set \(F\) in the statement consists of distinct common-one positions that must each be flipped at least twice. Thus every path has length at least \(|M|+2|F|\).

Conversely let \(A=M\cup F\). First, sweep positions from right to left, removing every currently present one in \(A\); then sweep from left to right, setting every target one in \(A\). Any position about to change has a zero immediately to its right: if that neighbor is a common one, the definition of \(F\) also puts it in \(A\), so it has already been removed in the first sweep or has not yet been restored in the second; if the neighbor is not a common one, it is either already zero or is a mismatch treated in the proper sweep order. During the removal sweep, each intermediate string is a coordinatewise subset of \(x\). During the restoration sweep, each intermediate string is a subset of \(y\). Since avoiding \(111\) is closed under changing ones to zeros, both sweeps stay in the allowed family. They use exactly one move per mismatch and two moves per forced common one. The lower bound is attained, proving the distance formula and connectivity.

**3. Universal upper bound on the diameter.** At each coordinate encode the pair \((x_i,y_i)\) by \(A=00\), \(B=01\), \(C=10\) or \(D=11\). Every forced coordinate is of type \(D\) and must be preceded (directly or via another forced \(D\)) by a mismatch (type \(B\) or \(C\)). There cannot be two consecutive forced \(D\)'s: that would yield \(BDD\) or \(CDD\), making a forbidden run \(111\) in one endpoint. Nor can two forced \(D\)'s be two positions apart: the intervening symbol must be a mismatch, giving \(BDBD\), \(BDCD\), \(CDBD\), or \(CDCD\). In each case three consecutive bits are one in at least one endpoint. Thus distinct forced coordinates are separated by at least three positions, and none can occupy position one. It follows that

\[
 |F|\le\left\lfloor\frac{m+1}{3}\right\rfloor.
\]

Moreover \(m=|M|+|F|+|\{i:(x_i,y_i)=D,\ i\notin F\}|+|\{i:(x_i,y_i)=A\}|\), whence \(|M|+2|F|\le m+|F|\). Therefore every distance is at most \(m+\lfloor(m+1)/3\rfloor\).

**4. Sharpness for every length.** Let \(m=3h+r\), \(0\le r<3\). Take the pair-symbol sequence \((BDC)^h\), append nothing if \(r=0\), append \(B\) if \(r=1\), or append \(BD\) if \(r=2\). Here \(B=01\), \(D=11\), \(C=10\). Its two binary projections consist of repeated \(011\) and \(110\), respectively, with the stated suffixes, so both avoid \(111\). Every \(D\) immediately follows a mismatch \(B\), hence all \(\lfloor(m+1)/3\rfloor\) occurrences of \(D\) are forced. Every other coordinate is a mismatch, so the distance is precisely \(m+\lfloor(m+1)/3\rfloor\). Substituting \(m=n-1\) yields the theorem. The cases \(n=2,3\) are included by the same construction.

## Verification

The standalone standard-library checker `verify.py` independently generates all permutations through \(n=8\), tests avoidance of all three ordinary patterns directly, constructs every legal adjacent-position swap, and checks exact equality with the claimed binary flip graph. It also builds every \(111\)-free binary flip graph through \(m=10\), performs exhaustive all-pairs breadth-first searches, checks the formula for every distance, verifies connectedness and the sharp diameter. The checked vertex counts for \(m=1,\ldots,10\) are \(2,4,7,13,24,44,81,149,274,504\), and the diameters are \(1,3,4,5,7,8,9,11,12,13\). Run it with `python3 verify.py` from the extracted package directory. No external dependencies or network access are required. These finite checks corroborate; the preceding proof is the all-length justification.

## Relationship to prior work

Barcucci, Bernini and Pinzani (2022) establish the inversion-vector bijection to \(111\)-free binary words (their general parameter \(k=3\)) and construct an adjacent-transposition Gray listing. A Gray listing proves reachability but does not establish shortest-path lengths or the largest such length. The exact sharp diameter and forced-coordinate metric above are the additional assertions.

Mütze (2023) surveys combinatorial Gray-code generation more broadly; Gray-code existence alone does not determine the shortest-path metric of the full legal-move graph. A separately indexed result on the full \(321\)-avoiding adjacent-swap graph gives a weak-order-meet distance expression, but its larger vertex set does not supply this smaller induced graph's sharp maximum without a nontrivial restriction and optimization. Without the extra \(2341\) prohibition, every binary inversion vector is allowed. The same right-facilitated flip rule then has diameter \(2m-1=2n-3\): the general upper bound is \(m+|F|\le 2m-1\), and the endpoint pair-symbol string \(BD^{m-1}\) attains equality. The \(2341\) restriction reduces this sharp maximum to \(n-1+\lfloor n/3\rfloor\), a linear-scale change rather than a numerical edge case.

## Limitations

The result concerns one specific forbidden four-pattern together with the listed two forbidden three-patterns; it does not establish diameters for all longer forbidden runs, other permutation pattern families, unrestricted adjacent swaps, or arbitrary graph move sets. The distance lemma extends to downward-closed binary domains, but its numerical maximum must be optimized separately for other domains. Priority cannot be absolutely guaranteed: an unindexed equivalent formulation or a corollary of a sufficiently strong uninspected theorem may exist. No independent mathematical audit is claimed.

## References

1. E. Barcucci, A. Bernini and R. Pinzani, *Strings from linear recurrences and permutations: a Gray code*, arXiv:2204.10069, first public 2022-04-21, especially Sections 4–5 and Propositions 5.1–5.2. https://arxiv.org/abs/2204.10069 . Published in *Theoretical Computer Science* 938 (2022), 112–120, DOI:10.1016/j.tcs.2022.10.012.
2. T. Mütze, *Combinatorial Gray Codes—an Updated Survey*, *Electronic Journal of Combinatorics*, first published 2023-07-14, https://doi.org/10.37236/11023 . Used as broad context, not as evidence of a full-text novelty exclusion.
3. *Sharp diameter of the 321-avoiding adjacent-swap graph*, publicly indexed mathematical result (2026-10-26), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-diameter-of-the-321-avoiding-adjacent-swap-graph--91a983c81cec . Only the indexed summary was accessible; its exact full-text relationship is a residual priority risk.
