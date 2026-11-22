# Adjacent-repeat rigidity and its sharp alphabet threshold in single-insertion two-list codes

## Finding

For an integer \(q\ge 2\), let \(\Sigma_q=\{0,\ldots,q-1\}\). A code \(C\subseteq\Sigma_q^3\) is *two-list-decodable after exactly one insertion* if every \(y\in\Sigma_q^4\) has at most two **distinct** codeword subsequences of length three. Write \(I_2(q,3)\) for its maximum cardinality and set
\[
A_q=\{abc\in\Sigma_q^3:a=b\text{ or }b=c\}.
\]
The following is a single sharp rigidity-threshold theorem:

1. For \(q=2,3\), \(I_2(q,3)=2q^2-q\), and \(A_q\) is the **unique labeled maximum code**. Thus the exact maxima are respectively \(6\) and \(15\).
2. For every \(q\ge4\), a two-list single-insertion code of cardinality
\[
2q^2-q+\left\lfloor\frac q4\right\rfloor
\]
exists. Hence \(A_q\), while still admissible, is not maximum for any \(q\ge4\). This threshold is exact.

No exact formula for \(I_2(q,3)\) is asserted for \(q\ge4\).

## Assumptions and scope

The channel inserts **exactly one** alphabet symbol at an arbitrary position of each three-symbol codeword. A received word is counted once per distinct source codeword, not once per embedding or insertion position. Codes need not be linear, symmetric, or constant-composition. A labeled maximum means a specified subset of the fixed alphabet's words; equality of codebooks is literal, not modulo relabeling. In this sense uniqueness is stronger than uniqueness up to alphabet permutations. The primary setting is nonbinary synchronization-error coding (MSC2020 94B25).

## Proof

**1. A universal two-list code.** The complement of \(A_q\) consists of the \(q(q-1)^2\) triples whose adjacent symbols are unequal, so \(|A_q|=2q^2-q\). Every received four-symbol word has at most two distinct three-symbol deletion outputs with an adjacent equality. To check this without a hidden alphabet bound, replace the distinct letters of a four-symbol word by \(0,1,\ldots\) in order of first appearance. The fifteen possible equality-pattern representatives are

`0000, 0001, 0010, 0011, 0012, 0100, 0101, 0102, 0110, 0111, 0112, 0120, 0121, 0122, 0123`.

In this order, the numbers of **distinct** one-deletion outputs lying in \(A_q\) are

`1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 0, 1, 2, 0`.

Each representative can be checked by deleting each of its four positions. The count is at most two, independent of \(q\).

**2. Sharpness and rigidity for \(q=2,3\).** For each received word, encode the set of its distinct length-three deletion outputs as a bit mask indexed lexicographically over \(\Sigma_q^3\). An arbitrary code of cardinality \(k\) is feasible exactly when each received-word mask intersects its code mask in at most two bits. The standalone `verify.cpp` enumerates every fixed-cardinality code mask, with no pruning that might omit a candidate. The complete size-layer results are:

| \(q\) | Code size tested | Number of code masks | Feasible masks |
|---|---:|---:|---:|
| 2 | 7 | 8 | 0 |
| 2 | 6 | 28 | 1 |
| 3 | 16 | 13,037,895 | 0 |
| 3 | 15 | 17,383,860 | 1 |

The layer sizes equal the corresponding binomial coefficients; the one feasible mask in each lower layer is exactly \(A_q\). Since feasibility passes to subsets, no code larger than the tested forbidden layer can exist. This proves both optima and literal uniqueness. Enumeration is a finite exhaustive proof of these two cases, **not** extrapolation from samples.

For reproducibility, the mask successor in the verifier takes a nonzero bit mask \(s\) of fixed Hamming weight, sets \(\ell=s\mathbin{\&}(-s)\), \(r=s+\ell\), then replaces \(s\) by \(r\mathbin{|}(((r\oplus s)\gg2)/\ell)\). This is the standard next larger integer of the same bit weight: it raises the lowest movable one and repacks all displaced lower ones into the least significant available positions. Starting at the lowest mask and stopping at the alphabet-sized limit visits each fixed-weight mask exactly once. The verifier also independently checks the total number visited.

**3. A four-letter improvement.** Over \(\{0,1,2,3\}\), take the following 29 source words:

`000 002 003 011 021 022 031 033 102 103 111 112 113 120 130 200 201 213 220 222 223 233 300 301 312 322 330 332 333`.

The standalone verifier generates all \(4^4=256\) possible received words, deletes each of their four positions, deduplicates identical outputs, and checks that no received word has more than two members of the displayed code. Thus this code has size \(29\), compared with \(|A_4|=28\). This is a complete finite certificate for the base block, not an optimizer's unsupported status.

**4. The blockwise lift.** For \(q\ge4\), partition the first \(4\lfloor q/4\rfloor\) alphabet symbols into disjoint blocks of four; possibly fewer than four symbols remain. Start from \(A_q\). In each complete four-symbol block, remove its 28 entirely-in-block members of \(A_q\) and insert a relabeled copy of the 29-word code from Step 3. Leave all words that are not entirely in a complete block unchanged.

To prove admissibility, fix any received four-word \(y\). If all its symbols lie in one complete block, the base certificate applies. If no complete block contains at least three of its symbols, every surviving source belongs to \(A_q\), and Step 1 applies. Otherwise precisely three symbols lie in one complete block and one lies outside. There is at most one distinct source word entirely inside that block (delete the outside symbol); there is at most one remaining eligible adjacent-repeat source containing that outside symbol. For the latter assertion, among the three in-block positions a deletion must leave two equal symbols adjacent to each other; deleting distinct occurrences cannot give two different resulting adjacent-repeat words containing the outside symbol. This also follows immediately from the fifteen equality patterns in Step 1, by marking the uniquely outside symbol. Therefore every received word has at most two source parents.

Each complete block increases the code's size by one, giving the stated \(2q^2-q+\lfloor q/4\rfloor\) construction. Since the increment is positive exactly for \(q\ge4\), the claimed threshold follows.

## Verification

The package contains a dependency-free C++17 program `verify.cpp` and its captured output `verification-output.txt`. Compile and run, for example, with:

```sh
g++ -std=c++17 -O2 -Wall -Wextra verify.cpp -o verify
./verify
```

The program checks both exhaustive small-alphabet size layers, identifies their unique optimum with the adjacent-repeat set, verifies the 29-word base code against all 256 received words, and directly checks the disjoint-block construction for every \(4\le q\le12\). The infinite-alphabet-size statement instead rests on the blockwise argument above, not on those finite checks. Separately, the two ternary integer optima and the exclusion of the displayed optimum were reproduced by an independently constructed incidence matrix and mixed-integer optimization; the exhaustive C++ verifier is the standalone proof certificate.

## Relationship to prior work

Con, Doron and Ribeiro (arXiv:2607.03989, first public July 4, 2026) establish the **asymptotic binary insertion list-decoding capacity**. Its full-text Sections 1 and 3 discuss binary long-block asymptotics and do not provide the three-symbol ternary exact optimum, equality classification, or the four-symbol block lift. Hayashi and Yasunaga's Johnson-type results bound list decoding through code distance and do not imply the exact unrestricted short-block packing/rigidity classification. Kiah, Wei and Zeng (arXiv:2609.21395, first public September 18, 2026) study broad constant-list insertion–deletion bounds; the accessible abstract does not state this exact result, but full-text inspection was not possible and remains a priority risk.

The published finite two-symbol, two-list insertion–deletion separation concerns **two-symbol source words**, not the three-symbol codebooks here. The known fractional **covering** of four-symbol outputs by three-symbol inputs minimizes a different objective; it does not determine the integral two-list **packing** optimum or uniqueness. Searches for equivalent ternary capacity tables, adjacency-run constructions, and the all-alphabet threshold found no direct statement. Absence from the inspected material is not a proof of novelty.

## Limitations

The exact optimum is established only for alphabet sizes two and three. For every larger alphabet the result is a constructive lower bound, not an exact capacity theorem; the improvement \(\lfloor q/4\rfloor\) may be far from best possible. No assertion is made about two or more insertions, different list sizes, longer block lengths, probabilistic channels, or linear-code restrictions. The uniqueness proof for the ternary case relies on a fully specified exhaustive 27-bit computation that must be executed or independently reviewed to validate the finite certificate. General unindexed extremal-digraph or list-packing literature could contain an equivalent result.

## References

1. R. Con, D. Doron, J. Ribeiro, *The Insertion List-Decoding Capacity and an Improved Bound on the Deletion List-Decoding Capacity*, arXiv:2607.03989v1 (July 4, 2026), https://arxiv.org/abs/2607.03989 .
2. T. Hayashi, K. Yasunaga, *On the List Decodability of Insertions and Deletions*, IEEE Transactions on Information Theory 66 (2020), 5335–5343, https://doi.org/10.1109/TIT.2020.2981321 .
3. H. M. Kiah, H. Wei, R. Zeng, *Constant-List Insertion--Deletion Codes: New Bounds and an Improvement of Levenshtein's Lower Bound*, arXiv:2609.21395v1 (September 18, 2026), https://arxiv.org/abs/2609.21395 .
4. *A sharp two-symbol list-two insertion–deletion separation* (public research record, 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-a-sharp-two-symbol-list-two-insertion-deletion-separation--777a6308e057 .
5. *Exact fractional covering of four-symbol supersequences by three-symbol subsequences* (public research record, 2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-fractional-covering-of-four-symbol-supersequences-by-three--e156c97c4d80 .
