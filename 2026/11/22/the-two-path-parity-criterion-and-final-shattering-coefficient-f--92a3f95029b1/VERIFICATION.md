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

# Reproducible verification

Run `python3 verify_even_derangements.py` with a standard Python 3 installation in the directory containing this document and the script. No additional package or network access is required. The included `verification_output.txt` is one recorded complete successful execution, finishing with the marker `EVEN_DERANGEMENT_ALL_CHECKS_PASS 52160`.

The test independently enumerates the even derangements for orders four, five, six, and seven and compares their actual Boolean trace sets with the structural criterion on **every** partial-permutation support of size at most the theoretical bound. In total it compares 52,160 supports across those orders; larger nonmatching supports are excluded separately by the elementary all-positive obstruction. It also checks the parity robustness lemma for all 55 residual four-row partial forbidden-match configurations and 120 five-row full forbidden matchings, verifies the cycle/rook coefficient formulas through order fourteen, and directly constructs witness completions for representative top-size supports through order fourteen.

The software checks finite cases only. The universal classification rests on the written proof using path-permutation parity, Hall's theorem, and complete analysis of the two- and three-path boundary cases. The rank-four order-six polynomial is a previously known special case, not independent evidence of all-order novelty. Independent mathematical review has not been performed.
