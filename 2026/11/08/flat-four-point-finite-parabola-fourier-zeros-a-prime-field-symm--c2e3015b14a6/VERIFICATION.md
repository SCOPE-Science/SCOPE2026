---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

PASS. The actual all-prime equal-modulus four-site statement has three matching possibilities because four unit complex numbers with zero sum form opposite pairs (first and third elementary symmetric sums vanish). Fixing a matching gives two linear equations in (a,b) over F_p, determinant proportional to (ti-tj)(tk-tl)((ti+tj)-(tk+tl)). Only equal pair sums give a rank-one matching and hence a full p-point frequency line; otherwise exactly one frequency per feasible matching. Three simultaneous matchings impossible for odd p by the disjointness mu_p intersect (-mu_p). For the line case, translating to support {-u,-v,u,v} and opposite coefficients gives two sine terms: for b!=0 equal-modulus cancellation would force |sin(2pi bu/p)|=|sin(2pi bv/p)| and u=+/-v, excluded, so no off-line zeros. Two remaining nonparallel matchings allow explicit coefficient witnesses of exactly 0,1,2 zero frequencies for every support; central symmetry permits p. The MUB support identity 4+(p²-Z) is exact under stated Fourier convention. Independent integer cyclotomic histogram for all four-point supports p=5,7 confirms witnesses and upper counts, and checked pinned artifacts/verify.py; the theorem for all primes and continuous phases is analytic, not finite extrapolation.

## originality

PASS

PASS qualified by inaccessible closely relevant primary paper. Fiorentino–Weigert 2022 proves general MUB support inequalities and low-dimensional bounds, not this fixed-four-site equal-magnitude all-prime zero-set spectrum. Dongwei Li 2026 gives a stronger *unrestricted-coefficient* four-site upper bound p+2, and a zero-line condition at sufficiently many zeros, but that upper bound does not yield the restricted p versus 2 dichotomy or all attainable phase-only counts. Rational and 2-power-root phase-alphabet parabola rigidity publications classify a proper subspace of complex unit phases, without two isolated zeros in general. Their statements do not dominate arbitrary unit-modulus phases. Full Li text could not be obtained; priority is expressly qualified, not claimed ruled out.

## value

PASS

PASS. For a fixed four-coordinate quantum state with equal-magnitude amplitudes, the exact zero set and complete p-dependent support uncertainty spectrum across mutually unbiased bases are natural operational/finite-harmonic invariants. The sharp symmetry-versus-nonsymmetry gap from p zeros down to at most two cannot be extracted from the broad complex-coefficient bound p+2 and provides a precise structural classification with equality cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
