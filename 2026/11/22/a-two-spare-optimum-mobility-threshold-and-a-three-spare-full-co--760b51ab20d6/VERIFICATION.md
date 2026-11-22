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

The two embedded Python 3 scripts `artifacts/verify_primary.py` and `artifacts/verify_independent.py` reconstruct all 192 maximal antipodal geodesics by different algorithms, test all 65,536 detector subsets, certify the full size and minimality polynomials, and check the exact connected component size distributions at budgets six through nine. Each computes all 780 optimum-to-optimum shortest distances at budget eight. They were executed from their actual embedded candidate paths and returned `VERIFY_PRIMARY_OK` and `VERIFY_INDEPENDENT_OK`.

Exhaustive enumeration proves the stated finite claims provided the included implementations are interpreted under Python 3's specified integer and set semantics. The proof additionally gives the mathematical equivalence between valid hitting sets and bitmask tests, and between single-bit toggles and legal addition/removal moves. No infinite-dimensional extension or external independent audit is claimed. Scientific historical priority is provisional.
