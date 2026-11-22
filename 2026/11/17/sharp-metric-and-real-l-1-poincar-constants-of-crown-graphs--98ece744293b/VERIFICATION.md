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

PASS: For n>=3, symmetrize arbitrary induced pseudometric over index permutations and bipartition exchange, preserving edge/pair sums. Orbit distances a,b,c satisfy a<=2c and b<=a+c<=3c; normalized average ratio <=3/2 and shortest-path distances (2,3,1) attain it. For real L1, coarea reduces to cuts; with s selected vertices, k left, ell right, t fully selected matched pairs, boundary B=(n-1)s-2k ell+2t. The bound k ell<=floor(s²/4), t>=0 and monotone envelope yield even (n-1)/(n-2) and odd n/(n-1); equality requires s=n, t=0, |k-ell|<=1. Independent all-cut search for n=3..8 verifies optimum and cut strata; infinite result uses inequalities, not finite extrapolation.

## originality

PASS

No earlier checked statement implies both crown-graph sharp constants plus the exact balanced opposite-pair equality layers; broad graph results and different operator/cut invariants are distinguished.

## value

PASS

PASS: Canonical almost-complete bipartite family distinguishes unrestricted metric and real L1 exponent-one gaps from n=5 onward. Exact all-n parity formula and full layer-cake equality strata provide meaningful structural benchmarks, not a simple restatement of a known table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
