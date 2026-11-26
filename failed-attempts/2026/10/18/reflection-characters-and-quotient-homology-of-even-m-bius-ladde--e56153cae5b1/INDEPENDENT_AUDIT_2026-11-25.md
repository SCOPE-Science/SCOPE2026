# Independent mathematical audit

## correctness

FAIL

The theorem checks with a small proof correction, but the frozen Step 3 makes a false graph identification. Deleting E_(n−j) only for 1≤j<m leaves E_n as well as E_0,…,E_m; at n=4 it leaves six vertices instead of the asserted five. The frozen program's survivor list already omits E_n, but its twin assertions skip j=0, so its log is not evidence for the literal written step. The missing justification is that rim incompatibility reduces to residues differing by ±1 modulo n, with spoke neighbors s_b,s_(b+1) depending only on the residue b. Thus E_j and E_(n−j) are nonadjacent false twins for 0≤j<m, including E_0,E_n; deleting one from each pair gives the path of triangles with tip {s_(-j),s_(j+1)} adjacent to the two successive path vertices. False-twin removal preserves I(−1), and summing over tips leaves exactly the two alternating path selections. The signed Lefschetz factor is (−1)^(d+1) times I(−1), yielding the stated edge trace. The vertex trace is zero because the fixed s_0 has no admissible incident rim orbit. Over Q, averaging the barycentrically subdivided quotient chains gives the invariant homology and the stated ranks. Independent bounded replay checked actual face traces at n=4,6,8,10 and all twin pairs and the corrected adjacency at even n=4,…,40: python3 /workspace/checks/frozen_review_checks.py reflection. The FAIL identifies the proof gap, not a counterexample to the theorem. No repair is submitted because the corrected result is covered.

## originality

FAIL

Distinct Resultary record 5d11c24249b1 contains both trace formulas in the same hypotheses and the orbit-graph triangle-chain proof. Record 73628ced8e0e gives a stronger integral action implying the same traces. The frozen quotient ranks add only the characteristic-zero involution invariant-dimension formula (2+tr)/2 to that coverage. Neither comparator is the assigned record. Their catalogue paths are later; this is a finding of demonstrated overlapping coverage and no distinct scientific remainder under review, not a claim that either historically preceded the frozen statement.

## value

FAIL

The distinction between the two axes and the mod-eight pattern are meaningful invariants. As an incremental contribution, however, the character and evaluation mechanism are covered, and the rational quotient ranks are mechanically recovered from the known character by averaging. The frozen result contributes neither an integral quotient invariant nor a distinct equivariant conclusion. Fixing the extra endpoint twin would not leave an independently valuable result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
