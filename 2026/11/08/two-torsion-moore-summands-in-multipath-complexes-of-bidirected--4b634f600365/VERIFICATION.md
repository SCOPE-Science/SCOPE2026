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

# Verification record

Run `python3 verify.py` in the same directory. The implementation uses only the Python standard library and builds all directed arcs, simplicial faces, the deterministic acyclic matchings, exact signed two-three Morse matrices, and three independent simplicial field-rank checks. It uses no precomputed face list, external package, network lookup, or other research artifact.

The lexicographically ordered arc-toggle orders are embedded in the executable. Every candidate face is constructed in two ways; independent component and transitive-closure cycle tests agree. The entire incidence digraph is checked for acyclicity. The signed Morse boundary has one invariant factor equal to 2 for each width. The output stored in `verify_output.txt` was produced by running that executable. The theorem concerns exactly these finite complexes, not an inference from finitely many examples of an infinite family.

Limits: global homotopy equivalence follows from the verified integral Morse differential and the simply connected two-skeleton, as explained in RESULT.md. Independent mathematical auditing has not been performed. The exact integer degree checks, unlike the supplementary modular ranks, determine the order of torsion.
