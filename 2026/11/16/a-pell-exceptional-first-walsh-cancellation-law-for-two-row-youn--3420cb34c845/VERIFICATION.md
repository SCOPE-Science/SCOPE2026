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

For a two-row Young ideal (a,b), 0<=b<=a<=n, the independent sign-prefix variables X_a,Y_b give W=sum_a X_a sum_{b<=a}Y_b. Parity of M=(n+1)(n+2)/2 proves zero-free n=0,1 mod 4; alternating Y gives exact attainable ±1/0/±2 gaps. Singleton zeros require t(t+1)/2=M/2, equivalent to (2n+3)^2-2(2t+1)^2=-1; positive odd Pell solutions give n=2,19,118,695,... and exactly two singleton cells. In all other singular n, explicit top-row pairs (k,3k+2) or (k+1,3k+3) give precisely half of the M diagrams with odd incidence, hence support two. The recurrence updating S_j by an independent Y sign and w by X_j*S_j counts all 4^n characters exactly in O(n^4) additions. Independent state transfer reproduced the six asserted nullities 6,18,789,2807,137820,511732 and total 4^n mass; finite agreement is not the Pell or recurrence proof.

## originality

PASS

Bounded search finds no prior covering the final substantive claim as a whole; all identifiable overlapping subresults are disclosed, especially the duplicate two-row parity/gap, and residual historical risks are retained.

## value

PASS

The new Pell-exceptional low-support zero classification identifies the sparsest Fourier obstructions on a natural distributive lattice of two-row Young diagrams. The exact polynomial-state recurrence determines every full nullity, a natural invariant not supplied by the otherwise related Brownian limiting-spectrum result. Both are usable for reconstructability and exact kernel analysis and add nontrivial information, although the common parity invertibility and sharp gap are already published and must not be claimed as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
