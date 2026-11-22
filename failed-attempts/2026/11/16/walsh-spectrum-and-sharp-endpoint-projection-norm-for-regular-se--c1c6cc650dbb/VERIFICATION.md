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

Parity constraints on K7 outdegree give an affine 15-bit quotient, with 64 frequency lifts. An independently constructed exhaustive 2^15 Walsh transform yields exactly 2640 regular orientations, 8656 quotient nonzeros and the full absolute spectrum histogram stated, and an exhaustive second transform gives ∑|H|=1427840, hence 11155/256. Translation-averaging proves any projection onto the range cannot beat the canonical invariant projection. Finite enumeration is exhaustive at order seven, not a general tournament theorem.

## originality

FAIL

A separate published full mathematical result has precisely the same seven-vertex regular-tournament indicator and evaluates exactly the entire absolute Walsh histogram, full rank 553984, nullity 1543168, gap 16, condition ratio 165, and universally sharp unrestricted endpoint projection constant 11155/256. The opposite edge-orientation bit convention only changes signs and relabeling, not these invariants. The present claim is entirely covered.

## value

PASS

For a natural smallest nontrivial multi-isomorphism regular tournament universe, the full Fourier recovery rank and sharp optimal endpoint projection amplification are well-motivated exact invariants, even though this particular result has already been published.

The dated certificate retains the supplied scientific assessment, sources and limitations.
