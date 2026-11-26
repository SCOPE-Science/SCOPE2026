---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

On an elementary half-base cell the sign is the side of the half-partition visited by x -> bx mod 1. Refinement yields b consecutive half-cells with alternating signs: equally many of each in an even base and one more with the parent's sign in an odd base. Thus a,c are the transition multiplicities and destination weights give the displayed two-state transfer matrix. The characteristic polynomial has trace 2a cosh(t) and determinant a^2-c^2. Its positive Perron root gives P_b; P_b'=a sinh(t)/sqrt(c^2+a^2 sinh(t)^2) increases strictly from -1 to 1. The finite-cell exponential counting bound gives the upper dimension. For the lower bound the Perron probabilities on individual child edges telescope, giving cylinder log mass per step tu-P_b(t) almost surely by stationarity and ergodicity. This yields a Euclidean dimension bound without assuming gaps: at each finite tilt the largest conditional child probability is p<1, and the conditional probability of landing within the extreme left or right subcell of relative depth ceil(eta*n) is at most 2p^ceil(eta*n). Borel–Cantelli and interpolation of the ball radii give local dimension (P_b(t)-tu)/log b as eta tends to zero. Kinks have zero mass. The endpoint upper bound follows by sending the tilt to infinity; the a self-sign children give matching dimension log(a)/log(b) when a>=2, by uniform cylinder mass and the bounded number of equal-length cells meeting a ball at that scale. For b=2, sparse infinite wrong signs and infinitely many correct signs make each endpoint set nonempty off the dyadics; the upper bound is zero. The even-base entropy and strict concavity follow from the explicit pressure. This concerns finite-sum slopes, not heights or derivatives of the limiting function.

## originality

FAIL

The binary result is the classical exact digit-frequency dimension. For every base, including odd bases and both endpoints, the frozen spectrum is already a special case of the known variational theorem for Birkhoff level sets on finite mixing shifts, using the established Takagi sign coding. Evaluating its pressure is the characteristic-root calculation of the already specified two-state tilted transition matrix, and does not leave a separate mathematical finding. This is demonstrable coverage by implication, not a claim that the displayed odd-base formula was found verbatim elsewhere.

## value

FAIL

The finite-slope spectrum is a natural pedagogical example, and the odd/even split is a useful illustration of the known correlation. However, in this submission all substantive conclusions are inherited from the exact sign law and the standard Birkhoff spectrum theorem, with only a two-by-two characteristic-root evaluation and elementary consequences. Neither the binary case nor narrowing to odd bases leaves an independently unresolved exact invariant or additional structure of the required scientific value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
