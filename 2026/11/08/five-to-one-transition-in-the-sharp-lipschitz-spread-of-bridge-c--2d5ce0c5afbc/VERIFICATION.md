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

The standalone `verify_barbell_spread.py` requires Python 3 and the standard library only. Invoke `python verify_barbell_spread.py` after extracting it beside this document.

Observed checks on the distributed script:

```
DIRECT_ALL_EXTREME_CLIQUE_POTENTIALS_OK 36 60516
INDEPENDENT_LABELLED_INTEGER_LIPSCHITZ_ENUMERATION_OK 25 42483
EXACT_REDUCED_INTEGER_OPTIMA_OK 16384
FIVE_TO_ONE_PHASE_AND_ALL_TIES_OK 46501
STRICT_FIXED_ORDER_BALANCING_OK 296
ALL_BRIDGE_BARBELL_SPREAD_TESTS_OK
```

The first two computations use distinct enumerations of anchored potentials; neither is a certificate of all-dimensional feasibility on its own. The exact integer-reduced tests and phase checks support the derived algebra. The universal sharpness and all extremizers follow from the analytical argument, not from the bounded enumerations. No independent audit is claimed.
