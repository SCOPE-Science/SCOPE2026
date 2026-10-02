---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-09-30.md",
      "INDEPENDENT_AUDIT_2026-09-30.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

The 8x8 rational Gram matrices were independently rebuilt from the Dirichlet/simplex moment formulas. The committed rational vector evaluates to 7553888936545658/2485078816758705, and exact LDL factorization of (61/20)A-B has eight strictly positive pivots, certifying the upper bound. The tuple witness is admissible modulo every prime at most 32.

## originality

PASS

Best-of-knowledge search found the general Maynard–Tao variational framework but no prior source giving the exact generalized-eigenvalue bounds for this particular eight-dimensional cell. The exact cell statement therefore survives originality, subject to the residual risk noted below.

## value

FAIL

The chosen subspace span{1,s,...,s^6,x1} is an ad hoc tiny slice with no independent mathematical motivation beyond testing whether it crosses already-known sieve thresholds. Certifying that this arbitrary slice stops below 3.05 neither constrains the natural larger optimization problem nor supplies a structural obstruction. Under the stated value bar this is an unmotivated narrow invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
