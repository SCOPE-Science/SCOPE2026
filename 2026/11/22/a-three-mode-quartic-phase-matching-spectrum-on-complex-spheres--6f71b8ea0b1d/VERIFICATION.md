---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Independent uniform coordinate phases and Dirichlet(1,…,1) squared moduli give the normalized Haar monomial moments in the stated dimension. The half-circle Fourier coefficients give diagonal 1/2 and permit off-diagonal differences only at odd multiples of the primitive (1,1,-2) step. Exact degree four bounds the multiple by two, so only ±1 contributes. At fixed spectator exponent, the edges have initial third exponent at least two. The six quartic edges contain just one three-vertex path and four single edges; degrees three and two have three and one single edges respectively. Exact half-integer products confirm all squared weights and the sum 354/4096 for the two path weights (replay: python3 /workspace/check-1.py). The centered path eigenvalues are ±the square root of that sum and 0, with strictly larger offset than any single edge. Counting spectator exponents gives 10+6r+r(r+1) noncentral eigenvalues, hence the stated central count, including at r=0. The Rayleigh bounds are sharp and the ratio is the squared, not unsquared, restriction condition number. Submitted check.py was inspected, not executed; sampling is not used for the theorem.

## originality

PASS

Credit is limited to the fully evaluated exact quartic spectrum and dimension-independent sharp extremal pair for the three-coordinate half-phase mask. Torus selection rules and the generic monomial matrix machinery are established methods.

## value

PASS

This mask couples two coordinates against a doubled third phase, and degree four is the first degree admitting two consecutive character steps. The resulting three-mode extremizer is qualitatively different from an isolated pair of modes. The evaluated spectrum gives the sharp energy and condition bounds for all ambient dimensions and exact multiplicities off the extreme eigenspaces, which can be used without reconstructing a dimension-sized matrix.

The dated certificate retains the supplied scientific assessment, sources and limitations.
