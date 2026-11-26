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

Higher-block coding is an exact suspension conjugacy, with p_new(k)=p_old(k+a+b); the fixed length offset costs at most a constant alphabet-size factor. For the one-symbol roof, orbit segments starting on the section have equal physical return times up to the first different symbol, which is visible at uniform positive distance on the compact embedded section. Uniform continuity for one sampling interval converts continuous-time separation at that crossing to separation at a preceding time-map iterate. Conversely, a common block on a linearly long forward segment with a fixed padding fixes all needed roof sums. Two phases in a short common phase cell can be compared with the same return index, using the flow chart extended slightly across a seam, and are close by uniform continuity. The number of cells is bounded independently of n. Iterating doubling then removes the constant rescalings; for negative time reversing the orbit segments preserves separated counts. For the primitive substitution the length and zero-minus-one counts along θ^k(0) are 4^k and 2^k. This unbounded discrepancy about frequency 1/2 excludes even eventual periodicity. The two-supertile cover and Morse–Hedlund give linear upper and lower complexity; the same prefixes in a two-sided extension give roof sums whose discrepancy from the only possible constant slope diverges, contradicting bounded telescoping. The finite checks in checks.py test the example, not the infinite suspension theorem; they were inspected, not executed.

## originality

FAIL

Originality of the main frozen theorem is not established against distinct, demonstrably stronger published coverage. The published summable-cylinder-variation theorem supplies both the fixed-linear-rescaling bounds and the bounded-doubling equality for all nonzero time maps. Finite-window roofs have eventually zero cylinder variations, so this covers the entire main roof class, not merely commensurate or constant roofs. Both findings are dated the same day; the broader work's reference to a previously established finite-memory case is consistent with a follow-up, but does not identify that result by source or establish priority between the two records. This is a coverage decision, not a claim that the broader work was published first. The particular non-cohomologous substitution example was not located in that source, but is an illustration and does not establish originality of the full frozen finding.

## value

PASS

Controlling a full generalized growth order for a nonconstant roof addresses the concrete section-crossing obstacle identified by Corrêa–Lacerda. The possibility of retaining linear generalized entropy without continuous cohomology is worth illustrating, and the proof identifies exact synchronization as the relevant finite-memory mechanism. This is a worthwhile question and example even though the main assertion is covered by the distinct larger roof class.

The dated certificate retains the supplied scientific assessment, sources and limitations.
