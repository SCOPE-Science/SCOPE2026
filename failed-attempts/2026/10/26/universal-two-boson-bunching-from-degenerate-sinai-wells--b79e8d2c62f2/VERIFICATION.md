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

The reverse inclusion hop cancels the same occupation factor as the forward hop, leaving rate ratio w_{i+1}/w_i. This proves the stated product-weight canonical law; irreducibility holds at fixed N, and diagonal densities remain diagonal under the Lindblad jumps. At fixed L normalize the maximal weights to one. Divide the marginalized weight of each nonground configuration by the number of compositions of N into K ground boxes. The remaining combinatorial ratio is ≤1 and tends to 1 at each fixed nonground configuration. Summable geometric weights give tightness and asymptotically full ground mass, and the uniform weak-composition grid converges to the uniform K-simplex law (point mass if K=1). As a direct moment check, conditional on putting n=N−M particles in the ground boxes, their expected sum of ordered pairs is 2K binom(n+K−1,K+1)/binom(n+K−1,K−1)=2n(n−1)/(K+1), with zero pairs when n<2. The path splits at the first and last minimum into positive meanders and K−1 positive return excursions with Catalan series E. The unmarked count 1/(1−2t) then gives (1−E)E^{K−1}/(1−2t). At fixed K its numerator is absolutely summable at t=1/2; convolution yields 2^{−K}, and these limits sum to one. Integrating twice the marked series over a uniform mark in [0,1] gives the stated logarithmic generating function, and the bounded pair moment averages to 4 log 2−2. At h=0 every one of the L sites is a maximum, giving exact pair probability 2/(L+1) for N≥2. The proof checks the stated order of limits, not a joint N,L scaling; the frozen checker was inspected, not executed.

## originality

FAIL

The exact random-well multiplicity series is a marginal of the earlier indexed two-level series, and Pitman–Tang explicitly give the limiting geometric law. The prior inclusion-process canonical theorem supplies the ground-box distribution conditional on the nonground occupancies. The remaining pair observable, finite-length transform, and zero-disorder comparison are mechanical consequences of uniform compositions and the already covered law. No inspected paper prints the physical scalar 4 log 2−2, but that is not distinct mathematical content once these statements are combined.

## value

FAIL

Co-location at high loading is a motivated observable in Longhi's model, and its contrast with the clean chain is a useful interpretation. As a proposed additional exact invariant, however, the number and finite-length curve are already determined by the covered walk law and a textbook factorial moment of a uniform weak composition. The singular h=0 case just replaces K by L under the same formula. The application supplies no separate surviving structural result, new regime, or independently unresolved exact fact at this scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
