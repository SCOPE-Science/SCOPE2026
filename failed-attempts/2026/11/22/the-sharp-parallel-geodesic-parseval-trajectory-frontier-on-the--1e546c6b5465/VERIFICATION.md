---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The longitudinal fibers in the square are chains in the primitive direction (q,-p). The longest has h+1 entries, h=floor(2N/s): its end-to-end maximum coordinate displacement is hs, and any such integer segment fits by separate coordinate translations. Each loop gives at most one Fourier coefficient on that fiber, so fewer than h+1 loops cannot give injectivity at any offsets. Bezout transverse coordinates give distinct equally spaced offsets whose root sum kills every nonzero alias step |r|<=h when L>=h+1. This proves Parseval with the given Haar and arclength probability normalization. The least feasible integer s is s_L=1+floor(2N/L). For s_L>=2, primitiveness forces the other coordinate nonzero and the minimum squared winding is s_L^2+1, with equality precisely for signed coordinate permutations of (s_L,1). When s_L=1 the unit axes attain the minimum. For L<=2N, Ls_L>=2N+1 and the length is strictly larger than 2pi(2N+1); otherwise it is 2pi L, uniquely minimized at L=2N+1. The checker was inspected, not executed; its 12,544 alias cases are corroboration, not the proof.

## originality

FAIL

The asserted distinct Parseval frontier is covered, at the statement/implication level, by the distinct indexed positive multi-direction geodesic design theorem: its one-direction moment criterion and rank factorization yield the threshold, arbitrary-offset obstruction, and fixed-L cost by elementary specialization. It also expressly gives the same global optimum. This is a finding of material theorem overlap, not a historical-priority finding: both entries carry the same UTC date, and the stronger record acknowledges a pre-existing parallel calculation without identifying its source. That acknowledgment could refer to the submitted calculation; the date and anonymous reference do not independently settle origin. The negative decision is based on the scope of extant mathematical coverage, not on which entry was first.

## value

FAIL

The parallel loop count versus winding cost is a natural acquisition benchmark. The covered global optimum is useful, but as a distinct exact contribution this record gives only the one-direction specialization of the stronger moment criterion and rank block plus a primitive integer-vector minimization. The fixed-L expression and the no-offset obstruction do not add a substantive new invariant or bound beyond that coverage. This does not diminish the usefulness of the benchmark itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
