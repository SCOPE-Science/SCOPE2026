---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

This counts distinct overlapping multiplicity-preserving trigram profiles of linear binary words after exactly one deletion, including both ends. Subtraction of the original profile is injective. Recounting the 32 five-bit contexts gives ten distinct interior deltas with multiplicities 8,8,4,4,2,2,1,1,1,1; the first and last two deletions contribute at most four additional deltas, giving 14. The fixed first four and last four bits of the witness give four distinct non-interior deltas. In the witness, 01000 uses the first three zeros of the extended run, 00100 its final two zeros plus 100, and 01001 its final zero plus 1001. The other seven required factors occur entirely in the fixed suffix. This corrects the misplaced location of 01001 in the proof text, not the claim or witness. For n<=3 all profiles are zero. For 4<=n<=20 the DP legitimately remembers the prefix, suffix, and exact set of interior deltas and covers every word. Independently ran python3 /workspace/review_evidence/recompute5.py in bounded slices 1–14, 15–17, and 18–20: each descendant was reconstructed and all its triple counts tallied from scratch in eight separate five-bit lanes (no carries because n-3<=17). Complementation permutes coordinates, so one leading-bit class is exhaustive modulo that invariant. The exact maxima were 1,1,1,4,4,6,6,7,8,8,9,10,10,10,11,12,12,12,13,14, with 48 extremizers at length 19 and 32 at length 20. The infinite claim rests on the verified contexts in the witness, not the finite run.

## originality

PASS

Best of current knowledge: the short-length binary spectrum, the first attainment at 20, and the explicit sharp family starting there are distinct from the inspected literature. The separate q-ary record genuinely recovers the binary maximum 14 and its interior counting argument, credits earlier binary work, and does not establish early binary saturation. The maximum is not credited as distinct from that recovery, and same-day index dates do not establish priority.

## value

PASS

For a natural equivalence on deletion descendants, the exact maximum and shortest witness resolve when the ten interior and four boundary signatures can actually coexist. The threshold and the complete short-length profile-ball maxima provide a meaningful binary baseline not supplied by larger-alphabet covering bounds or counts of raw descendants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
