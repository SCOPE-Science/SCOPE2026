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

Each legal itinerary through N tests is a uniform (N+1)-digit cylinder and the ordered matrices J-E_ab count exactly those itineraries. I checked the spectrum by restricting each step to the span of the all-ones vector and the relevant coordinate vector: A_i maps the span for a_(i+1) to the span for a_i, with 2x2 matrix H_k(d_i)=[[k,1],[-1,-d_i]]. The remaining eigenvalues of P are zero, because its image lies in the span for a_1. The trace of the product of the three H matrices is k^3-3k+sum d_i-product d_i; its determinant is the product of 1-kd_i, which never vanishes. The leading positive quadratic root is the spectral radius; evaluating the next quadratic at the preceding root gives the stated strict order (the r=0 vs r=1 comparison is immediate from the traces and opposite determinant signs). For a nonnegative P, its m-th power's sum of entries lies between its max-row-sum norm and k times that norm, so its exponential growth is exactly the spectral radius, including reducible cases. Monotonicity of survival between multiples of three gives the unrestricted limit. In the binary zero-overlap case the one-cycle itinerary count is 5, so P is not the identity, and (P-I)^2=0 gives the exact 2+3m path count. The class multiplicities follow by choosing all first digits and then each second digit with one or k-1 choices as required. At length two AB and BA have the same spectrum, while the two displayed length-three matrices and their radii differ. Repetitions and lower least periods are allowed throughout. A standalone direct-digit enumeration checked all 64 binary and 729 ternary schedules, the characteristic coefficients and class sizes, both binary example matrices, and the exceptional binary count at 3,6,9,12 tests for every binary zero-overlap schedule. Replay: python3 /workspace/branches/exact_review_checks.py 3. Frozen code and recorded evidence were inspected, not executed; the algebra, not finite enumeration, proves the theorem.

## originality

FAIL

The distinct indexed overlap-code theorem gives the rank-two H_b(t) product for arbitrary schedules and its periodic quadratic formula for b>=3. At period three, multiplication of these given 2x2 matrices yields precisely the frozen characteristic coefficients, and the same-weight three-bit codes are cyclic rotations. Its printed domain excludes b=2; this is not a direct quotation of the binary theorem. However, its displayed rank-two factorization and finite-prefix formula are algebraic identities valid verbatim at b=2, with no positivity or dimension theorem needed. At zero cyclic overlap every matrix in its prefix formula is H_2(0)=I+N with N^2=0, immediately giving n+2 legal strings for n tests, hence the frozen prefactor and defective multiplier. The minimal-order example is obtained by evaluating the two overlap codes 000 and 110 of the stated reorderings; at length two it is just cyclic similarity of the nonzero spectra. The class census is the elementary count of independent equality/inequality choices for the bits. Thus the principal classification is directly covered, and the binary and order refinements are mechanical from the indexed finite-count identity, rather than supported distinct contributions. The later catalogue date does not establish priority, provenance or dependence.

## value

PASS

As mathematical content, the minimal permutation-only example controls individual hole sizes and exposure counts while showing that order changes the asymptotic escape rate, not just finite-time mass. The complete period-three class structure and the binary non-exponential prefactor are useful explicit reference cases for moving Markov holes. This utility does not make the examples and formulas a separate contribution beyond the stronger indexed overlap-code calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
