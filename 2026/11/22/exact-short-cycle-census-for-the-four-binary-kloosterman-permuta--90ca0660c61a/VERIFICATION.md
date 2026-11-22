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

# Exact symbolic and finite-field verification

Run `python3 hx_two_cycle_checker.py` under Python 3 without external packages. The checker recomputes each composition numerator from the rational maps, verifies the displayed factorization exactly in \(\mathbb F_2[X]\), and verifies the irreducibility and fixed-point factor identities. Next it exhaustively enumerates all trace-one elements of \(\mathbb F_{2^n}\) for every \(1\leq n\leq15\), checks every eligible basic map is a permutation, and confirms observed fixed points and unoriented two-cycles. This totals 32,767 trace-one elements across the fifteen fields, with each eligible index treated separately.

The exact polynomial-factor and trace argument in RESULT.md, rather than enumeration, proves the claims for all extension degrees. The code is a reproducible check of finite algebra identities and bounded small-field examples; it is not an external formal proof or independent audit. No proof about longer cycles or arbitrary composite Kloosterman polynomials is asserted.
