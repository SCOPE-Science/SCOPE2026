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

Independently traced the canonical RKHS K_b=(1-b(z)conj(b(w)))/(1-zwbar) to the one-atom coordinate norm 2|x|²+4||g||² and K_b2=(1+zwbar)K_b1(z²,w²). Even/odd decomposition gives the exact C2 block L(a,b,p,q)=(a+b,p+Sq+sqrt(2)b*1,p+q), with finite rank coupling to B(p,q)=(p+Sq,p+q). Norm B<=2, while weakly-null high-degree nearly shift-invariant blocks approach 2: essential norm exactly 2. LL* eigen-equations for lambda>4 reduce to a decaying Hardy recurrence v_n=r^n, r=1/(lambda-1), forcing lambda^3-6lambda²+8lambda-4=0; unique root >4 and explicit adjoint eigenvector prove attainment. Independent Python reconstructing the rational extremizer gives squared output/input quotient 4.382975767906236, within 4e-15 of the root. Finite calculation checks arithmetic only; the operator-theoretic proof establishes the infinite claim.

## originality

PASS

A March 2026 isometric monomial-composition theorem is cross-space H(b1)->H(b1 composed z²), not the canonical same-space C2 on H(b2). A 2022 unbounded squaring example uses different boundary-zero multiplicities and equivalent norms. Nearby published exact norm-equivalence results compare norms, not this operator norm. Searches and inspected texts did not provide a dominating exact self-C2 cubic spectral formula; priority remains best-of-knowledge.

## value

PASS

The canonical same-space norm is sensitive to the precise RKHS norm, unlike equivalent atomic Dirichlet norms. This exact norm/essential-norm gap is a natural boundary-collision spectral phenomenon and explicit extremizing function; those exact constants and isolated mode are useful for testing composition-operator inequalities. No claim about all Schur functions or power maps.

The dated certificate retains the supplied scientific assessment, sources and limitations.
