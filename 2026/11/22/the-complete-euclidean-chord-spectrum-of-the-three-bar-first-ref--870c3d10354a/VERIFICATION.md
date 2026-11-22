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

# Exact finite verification

Run `python3 verify.py` from the directory containing `verify.py` and `CHORD_SPECTRUM.csv`. Only Python 3 standard-library modules are used. The program independently generates all 280 vertices by (i) a predecessor-mask topological-extension recursion and (ii) a brute-force filter over all \(9!\) permutations, then confirms exact equality of vertex sets. It calculates each of the 39,060 unordered squared Euclidean chord lengths by integer arithmetic, checks every CSV multiplicity, the exact 75-bin support, missing \(148\), two outer shells, and the 45-edge diameter matching with 190 isolated vertices. It also checks the exact arithmetic mean \(15206/217\).

Successful replay reports `BARCODE_CHORD_PASS vertices=280 pairs=39060 shells=75 diameter_sq=152 diameter_pairs=45`.

The count is finite and exhaustive for this standard 280-vertex representation. It does not certify unbounded families of barcode polytopes or determine higher-dimensional persistence invariants. No independent external audit has been conducted.
