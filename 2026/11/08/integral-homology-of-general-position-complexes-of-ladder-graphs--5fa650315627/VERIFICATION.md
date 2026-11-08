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

# Independent computational checks and scope

Execute `python3 verify.py` with Python 3.8 or later; this file uses only the standard library. The program constructs shortest-path distances in each ladder by the explicit coordinate formula and tests *every* vertex subset at orders \(2\) through \(8\), totalling 87,376 subset decisions. It checks every accepted triple and rejects every predicted nonface.

For each order from \(2\) through \(13\), it independently constructs all oriented alternating-row triangle boundaries, performs finite-field row reductions for primes \(2\), \(3\), \(101\), and verifies the exact proposed Betti dimensions. The verification run produced:

```
VERIFY_OK full_subset_orders=2..8 examined_subsets=87376 face_description=PASS homology_orders=2..13 prime_fields=2,3,101 rank_checks=36 exact_betti=PASS first_h2_order=6
```

The finite checks are not a proof of the statement for all graph orders or all primes. The paper's explicit array normal form establishes the boundary rank uniformly over arbitrary fields, and the integral universal-coefficient argument proves absence of torsion. Neither an independently authored review nor external mathematical certification has been performed.
