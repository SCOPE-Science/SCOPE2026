---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Reconstructed distances sqrt(3)/2 times |t| and |1-t| and projections to the farther line, yielding the exact affine map (i,t)->(i+1,(1-t)/2) below t=1/2 and (i-1,1-t/2) above. For s=t-1/2, s_next=-s/2+sgn(s)/4; exterior |s|+1/2 halves each step, sign switches, and interior sign is invariant while contraction factor is -1/2 toward ±1/6. Powers-of-two exterior endpoints hit a vertex then fixed midpoint; other exterior points enter the interior in ceil(log2 max(t,1-t)) steps. The even dyadic shells have length 2^{2j-1} and give exact density 2/3 at R=4^j and limiting 1/3 at R=2*4^j. Capture-time geometric law follows from length 2^{n-1} shells. Checked exact rational verification source; no finite run is mistaken for proof.

## originality

FAIL

Direct decisive statement-level prior coverage by the November 2 2026 Resultary full theorem. It has precisely the SAME infinite supporting-line geometry, farthest-projection/tie convention, three midpoints, two primitive 3cycles, dyadic exceptional set, exact orientation-shell parity and liminf/limsup 1/3 and 2/3. Its proof supplies shell lengths and first-capture times, implying the submitted geometric-distribution law. The November 17 submission is not an independently original theorem.

## value

FAIL

As a new contribution the claimed complete equilateral global basin/density classification and the accompanying capture-time distribution have no independent value beyond the already established November 2 theorem: the identical piecewise affine map, complete recurrent set, exact exceptional set, orientation-shell formula and sharp directional densities were published there. Its shell intervals and lengths immediately give the alleged additional capture-time geometric distribution by dividing 2^{n-1} by 2^m-1. The exact classification is mathematically natural, but recomputing a known complete natural classification and a direct counting corollary does not create a new mathematical gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
