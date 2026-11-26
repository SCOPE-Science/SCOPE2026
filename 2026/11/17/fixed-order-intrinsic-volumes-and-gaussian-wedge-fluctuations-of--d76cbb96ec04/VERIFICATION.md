---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The Steiner-normalized wedge sum equals 2^(dk)/k! times the with-replacement mean, since zero and repeated columns contribute zero. Grouping the Boolean rows by pattern gives the exact multinomial formula, including singular cases. The population Gram matrix is M=(I+11^T)/4. For a row, put U=xi^T M^(-1)xi and let S be the sum of k independent signs. Then U-k=(2S-(S^2-k))/(k+1); E S^2=k, E S^3=0 and E S^4=3k^2-2k give Var(U)=2k/(k+1). For the whitened centered sample Gram matrix H, E(tr H)^2=Var(U)/d and E tr(H^2)=(E U^2-k)/d. The coefficients 1/8 and -1/4 of those terms in sqrt(det(I+H)) give relative correction -k^3/[4(k+1)d]; its linear term and the scalar CLT yield variance k/(2·4^k). A fixed positive-definite neighborhood has exponentially small exceptional probability by entrywise bounded-variable concentration; the Gram determinant is bounded outside it for fixed k. Taylor through degree three suffices: centering gives cubic expectation O_k(d^-2) and fourth absolute moment O_k(d^-2), proving the claimed remainder. Division by the k=1 expansion yields (4), including -5/(12d) at k=2. Independent exact determinant-multiplicity comparisons passed in 15 prespecified finite cases; finite binomial moment checks passed at k=1 through 10. These corroborate the arithmetic, not the limit proofs. Replay: python3 /workspace/branches/f04aeafb-7f50-468b-902d-3d0a846f7f74/finite_repro.py; see finite_repro_results.txt in that directory. The frozen verifier was read as evidence, not executed.

## originality

PASS

Pass applies to the fixed-order Boolean-specific asymptotic coefficients and wedge fluctuation law, not to the established intrinsic-volume identity or its direct multinomial specialization. Compared sources do not give the same constants and law or a stronger result already determining them without the row-moment calculation. Historical priority remains provisional.

## value

PASS

The natural Boolean-generator zonotope has many highly nonorthogonal directions. The normalized intrinsic volumes quantify the surviving alignment (already sqrt(3)/2 at order two), and the explicit bias and fluctuation scale distinguish the fixed-order geometry from the established general wedge identity or a leading-order law of large numbers. These are reusable Euclidean invariants with a clear fixed-k scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
