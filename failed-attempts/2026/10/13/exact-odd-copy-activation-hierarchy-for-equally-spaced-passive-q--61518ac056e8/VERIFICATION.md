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

All energy shells t=0 through 2N occur. It suffices to compare adjacent shells, because minimum population in the lower shell exceeding or equaling maximum population in the next propagates by transitivity. For two such words, twice minus the log population ratio is u+v+(u-v) times the difference in middle-level counts, with the intended grouping (u+v)+(u-v)*Delta. The difference is odd and lies between -r_N and r_N. Both extremes occur: compare the r_N ones against the endpoint-only words at energies r_N-1 and r_N+1; append the same zero for even N. Thus the sharp inequality is u+v>=r_N|u-v|, with equality passive by rearrangement. Rearranging gives the sandwich. The least allowed odd r_N strictly exceeding 2 max(u,v)/|u-v|-1 gives the floor formula including integer-ratio boundaries; equal slopes give Gibbs and no activation. Independent replay: python3 -I -B /workspace/audit_replays/frozen_math.py 5, with 12240 exact adjacent-shell checks up to 15 copies for ordered positive integer triples bounded by 16.

## originality

FAIL

The distinct indexed Sharp odd-copy activation law has the same spectrum, initial population order, arbitrary global operations, all-copy iff boundary, Gibbs case, equality rule and parity pairing. Its floor formula is exactly the same after shifting the min/max quotient by one. This is verified mathematical coverage, not a priority claim based on record dates. The alternative proof via parity and the symmetric sandwich do not change the theorem.

## value

FAIL

An exact resource threshold at Gibbs proximity is a natural invariant, but the identical threshold, parity pairing, and equality convention are already given in the matched record, which also treats the divergence near thermal populations. The symmetric expression and one additional rational witness do not add a distinct boundary, population regime, or extraction result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
