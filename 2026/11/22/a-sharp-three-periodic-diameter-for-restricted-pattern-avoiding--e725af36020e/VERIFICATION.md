---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

An entry with two lower entries to its right creates 321 or 312. Conversely a binary positional Lehmer word avoids both; a run of k ones followed by a zero uses the next k+1 consecutive values in the relative order (2,3,...,k+1,1). These blocks are ordered by value, so 2341 occurs exactly when some k>=3. Append the forced last zero. At adjacent positions i,i+1 a following zero means the two entries are the two smallest remaining and the swap toggles just b_i. A following one means the second entry is third smallest at step i, so exchanging produces a digit two. Under the resulting right-zero rule each mismatch needs a flip and each forced common one needs two. In the reverse removal and forward insertion sweeps each facilitating neighbor is already zero or still zero, and intermediate words lie coordinatewise below the respective endpoints. This works for every downward-closed binary family and gives precisely |M|+2|F|. In the 111-free case a forced common one has an immediately preceding mismatch: the first forced common one after a mismatch cannot be followed by another forced one without violating 111 in one word. Two forced positions two apart would have word types D-(B or C)-D, with the middle one in an endpoint sharing both D positions, again violating 111. Thus forced positions start at index at least two and are spaced by at least three, giving |F|<=floor((m+1)/3). The (BDC)^h construction with suffix empty, B or BD according to m mod 3 is 111-free in each projection, with all non-D positions mismatches and every D forced; this includes m=1 and 2. The asserted sharp diameter follows. VERIFICATION.md and verify.py were read, not executed; the bounded BFS and direct permutation enumeration described therein are corroboration, not the proof. Replay from RESULT.md lines 25–49; there is no claim for arbitrary adjacent-value moves or general forbidden runs.

## originality

PASS

The distinct main claim is the exact restricted sharp diameter n-1+floor(n/3), with its spacing obstruction and all-residue-class sharpness. The inversion coding, Gray connectivity, weak-order-meet metric, and unrestricted-double-avoidance comparison have verified antecedents as detailed below. The restricted pairwise distance already transfers from the earlier meet result; the forced-coordinate formula is an explicit encoding and constructive proof, not a separate claim to priority for the abstract metric. The unrestricted 2n-3 comparison coincides with a distinct same-day indexed result by symmetry. Neither of these overlaps determines the claimed sharp diameter with the 111 constraint.

## value

PASS

The known adjacency listing establishes a navigable class but gives no sharp worst case. The forbidden run changes exact move complexity on a natural pattern class: the obstruction is propagation of common ones, but 111 forces these obstructions to be separated by three. Packing and explicit extremizers explain the diameter's linear slope and period rather than just computing examples. Value rests on that restricted optimization, not on restating the known meet metric or the unrestricted 2n-3 result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
