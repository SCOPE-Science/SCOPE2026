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

# Verification scope
The proof is a self-contained edge-increment decomposition and planar polygon argument. Its critical nonstandard step is the armwise maximization inequality: strict positivity of every within-arm covariance coefficient and an achievable common-direction upper bound imply full arm rigidity. All probabilities and edge lengths are arbitrary positive reals, not merely rationals.

The standalone file `check.py` uses only the Python standard library. From this package's folder, execute `python3 check.py`. On the actual packaged file, it tests exact rational covariance identities on 3,240 rational increment assignments, 270 finite sign-polygon comparisons, dominant-arm constructions and a four-vertex dimension-gap example.

These calculations are bounded finite tests, not a proof of the general parameterized theorem. The complete mathematical argument is in `RESULT.md`. The literature comparison remains non-exhaustive; independent audit has not been performed.
