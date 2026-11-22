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

# Verification

Run `python3 verify.py` in the extracted directory. The script uses only Python's standard library. It constructs each weighted grounded Laplacian on the full vertex set and solves rational normal equations for each nonterminal GMRES iterate, comparing all residual components with the predicted uniform ball vector. It then tests termination by an independent Krylov Gram projection and checks the all-regular-degree ball-count identity. On the reviewed version, 10,602 exact rational/integer assertions passed across 879 weighted grounded trees.

Finite checks supplement the all-height analytical proof. Tests do not certify arbitrary real conductances or floating-point performance; the proof establishes the former and no claim is made for the latter. Independent audit has not been performed.
