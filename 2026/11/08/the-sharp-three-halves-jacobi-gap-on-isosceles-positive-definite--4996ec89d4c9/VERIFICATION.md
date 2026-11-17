---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The 1-a antisymmetric eigenmode and 2x2 symmetric block give the exact SPD domain. For any diagonal scaling, Loewner sandwich by a diagonal H and transposition averaging gives a globally valid equal-first-two-coordinate optimizer (not merely symmetry conjecture). The resulting eigenvalues lambda0=(1-a)x and lambda+/- for the 2x2 block yield x*=max{1/(1+a),(a-b^2)/(a(1-a))}; the three regimes u=b^2<=a^2, a^2<=u<=2a^2/(1+a), u>=2a^2/(1+a) give strict positive F1,F2,F3 bounds. Independent symbolic reexpansion verified F2 square completion and F3 factorization, and the family a=1-t^2,u=1-t gives kappa_*=(1+t)(2-t)/t^2, Jacobi lambda_max->3, lambda_min=t^2, ratio->3/2. Finite numerical checks were not used as proofs.

## originality

PASS

Best-of-knowledge originality: Pointwise optimality does not literally state sharp uniform supremum; from explicit formulas one can derive it by the three-region inequalities plus limit supplied here. No inspected stronger theorem directly implies the 3/2 value without this analysis.

## value

PASS

A natural dimension-three worst-case approximation constant for ubiquitous Jacobi scaling, considerably sharper than the generic dimension factor; strictness and a near-singular extremizing family provide a usable conditioning benchmark rather than merely rederiving a pointwise optimizer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
