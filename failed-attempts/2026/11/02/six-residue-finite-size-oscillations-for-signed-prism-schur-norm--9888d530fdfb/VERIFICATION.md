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

The constant diagonal of |J−2A| yields the upper bound Tr|J−2A|/(2m) by a Schur factorization; the real orthogonal spectral-sign witness gives the matching all-ones Rayleigh quotient even at zero eigenvalues and for the complex norm. The prism adjacency eigenvalues are 2cos(2πj/m)±1, and only the all-ones eigenvalue is changed by J. For m≥3 this gives s_m=1−6/m+E(P_m)/m, where E is adjacency energy. The identity |x+1|+|x−1|=2max(1,|x|) reduces the energy to a mesh of size n=m/gcd(m,2). The two outer arcs include 2⌊n/3⌋+1 indices (cutoff equality is harmless); summing their cosine terms gives the stated sine quotient, valid also for n=2. With δ=1−2(n mod 3)/3, expanding the quotient gives the correction π√3(1/6−δ²/2)/n²; its δ-linear term cancels the endpoint count. This gives all listed coefficients and a uniform O(m⁻³) error. The 6k−1 to 6k difference has leading coefficient 6−13π√3/9<0 in units (6k)⁻². Since s_m approaches its limit strictly from below eventually, it cannot be eventually nonincreasing either. The small m=5,6 values follow from the same sum and permutations preserve the norms.

## originality

FAIL

The Schur norm is a simple affine normalization of adjacency energy. Published exact trigonometric formulas for odd prisms and even Möbius ladders give the entire energy sequence here by a frequency split, not just the leading limit. The six coefficients and eventual descent follow by elementary Taylor expansion and subtraction; a different norm label does not remove the coverage.

## value

FAIL

The approach highlights a natural relationship between Schur norms and graph energy, but that relationship follows immediately from the invariant trace theorem and the trivial eigenvalue shift. The claimed arithmetic corrections and eventual decline are straightforward consequences of existing exact spectral energies and do not supply a separate sharp boundary beyond those formulas. This is a correct normalization and expansion of existing information, not a distinct new invariant calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
