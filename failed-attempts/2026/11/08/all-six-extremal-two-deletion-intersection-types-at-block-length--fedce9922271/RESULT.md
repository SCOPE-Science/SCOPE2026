# All six extremal two-deletion intersection types at block length four

## Finding
For every finite alphabet of cardinality \(q\ge2\), let \(D_t(w)\) denote the *set of distinct words* obtained by removing exactly \(t\) indexed positions from a length-four word \(w\). For **ordered** length-four words \(x,y\) satisfying
\[
D_1(x)\cap D_1(y)=\varnothing,
\]
the sharp bound is
\[
\bigl|D_2(x)\cap D_2(y)\bigr|\le4.
\]
Equality holds, up to a **single simultaneous bijective relabeling** of alphabet symbols, for precisely these six ordered pairs (the digits represent distinct symbols):

| First word | Second word | Distinct symbols |
| --- | --- | --- |
| `0110` | `1001` | 2 |
| `0112` | `1021` | 3 |
| `0120` | `1002` | 3 |
| `0120` | `1021` | 3 |
| `0120` | `2102` | 3 |
| `0123` | `1032` | 4 |

Consequently the exact number of **labeled ordered** equality cases is
\[
E(q)=(q)_2+4(q)_3+(q)_4,
\]
where \((q)_j=q(q-1)\cdots(q-j+1)\) for \(j\le q\) and \((q)_j=0\) otherwise. In particular, \(E(2)=2\), \(E(3)=30\), and \(E(4)=132\).

## Assumptions and scope
The underlying alphabet consists of \(q\ge2\) labeled symbols. Each deletion output is counted once regardless of how many distinct deletion-position choices yield it. The two source words are ordered, must have length exactly four, and have no common length-three subsequence. The reported six types use equivalence solely under a simultaneous bijective symbol relabeling; reversal and interchange of the words are not additional equivalence operations. This claim concerns precisely two deletions versus one deletion and does not assert maxima at other lengths.

## Proof
**Canonicalization.** Form the concatenation \(xy\), an ordered list of eight alphabet entries. Its equality relation is a set partition of the eight indexed positions. Relabel each distinct alphabet symbol by its rank in order of first occurrence, starting at `0`. The resulting restricted-growth string starts with `0` and has each subsequent digit at most one greater than the maximum of its predecessors. Conversely every such eight-digit string defines exactly one equality pattern up to alphabet relabeling. The total number of length-eight restricted-growth strings is the eighth Bell number, \(B_8=4140\). A pattern with more than \(q\) distinct digits does not occur over an alphabet of size \(q\).

**Exhaustive finite decision.** For each restricted-growth string, split after its fourth entry to produce \(x,y\). For each word form \(D_1\) by deleting each of its four positions, and \(D_2\) by deleting each of the six distinct pairs of positions. Store outputs as sets of symbol tuples, so repeated deletion histories cannot introduce duplicate outputs. Discard a pair if its \(D_1\) intersection is nonempty. Count its distinct common \(D_2\) outputs otherwise. The complete, standalone `checker.cpp` performs this deterministic enumeration using integer symbols and has no source of randomness or external data. Its enumeration visits all \(4140\) restricted-growth strings, finds exactly \(3690\) satisfying the one-deletion disjointness condition, finds a maximum common-two-deletion count of exactly \(4\), and outputs the exact six equality patterns displayed above. Thus, unlike a sample over bounded alphabet sizes, this exhaustive finite check proves the all-alphabet assertion: any pair over any alphabet has one of the enumerated equality patterns, and deletion-set membership depends exclusively on that pattern.

**Label counting.** A canonical pattern with \(j\) symbols has exactly \((q)_j\) labeled instantiations by an injection from its \(j\) symbols into the alphabet. Among the six maximizing patterns, one has two symbols, four have three, and one has four. These are disjoint labeled classes by uniqueness of the first-occurrence canonicalization, giving \(E(q)=(q)_2+4(q)_3+(q)_4\). The two-symbol pattern exists for every \(q\ge2\), so the maximum four is sharp for all such alphabets. This finishes the finite exhaustive proof.

## Verification
Run `g++ -std=c++17 -O2 checker.cpp -o checker && ./checker` with a conforming C++17 compiler. The checker builds the complete restricted-growth tree; it asserts `canonical_patterns==4140`, `admissible_count==3690`, `max_intersection==4`, and precise equality of the maximizer set with the six displayed strings. It also evaluates the formula \(E(q)\) for alphabet sizes two through seven. Separately, direct all-word-pair enumeration over alphabet sizes two, three and four yielded respectively \(2\), \(30\) and \(132\) ordered extremizers; these finite cross-checks are supporting tests, not the reason the theorem holds for all alphabets.

## Relationship to prior work
Wang, Li and Fu (2026) investigate the \(q\)-ary deletion-reconstruction overlap parameter and characterize its large-length behavior. Their sufficiently-large-block-length results do not imply the stated exhaustive length-four equality-pattern classification or its labeled counts. Sun and Ge (2026) examine deletion-ball intersection bounds under lower-order deletion-disjointness constraints, including general upper bounds that specialize to two deletions; those generic upper estimates do not supply this sharp length-four extremizer classification. The exact four-length finite boundary and six ordered equality types are the new focus here. Relevant scholarly search and mathematical-record comparisons did not identify identical earlier classifications, but absence from searchable sources is not a proof of priority.

## Limitations
Only fixed length four, exactly two deletion positions, and disjoint one-deletion output sets are covered. The proof is a finite exhaustive argument over equality patterns, backed by standalone source, not a closed-form structural derivation for arbitrary length. The results do not establish coding-rate bounds, and there remains a risk of an unindexed equivalent finite classification. No independent research audit has been performed.

## References
1. X. Wang, H. Li, F.-W. Fu, *On Sequence Reconstruction Problem for q-ary Deletion Channels*, arXiv:2609.16837, first public 2026-09-15, https://arxiv.org/abs/2609.16837.
2. Y. Sun, G. Ge, *Extremal Deletion-Ball Intersections under Run-Count and Lower-Order Deletion-Ball Intersection Constraints*, arXiv:2606.25822, first public 2026-06-24, https://arxiv.org/abs/2606.25822.
