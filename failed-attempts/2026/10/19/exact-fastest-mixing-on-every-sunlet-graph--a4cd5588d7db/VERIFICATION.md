---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Dihedral averaging reduces the global SLEM value to the two-orbit family with p+2q≤1, not the set of all optimizers. The first Fourier block gives the lower bound 1−p−qt+sqrt(p²+q²t²) at t=1−cos(2π/n). It decreases strictly in q when p>0; p=0 has a unit eigenvalue on the nonconstant subspace. On q=(1−p)/2 the bound is strictly convex in p, with second derivative a²/(p²+a²(1−p)²)^(3/2)>0 for a=t/2. At the claimed p and q the square root is x/2 and the scalar derivative vanishes, verifying the interior minimum. The plus branches decrease with t_k, and the minus branches are bounded below by −sqrt(p²+(1−p)²) at t_k=2. The difference of squares from the claimed SLEM is x(x+2)(2−x²)/D²>0 since x²≤3/2, including the triangle boundary. The nonconstant k=0 eigenvalue (2−x²)/D is also strictly below the SLEM. Thus the lower bound is attained, and both equality conditions prove invariant uniqueness. The exact gap x²/D∼π²/n² gives the claimed factor 1/2 against the bare cycle.

## originality

FAIL

One distinct Resultary finding states the exact sunlet theorem, including the half-gap comparison, and a broader indexed corona theorem gives the edge probabilities, SLEM, saturated rim, and more rigidity by specialization. This is verified mathematical coverage, with later dates on the overlapping catalogue records, not a claim of historical precedence. The earlier same-graph priced conductance theorem and the published wheel theorem do not establish this overlap.

## value

PASS

The natural all-size pendant perturbation of a cycle yields a useful exact network design law: the stochastic constraint saturates precisely at the rim and the spectral gap is halved to leading order. The mathematical content is substantial as an extremal theorem, but its exact coverage precludes a new intake or a repair by parameter renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
