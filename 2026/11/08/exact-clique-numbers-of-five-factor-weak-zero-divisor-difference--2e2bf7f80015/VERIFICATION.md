---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the five-factor clique formula

The proof is self-contained in `RESULT.md`; the executable checks below supply finite corroboration, not an infinite proof.

From the directory containing these files run:

```sh
python3 verify.py
```

The checker has only standard-library dependencies. It constructs the 30-vertex support-intersection quotient and enumerates all 81 maximal cliques independently by a bitmask Bron--Kerbosch algorithm. For 39 field-size tuples it compares the maximum weighted clique with the unordered positive-part formula and the seven ordered candidates. It separately enumerates all unordered vertex pairs in four products of prime fields and reconstructs the difference-edge relation from annihilator witnesses and coordinate multiplication. The four direct comparisons cover 435, 990, 2211 and 2211 pairs respectively. The stored log `verification_output.txt` records the actual run and ends with `VERIFY_OK`.

Critical symbolic boundaries: co-atoms form independent *internal* classes, so their clique weight is one rather than their number of ring elements; all size-two supports are pairwise intersecting only for star/triangle systems; a selected pair excludes exactly its complementary triple; sorting is harmless because each replacement gain increases by a nonnegative factored difference. Every term is checked in the proof. Arbitrary extension-field multiplication is not computationally simulated: the theorem uses only the nonzero-coordinate support structure, which holds in all finite fields.

No independent audit or external formal certification has been performed.
