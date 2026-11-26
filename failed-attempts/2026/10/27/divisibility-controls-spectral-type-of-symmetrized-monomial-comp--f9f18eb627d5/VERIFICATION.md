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

The adjoint monomial action gives oriented edges nk→mk and the constant summand [2]. To check completeness independently, put m=ga, n=gb, with a,b coprime. Outside the multiples of g the positive-degree vertices are isolated. On multiples of g divide the index by g. If a,b>1, each reduced positive index has a unique form a^p b^q u with a∤u, b∤u, using maximal integer-power exponents. The edges increase p and decrease q, keeping u and p+q fixed, so the full components are paths of size p+q+1, of each size countably many. If one reduced degree is 1, the same argument with maximal powers of the other degree gives rays (up to reversal); positive indices outside multiples of the smaller original degree are infinite isolated zeros. Discrete sine vectors diagonalize finite paths, and the half-line sine transform makes a ray multiplication by 2 cos θ on (0,π); its spectral measures are absolutely continuous and it has no eigenvalues. Both ordinary spectra fill [−2,2], with no isolated points, so the Fredholm essential spectra are the whole interval. In both cases 2 is a simple eigenvalue and −2 is not an eigenvalue; the dense atoms in the nondivisible case do not make every spectral point an eigenvalue.

## originality

FAIL

The entire frozen classification follows directly from the pre-existing published unitary classification of the reverse product U_n*U_m in Resultary 71d831748432. The different order of factors is not a substantive difference: dilation identifies U_n*U_m unitarily with the restriction of U_mU_n* to indices divisible by gcd(m,n), and the complement is zero. Symmetrizing the classified blocks and applying the standard sine spectra yields the full frozen claim. A separate later indexed classification e66a895c9359 directly treats U_mU_n* and supplies a second route to the same result; its date is not evidence of earlier priority.

## value

FAIL

The distinction between an absolutely continuous component and dense atomic spectrum at the same essential interval is meaningful. As a proposed new finding, however, this exact classification requires only a basis dilation, symmetrization of the already classified blocks, and textbook sine diagonalizations. No independent application, new invariant, or additional case remains in the frozen scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
