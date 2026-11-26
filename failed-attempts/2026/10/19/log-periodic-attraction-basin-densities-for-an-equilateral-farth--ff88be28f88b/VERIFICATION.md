---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The two distances are (sqrt(3)/2)|t| and (sqrt(3)/2)|1-t|. Taking the farther line and projecting gives the stated two affine branches; both chart descriptions of a vertex give the same opposite midpoint. On t>1 two steps give t/4, and on t<0 they give 1+(t-1)/4. Iterating to [0,1] exhausts all exterior states; the two open half-sides remain invariant and contract by -1/2 per step toward the two three-cycles. The endpoints and midpoint are precisely the exceptions in [0,1]; pulling these back by the two-step maps gives the stated four progressions and the midpoint. Across each such point, nearby iterates on opposite sides land in different invariant half-sides. The progressions give 4 log_4 R+O(1) per chart, and shared vertices affect the distinct count by O(1). The positive-ray minus basin occupies (0,1/2) and (4^k,2·4^k); adding their clipped lengths gives the boxed formula, with a continuous phase rising to 2/3 and falling to 1/3 on [1,4]. This is for complete lines and directed cutoffs, not all cutoff conventions. The frozen verifier reports finite checks, not an independent audit. A separate bounded check (python /workspace/branches/independent_checks.py 4) agreed for 1,887 exact rational geometric orbits; it is not a proof for all real states.

## originality

FAIL

A distinct Resultary finding, 9ee2bb535370, gives the same full basin partition, midpoint preimages and sharp one-sided limits under a translation of the side coordinate and a relabeling of the cycles. The exact uncentered B_-(R) formula and exceptional-point count are direct summations/counts of those same shells, not a distinct surviving result. This is a finding of equivalent coverage in the current corpus, not a claim that the November 2 catalogue entry preceded the October 19 frozen entry or that either copied the other. Everett and the earlier arbitrary-triangle three-cycle result do not themselves cover the global basin law.

## value

PASS

The global partition of a natural unbounded piecewise contraction and the nonexistence of a one-sided basin weight despite a discrete separator are useful dynamical facts. The exact phase law explains that failure and contrasts with symmetric cutoffs. This mathematical value does not make the duplicate shell law a distinct contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
