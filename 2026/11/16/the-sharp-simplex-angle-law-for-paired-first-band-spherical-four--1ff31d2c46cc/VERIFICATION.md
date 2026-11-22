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

Normalized degree-0/1 real spherical reproducing kernel K(x,y)=1+d<x,y> gives one-pair MSE = (d-1)||f||²/2 + E[f(X)f(Y)(1+d<X,Y>)]/2. Haar symmetrization cannot raise the top error eigenvalue, and yields levels A=d(1+u)/2 and B=(d-1+u+dv)/2 with u=E<T>, v=E<T²>=u²+Var T. The exact factorization A-B(u,u²)=(1-u)(1+du)/2 yields unique minimizer u=-1/d and v=u², hence T=-1/d almost surely even for nonsymmetric originals. Explicit Haar-invariant tangent-circle coupling realizes the equality; independent and antipodal baselines checked. Separate Sympy calculations reran key identities for d=3,4,8; empirical spectrum is only corroboration, not proof.

## originality

PASS

Fresh claim-vs-prior, equivalent-statement, stronger-coverage and exact-table comparisons identified no decisive covering implication in inspected evidence; priority remains best-of-knowledge with named full/partial reading and risks.

## value

PASS

First-band projection is a natural, nontrivial baseline for replacing exact cubature with randomized sampling; complete minimax over ALL uniform-marginal pair dependence and sharp iff geometry are motivated design facts, unlike a routine variance bound. Distinguishing optimal simplex-angle from harmful antipodal sampling gives a precise reusable principle without claiming higher-harmonic or deterministic-cubature optimality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
