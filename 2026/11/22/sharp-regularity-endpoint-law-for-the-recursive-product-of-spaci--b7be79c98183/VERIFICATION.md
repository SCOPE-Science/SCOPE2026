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

Run `python checker_regular.py` using Python 3 and SymPy. The script exactly constructs the binomial-window Hessian matrices and determinants for \(2\le m\le10\), checks leading principal minors and the strict Moran comparison, and compares two implementations of the recursion on deterministic random simplex points. It additionally checks local Taylor expansions and the first two exact determinants. The recorded finite run was `PASS 453 finite checks`; \(\det Q_2=8\) and \(\det Q_3=1215/4\).

The proof for every fixed integer \(m\ge2\) is in RESULT.md and uses analytic Taylor expansion and simplex-volume asymptotics. No finite enumeration proves the theorem beyond its tested cases. The coefficient is for the near-*minimum* (regular-spacing) endpoint, not the opposite large-score tail. Independent mathematical validation and historical-priority audit have not been performed.
