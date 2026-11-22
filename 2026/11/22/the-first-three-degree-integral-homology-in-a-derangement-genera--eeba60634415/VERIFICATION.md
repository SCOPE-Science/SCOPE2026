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

# Reproducible verification

The companion `derangement_homology_check.py` is standalone Python 3 code using only the standard library. It constructs all derangements of each alphabet of sizes two through six, enumerates every distinct nonempty subsequence, and forms the full signed-deletion cellular boundary matrices over the integers. It checks \(\partial^2=0\) for all applicable dimensions.

It then reduces each integral boundary by elementary unimodular row and column operations about pivots \(\pm1\). All residual matrices are identically zero, certifying that the Smith forms have only unit nonzero factors. Consequently every computed homology group is torsion-free. Separately coded modular Gaussian elimination for three primes reproduces the integer ranks. The Euler identities and exact outputs for all five sizes are asserted.

The actual completed run printed the results in `derangement_homology_check_output.txt`. Replay with `python3 derangement_homology_check.py`; success produces the terminal `PASS` line. These are finite, exhaustive exact certificates for the stated range, not an infinite proof or independent external audit.
