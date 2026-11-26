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

Over characteristic not two write X=aI+U, Y=bI+V with U,V traceless. Cayley–Hamilton makes the traceless part of the square sum 2(aU+bV); if a or b is nonzero, U,V are dependent and commute. Thus the noncommuting case is traceless. For Q(u,v,w)=u²+vw and any d, counting vw=d−u² gives n(d)=q²+qχ(d), including n(0)=q². An independent check of the pair convolution starts with the unrestricted level Q(U)+Q(V)=c: the two product variables form a dot product against a coefficient pair. If that pair is nonzero it contributes q³(q²−1); if zero it contributes q² times the two-square count q−χ(−1) at c≠0 and q+(q−1)χ(−1) at c=0. Remove 2q²n(c), adding back q⁴ only when c=0. For commuting invertible traceless pairs the nonscalar first factor has centralizer span(I,U), so V=tU with t≠0. At zero the commuting count is (1+χ(−1))(q−1)q². Otherwise sum n(c/(1+t²)) over t≠0 with 1+t²≠0; the character sum on nonzero t equals −2, by (z−t)(z+t)=1. Subtraction yields both frozen formulas. The square/nonsquare difference is 4q(q²−1); relative to the larger nonsquare level, the zero level exceeds it by q(q²−1)(q−2). The smallest nonzero-target lower bound is positive at q=3 and increases thereafter.

## originality

PASS

The supported distinction is the exact ordered, invertible, noncommuting scalar square-sum census, not general square representability or an originality claim for the Cayley–Hamilton reduction. The strongest matched statements do not specify or mechanically give this restricted census.

## value

PASS

Central outputs are a natural singular locus of the square-sum map where noncommutation enforces a sharp reduction. The exact census shows all scalar values survive both invertibility and noncommutation, even over F₃, and identifies a residual square-class bias invisible in existence or unrestricted matrix counts. This is a meaningful restricted word-fiber invariant for all odd prime-power fields.

The dated certificate retains the supplied scientific assessment, sources and limitations.
