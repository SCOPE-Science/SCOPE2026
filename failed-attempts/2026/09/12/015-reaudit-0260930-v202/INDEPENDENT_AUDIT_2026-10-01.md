---
{"schema_version":1,"audit_date_utc":"2026-10-01","status":"failed"}
---

# Independent mathematical audit

## Final claim

For the stated nine-dimensional gentle algebra arising from the chosen once-punctured-torus cut in characteristic zero, the first Hochschild cohomology has dimension two and the second vanishes; consequently the mixed Gerstenhaber action into the second group is identically zero.

## Correctness — PASS

The algebra basis and multiplication were reconstructed from the quiver and relations. The actual exact-rational verifier checks associativity, d squared equals zero, rank two for the degree-zero coboundary, rank eight for the next map, and an independent Bardzell-resolution cross-check. Hence the first Hochschild cohomology has dimension two and the second is zero; the stated mixed bracket target is therefore zero.

Checked sources: artifacts/verify.py (blob d3aa9da2bd22dd0f3f39a79850abe27d7e49c8ef)

Residual risks: The calculation is characteristic-zero and tied to the specific admissible cut.

## Originality — FAIL

Ladkani gives a general combinatorial formula for the Hochschild cohomology dimensions of gentle algebras in terms of the Avella-Alaminos-Geiss invariant. The audited algebra is a small gentle algebra, so its low-degree dimensions are a direct instance of that published theorem. Once the second group vanishes, the claimed mixed bracket vanishing is tautological and adds no separate originality.

### Equivalent formulations

The package bar-complex computation is another way to evaluate a known invariant formula for this algebra. Evidence: Ladkani formulates the dimensions of all Hochschild cohomology groups of a gentle algebra from a complete combinatorial invariant.

### Broader coverage

The final dimensional statement is a special case of a much broader theorem. Evidence: The published formula applies to every gentle algebra and hence strictly contains this nine-dimensional example.

### Exact database or table

Instance-level exact dimensions do not establish originality when a general formula already determines them. Evidence: No exact external table for this named cut is required because theorem-level coverage is decisive.

### Claim versus prior implication

The prior result mechanically implies the low-degree dimensions after routine combinatorial evaluation; the bracket statement then follows from the zero target. Evidence: The quiver with relations determines the gentle combinatorics, and the general theorem determines the Hochschild dimensions.

### Source inspections

- **Hochschild cohomology of gentle algebras** — https://arxiv.org/abs/1208.2230. Trigger: Exact object class and invariant. Material read: Main theorem/corollary giving Hochschild-cohomology dimensions from the Avella-Alaminos-Geiss invariant, including surface-gentle consequences. Method: Primary full-text inspection. Assessment: COVERING. Evidence: The theorem determines the audited low-degree groups for any gentle algebra, including this one.
- **Gerstenhaber structure on Hochschild cohomology of gentle algebras** — https://arxiv.org/abs/2311.08003. Trigger: Same algebra class and bracket structure. Material read: Scope and structural results for Gerstenhaber operations on gentle algebras. Method: Primary literature inspection. Assessment: BROADER_CONTEXT. Evidence: The literature treats nontrivial bracket structure generally; in the audited example the target group already vanishes.

Checked sources: https://arxiv.org/abs/1208.2230; https://arxiv.org/abs/2311.08003

Residual risks: No claim is made that every presentation-equivalent surface algebra has the same dimensions without checking the gentle invariant; the audited algebra itself is covered.

## Scientific value — FAIL

The low-degree dimensions are a routine finite evaluation of a known general gentle-algebra formula, and the advertised bracket rigidity is vacuous because the target Hochschild group is zero. This does not clear the value bar without an additional nontrivial bracket, deformation consequence, or structural boundary.

Checked sources: Ladkani general formula; package Bardzell/bar calculation

Residual risks: A comparison across non-equivalent cuts or a nonzero higher operation could be valuable, but neither is part of the audited final claim.

## Disposition

FAILED. Acceptance requires PASS on correctness, originality, and scientific value.
