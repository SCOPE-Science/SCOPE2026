---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For a fully occupied simple ring with exactly b blue and r red (1<=b<=r, n>=3), symmetric p(1/3)=p(2/3)>p(1)=0 makes strict mutual improvement possible exactly when both colors have segregated triple centers. Thus stability requires one color with all runs of length <=2. Alternating run compositions and n/k marked-origin counting give N=F(b,r)+F(r,b)-H(b,r), correctly accounting for labeled ring vertices. Each run contributes min(length,2) integrated vertices, giving maximum min(n,3b) and minimum stable b+min(r,ceil(b/2)+1). Independently enumerated 2,209 labeled profiles for 29 population splits, checked all unlike swaps, total 1,612 stable cases, count and both welfare extrema.

## originality

FAIL

A FULL October 25, 2026 mathematical theorem already gives the same half-peak, closed-neighborhood, full-occupancy, free distant swaps and labeled-coloring setup. It establishes the same iff triple-run condition; the exact identical binomial count as z=1 of its more general integration generating polynomial; and the same exact minimum, maximum and price of anarchy. Its b+ceil(b/2)+1 equals b+min(r,ceil(b/2)+1) on the submitted domain n>=3, b<=r. This is full prior coverage, not a nomenclature difference.

## value

PASS

The structural run criterion and finite-population enumeration are motivated combinatorial and game-theoretic quantities, but the older complete equilibrium integration polynomial is strictly stronger; the submission does not add value beyond covered prior mathematics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
