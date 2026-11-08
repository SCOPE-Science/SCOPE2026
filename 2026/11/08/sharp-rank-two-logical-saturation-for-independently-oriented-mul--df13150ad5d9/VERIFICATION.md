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

# Reproduction and mathematical checks

Run `python checker.py` with Python 3.9 or later and the standard library only. The executable constructs optimal models for \(k=1,2,3,4,5,6\), then exhaustively enumerates independent tournament families for \(k=1\) on \(n=2,3,4,5\) and for \(k=2\) on \(n=2,3,4\). The enumeration checks exact rational single-vertex deficiency probabilities, every pair's joint deficiency probability, and the failure of three-way independence at \(k=1,n=3\). Output from the supplied file was:

`ALL_CHECKS_OK finite_structures= 5262 cyclic_witness_sizes= [3, 5, 9, 17, 33, 65]`

The general finite-size claims are established in the proof by two-round games, cyclic two-factor decomposition, conditional independence, and inclusion–exclusion. The sharp random-window distribution is proved by conditional Bonferroni bounds and convergence of factorial moments; experiments are not proof of its infinite limit. The numerical checker is intentionally finite and cannot establish novelty or independent validation.
