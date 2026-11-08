# The first excess in uniform distinct-multiple interval matching

## Finding
For an integer \(n\ge1\), define \(F(n)\) to be the smallest positive integer \(H\) for which every interval of consecutive integers
\[
I(m,H)=\{m+1,m+2,\ldots,m+H\},\qquad m\in\mathbb Z,
\]
admits distinct representatives \(a_1,\ldots,a_n\in I(m,H)\) satisfying \(i\mid a_i\) for every \(1\le i\le n\).

The exact first values and the first departure from the elementary lower bound are
\[
\boxed{F(n)=2n-2\quad(2\le n\le16),\qquad F(17)=33.}
\]
Further, among the \(12{,}252{,}240\) start residues modulo \(\operatorname{lcm}(1,\ldots,17)\), exactly 32 fail to admit an assignment in an interval of length 32. The least nonnegative failed start is \(m=485749\). These are exact results, not sample-based estimates.

## Assumptions and scope
Integers and divisibility have their ordinary meanings. All intervals use the half-open convention \((m,m+H]\); repeated integer multiples are not allowed. The start \(m\) may be any integer. For each fixed \(n\), periodicity makes quantification over all starts finite. The exact finite classification claimed here is restricted to \(2\le n\le17\).

## Proof
**Uniform lower bound.** For every \(n\ge2\), put \(m=(n-1)^2\) and \(H=2n-3\). Within \(I(m,H)\), the only integer divisible by \(n\) is \(n(n-1)\), at offset \(n-1\); the same integer is the only multiple of \(n-1\) in that interval. Hence indices \(n-1\) and \(n\) cannot be assigned distinct multiples. Therefore \(F(n)\ge2n-2\).

**Period reduction.** Define \(L_n=\operatorname{lcm}(1,\ldots,n)\). For a fixed \(H\), the divisibility of \(m+j\) by any \(1\le i\le n\) depends only on \(m\bmod L_n\). Therefore existence of a matching for every integer \(m\) is equivalent to existence for every \(0\le m<L_n\).

**Exact finite matching equivalence.** Construct a bipartite graph with left vertices the moduli \(i\in\{1,\ldots,n\}\), right vertices the offsets \(j\in\{1,\ldots,H\}\), and edge \((i,j)\) when \(i\mid m+j\). A matching saturating all left vertices is exactly the required system of distinct multiples. The included `verify.cpp` implements augmenting paths with exact integer divisibility and checks every start in the full period. Its independent, nonrecursive alternating-path implementation also checks every start for \(n<17\), every 997th start at \(n=17\), and all failures at \(n=17\). For each failed start an independent exhaustive Hall-subset check supplies a deficiency witness.

The finite, exhaustive computation gives no failures at \(H=2n-2\) for each \(2\le n\le16\), no failures at \(n=17,H=33\), and exactly 32 failures at \(n=17,H=32\), with least failed residue 485749. Since the implementation traverses *all* residues, the first two results prove the upper bounds \(F(n)\le2n-2\) (\(2\le n\le16\)) and \(F(17)\le33\). Combining with the lower bound yields the complete asserted values.

**Explicit obstruction at \(n=17\).** For \(m=485749\) and \(H=32\), the available offsets for six moduli are
\[
\begin{array}{c|c}
\text{modulus}&\text{eligible offsets}\\\hline
11&11,22\\
12&11,23\\
13&9,22\\
14&9,23\\
15&11,26\\
17&9,26
\end{array}
\]
The union consists of exactly five offsets \(\{9,11,22,23,26\}\) for six moduli; Hall's theorem therefore forbids any assignment at length 32, so \(F(17)>32\). This proves \(F(17)=33\) and that \(17\) is the first excess index.

## Verification
Compile and execute the standalone exact-integer verifier with `g++ -O3 -std=c++17 verify.cpp -o verify && ./verify --dual`. All \(26{,}368{,}160\) period-start/length instances are checked by the primary augmenting-path routine. A second independently written BFS matcher cross-checks every instance for \(n\le16\), a periodic sample for \(n=17\), and every claimed failed instance. The output also contains a deterministic 64-bit checksum of the ordered exceptional residues and their count (32). The explicit six-modulus obstruction can be checked by hand. A finite exhaustive certificate is legitimate here because period reduction is exact.

## Relationship to prior work
Erdős and Pomerance (1980) introduced the uniform interval matching problem and proved general upper bounds. Kominers (arXiv:2607.10431, first posted July 11, 2026) investigated asymptotically large intervals without matchings; Chen (arXiv:2607.26450, first posted July 29, 2026) improved the known asymptotic lower and upper estimates using Hall's framework. These asymptotic theorems neither state nor determine the exact first deviation from the \(2n-2\) lower bound. This work uses the known matching and periodicity principles but computes a new exact initial threshold and an obstruction-residue count. Its historical priority remains subject to possible earlier unpublished tables or unindexed finite computations.

## Limitations
The result does not determine \(F(n)\) for \(n\ge18\). The full-period positive matching assertions depend on executing the supplied finite verifier; the standalone Hall obstruction gives only the lower bound at \(n=17\). The two independent matching implementations are not an independent mathematical audit. Periodicity guarantees completeness only once all \(L_n\) residue classes have been processed. The 32 exceptional residues are a finite-period count, not a density statement uniform in \(n\).

## References
- P. Erdős and C. Pomerance, *Matching the natural numbers up to n with distinct multiples in another interval*, Proceedings A 83 (1980), 147–161, https://math.dartmouth.edu/~carlp/PDF/matching.pdf.
- S. D. Kominers, *Long Intervals Without Distinct Multiples of the First n Positive Integers*, arXiv:2607.10431, first posted 2026-07-11, https://arxiv.org/abs/2607.10431.
- K. Chen, *Improved Bounds for Distinct Multiples in Intervals*, arXiv:2607.26450, first posted 2026-07-29, https://arxiv.org/abs/2607.26450.
- P. Hall, *On Representatives of Subsets*, J. London Math. Soc. 10 (1935), 26–30.
