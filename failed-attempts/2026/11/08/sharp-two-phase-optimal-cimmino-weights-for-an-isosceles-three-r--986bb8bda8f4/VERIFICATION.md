---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Symmetry exchange of rows 2 and 3, convexity of operator norm, exact 2+1 spectral decomposition and ratio balancing correctly give the claimed class-symmetric weights and optimal contraction. The mode crossing c^2=2d^2/(1+d) follows from comparing lambda_minus(q) with 1-d; common scalar weight b=2/(lambda_max+lambda_min) then yields sharp ||I-Udiag(w)U^T||. Independent algebra for (d,c)=(1/2,1/4) gives q*=4/7 and weights (16/29,28/29,28/29), matching exact prior spectrum. Source checker inspected; random tests corroborate but do not prove global optimality.

## originality

FAIL

FAIL by decisive older pointwise optimal scaling. The previously published full Nov 8 isosceles correlation-matrix theorem explicitly gives x_*=max{1/(1+d),(d-c^2)/(d(1-d))} and two-phase optimal spectral condition number for exactly the same Gram after reordering rows. Since Cimmino weight ratio q=1/x, this exactly equals q_*=min{1+d,d(1-d)/(d-c^2)}, with identical c^2=2d^2/(1+d) branch and contraction (kappa_*-1)/(kappa_*+1). Moreover prior theorem credits Kolotilina (2006) for a general 3x3 SPD pointwise scaling solution. No independent nontrivial residue remains.

## value

FAIL

FAIL for unchanged final claim: all optimizing ratios, weights and contraction rates are direct parameter relabelings plus the standard optimal common scale of an already evaluated diagonal-scaling problem. No separately motivated new invariant or boundary survives prior implication, despite correct algebra and reproducible examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
