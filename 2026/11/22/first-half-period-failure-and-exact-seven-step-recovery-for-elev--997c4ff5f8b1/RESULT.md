# First half-period failure and exact seven-step recovery for eleven-point prime cycles

## Finding
Let \(p\in\{3,5,7,11\}\), and let \(X_p=\{0,1,\ldots,p-1\}\) carry its usual linear order. For every permutation \(f:X_p\to X_p\) comprising one cycle, define its first \(k\) ordinal orbit comparisons by
\[
 B_k(f)=\bigl(\mathbf{1}_{\{f^t(i)>i\}}\bigr)_{1\le t\le k,\;0\le i<p}.
\]
Write \(h(p)\) for the smallest \(k\) for which \(f\mapsto B_k(f)\) is injective over all \(p\)-cycles. Then the exact minimal horizons are
\[
 \boxed{h(3)=1,\qquad h(5)=3,\qquad h(7)=4,\qquad h(11)=7.}
\]
In particular, eleven is the first odd prime at which observing the first \(\lceil p/2\rceil\) comparisons of *every* orbit point does not recover the cycle. Moreover, the complete six-step ambiguity distribution at length eleven is

| Fiber cardinality | Number of distinct fingerprints | Number of cycles in those fibers |
|---:|---:|---:|
| 1 | 3,470,400 | 3,470,400 |
| 2 | 77,760 | 155,520 |
| 4 | 720 | 2,880 |
| **Total** | **3,548,880** | **3,628,800** |

There are exactly \(82,080\) unordered pairs of distinct eleven-cycles with matching six-step fingerprints. Every one of the \(3,628,800\) seven-step fingerprints is unique.

## Assumptions and scope
The point labels are their *ordered spatial ranks*, not arbitrary names. Each candidate map is a single cycle of the indicated **prime** length; the complete set \(X_p\) and the direction of forward iteration are known. Comparisons are made against each point's original position at successive positive times. Since \(t<p\), no iterate equals its initial point, so strict greater-than and complementary less-than carry the same information. The theorem concerns temporal observations of one periodic orbit, not determining a global interval map from its entire periodic spectrum. All numerical statements are exhaustive exact classifications for \(p\in\{3,5,7,11\}\), with no claim for larger primes.

## Proof
**Canonical exhaustive domain.** Every \(p\)-cycle has one and only one representation
\[
 f=(0,a_1,a_2,\ldots,a_{p-1}),
\]
where \((a_1,\ldots,a_{p-1})\) is a permutation of \(1,\ldots,p-1\) and each entry maps to the next, with the last mapping to zero. These are exactly \((p-1)!\) distinct candidate maps. For \(1\le t<p\), the point of smallest rank always moves to its right and the point of largest rank always moves to its left. Consequently their two indicator columns are constant across candidate cycles. Dropping those columns leaves precisely \(p-2\) informative bits per time step and does not change fingerprint equality.

**Finite complete counting algorithm.** The included `check_horizon.cpp` enumerates all \((p-1)!\) canonical words by lexicographic successor, constructs each cycle's successor array, and evaluates each orbit iterate \(f^t(i)\) by exact integer indexing. Each comparison contributes a bit in a fixed, injective order, so a \(k\)-step fingerprint is represented without collisions by a binary integer with \(k(p-2)\) bits. For the largest required case, \(p=11\) and \(k=7\), this requires only \(63\) bits and fits safely in an unsigned 64-bit integer. The first \(k\) rows are obtained from the full seven-step word by discarding precisely its final \((7-k)(p-2)\) bits. Sorting all resulting integer codes and counting equal consecutive keys gives *exactly* the number of fibers of each cardinality, not a random sample or a truncated search.

The complete enumeration gives \(h(3)=1\). At length five the two-step fingerprint has four two-element ambiguity fibers, while the three-step fingerprint is injective. At length seven the three-step fingerprint has \(508\) singleton, \(92\) doubleton, \(4\) tripleton, and \(4\) four-element fibers, while the four-step fingerprint is injective. At length eleven the six-step fiber census is as displayed above; the seven-step census consists of \(3,628,800\) singleton fibers. Since retaining more time steps can only refine a fingerprint partition, these adjacent noninjective/injective checks prove all four exact minima.

**Explicit obstruction at the eleven-point half horizon.** With cycle notation listing the forward orbit beginning at zero, let
\[
 f=(0,1,2,8,3,4,5,10,6,7,9),\qquad
 g=(0,1,2,10,3,4,5,9,6,7,8).
\]
They are distinct eleven-cycles. For times \(t=1,\ldots,6\), their nine-bit comparison rows over the interior ranks \(1,\ldots,9\) agree, respectively:

`111111100`, `111111000`, `111110000`, `111110010`, `111100100`, `111001000`.

Their seventh strings are `110000010` and `110000001`, respectively. The two omitted extreme-rank comparisons are constant. Thus \(B_6(f)=B_6(g)\) but \(B_7(f)\ne B_7(g)\). The direct checker `check_witness.py` validates the displayed calculation independently of the enumeration.

## Verification
The file `check_horizon.cpp` verifies that every canonical cycle is generated exactly once, that counted fiber cardinalities sum to \((p-1)!\), and that the displayed critical tables and four minimal horizons hold. The separately written `check_phase.cpp` computes the same eleven-point six- and seven-step data via positions in the cyclic word, rather than via repeated successor-array iteration. It independently confirms all three nonzero six-step fiber cardinalities and complete seven-step injectivity. `check_witness.py` directly compares all pointwise orbit directions for the explicit pair. The actual compiler and execution results are reproduced in `CHECK_OUTPUT.txt`; all checks passed. Exhaustive computation is a proof here because every possible object in the stated finite domain is enumerated with exact operations, not because finite tests would imply a theorem for unbounded prime lengths.

To reproduce, using a C++17 compiler and Python 3, run `g++ -std=c++17 -O2 check_horizon.cpp -o check_horizon && ./check_horizon`, then `g++ -std=c++17 -O2 check_phase.cpp -o check_phase && ./check_phase`, and finally `python3 check_witness.py` in the directory containing the files.

## Relationship to prior work
Fuhrmann, Gröger, and Passeggi prove that the **complete** left-right behavior determines any prime cycle, with a reconstruction procedure from all non-return time columns (Lemma 2.1 and Remark 2.4). Their theorem covers injectivity after \(p-1\) steps but does not imply an exact smaller minimal horizon, or determine a six-step ambiguity distribution. The public note *Quadratic-time reconstruction of prime cycles from left-right orbit signatures* improves the algorithm for the *full* signature table; it likewise does not classify shortened signatures. A separate note, *Exact exponential ambiguity fibers for composite ordered periodic cycles*, constructs ambiguous **complete** signatures for composite cycle lengths; its hypothesis explicitly excludes prime lengths. The present theorem supplies the first four exact prime minimal horizons and, at the first failure of the half-period heuristic, an entire exact ambiguity distribution.

## Limitations
The classification stops at eleven and gives no formula, upper bound improvement, or asymptotic for larger primes. The finite checker is source-reproducible rather than independently certified. The first-prime distinction refers only to primes up to eleven, whose complete ordered list starts \(2,3,5,7,11\); the trivial two-cycle is distinguishable at its only non-return observation. These fingerprints assume every orbit point's spatial rank is observed, not noisy, unlabeled, or incomplete data. Independent review of novelty and mathematics has not been performed; older literature not present in the inspected records may contain equivalent specialized enumerations.

## References
1. Gabriel Fuhrmann, Maik Gröger, Alejandro Passeggi, *Period spectrum and rigidity of interval maps*, arXiv:2610.07435v1 (first public 2026-10-05), especially Section 2, Lemma 2.1 and Remark 2.4. https://arxiv.org/abs/2610.07435
2. *Quadratic-time reconstruction of prime cycles from left-right orbit signatures*, publicly available research note (2026), complete-table reconstruction. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-quadratic-time-reconstruction-of-prime-cycles-from-left-right-or--f270190d0cd7
3. *Exact exponential ambiguity fibers for composite ordered periodic cycles*, publicly available research note (2026), composite-cycle fibers. https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-exact-exponential-ambiguity-fibers-for-composite-ordered-periodi--5f39ed9e3fea
