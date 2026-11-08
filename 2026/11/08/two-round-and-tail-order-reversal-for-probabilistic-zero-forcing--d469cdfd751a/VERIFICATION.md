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

The exact formulas for round-two completion were derived from independent forcing attempts and the two-part blue-count Markov states. The proof of the infinite statement uses central binomial bounds for even \(b\ge14\) and odd \(b\ge17\), and exact integer positivity for the remaining values \(3\le b\le15\). A finite-state spectral argument proves the late-time rates.

Reproduction: `python3 check_pzf.py` from this directory (Python standard library only). Recorded output: 13 exact positive differences; 10 independent labeled-state/two-count identities; 98 finite spectral comparisons plus their descendant states; analytic-bound spot checks; `All tests passed.` The script's finite checks do not replace either infinite argument. No independent mathematical audit or external certification has been performed.
