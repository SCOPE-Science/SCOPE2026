# The four symmetry-and-delay classes of minimal two-neighbour seeds on \(Q_4\)

## Finding

In synchronous two-neighbour bootstrap percolation on the sixteen-vertex binary hypercube \(Q_4\), precisely \(256\) initial vertex sets are inclusion-minimal and eventually infect the whole cube. They form exactly **four** orbits under the \(384\)-element affine coordinate-isometry group. Their seed sizes, percolation times, orbit counts, and representatives are:

| Seed size | Completion round | Number of labelled sets | Representative vertices (four-bit words) | Sorted six or three pairwise Hamming distances |
|---:|---:|---:|---|---|
| 3 | 4 | 48 | 0001, 0111, 1000 | \((2,2,4)\) |
| 3 | 5 | 96 | 0011, 0100, 1000 | \((2,3,3)\) |
| 4 | 3 | 16 | 0001, 0010, 0100, 1000 | \((2,2,2,2,2,2)\) |
| 4 | 4 | 96 | 0000, 0011, 0111, 1000 | \((1,1,2,3,3,4)\) |

An inclusion-minimal three-element set percolates exactly when its unordered Hamming-distance triple is \((2,2,4)\) or \((2,3,3)\). An inclusion-minimal four-element set percolates exactly when either (i) all six distances are two and the bitwise XOR of its vertices is nonzero, or (ii) the six distances are \((1,1,2,3,3,4)\) and the two distance-one pairs are disjoint. These geometric criteria are asserted **only** for the specified seed sizes.

The maximum percolation time for any seed is five rounds, a previously known bound. Its equality classification on \(Q_4\) is: exactly \(192\) labelled seeds attain five rounds, consisting of the \(96\) minimal slow triples above and exactly \(96\) four-element sets. Each slow triple admits **exactly one** fourth vertex whose addition preserves the five-round completion time. These \(96\) extensions are all different and are nonminimal as percolating sets. No other seed attains five rounds.

## Assumptions and scope

Label \(V(Q_4)=\{0,1\}^4\), with edges between words differing in exactly one coordinate. Given an initial set \(A_0=S\), define for all integers \(t\ge1\)
\[
A_t=A_{t-1}\cup\{v\in V(Q_4): |N(v)\cap A_{t-1}|\ge2\}.
\]
A seed *percolates* when \(A_t=V(Q_4)\) for some \(t\). Its *completion round* is the least such \(t\), with round zero referring to the initial state. A percolating seed is *inclusion-minimal* if removing any single selected vertex makes it nonpercolating; monotonicity makes that equivalent to no proper subset percolating. Counts distinguish actual labelled vertex subsets, not quotient orbits. Hamming signatures are unordered multisets; XOR refers to four-bit vector addition in \(\mathbb F_2^4\).

The full isometry group consists of \(x\mapsto b\oplus\pi(x)\), with \(b\in\mathbb F_2^4\) and \(\pi\in S_4\). Hence it has order \(16\cdot24=384\). Its action preserves percolation, minimality and completion time. This result is specifically for binary dimension four and threshold two; no general-dimension orbit formula is asserted.

## Proof

**1. Finite closure recurrence, with exhaustive domain.** Represent any seed by a sixteen-bit integer \(s\). Precompute \(M_v\), the sixteen-bit neighborhood mask of vertex \(v\). Given active mask \(a\), calculate simultaneously
\[
U(a)=a\mathbin{\mathrm{OR}}\bigvee_{v\notin a,\;\operatorname{popcount}(a\mathbin{\mathrm{AND}}M_v)\ge2}2^v.
\]
Here the symbolic powers and bit operations are mathematical descriptions of the checker; integer indices run over \(0,\ldots,15\). The operation is monotone and, if it changes the mask, adds at least one vertex. It therefore stabilizes after at most sixteen changes. Exhaustive evaluation of all \(2^{16}=65{,}536\) masks is a finite proof of all possibilities, not a sample or an extrapolation. The included `verify_direct.cpp` enumerates every mask; for each percolating mask it tests every single-bit deletion. Its exact output is \(63{,}687\) percolating masks and \(256\) inclusion-minimal masks, with the four size-by-time entries \((3,4):48\), \((3,5):96\), \((4,3):16\), \((4,4):96\). It also confirms the global maximum time of five and its count \(96\) at each of sizes three and four, with no other cardinality attaining five.

**2. Symmetry-orbit classification, by a second method.** The independent `verify_orbits.py` generates all \(384\) coordinate-isometries on each of the four explicit representatives. Their image sets have cardinalities \(48,96,16,96\), are pairwise disjoint, and total \(256\). For all seed sets of size at most four, the second checker determines percolation by repeatedly merging subcubes at distance at most two into their minimal containing subcube; the standard subcube-merging theorem identifies the result with two-neighbour bootstrap closure. It checks all \(\sum_{j=0}^4\binom{16}{j}=2{,}517\) subsets in those cardinalities, and the \(256\) minimal ones agree **exactly** with the union of the four generated orbits. The direct checker independently excludes additional inclusion-minimal seeds of sizes five through sixteen. In particular this computation makes no unsupported inference from partial low-cardinality enumeration.

**3. Geometric descriptions.** Direct enumeration of all triples establishes that the two Hamming signatures \((2,2,4)\) and \((2,3,3)\) occur in precisely \(48\) and \(96\) triples, respectively, equal to the two three-seed orbit sizes. Four-element sets with six distances equal to two split into two classes of sixteen; the nonzero-XOR class is the stated sixteen-member orbit. Four-element sets with signature \((1,1,2,3,3,4)\) split into two classes of ninety-six, according to whether the two cube edges share an endpoint or are disjoint; the disjoint-edge class is the stated ninety-six-member orbit. The verifier checks equality between these direct geometric predicates and the four-orbit union. This supplies the claimed *if and only if*, not just example shapes.

**4. Round times and maximal-delay extension uniqueness.** For the four representatives, the successive infection-set cardinalities are, respectively,
\[
(3,7,11,15,16),\quad (3,5,7,11,15,16),\quad
(4,11,15,16),\quad (4,6,10,14,16).
\]
They are obtained by the exact recurrence in step 1 and apply to every member of each orbit by symmetry. The direct checker proves that precisely \(192\) of all \(65{,}536\) seeds attain time five. The independent checker tests each of the \(96\) slow triples against all thirteen unselected fourth vertices: exactly one extension per triple retains time five. All the resulting ninety-six four-sets are distinct. Together with the direct check that there are exactly ninety-six slow four-sets, this completes the equality classification.

## Verification

Two independently implemented and executable artifact paths accompany this result: `verify_direct.cpp` (exhaustive synchronous bitmask dynamics for all masks) and `verify_orbits.py` (coordinate-group orbit construction, subcube-merging percolation tests for sizes at most four, explicit geometric predicates, representative round times and unique slow extensions). Compiling and executing the first with `c++ -O2 -std=c++17 verify_direct.cpp -o verify_direct && ./verify_direct` and the second with `python3 verify_orbits.py` produces a final `PASS` for each. Both were actually executed and their result totals compared. Neither program relies on randomness, third-party libraries or externally generated certificates.

## Relationship to prior work

Riedl established the exact largest size of a minimal percolating set on every binary hypercube; for dimension four it is four. His 2010 paper also notes two isomorphism classes of cardinality-four minimal seeds, a prior classification credited here. Przykucki proved in 2012 the maximum completion time \(\lfloor n^2/3\rfloor\), hence five for dimension four, and supplied an attaining three-vertex example. Shende proved the connection between inclusion-minimal percolating sets and maximal induced paths in hypercubes. None of these inspected statements gives the complete two-size/four-orbit time census, the geometric membership criteria for *all* minimal triples and quadruples, or the unique time-preserving extension of every slow triple. The new content is that joint classification and its equality cases, not the old extremal sizes or general closure principles.

## Limitations

This is an exact finite result, not an asymptotic theorem or a claim concerning higher-dimensional cubes. The geometric membership criteria refer only to seeds of cardinalities three or four. The subcube-merging criterion is a previously known theorem and is not claimed as new. Absolute priority against unpublished and unindexed computations is not established; the results have not been independently audited beyond the documented checks. The cited earlier results about maximal cardinality and maximal time remain prior work.

## References

1. E. Riedl, *Largest Minimal Percolating Sets in Hypercubes under 2-Bootstrap Percolation*, Electronic Journal of Combinatorics 17 (2010), R80. DOI: https://doi.org/10.37236/352 ; full text: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v17i1r80/pdf (first publicly verified 2010-05-25).
2. M. Przykucki, *Maximal Percolation Time in Hypercubes Under 2-Bootstrap Percolation*, Electronic Journal of Combinatorics 19 (2012), P41. DOI: https://doi.org/10.37236/2412 ; full text: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v19i2p41/pdf/ .
3. A. M. Shende, *Maximal induced paths and minimal percolating sets in hypercubes*, Journal of Algebra Combinatorics Discrete Structures and Applications 2 (2015), 17–24. DOI: https://doi.org/10.13069/jacodesmath.15518 ; full text: https://jacodesmath.com/index.php/jacodesmath/article/download/9/7/12 .
