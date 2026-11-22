---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For full root segments and Euclidean Steiner V3, the zonotope wedge-sum theorem weights three disjoint incidence edges by 2sqrt2, an incident pair plus separate edge by sqrt6, a 3-edge connected tree by 2, and triangle by zero. Counting incident pairs gives V3=2sqrt2*binom(n,3)-a(n-2)W-cP+bS-dT with a=2sqrt2-sqrt6, b=2+4sqrt2-3sqrt6, c=2sqrt6-2-2sqrt2,d=3sqrt6-4sqrt2. Defining h=W-n=sum_v binom(dv-1,2), h=0 only at cycle and h>=2 is strictly below the pendant-edge candidate using S<=(n-1)h/3 and P,T>=0. For h=1 a unique cubic vertex and leaf force a cycle with one attached path; the t=1, longer-path and triangular-cycle deficits differ by c or d-2c=4-sqrt6>0, so unique runner-up is H_n. Independently enumerated connected labelled unicyclic n=5 (222 graphs) and n=6 (3660 graphs), checking cycle and H_n counts/values, not extending finite enumerations to the all-n proof.

## originality

PASS

Joós-Lángi proves the general zonotope intrinsic-volume sum and more global geometric inequalities, which are used as prior input. Results on trees, nearly complete graphical zonotopes and cycle profiles have different graph classes/targets. No examined source implies the unique first and second V3 extremizers over all connected simple unicyclic graphs at fixed n.

## value

PASS

The extremal and runner-up classifications with explicit sharp gap distinguish how single branching affects a natural metric invariant of graphical zonotopes; the rigidity in h=0,1 and strict h>=2 separation is structurally meaningful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
