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

Faber–Pandharipande Theorem 2 gives H_g(x)=4^{−g}[u^{2g}](u/sin u)^{x+1}. For each multiplicity partition, Legendre's digit-sum formula gives ν_p((2a+1)!)≤⌊a/s⌋. Set f=Σ λ_a⌊a/s⌋ and t=q−f. The large-part count is at most f, and the small-part count is at most r+st by the weight constraint. Applying the multinomial valuation inequality to the two groups separately yields the frozen denominator bound. For t≥1, r+st<(p−1)t gives ν_p((r+st)!)≤t−1, hence D≤E−1. Otherwise f=q and the length is ≤q+r, with equality only for q copies of s and r copies of 1. Its denominator is q!r!(p!)^q6^r with valuation E; Wilson's theorem gives the claimed sign and unit. Monicity of rising factorials, translation x↦x+1 and the p-unit 4^{−g} preserve sharpness. This includes r=0 and p=2g+1 and does not assume q! is a p-unit. An independent exact differential recurrence S A′+(x+1)S′A=0 in u=t² verified integrality, vanishing and the nonzero top residue on 153 prime/genus pairs, including 43 with p dividing q!.

## originality

FAIL

The exact degree and Wilson unit are not stated as such by Holmes, but are mechanical consequences of his explicit partition proof: its actual equations already bound the counts of large and small parts separately, isolate the same extremal term and rule out every t≥1 term. Simply retaining the length bound before specializing to j=m gives the cutoff; reducing the already isolated unit gives the residue.

## value

FAIL

Locating the largest Hodge index attaining the maximum denominator is a natural refinement, but on this scope it is already determined by the length inequalities and the sole extremal partition in the cited proof. Recording that immediate residue does not establish an independently unknown invariant, new valuation mechanism or classification below the cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
