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

The convolution matrix has constant absolute row and column sum, attained respectively by aligning the input phases with one row and by a point mass. At nonzero arguments the raw kernel consists of four quartic periods, each repeated (p−1)/4 times. Since −1 is in the opposite coset, the periods pair by conjugation. The quadratic Gauss sum gives real parts (√p−1)/4 and (−√p−1)/4, neither zero. For J(χ,χ), the x↔1−x pairing has an even number (p−5)/4 of real nonfixed pairs and fixed term −1, so Re J≡−1 mod 4; its Gaussian norm p then gives Re J=−a. Taking real parts in τ(χ)²=√p J and using |τ(χ)|²=p gives the two asserted squared moduli U_p/16 and V_p/16; expanding the square roots uniformly gives the stated asymptotic. RESULT.md line 28 should allow either imaginary sign (p=5, g=2 gives J=−1−2i); choosing the conjugate quartic character if needed fixes the convention without changing any claim, since only the real part is used. The nonvanishing and the two triangle equality conditions give exactly the stated complex ℓ∞ extremizers. For clarity on the indirect ℓ¹ comment: two distinct occupied input sites would force K(t)/|K(t)| to be an additive character, by proportional translated phases and primeness. Then the spectrum H would be symmetric about that character's frequency. For |H|>1, summing H gives zero, forcing the center to be zero, contrary to −1∉H; hence only point masses attain ℓ¹ there. At p=5 the kernel is a single character and the ℓ¹ extremizers are that modulation of nonnegative inputs up to global phase. A fresh nine-prime raw-kernel check, including ± values of a, matched the norm and attainment; this is floating-point corroboration, not the proof.

## originality

FAIL

The scalar endpoint formula is a mechanically extractable specialization of published quartic period coefficients, using the generic absolute convolution row sum. The phase classification is the generic triangle equality for a nonzero row, enabled here by the known real parts. No independent mathematical remainder of the claimed contribution is established. This is demonstrable implication, not a claim that a prior source prints the identical projector theorem.

## value

FAIL

This is a natural projection and the closed expression is a useful expository calculation, but the exact fact is mechanically implied by existing explicit period data and the universal row/column sum rule. The extremizers in the record are generic phase alignment, and the expansion is routine; there is no separately established nonroutine invariant or new phenomenon that survives removal of the covered calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
