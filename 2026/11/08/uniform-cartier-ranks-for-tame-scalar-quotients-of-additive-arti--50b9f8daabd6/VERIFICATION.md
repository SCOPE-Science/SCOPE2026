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

# Reproducibility and scope

Run `python verify_cartier_quotient.py` using Python 3 (standard library). The exact verifier computes first-Cartier matrix entries over prime fields from the Artin–Schreier expansion, performs row elimination modulo \(p\), independently counts the invariant triples in the source's universal image basis, and compares both with the formula. The eight tested parameter pairs are \((3,2),(3,4),(3,6),(5,2),(5,4),(7,2),(11,2),(13,2)\).

Expected terminal marker: `VERIFY_OK`. Representative outputs are genus \(20\), rank \(9\), \(a=11\) for \((p,h)=(3,4)\), and genus \(156\), rank \(63\), \(a=93\) for \((p,h)=(5,4)\).

The direct numerical calculation uses the coefficient specialization \(R=x+x^{p^2}+\cdots+x^{p^h}\) and only finite parameter pairs. It tests rather than proves the all-coefficient and unbounded-parameter theorem. Uniform coefficient-independence depends on the full-image result and triangular minor proved in [2, Theorem 6.6]; the exact quotient computation is given in RESULT.md. The finite check is not an independent mathematical audit.
