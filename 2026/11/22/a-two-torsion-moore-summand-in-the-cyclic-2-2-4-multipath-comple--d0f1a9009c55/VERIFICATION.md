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

# Verification of the finite homotopy classification

The accompanying `verify.py` is the complete deterministic, standalone verifier (Python 3 standard library only). It reconstructs the twenty arc labels and all 2,574 nonempty arc-set simplices; tests the 1,269 matching pairs and all Hasse incidences for acyclicity; calculates the integer Morse differential by signed gradient elimination; and checks the rational rank and two determinantal divisors (gcd of entries = 1 and gcd of all two-by-two minors = 2). This proves Smith factors `(1,2)` for the only nonzero Morse differential. The recorded complete simplicial-chain ranks are also recomputed independently over primes two, three and five. Three alternate matching orders reproduce the rational/mod-two discrepancy.

Reproduction: `python3 verify.py` from this directory. The reproducible console output is in `verify_output.txt`, including the complete five-by-thirty signed Morse matrix. No precomputed external data files, downloads or network access are required. The finite calculation establishes the stated result for exactly this eight-vertex digraph; the verifier makes no inference about larger shores. Scientific review was completed without independent external validation.
