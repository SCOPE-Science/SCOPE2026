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

# Verification and limitations

The complete proof is in `RESULT.md`; execute `python3 checker.py` from the same directory. The checker explicitly enumerates the full normal-form parameter space and directly checks all five preconditional axioms, identity, semicomplementation and double-negation inflation on every element and relevant ordered tuple for \(m=1,2,3,4\). Its successful final line is `POINTED_COATOM_PRECONDITIONAL_CHECKS_OK`.

An additional finite row-candidate program enumerated all row functions satisfying the primitive row implications before imposing cross-row axiom (P5), for \(m\le3\). The independently calculated \((T_m,F_m)\) pairs were \((2,2)\), \((9,5)\), and \((76,14)\). These computations are finite sanity checks, not a substitute for the full proof or an independent expert audit. For any \(m\ge1\), the exact formulas follow by the forced-row and bijective counting arguments. External historical priority has not been certified.
