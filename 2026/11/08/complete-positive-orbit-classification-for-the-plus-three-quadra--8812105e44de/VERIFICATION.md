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

# Reproducible checks

Run `python3 verify.py` with ordinary Python 3. All tests use exact integer arithmetic and no third-party packages. Tested inputs: odd \(q\le100000\); \(15\) dyadic valuation depths and \(250\) odd multipliers for the terminal-exclusion consistency check; terminal cycles with \(2\le m\le17\); all starting values \(1\le n\le2000\); bounded-start counts at \(X\in\{100,1000,10000\}\).

Observed output:
```
VERIFY_OK odd_transition_100000=yes terminal_arrivals_tested=15x250
VERIFY_OK exact_cycles_m=2..17 direct_start_n=1..2000
VERIFY_OK bounded_counts_X=100,1000,10000
PROOF_STATUS infinite_classification_derived_algebraically_not_from_finite_tests
```

Limits: finite trajectory cutoffs and finite parameter tests are checks, not exhaustive coverage of the infinite domain. The unrestricted exclusion of arrivals into the terminal cycles follows from the parity and modulo-three argument in `RESULT.md`; the full-dynamics and counting claims follow from that lemma.
