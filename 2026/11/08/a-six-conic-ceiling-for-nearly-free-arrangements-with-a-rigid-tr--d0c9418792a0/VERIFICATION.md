---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility of the corrected triple-free theorem

The standard-library program `verify_conic_cutoff.py` exactly enumerates nonnegative integer incidence vectors compatible with Bézout, the near-free Tjurina identity and Zieliński's orbifold inequality for component counts five through eight. In the no-triples category, the only five-conic admissible vector is `(13,0,0,1,6)`, with none for six through eight. These finite calculations support, but do not substitute for, the displayed uniform proof excluding six components and forcing the unique five-conic necessary profile.

The existing SymPy script `verify_four_conic_example.py` exactly checks the previously known four-conic example, including its four `A7` contact identities, eight nodes and Jacobian-syzygy minimal degree three. This known construction certifies sharpness solely for the nodes-plus-`A7` subclass; it is **not** an original construction here.

The K2,3 contact-graph implication follows from the written two-contact projective normal-form argument and Mantel's theorem, not from a finite table. The external near-freeness and orbifold inequalities are cited premises rather than re-proved theorems. No proof-assistant certification or expert attestation is represented by the scripts.
