---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

Execute the standalone Python 3 standard-library script `verify.py` in the same directory, using `python3 verify.py`. It directly constructs all open neighborhoods of every cycle and verifies nonempty pairwise distinct traces, without using the forbidden-pair simplification for its graph-level decision. A separate function checks the omission condition and compares results for each binary subset, including the exceptional four-cycle.

The script enumerates every one of 262136 labelled vertex subsets of \(C_n\) for \(3\le n\le17\), finding 2083 OLD codes. Complete size distributions agree with the theorem. A four-state weighted transfer-matrix trace independently counts independent sets of cycle squares of lengths three through ninety and matches every coefficient from the stars-and-bars formula. Full support and the parity-dependent minimum are checked for orders up to 250. The explicit nine-vertex OLD code on \(C_{13}\) also passes direct graph-level testing.

Actual execution:

`VERIFY_OK cycles=3..17 masks=262136 OLD_sets=2083 transfer_cycle_squares=3..90 size_support=3..250 C13_witness=PASS`

This is finite corroboration, not an infinite certificate. The universal assertion is supported by the mathematical bijection and cyclic composition argument. No independent mathematical audit has been performed.
