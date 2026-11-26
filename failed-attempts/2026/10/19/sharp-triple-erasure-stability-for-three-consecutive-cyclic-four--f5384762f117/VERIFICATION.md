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

Parseval subtraction and column rephasing give A(E)=1−λ_max(C_E)/N with real entries 1+2cos(2π(j−k)/N). The consecutive Gram splits into a scalar 3−b_N and a symmetric block giving L_N. For N≥8 all nonneighbor magnitudes are ≤b_N since b_N≥1 and the negative lobe is ≥−1; after relabeling, the entrywise absolute Gram is bounded by the consecutive Gram and nonconsecutive masks lose at least one adjacent pair. Strict irreducible Perron comparison proves the unique winning type. At N=7 the nonneighbor magnitude bound is d=a+b−2, and the nonconsecutive Gershgorin bound is below the consecutive all-ones quotient by (6−2a−b)/3>0. At N=6 the only gap types give shifts 2√2, √5, and 0. The retained Vandermonde has full rank for N≥6, but not for N=5; expanding the exact root gives the stated corrections. Independent bounded enumeration using the actual retained complex Fourier matrices, not the supplied cubic solver, confirmed the minimum and its exact mask class for N=6 through 16 to numerical tolerance.

## originality

FAIL

The exact mathematical claim is already represented in three distinct indexed findings at review time. In particular 1b09479ce727 and 486de14133a7 give the same formula and unique equality masks with additional spectral or recovery conclusions. The comparison is about present equivalent coverage, not a finding of pre-October publication, priority or derivation: all three comparators have later stated catalogue publication dates, and their first_public_date fields refer to lead sources, not verified dates of the theorem. The October comparators in the source do not cover the result.

## value

FAIL

The exact worst retained bound is a natural and useful stability quantity, and identifying every worst mask is intrinsically meaningful. For a distinct contribution in the current catalogue, however, the frozen claim has no additional invariant, range, equality case or mechanism that materially advances the matching results. The large-N expansion is a Taylor expansion of the already represented formula. This is a value judgment on incremental contribution, not on historical precedence or the usefulness of the theorem itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
