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

The relevant proof is in `RESULT.md`. The standalone `verify.py` constructs principal lower sets and every simplex of the finite incidence-poset order-complex filtration, performs graph persistence reduction in degrees zero and one, and compares all positive-length intervals to the claimed formulas. A package-path replay returned:

```
VERIFY_OK
connected_test_graphs 1100 root_test_cases 14946 plus_two_cubic_examples 50
petersen_prism_profile_equal True petersen_has_4cycle False prism_has_4cycle True
```

The exact proof uses no computational assumptions: set-difference weights and forest/cycle ranks establish all orders and all fields. The replay is a regression check, not an exhaustive proof over infinite graph orders. The finite-space nonhomotopy consequence uses the published Stong-core classification for incidence posets. No external independent mathematical validation has been performed.
