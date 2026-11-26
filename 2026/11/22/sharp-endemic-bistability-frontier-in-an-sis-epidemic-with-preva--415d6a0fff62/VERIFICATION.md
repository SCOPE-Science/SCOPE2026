---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The specific positive affine defection advantage follows by inserting the two constant-row payoff gaps in the originating model's equations (1)–(5). On the behavioral nullcline x=h(I), positive equilibria correspond bijectively to g(I)=k in (0,1). The logarithmic derivative of g is strictly decreasing, starts at -1+d/(1+exp(c)), and tends to minus infinity. This certifies each root count, including k=g_0 (the root at zero is excluded) and the double root at k=g_m. The critical equation gives w=d(1-I_m)-1 with w exp(w)=exp(c+d-1), and substitution gives g_m=w/d. The endemic Jacobian has negative trace and determinant -beta I g'(I); the disease-free eigenvalues are -1 and beta(g_0-k). At the fold, with b=-beta I_m(1-I_m), right and left null vectors may be taken as (h'(I_m),1) and (b,1); their pairing is nonzero. Projection of the parameter derivative onto the left null vector gives -beta I_m and projection of the second derivative in the right null direction gives beta I_m g''(I_m), both nonzero, confirming the dynamical saddle-node. The strict witness follows from 2<e<4 by comparing g at 0, 1/10 and 1, not from rounded roots. The source's sufficient threshold and condition (16) specialize as reported; failing them does not contradict the source. No disease-free stability classification at equality or global basin statement is needed. The finite frozen numerical checker was inspected, not run; the analytic argument is decisive.

## originality

PASS

The credited model, reduction to equilibrium conditions, and the general existence of behavioral epidemic bistability are not contributions of this record. What was not covered in the inspected statements is the complete, sharp fold and local stability classification for this positive, opponent-action-independent affine family.

## value

PASS

In this commonly used abstract feedback form, the disease-free linear threshold does not determine how many locally stable stationary states the model has. The exact necessary and sufficient frontier distinguishes this ambiguity from simple threshold crossing, gives a degenerate boundary and clarifies the limitations of the originating sufficient results. The complete classification is useful beyond a single simulated or algebraic witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
