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

# Reproducibility and limitations

Run `python3 verification/check_centralizers.py` from the package root. The program enumerates every permutation for \(1\le m\le7\) and \(1\le k\le10\), checks the exact phase-congruence condition against the factorial wreath formula, and independently checks the homomorphism law on sampled ray points. It uses Python's standard library only and no external data.

The proof's noncomputational steps are derived in RESULT.md: the published finite-omega-limit phase convergence, the continuity criterion across all sampled rays, the characterization of surjectivity, and the integer coprimality argument giving the wreath decomposition. The program tests bounded instances and does not by itself establish completeness over every \(m\) and \(k\). The claim of historical priority remains subject to independent specialist comparison. No independent audit has been performed.
