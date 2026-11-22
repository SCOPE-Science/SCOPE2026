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
# Verification of the exact-start BDF2 phase theorem

`python3 verify.py` executed successfully with:

```
EXACT_IDENTITIES_AND_FINITE_TESTS_OK 743 checks
```

The script uses Python 3 and SymPy. It verifies the exact polynomial identity producing the positive derivative \(\theta'-\phi'\), the formula for the second-stage scalar minimum, its derivative and the thirteen-vertex star algebra. It also performs exact rational recurrence identities, finite scalar phase/recurrence comparisons, root-bracketing checks through stage \(26\), and sampled separated finite-star negativity bands. The script is the complete reproducer; no other files or external data are required.

**Analytical completeness.** The all-\(k\) zero count follows from the explicitly derived continuous strictly increasing phase spanning \((-\pi/2,k\pi/2)\), not the bounded sample enumerations. At each zero the derivative of the cosine factor is nonzero. The finite-graph consequence follows from exact star spectral projectors and a finite choice of one interior sample per negative scalar interval. The 12/13 cutoff follows from the unique global minimum of \(g_2\) and its spectral lower bound, with the thirteen-vertex witness established by \(e^3>16\). Exact source claims and proof details are in `RESULT.md`.

**Limits of checks.** Floating-point root brackets are corroborative, not exhaustive, and recurrence checks do not certify all stages. Literature priority is qualified; a later independent mathematical review has not occurred.
