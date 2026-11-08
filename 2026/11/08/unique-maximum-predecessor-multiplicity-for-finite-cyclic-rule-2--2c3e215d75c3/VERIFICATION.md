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

# Reproducible verification of the finite and algebraic proof components

Run from this extracted directory using standard Python 3:

```
python3 algebra_certificate.py
python3 proof_bounds.py
python3 verify.py
python3 brute.py
```

All programs use Python's standard library only. On the reviewed package they printed:

```
EXACT_RESIDUAL_NORM_IDENTITIES_PASS powers=3,4,5
EXACT_RATIONAL_INEQUALITIES_PASS 146557/100000 73279/50000
FINITE_BOUNDARY_PASS 15250 cases n=1..24
COUNTS_N1_TO12 [2, 2, 5, 6, 7, 11, 16, 22, 32, 47, 68, 99]
MIN_GAP 1
LAST_BOUNDARY (24, 9643, 1278)
INDEPENDENT_BRUTE_PASS n=1..14
```

`algebra_certificate.py` reduces exact polynomial expressions modulo the defining cubic to confirm the three weighted residual Frobenius identities. `proof_bounds.py` uses exact rational arithmetic, isolates the Perron root, and verifies the strict scalar bounds. `verify.py` visits every output having 1–3 ones at each length 1–24, checking exact predecessor counts. `brute.py` calculates all predecessor fibers by direct ring evaluation through length 14, corroborating the transfer representation.

The infinite-length conclusion comes from the analytic singular-value and residual-norm argument in `RESULT.md`, not from extrapolating finite verification. The package has not undergone independent scientific or priority audit.
