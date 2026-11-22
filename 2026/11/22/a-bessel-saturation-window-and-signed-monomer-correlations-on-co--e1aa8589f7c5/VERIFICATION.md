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

# Reproduction and verification

The supplied `CHECK.py` is standalone Python 3 source and requires no external packages. Invoke `python3 CHECK.py` after extracting the files. Its expected completion line is `MONOMER_DIMER_EXACT_CHECKS_PASSED 728`.

The checker validates exact rational matching-count probabilities on numerous small graphs, constructs all labeled matchings independently by recursion through four smaller-shore vertices, checks finite pairwise covariance signs and the cross-shore variance identity, and checks the explicit total-variation bound numerically across several sizes and imbalances. Its finite checks do not certify the infinite theorem. The all-size argument uses exact matching enumeration, Laguerre orthogonality and real-rootedness, a Bessel-series coupling bound, and factorial-moment convergence; each is reconstructed in `RESULT.md`.

Scientific limitations: fixed integer imbalance, positive uniform activity, equilibrium measure. Earlier literature may contain an equivalent formulation; independent audit is not performed.
