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

Writing q=xy and H(z)=log(1+αz)/(αz) removes the apparent zero-coordinate singularity and yields grounding and uniform margins. Differentiating log C gives x(log C)_x=1+g(x)−g(q), y(log C)_y=1+g(y)−g(q), and xy(log C)_{xy}=−qg′(q), proving the normalized density identity. For α>0, 1+g=u/[(1+u)log(1+u)] belongs to (0,1) and decreases, so both factors and the contribution −qg′(q) are positive. For α=−t, 1+g=(e^s−1)/s=∫₀¹e^(sr)dr, s=−log(1−tz). The two factors are at least one and qg′(q)=F(−log(1−tq)), where F(s)=(e^s−1)∫₀¹r e^(sr)dr rises strictly from zero to infinity. The worst lower bound is attained at (1,1), where the normalized factor is the actual density. This proves sufficiency including the endpoint, strict interior positivity there, and failure of a small interior rectangle when the corner density is negative. At α=0 the limit is independence; the α→−1+ interior limit is identically zero and cannot yield a continuous copula with the stated margins. The explicit computation F(log 2)<1 shows t*>1/2. An independently written 80-digit Decimal bisection confirmed s*=0.7761266919684155385876… and t*=0.5398149979439905133946…, with opposite corner signs at t=0.5397 and 0.5399; the numeric work is not the continuum proof.

## originality

PASS

The formula and nonnegative parameter validity are not new. The supported distinction is the exact necessary-and-sufficient negative endpoint and the corner mechanism. The exact catalogue match is this very frozen record. Related catalogued parameter frontiers concern different families; no reported theorem or inspected statement establishes the new negative endpoint. The inability to reopen the complete primary papers is a limitation, not evidence against prior coverage.

## value

PASS

Resolves an explicit admissibility question for a published dependence model. It determines exactly which candidate functions are distributions, improves on the reported numerical −1/2 suggestion, and identifies the obstruction mechanism and endpoint inclusion analytically, rather than presenting a grid estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
