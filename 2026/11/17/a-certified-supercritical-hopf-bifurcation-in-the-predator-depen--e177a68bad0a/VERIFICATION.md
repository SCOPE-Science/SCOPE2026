---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Re-derived the exact polynomial vector field, positive coexistence branch p=1/delta(x), y=(5x-1)/(3(2-x)), K=1/(delta(r-delta*y)) on 1/5<x<1. The 8th-degree Routh determinant Q from original RESULT matches independent symbolic Jacobian computation. Original inspected verify_hopf.py computes a rational Sturm count of exactly one physical root, isolates x in (3381326771974,3381326771975)/10^13, and uses interval arithmetic to enclose a1,a2,a3>0, d(a1a2−a3)/dx>0 and Kprime<0. Independently evaluated x≈0.338132677197410, K≈1.66170734735366, eigenvalues −1.43939008 and ±0.17272326i; contracted second/third derivatives and spectral projection reproduce first Lyapunov coefficient −5.877089144686, within claimed rigorous interval (−5.877089159,−5.877089130). Negative coefficient and positive transversality justify a local supercritical Hopf attracting positive periodic orbit, not any global uniqueness or basin statement. An independent floating-point evaluation supplements but does not replace the inspected rational/interval certificate.

## originality

PASS

The Cruz–Neves original study describes numerical Hopf evidence for precisely this positive payoff scenario and explicitly leaves a rigorous periodic-orbit proof unestablished. The new rational isolating interval, transverse crossing and negative first Lyapunov sign prove existence/stability, which the numerical plots and generic Hopf theorem alone do not imply. Priority remains limited to searched sources.

## value

PASS

Converts a numerically indicated positive-coexistence Hopf into a rigorous local theorem for a biologically motivated three-dimensional replicator flow: unique physical Hopf candidate, validated crossing direction, sharp threshold and attracting positive periodic onset. The exact nondegeneracy certificate resolves a specific documented open analytical gap rather than a routine restatement of the Hopf theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
