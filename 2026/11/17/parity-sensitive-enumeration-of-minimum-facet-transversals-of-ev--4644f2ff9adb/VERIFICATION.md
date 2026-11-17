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
# Reproducibility and checks

Run `python3 verify.py` in the directory holding this file. The script uses only the Python 3 standard library. It builds the facets from the *original Gale evenness test*, not from the matching lemma being checked, and brute-forces all labeled vertex transversals for the finite tested parameter ranges. It then verifies the minimum cardinality, its exact count, and the claimed full family of minimizing sets.

The script passed 34 cases with 1,232 Gale facets checked and no discrepancy. A second independent check compared Gale facets with disjoint cycle-edge unions for all even-dimensional cyclic polytopes through 13 vertices. These are finite corroborations. The unrestricted proof requires the Gale criterion, the path matching/independence identity, and the parity run enumeration; none is replaced by experimentation.

External independent validation: not performed.
