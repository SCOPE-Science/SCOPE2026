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

Reconstructed standard initial-block decomposition C(z,u)=1/(1-zC)+(u-1)(zC)^r, irreducible generating function I=1-1/C, and outer-component series F=1/(1-sI). Formal differentiation at u=s=1 and residue z=t(1-t) yield [z^n]C_u=M_n,r=binom(2n-r-1,n-r), [z^n]F_s=3n Cat_n/(n+2), and mixed [z^n]F_su=((3n-2r)/n)M. Thus Cov(R_n,C_n,r)=(M/Cat)*2(3n-r(n+2))/(n(n+2)), with exact signs and equality r=2,n=4. Independent exhaustive enumeration of labelled noncrossing partitions for n=2..7 (all feasible r) gave every rational mixed moment and covariance. Direct factorial asymptotics give limit (3-r)/2^r for fixed r!=3 and n*Cov(R,C3)->-3/4; finite enumeration does not establish all n.

## originality

PASS

Earlier marked-block identities give the exact mean M_n,r, and earlier outer-block work gives its marginal mean 3n/(n+2), but neither fixes the mixed derivative or sharp sign rule. A thesis explicitly raises more general joint size-resolved outer/total block problems. This specialized cross moment is at least not expressly stated in inspected primary sources; the formal-series framework is standard and can encode it implicitly, so priority is best-of-knowledge.

## value

PASS

The covariance between a global nesting statistic (number of outer components) and local class-size counts is a natural exact Catalan invariant. The all-n phase diagram (singleton positive, size >=3 negative, doubleton finite-size reversal at n=4) and size-biased expected outer count 3-2r/n give interpretable structural information unavailable from separate marginals. Exact finite-sign boundaries and n^{-1} borderline size-three asymptotic are not arbitrary slices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
