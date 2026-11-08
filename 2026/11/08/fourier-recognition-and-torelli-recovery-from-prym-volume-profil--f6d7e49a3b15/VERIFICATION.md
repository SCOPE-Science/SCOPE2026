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

`VERIFY.py` uses only Python's standard library and exact `fractions.Fraction` values. Run:

```sh
python3 VERIFY.py
```

It independently evaluates every sign-cut squared volume for selected examples with \(3\le n\le7\), recomputes all quadratic Walsh coefficients, checks the single/double-cut inverse, and verifies that every higher even Walsh coefficient vanishes. It checks the positive rank-one tetrad equations and the reconstruction identity \(\prod_{i<j}w_{ij}=(\prod_i\ell_i)^{\binom{n-1}{2}}\), including nonuniform rational inputs. An additional positive weighted-cut profile violates the tetrad constraint and is correctly rejected as a graph-volume profile.

The script's final line is `EXACT_PROFILE_CHECKS_PASS`. Its examples are finite tests and do not prove all-\(n\) uniqueness or characterization. The unrestricted theorem is proved symbolically in `RESULT.md`, conditional only on the cited published Kirchhoff–Prym forward-volume theorem. The proof does not address independent historical priority, unlabelled spectra, ramified covers or more general graphs.

Independent audit: not performed.
