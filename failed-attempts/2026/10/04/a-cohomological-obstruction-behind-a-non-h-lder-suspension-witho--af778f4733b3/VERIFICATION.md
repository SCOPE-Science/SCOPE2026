---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The stable-orbit calculation is correct: for the one-symbol point at index \(-1\), the forward distances to the zero fixed point are exactly \(2^{-k}/6\), so Wen's roof differences form the divergent harmonic-type series \(\sum_k(1+\log 6+k\log 2)^{-1}\). Under a hypothetical decomposition \(\tau=h+u-u\circ\sigma\), Hölder differences of \(h\) are geometrically summable and the continuous coboundary telescopes to a convergent endpoint, contradiction. For \(0<c<1\), the proposed \(r_c\) is positive, continuously cohomologous to the constant roof, and the exact one-symbol tail calculation gives polynomial \(n^{-2}\) variation against exponentially small symbolic distance, excluding every positive Hölder exponent.

## originality

FAIL

The negative cohomology conclusion is already a direct implication of the two exact prior statements once the standard conjugacy theorem is applied. Wen proves that this very logarithmic-roof suspension has no local product structure and that every Hölder positive roof over the same full shift does have local product structure. Fisher--Hasselblatt Proposition 1.3.19 says positive cohomologous roofs generate conjugate special flows. Hence, if Wen's roof were continuously cohomologous to a Hölder roof, its suspension would be conjugate to a Hölder-roof suspension and would have local product structure, contradicting Wen. The submitted stable-drift proof is an alternate proof of that already implied corollary. The explicit rough roofs cohomologous to the constant roof are likewise a routine coboundary construction once Proposition 1.3.19 is available.

## value

FAIL

The package gives a clear explanatory reformulation of Wen's counterexample, but the final mathematical contribution is a direct corollary of Wen's two flow theorems plus the standard special-flow conjugacy proposition. The positive comparison family is obtained by adding a small continuous coboundary to a constant roof. Under the audit value bar, this is a useful exposition rather than a new structural lemma, classification, boundary, or nonroutine exact invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
