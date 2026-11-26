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

Summing the binary column equations gives digit-sum change equal to three minus the total carries. A carry entering a zero gap has already cost at least one carry; surviving three more zero columns incurs at least four, so accepted paths are carry-free after those columns. All subsequent zero columns, including the rest of a final zero run, are inert and their freely chosen digits do not affect the density. For an arbitrary original shift the event is therefore determined by a finite low-bit residue class; coordinate deletion of the inert bits preserves the proportion of accepted residues. Parity shows c_(2t)=c_t. Independently, /workspace/branches/replay_4.py computes exact tail densities using the even/odd splitting recurrence on shifts, based at t=1 on the geometric law of trailing ones, not the frozen carry transfer. It recovers all sixteen counts row by row: (43,76,164,336), (76,160,320,656), (164,320,640,1312), (336,656,1312,2688). Dividing by 2^(6+G+H) gives exactly the table, only the two minimal cells (0,1),(1,0), and the unique maximal cell (0,0). The frozen verifier was inspected, not run. Its Python 3.8 compatibility note is inaccurate for int.bit_count(); it needs Python 3.10 or later as written.

## originality

FAIL

Strong positive coverage evidence: Resultary 04e8343e48d1 proves a stronger all-weight gap-clipping theorem and reports the exact weight-three minimum and extremizers. Substituting k=3 gives the same sixteen shifts; applying the already available exact transfer or prior distribution recurrence to those representatives is sufficient to read out every entry, the value set and the maximum, with no new inference about arbitrary shifts. The full spectrum is not expressly printed in the matched Finding, but is a direct finite corollary. This assesses distinctness given the inspected evidence, not which record first discovered the result; the catalogue dates differ and cannot resolve priority or derivational dependence by themselves.

## value

FAIL

The exact spectrum is a naturally motivated invariant, and a new arbitrary-gap cutoff would substantively address it. But the cutoff and extremal minimum are already covered, and the remaining maximum and list of values are a sixteen-entry recomputation using the same clipped domain and known exact recurrences. No independently useful unknown claim survives narrowing the frozen result to those entries. This is a failure of distinct scientific contribution, not of the arithmetic or the motivation for the question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
