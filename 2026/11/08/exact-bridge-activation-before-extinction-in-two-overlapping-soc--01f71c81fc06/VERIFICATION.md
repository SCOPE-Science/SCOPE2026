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

# Reproducibility and limits

Execute `python3 verify.py` using the Python standard library. The checker uses exact fractions for all finite-state calculations. It evaluates the hypergeometric/order-statistic expression and independently solves an absorbing harmonic linear system for every pair of overlap/outside source-active counts on 165 parameter sets (source size two through six). It separately solves the entire \(2^a\)-microstate system for 56 configurations, including threshold-ineligible cases, for source sizes three through five. Its algebraic examples include a four-member source, two-member overlap, target threshold two, and rates \((\alpha,\beta,\delta)=(3,2,1)\), yielding \(720/767\).

Large finite-\(\alpha\) rational calculations illustrate the asymptotic coefficient but cannot establish the theorem for all \(\alpha\). The proof's renewal identity, order-statistic Laplace factorization, and finite-product asymptotic do provide the general arguments. The program neither tests arbitrary real rates nor establishes priority in the literature. The statements about independent external review are administrative status only; no external review has been performed.
