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

For u=(x/a)^2, K'' is proportional to (3u-1)/(1+u)^3+W(3u-t)/(u+t)^3, with t=(b/a)^2 and W=(b/a)(1-w)/w. Its roots are R_t(u)=W on (1/3,t/3). Independently differentiated R_t' and verified exact factor 6(t-1)(u+t)^2[5u^2-(t+1)u+t]/[(t-3u)^2(u+1)^4]. Discriminant t^2-18t+1 yields sharp t*=9+4sqrt5; monotonicity and endpoint limits give two/four/six distinct real roots and double/triple transition multiplicities. Exact rational quartic witness for (a,b,w)=(1,5,1/37) has three distinct positive roots. The proof, not finite evaluations, covers the entire continuum.

## originality

PASS

The invariant concerns curvature zeros of centered arithmetic mixtures, not modes or individual elliptic-operator Poisson kernels. No inspected primary theorem or relevant indexed record yields the sharp 2+sqrt5 mixture criterion; a differently indexed elementary calculation remains possible.

## value

PASS

A natural positive and strictly unimodal convolution family unexpectedly develops six curvature sign changes. The theorem classifies the whole parameter chamber and sharp onset of failure of two-inflection behavior, mathematically meaningful independent of higher-order bell-shape claims.

The dated certificate retains the supplied scientific assessment, sources and limitations.
