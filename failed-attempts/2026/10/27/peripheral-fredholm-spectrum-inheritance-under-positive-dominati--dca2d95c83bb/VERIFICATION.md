---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

On c₀, AP_m has finite rank, and for compact K the norm ||K Q_m|| tends to zero because K* has compact image of the ℓ₁ unit ball and ℓ₁ tails tend uniformly to zero on compact sets. This proves the input-tail formula by comparison to arbitrary K. Iteration of |[S+z(T−S)]x|≤T|x| for |z|<1, applied to Q_m x, then bounds the Calkin norms of all powers by the corresponding powers of T. Gelfand gives the claimed spectral disks without assuming the interpolated operator is positive. For r>0 the spectral mapping of (1+conj(λ/r)G(z))/2 and Vesentini give equality of its radius with one throughout the disk, forcing persistence of λ/r by equality in the triangle inequality. Invertibility is open at z=1. At r=0, nonempty spectra of the unital Calkin algebra lie in {0}, so the result is automatic. The Fredholm interpretation follows from Atkinson. No computation is required.

## originality

FAIL

The result is a direct c₀ corollary of Dobrick's general theorem for positive operators on complex Banach lattices via the canonical action on ℓ∞/c₀. It is also obtained by applying Dobrick's precise Banach-algebra boundary persistence proposition to the Calkin interpolation after the elementary tail bound. The ordinary-spectrum versus essential-spectrum terminology does not prevent implication; the quotient preserves the relevant spectra. This is a finding of prior mathematical coverage, not of incorrectness or an inference from an inaccessible source.

## value

FAIL

The Calkin formulation may be useful as an expository corollary, but the record obtains the identical already covered outer-circle conclusion by combining an elementary coordinate-tail estimate with the established holomorphic spectral theorem. There is no separately established new boundary phenomenon, quantitative invariant, or independent useful remainder to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
