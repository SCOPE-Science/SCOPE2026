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
# Exhaustive finite verifier

Run `python3 verify.py` on Python 3.10+ without external libraries. The code generates all faces using forbidden Hamming distances four and five, constructs each matching, and enumerates every oriented Hasse cover to certify acyclicity by complete topological sorting. It verifies the full, single-punctured, antipodal-double-punctured, and full vertex-link complexes.

The signed-free discrete-Morse acyclicity certificate is sufficient for the antipodal puncture's one-four-cell CW decomposition. The map statements follow mathematically from link identification and integral long exact sequences. The full and one-puncture homotopy facts were known and are credited. `verification_output.txt` captures successful exact counts. No infinite extrapolation, external certification or independent mathematical audit is asserted.
