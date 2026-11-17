---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Count generator on transient k=1,2,3 has T=[[-1-2c,2c,0],[2,-2-2c,2c],[0,3,-3]], initial (.5,0,.5). Its survival Laplace resolvent numerator V=z^2+(11+8c)z/2+(17+14c+8c^2)/2 and denominator D=z^3+(6+4c)z^2+(11+8c+4c^2)z+6 satisfy resultant(D,V)=-(c-1)(4c^2+5c+6). The sole nonnegative residue crossing at c=1 cancels middle pole -3. Initial h'(0)=-1/4-c; for c<1 negative middle spectral coefficient makes h'(t)>0 eventually and 3-mode exponential sign variation has at most one crossing. For c>=1 positive surviving coefficients force h'<0. For <=2 occupied sites, at most two exponentials give constant-sign hazard derivative. c=0 formula and boundary c=1 cancellation checked; inspected symbolic/labeled-state verify.py. This is not a claim for arbitrary 3-site initial distributions.

## originality

PASS

Best-of-knowledge PASS: classical generalized-mixture reliability work establishes the possibility of bathtub hazards, and QSD/metapopulation studies give context, but the exact c=1 coefficient-cancellation boundary for this absorbing complete-graph contact process and sharp three-habitat minimality are distinct. The relevant reliability primary article could not be inspected fully; its possible stronger classification is a documented risk.

## value

PASS

The sharp threshold separates qualitatively different extinction risks while preserving the same model, and establishes exact minimum habitat count. Analytic finite-state benchmarks are meaningful for extinction dynamics and spectral reliability; this is not merely a numerical bathtub example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
