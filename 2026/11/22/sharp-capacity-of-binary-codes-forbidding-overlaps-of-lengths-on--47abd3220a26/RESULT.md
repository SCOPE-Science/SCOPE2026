# Sharp capacity of binary codes forbidding overlaps of lengths one through seven

## Finding

Let \(C(n,7)\) be the maximum cardinality of a binary block code of length \(n\) in which no prefix of length \(t\) of any codeword equals a suffix of length \(t\) of any (possibly the same) codeword, for each \(1\le t\le7\). For every integer \(n\ge14\),

\[
\boxed{C(n,7)=744\cdot2^{n-14}.}
\]

The sharp lower construction with 24 allowable seven-bit prefixes and 31 allowable seven-bit suffixes was previously given by Blackburn, Esfahani, Kreher and Stinson. The contribution here is the **matching global upper bound**, established by a complete, reproducible branch-and-bound certificate over the reduced finite overlap graph. In particular, its 744 base value is not presented as a new construction.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\). A code is a **set** of length-\(n\) words, not a multiset, and the forbidden overlaps involve all ordered pairs of words, including equal words. The forbidden overlap lengths are precisely \(1,2,3,4,5,6,7\); overlaps longer than seven are allowed. The blocklength range is \(n\ge14\). No balance, Hamming-distance, cyclic, or additional run-length restrictions are imposed.

Write \(\operatorname{pre}_t(w)\) and \(\operatorname{suf}_t(w)\) for the first and last \(t\) bits. The permitted condition is \(\operatorname{pre}_t(x)\ne\operatorname{suf}_t(y)\) for every ordered \(x,y\) in the code and every \(1\le t\le7\).

## Proof

**Reduction to a finite bipartite problem.** For a nonempty admissible code, prohibition of overlap length one means that its set of first bits and its set of last bits are disjoint nonempty subsets of the binary alphabet. Thus they are singletons of opposite values. Exchanging zero and one if needed, all codewords start with zero and end with one.

Let \(X\) be the set of the 64 seven-bit strings beginning in zero, and let \(Y\) be the set of the 64 seven-bit strings ending in one. For \(p\in X\), define

\[
B(p)=\{s\in Y:\operatorname{pre}_t(p)\ne\operatorname{suf}_t(s)\ \text{for every }1\le t\le7\}.
\]

If \(P\subseteq X\) is the prefix set of a code and \(S\subseteq Y\) its suffix set, then \(S\subseteq\bigcap_{p\in P}B(p)\). Each fixed compatible pair \((p,s)\) permits at most \(2^{n-14}\) distinct middle strings. Conversely, every such middle string may be included: no overlap of length at most seven can depend on middle positions. Hence, with the convention that an empty intersection is \(Y\),

\[
C(n,7)=2^{n-14}\max_{P\subseteq X}|P|\left|\bigcap_{p\in P} B(p)\right|.
\tag{1}
\]

This exact reduction applies for all \(n\ge14\); no limiting argument is used.

**An exact exhaustive upper certificate.** Label the 64 elements of \(X\) as integers from 0 through 63 in big-endian binary, and similarly enumerate the 64 odd integers in \(Y\). The accompanying `verify.py` calculates each \(B(p)\) as a 64-bit integer bitmask by the direct definition. It independently builds the transpose mask table for a reverse search.

For a fixed permutation of the 64 prefixes, let a search node be \((i,c,M)\), where the first \(i\) prefixes have been processed, \(c\) have been included in \(P\), and \(M\) is the intersection of their compatibility masks. The code considers both choices for each unprocessed prefix. At this node, all extensions obey the rigorous upper bound

\[
|P|\,|S(P)|\le(c+64-i)\operatorname{popcount}(M),
\tag{2}
\]

because there can be at most \(64-i\) further chosen prefixes, and intersecting more masks cannot increase the number of compatible suffixes. It is therefore safe to prune if the right side of (2) is at most the best complete value already found. It is also safe to prune a node sharing the same \((i,M)\) with an already explored node having \(c'\ge c\), since the latter has the same possible continuations and a no-smaller objective after each continuation. An include branch producing zero compatible suffixes cannot improve a positive incumbent. All remaining branches are exhaustively searched. No heuristic assumption about the shape of an optimal set is used, and none of these pruning rules can remove a strictly larger valid solution.

The standard-library-only implementation searches 9,209 forward nodes (4,604 retained memo states). The same complete algorithm on the **transposed** compatibility matrix independently searches 9,191 reverse nodes (4,595 retained states). Both certify that the maximum product in (1) is exactly \(744\). The source itself, rather than an uncheckable output log, specifies every finite operation and permits replay. Auxiliary small cases reproduce the independently known maxima \(1,2,6,20,64,216\) at overlap cutoffs one through six; for cutoffs one through four an additional literal all-subsets search matches the optimized search.

**Matching attainment.** Take \(P\) to be the first 24 integers from 0 through 23, represented as seven-bit binary strings. Direct evaluation of the compatibility rule yields exactly 31 suffixes. For reproducibility they are

`0011011 0011101 0011111 0100111 0101011 0101101 0101111 0110011 0110101 0110111 0111011 0111101 0111111 1001101 1001111 1010011 1010101 1010111 1011011 1011101 1011111 1100111 1101011 1101101 1101111 1110011 1110101 1110111 1111011 1111101 1111111`.

Every \(p\in P\) is compatible with every listed suffix, including against itself when relevant. The resulting code consists of all concatenations \(pms\) with \(m\in\{0,1\}^{n-14}\). It has precisely \(24\cdot31\cdot2^{n-14}=744\cdot2^{n-14}\) words and satisfies the seven overlap constraints. This establishes the lower bound. Together with the complete upper computation and (1), it proves the theorem. \(\square\)

## Verification

Use Python 3 (standard library only), in the directory containing `verify.py`:

```sh
python3 verify.py
```

The program recomputes all overlap masks from the seven-bit definition, runs both complete branch-and-bound directions, checks expected smaller-cutoff optima, executes additional raw all-subsets tests for cutoffs at most four, and checks the explicit \(24\times31\) witness against literal string prefix/suffix comparisons. The verified seven-overlap result was \(744\), with forward/reverse visited-node counts \(9209/9191\), respectively. `verification_output.txt` records one reproducible execution. Node counts depend on the fixed deterministic ordering in the supplied script; the mathematical theorem does not depend on them.

## Relationship to prior work

Blackburn, Esfahani, Kreher and Stinson, *Constructions and bounds for codes with restricted overlaps* (first public arXiv release 18 November 2022), introduced the graph formulation and explicitly constructed the \(24\times31\) family, obtaining only the **lower bound** \(C(n,7)\ge744\cdot2^{n-14}\). Their Table V gave a strictly larger upper bound at this cutoff, and discussed the perceived computational difficulty beyond cutoff six. The present result adds a matching upper certificate, not a new graph reduction or lower construction.

Stanovnik (2024) developed upper bounds, constructions and expandability results for broader overlap restrictions, but its reviewed general bounds and statements do not imply the binary seven-overlap sharp value. The 2023 Cai–Wang–Feng work and later work on additional restrictions were consulted to the extent available; inaccessible full text is noted as a historical-priority risk, rather than treated as evidence of noncoverage.

## Limitations

The upper proof uses an exact finite computation, with the complete algorithm supplied for independent replay; it is not a closed-form handwritten inequality for the 64-by-64 incidence problem. The only proved exact cutoff new here is seven, and only for the binary alphabet at blocklength at least 14. No assertion is made for larger cutoff, shorter blocklength, alphabet size greater than two, or stronger non-overlap conditions. Previously published construction and bipartite reduction are explicitly credited. The literature comparison cannot exclude unindexed or inaccessible prior equivalent proofs. No independent external audit has been performed.

## References

1. S. R. Blackburn, N. Nasr Esfahani, D. L. Kreher, D. R. Stinson, *Constructions and bounds for codes with restricted overlaps*, arXiv:2211.10309, first public release 2022-11-18, https://arxiv.org/abs/2211.10309 ; full text https://arxiv.org/html/2211.10309v4 .
2. L. Stanovnik, *Codes with restricted overlaps: expandability, constructions, and bounds*, arXiv:2411.02899, first public release 2024-11-05, https://arxiv.org/abs/2411.02899 .
3. Y. Cai, Z. Wang, K. Feng, *Constructions and Bounds for q-Ary (1,k)-Overlap-Free Codes*, IEEE Transactions on Information Theory, DOI:10.1109/TIT.2023.3319010, https://doi.org/10.1109/TIT.2023.3319010 .
4. H. Yang, C. Ding, *Q-Ary (t1,t2)-Overlap-Free Codes*, DOI:10.1587/transfun.2025EAL2050, https://doi.org/10.1587/transfun.2025EAL2050 .
