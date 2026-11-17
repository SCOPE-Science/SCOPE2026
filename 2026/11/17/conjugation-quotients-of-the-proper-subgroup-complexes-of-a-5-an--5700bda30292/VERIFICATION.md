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

Execute `python3 verify.py certificate.json` using Python 3, standard library only. The checker regenerates the multiplication tables, all subgroups of the two permutation groups, conjugacy-orbits of all strict subgroup chains, face maps, integer cellular boundary identities, all elementary free-face deletions and the residual circle/surface invariants. It compares every generated certificate field against the recorded `certificate.json`.

Actual result:

```text
VERIFY_OK
A5 59 [7, 8, 1] 3 [5, 5, 0] circle
S5 156 [17, 49, 41, 7] 26 [12, 30, 20, 0] sphere
```

The proof of homeomorphism of the terminal two-complex to the sphere also uses the standard classification of connected compact surfaces. The finite verifier does not claim to establish uniqueness in the literature, classify higher groups, or constitute independent auditing.
