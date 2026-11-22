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

# Reproducibility

Execute `python3 verify.py` from a directory containing that script. It uses only the standard library and checks every residue class for all 368 odd primes below \(2529\); prime generation, nonzero square lookup and Euler-exponent symbol evaluation are explicit. Both exhaustive histogram constructions agree. The exact absent-word primes are listed in RESULT.md, and \(61\) misses only mask `1001` with the first position as the high bit. The deterministic histogram SHA-256 is `194838fb1badf1f21c7f2a978cef964c71d50b13656a9a1537bd30f09ea254aa`.

The infinite range is proved symbolically using separability and pairwise coprimality of the four quadratics for \(p>13\), the bound for squarefree polynomial character sums, and the explicit zero-value correction. The finite verification is not treated as evidence for unenumerated primes; the analytic inequality covers them. No independent audit has been performed.
