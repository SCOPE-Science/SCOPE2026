---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For coprime n,m and generators x_i,y^n,y^m,x_i^{lambda_i}y, y is integral and belongs to the same fraction field, so B=C[x_i,y] is the normalization. The semigroup H=<n,m> and q(b)=b-max(H∩[0,b]) give exact monomial membership x^a y^b in R iff u(a)=sum floor(a_i/lambda_i)>=q(b), because all mixed-generator counts 0..u(a) are attainable. Requiring membership of every y^t multiple gives conductor iff u(a)>=Q(b)=max_{t>=b}q(t). Missing monomials per b<c are stars-and-bars binom(q(b)+s-2,s-1) times product lambda_i; for m=n+1 the block gaps sum to binom(n+s-1,s+1). Independent enumerations checked 1341 membership/conductor cases and sample exact deltas. Finite tests do not establish generality.

## originality

PASS

The exact ring family is previously identified by Dalbelo–Rodrigues Hernandes–Ruas, whose Theorem 3.6 gives normal-form/isolated-singularity structure but not explicit conductor or colength. Rodrigues Hernandes–Ruas 2021 Proposition 5.1 supplies only two-sided delta bounds; their double-point invariant is distinct. The exact all-parameter conductor and delta are not mechanically stated by those. A plausible 2019 surface paper remained inaccessible after lawful OA search and Oxford VPN authorization failure; its possible subfamily priority is explicitly retained without turning access alone into failure.

## value

PASS

The precise conductor ideal and finite normalization quotient length are natural invariants of isolated toric singularities, refining actual published bounds and extending across dimension, conductor thresholds and generator multiplicities. The sharp consecutive-semigroup binomial closed form is independently reusable in surface and higher-dimensional examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
