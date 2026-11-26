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

Reconstructed the proof in RESULT.md, lines 29–74. The radial Bergman moments give d_k=(k+1)/(k+1+s/2); the shift self-commutator has diagonal h_k=1/((k+1)(k+2)), including k=0. Substitution a_k=sqrt(h_k)y_k gives the stated off-diagonal j_{s,k}. The absolute adjacent sum is dominated by the form on the coordinatewise moduli, with equality available on nonnegative strings; finite strings are dense and alternating signs negate J_s. For a=s/2, dividing the two quadratic leading expansions gives j_{s,k}/a=1+(1/2-2a)/k+O_s(k^-2). The tail difference from the constant shift is compact by norm approximation with finite-rank truncations. At a=1/4 the denominator is (k+1)(k+5/2)+5/16, strictly exceeding the numerator by AM–GM; it increases with a. Below the threshold the positive correction is bounded below by a fixed positive multiple of 1/N throughout a block of length floor(N^(3/4)), with sine-vector kinetic loss O(N^-3/2). Separated blocks have no cross terms, giving arbitrary-dimensional Rayleigh subspaces above s; the alternating unitary and endpoint recurrence give the negative outliers and simplicity. Each positive block already gives a polynomial counterexample. The Toeplitz cross term normalized by H^(1/2) has off-diagonal modulus |c|j_{s,k}; positivity is tested on all finite y because every such y lies in the range of H^(1/2). The frozen check.py was inspected as a finite diagnostic, not used as proof.

## originality

FAIL

A distinct indexed Resultary record states the same normalized Jacobi matrix, sharp half-power norm transition, equivalent Toeplitz radius, and infinitely many simple outliers on each side below the cutoff. It additionally states an edge counting asymptotic. The polynomial coefficient formulation adds no independent result: finite-support density and phase alignment give exactly the norm in the overlapping record. This is demonstrable equivalent coverage; the shared date does not establish priority in either direction.

## value

PASS

Considered on mathematical merit, computing the exact cutoff answers a motivated unresolved regime of the earlier norm criterion: it identifies when the essential band controls hyponormality and when infinitely many discrete states obstruct it. The transition and its two spectral mechanisms are more than routine normalization. This assessment does not claim an additional contribution beyond the overlapping catalogue theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
