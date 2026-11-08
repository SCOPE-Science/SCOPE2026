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

# Verification and reproducibility

All computations use exact binary arithmetic and the Python standard library. The two code files are independent implementations of the central finite claims. Run `python verify/matching_check.py` and `python verify/dynamics_check.py` from the directory containing the research statement.

`verify/matching_check.py` uses labelled Prüfer enumeration and the rooted matching-polynomial recurrence over \(\mathbb F_2[X]\); it does not form matrix powers. It checks all labelled trees on \(4,6,8\) vertices having exactly two even-degree vertices, counting \(12,840,101696\) cases. Each computed polynomial is compared to \(X^{N-2m}(1+X+\cdots+X^m)^2\), where \(m=d+1\). Its output is captured in `verify/matching_check.out`.

`verify/dynamics_check.py` constructs trees independently and performs binary adjacency-matrix powers, GF(2) ranks and direct state iterations. It checks \(96\) instances at orders \(4,6,8,10,12,14,18,22\), with \(12\) examples at each order. It directly iterates \(5440\) initial binary states in the smaller examples and checks every fixed-point population against polynomial gcds. Its output is captured in `verify/dynamics_check.out`.

These finite checks do not certify arbitrary sizes or fields by themselves. The analytic argument establishes the general characteristic polynomial, module similarity, and period formulas for every finite characteristic-two field. No external or independent audit has been performed.
