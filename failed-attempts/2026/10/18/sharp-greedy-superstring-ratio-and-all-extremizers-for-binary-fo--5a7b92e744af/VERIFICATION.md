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

The finite theorem is correct. The frozen endpoint proof skips a step: distinct end words rule out overlap exactly four, but a longer overlap would not directly identify the end words. The necessary invariant follows by greedy induction. Live strings start factor-free. If A,B merge at the current maximal overlap k, any surviving C newly contained in AB must cross the overlap (start before B starts and end after A ends, since otherwise C was contained in A or B). This would give overlap A→C greater than k; conversely AB cannot be contained in C as it contains A. For overlaps AB→C, anything longer than |B| would make C contain B; all shorter candidates are old overlaps B→C. The incoming estimate is symmetric with A. Hence factor-freeness persists and the largest overlap cannot increase from the original bound 3. The initial/final four-mer endpoints therefore suffice for all legal merges; this is also Chukhin et al.'s Lemma 2.2. In particular after all cross overlaps are zero, future overlaps stay zero. The OPT recurrence is exact by ordering occurrences by start (each adjacent gap is at least 4 minus the maximum overlap); each order also gives a superstring by merging. Independently replayed all 65535 masks with exact ratio cross-products in branches/6ce0ce10-ab0d-4f0c-a312-8c6a48f5cb8d/independent_binary4_replay.py. independent_full_replay.log lines 513–514 and independent_full_replay.exit record exit zero, 17/11 and exactly masks 1343, 5431, 60584 and 64672. The literal greedy witness uses overlaps 3,3,3,3,2,1,0; the eleven-character optimum is also proven by eight distinct four-mers needing at least eight factor positions. Frozen support was inspected, not executed. The proof check and replay certify the theorem, not an originality claim.

## originality

FAIL

The distinct indexed record c5782f9cc70b has the same entire sharp-ratio and all-extremizers theorem under identical hypotheses. Its different example output for the same extremizing set is allowed by the same tie rule and is not a separate theorem. This is a verified lack of distinguishable scientific content relative to the checked catalogue, not a historical priority judgment: the catalogue path dates differ, but dates and access do not establish provenance or direction of dependence.

## value

FAIL

A sharp finite binary-domain ratio and equality census would be a meaningful exact benchmark if not already covered. This record adds an alternate witness and another certificate for the identical theorem and no distinct classification or structural result. The replay has verification value but does not turn the duplicate into a separate scientific finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
