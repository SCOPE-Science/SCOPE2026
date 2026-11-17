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

For n>=2 in characteristic two, S_n is cyclic by its endpoint Krylov basis. Its path characteristic polynomial at eigenvalue one has multiplicity m=2^{ν₂(n+1)+1} exactly when 3|(n+1); otherwise 0, from primitive cube-root Laurent substitution and local nonzero derivative. The ladder matrix becomes (u,v)->(Cu,u+Cv) with C=S_n+I. On its zero-primary sector multiplication by t+ε on K[t,ε]/(t^m,ε²) is equivalent to two length-m nilpotent blocks because m is a power of two. Fitting kernel counts give all first-entry shells and the 1−q^-2 last-step fraction. Independent GF(2) rank checks reproduced 208 cases for n=2..30.

## originality

PASS

Path-rule characteristic-polynomial methods were known, and general Fitting transient counting is standard; the sharp two-block ladder Jordan classification, mod-three reversibility, and full two-adic first-entry census for all open ladder lengths are the surviving result.

## value

PASS

A sharp reversibility boundary and unbounded normalized transient depth on a bounded-width natural grid family are meaningful structural dynamics, not merely a small instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
