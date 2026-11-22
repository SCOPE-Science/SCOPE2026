# A mod-four square-zero rank defect in parity-preserving fence inverse monoids

## Finding
For every integer \(n\geq1\), let \(M_n=IOF_n^{\mathrm{par}}\) be the inverse monoid of increasing partial injections of the chain \([n]\) which preserve the alternating fence order in both directions and preserve the parity of every point. Let \(0\) be the empty map. Define
\[
R_n=\max\{|\operatorname{dom}f|:f\in M_n,\ f^2=0\},\qquad
T_n=|\{f\in M_n:f^2=0,\ |\operatorname{dom}f|=R_n\}|.
\]
The sharp square-zero rank is
\[
\boxed{R_n=\begin{cases}\lfloor n/2\rfloor-1,&n\equiv2\pmod4,\\\lfloor n/2\rfloor,&n\not\equiv2\pmod4.\end{cases}}
\]
In three of the four congruence classes the entire top-rank stratum has the following closed form, for all \(m\geq0\) with the stated positive chain size:
\[
\boxed{T_{4m}=2^m\ (m\geq1),\quad T_{4m+1}=(m+1)2^m,\quad T_{4m+3}=(m+2)2^m.}
\]
In particular, the obstruction at \(n\equiv2\pmod4\) persists at arbitrarily large sizes, while the full-rank square-zero strata in the other three congruence classes admit explicit run-composition bijections. The case \(n\equiv2\pmod4\) is included in the maximum-rank theorem, but the number of maps at its (one-lower) maximum rank is not claimed in closed form.

## Assumptions and scope
Here \([n]=\{1,\ldots,n\}\), and the alternating fence has covers \(1\prec2\succ3\prec4\succ\cdots\). Each map is an injective partial function that increases along the usual chain order. Two-sided fence preservation requires both the map and its inverse partial map to preserve all comparable pairs in their respective induced fences. Parity preservation means \(f(i)\equiv i\pmod2\). Rank is the number of domain points, not the minimum size of a monoid generating set. The empty map has rank zero and satisfies \(0^2=0\). The boundary values are \(R_1=R_2=0\) and \(T_1=T_2=1\). No statement concerns nilpotency indices greater than two.

## Proof
**1. Pairing and square-zero criterion.** Write the domain and image as increasing lists \(d_1<\cdots<d_k\) and \(i_1<\cdots<i_k\). Increasingness makes \(f(d_j)=i_j\) the unique possible map. The map belongs to \(M_n\) precisely when each \(d_j\equiv i_j\pmod2\) and, for \(1\le j<k\),
\[
d_{j+1}-d_j=1\quad\Longleftrightarrow\quad i_{j+1}-i_j=1.
\]
This is the domain-image characterization of Sareeto and Koppitz [1, Proposition 1]; the parity condition also incorporates their remaining even-gap condition. Since \(f^2\) is defined at \(x\) exactly when \(f(x)\) lies in the domain, \(f^2=0\) if and only if the domain and image are disjoint.

**2. Rank and the one-rank defect.** Disjointness gives \(2k\leq n\). In a parity-preserving bijection from the domain to its image, the two sets contain equal numbers of odd points, and equal numbers of even points. If \(n\equiv2\pmod4\) and \(k=n/2\), these disjoint sets cover the whole chain, but each of the odd and even parity classes has odd cardinality, a contradiction. Thus \(k\leq n/2-1\) in that case. For \(n=4m+2\), a square-zero map of rank \(2m\) is obtained by taking a rank-\(2m\) map on the first \(4m\) positions and leaving the last two positions unused; when \(m=0\), use the empty map. Rank \(\lfloor n/2\rfloor\) is attained for \(n=4m\) by the map taking the first \(2m\) consecutive points in order to the last \(2m\), for \(n=4m+1\) by appending one unused point, and for \(n=4m+3\) by placing one unused point between the two consecutive runs, each of length \(2m+1\). The latter insertion changes their starting-parity discrepancy by one, making it even. These constructions establish the sharp formula for \(R_n\).

**3. A run-composition lemma.** For a square-zero map of rank \(k>0\), color domain points \(D\), image points \(I\), and unused points \(\cdot\). Break a colored word into maximal monochromatic runs, with dots breaking runs. Equality of the two adjacency signatures in Step 1 says that the lengths of the successive \(D\)-runs and of the successive \(I\)-runs are the same ordered composition
\[
a_1+\cdots+a_h=k,\qquad a_j\geq1.
\]
There are precisely \(h\) runs of either color. Suppose at most one dot is present. If no dot is present, the runs strictly alternate and occur in adjacent, consistently oriented pairs \(D^{a_j}I^{a_j}\) or \(I^{a_j}D^{a_j}\), with one orientation throughout. Matched elements in such a pair have the same parity exactly when \(a_j\) is even.

If exactly one dot is present, there are two possibilities. First, the colored run types may still alternate. Then the orientation of all run pairs is fixed; the dot lies either at one of the \(h+1\) boundaries between whole pairs (including the two endpoints), in which case **every** \(a_j\) is even, or between the two runs of precisely one pair, in which case that one \(a_j\) must be odd and all others even. Second, the dot can separate two consecutive runs of the same color, thereby producing exactly one reversal of pair orientation. Such a reversal may occur at any of the \(h-1\) boundaries between adjacent pairs, and requires every \(a_j\) to be even. These alternatives exhaust the possibilities: with at most one dot, the run-type sequence can contain at most one adjacent equal-color pair; its ordered \(D\) and \(I\) run counts are equal, so a change of orientation can only occur between completed pairs. All choices reconstruct distinct maps because the colored word uniquely determines both ordered lists.

**4. Counting the saturated strata.** For \(n=4m\), there are no unused points and \(k=2m\). All \(a_j\) must be even, so \((a_1/2,\ldots,a_h/2)\) is a positive composition of \(m\). For \(m\geq1\) there are \(2^{m-1}\) such compositions and two possible orientations, giving \(T_{4m}=2^m\).

For \(n=4m+1\) and \(m\geq1\), one unused point is present and \(k=2m\). An odd number of odd parts is impossible because the total is even, so the one-odd-part alternative of Step 3 cannot occur. For each positive composition of \(m\) into \(h\) parts there are two initial orientations, \(h+1\) non-reversing placements of the dot and \(h-1\) reversing placements. Thus
\[
T_{4m+1}=4\sum_{h=1}^{m}h\binom{m-1}{h-1}=(m+1)2^m.
\]
The zero-rank boundary \(n=1\) has one map, consistent with the formula.

For \(n=4m+3\), one unused point is present and \(k=2m+1\) is odd. The run lemma forces exactly one odd part, with the dot placed between the two runs of that part. For a composition with \(h\) parts, choose the odd-part index in \(h\) ways, write that part as \(2b+1\) and all other parts as positive even integers, and obtain \(\binom{m}{h-1}\) choices of their half-lengths. Each has two orientations, hence
\[
T_{4m+3}=2\sum_{h=1}^{m+1}h\binom{m}{h-1}=(m+2)2^m.
\]
The binomial identities follow by differentiating \((1+x)^m\) or summing elementary compositions. This proves all asserted formulas.

## Verification
The included standalone standard-library program `verify.py` constructs the actual partial functions from all disjoint domain-image sets, checks both directions of fence comparability, checks pointwise parity, and evaluates the square by composition; it does not assume the run classification. It exhaustively compares maximum ranks and, where asserted, their exact counts for every \(1\le n\le13\). It separately evaluates the composition sums in Step 4. Executing `python verify.py` prints `FENCE_SQUARE_ZERO_SATURATION_VERIFIED` upon success. These finite calculations corroborate but do not establish the infinite formulas.

## Relationship to prior work
Sareeto and Koppitz [1] provide the defining monoid and its domain-image characterization, and determine its semigroup generator rank; [2] studies its ideals, Green relations, and maximal subsemigroups. These facts are inputs here, not new findings. The prior algebraic generating function for the **entire monoid** [3] counts each rank but does not impose disjoint domain and image, so it does not directly determine the sharp square-zero rank defect or the exponential top-stratum counts. The known square-zero census for complete multipartite partial-isometry monoids [4] employs graph-distance isometries with arbitrary partwise injections, whereas the present maps must preserve total-chain and fence order, giving different admissible maps and multiplicities. The order-preserving contraction result [5] concerns maximal *nilpotency index* at prescribed rank rather than maximal *rank* subject to square-zero in this inverse monoid. No global claim of publication priority is made.

## Limitations
The number of maximum-rank square-zero maps when \(n\equiv2\pmod4\) is intentionally not asserted; only the sharp rank bound is established in that congruence class. The theorem does not count lower-rank square-zero maps or higher-index nilpotents. The stated original contribution is the run-composition classification and its saturated counts in the other three residue classes, together with the complete maximum-rank profile. An undiscovered general structural or enumerative theorem could imply some of these conclusions, and the bibliographic searches do not establish independence or absolute priority.

## References
[1] A. Sareeto and J. Koppitz, *The rank of the semigroup of order-, fence-, and parity-preserving partial injections on a finite set*, arXiv:2208.03202, first submitted 5 August 2022, Proposition 1. https://arxiv.org/abs/2208.03202

[2] A. Sareeto and J. Koppitz, *The maximal subsemigroups of the ideals on a monoid of partial injections*, arXiv:2403.06957, first submitted 11 March 2024, Section 2. https://arxiv.org/abs/2403.06957

[3] *Algebraic cardinality series and sharp growth of parity-preserving fence inverse monoids*, published-finding corpus research record (2026), full mathematical statement and rank-refined diagonal formula. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-algebraic-cardinality-series-and-sharp-growth-of-parity-preservi--cd10259c2cbb

[4] *The complete square-zero rank distribution of multipartite partial-isometry monoids*, published-finding corpus research record (2026), general multipartite graph-isometry rank polynomial. https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-the-complete-square-zero-rank-distribution-of-multipartite-parti--aab2f4eae4e5

[5] *Extremal nilpotency in order-preserving partial contractions is governed by integer partitions*, published-finding corpus research record (2026), fixed-rank maximal-index classification. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-extremal-nilpotency-in-order-preserving-partial-contractions-is--cbbee36cc90b
