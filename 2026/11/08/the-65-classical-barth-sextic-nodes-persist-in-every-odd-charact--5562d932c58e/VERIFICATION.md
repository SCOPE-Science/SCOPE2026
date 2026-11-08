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

# Exact verification

Run `python3 verify.py` with Python 3 standard library. The actual execution printed:

```
BARTH_ODD_NODE_CERTIFICATE_OK nodes=65 types={'infty_axis': 3, 'infty_cross': 12, 'sphere_axis': 6, 'sphere_cross': 24, 'outer_diagonal': 8, 'outer_cycle': 12} possible_bad_primes={2} pairs_with_nontrivial_norm_gcd=679
```

Run `python3 verify_representatives.py` with SymPy 1.14. The actual execution printed:

```
BARTH_REPRESENTATIVE_CHECK_OK 6
```

The main checker defines the rank-two integer ring by pairs of coefficients and reduces products using the relation `t*t=t+1`. It generates the sextic polynomial and differentiates it formally over that ring, then checks all 65 point/gradient identities, all 65 Hessian norm units after inverting two, and all 2080 projective-minor norm gcds. The symbolic cross-check reconstructs the equation independently, recomputes six affine Hessians, and obtains the expected signed norms. The abstract norm-divisibility argument in RESULT.md upgrades these exact finite integer calculations to a proof for every odd characteristic.

The computation does **not** enumerate or certify all points of any entire special-fiber singular locus, and no claim is made about other singularities, scheme-theoretic exhaustiveness, or the maximal number of nodes in positive characteristic. No independent review or external audit has been performed.
