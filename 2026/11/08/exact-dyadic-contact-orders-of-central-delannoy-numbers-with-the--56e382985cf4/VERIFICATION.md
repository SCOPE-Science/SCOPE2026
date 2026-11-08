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

# Checks and limits
The standalone standard-library script `verify_delannoy.py` executed successfully. It reproduces the exact valuations of the degree 3–16 rational coefficients of the index-16 truncation by two algebraically different methods; checks \(\nu_2(D_n-(-1)^n)\) for every \(1\le n\le600\); and checks the tail combinatorial bound for \(17\le j\le512\). The crucial all-index argument is the proved formula for \(S_j\) and the bound \(S_j\le j/2\); inspecting finitely many \(j\) would not be enough. The two vanishing coefficients are proved through convergent 2-adic logarithms and a differentiable formal dilogarithm identity, not inferred from numerical values. No independent mathematical validation has been conducted.
