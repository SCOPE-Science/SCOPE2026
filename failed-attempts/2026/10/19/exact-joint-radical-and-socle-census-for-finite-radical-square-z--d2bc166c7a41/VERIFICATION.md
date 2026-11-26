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

The all-ordered-products relations impose U⊆K. At a fixed such flag the matrices are uniquely k maps from the t-dimensional quotient V/K to U. Exact K means the stacked linear map is injective; exact U means the images span U. With images restricted to an a-subspace A≤U the first constraint counts ordered independent t-tuples in A^k, giving the injection product. Möbius inversion in the subspace lattice gives the stated factor, and the two Gaussian coefficients count flags with dimensions r,n−t. The formula vanishes when just one dimension is zero, gives one at (0,0), and no flag is possible if r+t>n. Simultaneous transpose exchanges the image sum and common kernel by annihilators and preserves all products being zero. Radical and socle are JM and its J-annihilator because J²=0 and the quotient algebra is the field. No conjugacy quotient or characteristic condition enters. The supplied prime-field enumeration and formula-only checks were inspected, not run. A separate exhaustive binary check took all 16 matrices on F_2², formed all 256 ordered pairs, tested the four products and computed both ranks; its strata were (0,0):1 and (1,1):9. This finite check corroborates the normalization, not the general proof.

## originality

FAIL

A distinct indexed framed top–socle census prints the identical arbitrary-arity formula over every finite field, and a finer indexed rank census takes it as a marginal. These entries have later catalogue paths, so the match establishes mathematical coverage at review, not earlier chronological priority. The older pair census and variety papers do not themselves state the complete point count.

## value

FAIL

The dimensions of the radical and socle are natural, and their joint labeled count is mathematically finer than geometry or a pooled count. But the precise invariant is already covered by an identical indexed formula and by stronger enumerations; the sum and transpose symmetry do not leave a separate unknown contribution in this Finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
