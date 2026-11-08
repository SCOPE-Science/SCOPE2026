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

# Verification notes

The analytic proof handles every integer dimension at least three and every real cap parameter between one-half and one. The associated Python script performs exact-rational supplementary checks in dimensions three through seven for rational parameter choices that include the phase-transition cap and the symmetric degenerate endpoint. It checks the common center, sampled facet and interior coverage, and witnesses immediately below the proposed threshold. Execute with `python3 verify_capped_simplex.py` (Python standard library only); the observed output was `CAPPED_SIMPLEX_EXACT_OK 19385`.

The enumerated points cannot prove coverage of all continuum points; that conclusion follows from the facet-cover and common-star-center argument. Numerical and rational checks do not establish historical priority. Independent mathematical validation has not been performed.
