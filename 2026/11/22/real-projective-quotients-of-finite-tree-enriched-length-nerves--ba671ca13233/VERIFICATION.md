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

# Verification and scope

The included `verify_tree_enriched.py` uses only Python's standard library and exact finite-field arithmetic. It explicitly builds normalised ordered chain groups from all distance-bounded tuples and maps face orbits for the free involution. It checks 138 Betti-vector predictions over primes 2, 3 and 5 on paths, a 4-vertex star, and a 6-vertex symmetric branched double-star, across positive integer stages up to four. It was run directly as `python3 verify_tree_enriched.py` with output `PASS: 138 independent modular homology checks over p=2,3,5`.

The theorem itself is integral and for every finite unweighted tree, not just these test graphs. Completeness comes from the proof of magnitude diagonality, the first length-drop differential, connectivity, the equivariant central-edge model, and the integral projective relative homology complement. No finite-field computation certifies all-tree statements, integral torsion, higher homotopy or publication priority. The computation does not replace independent expert validation.
