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

The root value is observed without loss at the output root, and on the copied output vertices the root term is absent. The full level averages are convex combinations of the p-th powers of the respective input level norm and root value; this proves contractivity and the constant function gives equality. With each level rescaled to a standard ℓ_p block, each copy is δ_j times an isometric coordinate embedding. Keeping the root term plus k−1 coordinates gives rank at most k, and deleting arbitrary coordinates within an ℓ_p block has norm at most one. Conversely on the span of the root input unit and k copied coordinates of weights ≥w_k, the norm of the output dominates w_k times the full input norm, by testing separately the root and each copied piece. Every rank ≤k map has a kernel vector there. This works even when some input and output depths coincide, since a single application does not compose those copies. Exact tails and unit vectors on distinct input levels give both directions of compactness; no weak convergence hypothesis on the ℓ∞ sum is needed. In the arithmetic case the a-index endpoints are J_{j−1}+2 and J_j+1, giving exactly the printed liminf and limsup. For arbitrary ρ the ceilings are nondecreasing and each weight is between q^(−1/p)q^(−j/ρ) and q^(−j/ρ); the cumulative block count is comparable to q^j even when weights tie. The proof, not the diagnostic, establishes these claims. The frozen checker was statically inspected: its normpower function divides two integers using `/`, so some input averages are floating-point despite the advertised exact-rational scope. This does not enter the proof; do not cite those comparisons as an exact certificate.

## originality

PASS

Best-of-knowledge for the complete approximation-number profile and its threshold realization; the norm and qualitative compactness are prior consequences, and the general proof technique is standard.

## value

PASS

This gives all optimal rank errors for a simple family of unweighted symbols in a setting where the general criterion is qualitative. In particular it exhibits every positive strong/weak approximation summability transition on one fixed tree Hardy space and computes the distinct endpoint constants instead of just a decay exponent. The calculation is useful independently of generalizations to other symbols; no Schatten conclusion is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
