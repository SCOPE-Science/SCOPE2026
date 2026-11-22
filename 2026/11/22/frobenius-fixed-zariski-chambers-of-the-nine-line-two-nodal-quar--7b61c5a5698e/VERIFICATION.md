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

# Verification notes

The supporting scripts reconstruct the theorem's finite integral and combinatorial calculations without access to external data. `verification/verify_matrix.py` uses SymPy for exact intersection-pairing determinants and enumerates every subset of the eleven negative curves. It derives all five conjugacy types of the eight-element line-pair stabilizer, then tests fixed supports and their size profiles, two equal negative-curve cycle partitions, direct orbits, and Burnside's identity. Its final marker is `TWO_NODAL_QUARTIC_MATRIX_OK`.

`verification/verify_incidence.py` uses only Python's standard library, constructs supports from curve-disjointness and root-incidence restrictions independently of matrix determinants, and derives every bivariate support-count table. Its terminal marker is `TWO_NODAL_QUARTIC_INCIDENCE_OK`. Their deterministic stdout is included as `verification/expected_output.txt` with labels identifying the two sources; its byte content was compared with actual runs.

Both verifiers perform finite exhaustive checks for their exact eleven-curve universe. The fact that this universe includes *all* geometrically negative curves is established by the Bézout and adjunction proof in `RESULT.md`, not by enumeration. The arithmetic interpretation uses the classical descent of the Zariski decomposition and explicitly constructed geometric configurations. Historic priority remains provisional; no independent mathematical audit has been performed.
