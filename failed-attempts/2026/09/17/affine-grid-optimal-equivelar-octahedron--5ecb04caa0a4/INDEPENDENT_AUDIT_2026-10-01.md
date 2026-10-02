# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260917-5ecb04caa0a4`

## Correctness — PASS

The affine-radius theorem is correct for the stated affine orbit. The complete verifier was inspected and independently reimplemented: the displayed affine map sends all 24 vertices to integer points with coordinate ranges 156, 168, 168; the transformed difference lattice has index one; and among the 74 nonzero integer covectors forced by the width-167 inverse-matrix bound, only the two signed first-coordinate covectors have width at most 167. Hence three independent output rows cannot all have width below 168, while the displayed image attains radius 84.

### Sources
- artifacts/verify_affine_grid.py
- artifacts/VERIFICATION.txt
- independent exact-rational enumeration

### Risks
- The theorem is only about affine-integer images of Mizhaev's concrete realization, not all realizations of the abstract surface.

## Originality — FAIL

A later published record gives the same sharp affine-integer radius 84 for exactly Mizhaev's 24-vertex realization and proves the same full affine-orbit lower bound; it additionally proves a symmetry-preserving optimum. Under the current-coverage audit rule this is decisive coverage of the audited claim. The later publication date means this finding does not by itself decide historical priority of the September 17 record.

### equivalent_formulations

Searches:
- affine integer realization genus 3 equivelar octahedron radius 84
- Mizhaev affine grid radius 84

Evidence:
- A September 18 published record states the same theorem: the minimum affine-integer grid radius of the same vertex set is 84.

Reasoning:
The objects, admissible affine maps, integrality condition, and optimum coincide; different optimal affine maps do not make the theorem different.

### broader_coverage

Searches:
- affine-lattice box optimality Mizhaev genus 3 octahedron

Evidence:
- A September 19 record gives additional affine-lattice width and box-profile results for a normalized copy of the same realization.

Reasoning:
The September 18 theorem already covers the exact claim; the September 19 result is further surrounding coverage.

### exact_database_or_table

Searches:
- published record table for optimal affine grid radius

Evidence:
- The exact value 84 and lower-bound certificate are explicitly stated in the later published result.

Reasoning:
This is exact theorem coverage, stronger than mere presence in a numerical table.

### claim_vs_prior_implication

Searches:
- claim comparison to later optimal affine grid radius theorem

Evidence:
- The later theorem has the same minimization domain and conclusion and therefore directly implies the audited statement.

Reasoning:
No additional hypothesis is needed to derive the audited claim from the later published theorem.

### source_inspections

- **Optimal affine integer grid radius for Mizhaev's genus-three equivelar octahedron** — https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-optimal-affine-grid-radius-equivelar-octahedron--6a52f1a9c045. Trigger: Highest-similarity published result for the same object and invariant. Material read: Complete published RESULT.md. Method: Direct theorem/hypothesis/implication comparison. Assessment: DECISIVE CURRENT COVERAGE: Theorem 1 is the same radius-84 affine-integer optimization and also proves a separate radius-90 symmetry-preserving theorem. Evidence: It states min R(F)=84 over invertible affine maps sending the same 24 vertices to integer points.
- **Integer Realization of an Equivelar Octahedron of Genus 3** — https://arxiv.org/abs/2609.17700. Trigger: Primary source of the vertex realization. Material read: Primary abstract and scope. Method: Object-identification comparison. Assessment: Supplies the same 24-vertex integer surface, but not the affine optimum in the inspected abstract. Evidence: The paper provides the integer realization, face data, exact verification, and symmetry.
- **Assigned affine verifier** — artifacts/verify_affine_grid.py. Trigger: Critical correctness certificate. Material read: Complete source and recorded output. Method: Source inspection plus independent exact enumeration. Assessment: Confirms the audited numerical theorem despite the originality failure. Evidence: Index one and the complete small-covector list reproduce exactly.

### checked_sources

- published September 18 radius-84 result
- published September 19 affine-lattice box result
- arXiv:2609.17700
- assigned verifier
- Resultary semantic search

### residual_risks

- The coverage source postdates the audited September 17 publication, so historical-priority claims require separate chronology-sensitive treatment.

## Scientific value — PASS

Independently of present-day coverage, a sharp affine-integer coordinate optimum for a concrete new genus-three polyhedral realization is a natural geometric/lattice invariant with a compact reusable certificate. The scientific rejection here is originality-only.

### Sources
- Mizhaev integer realization
- assigned lattice-width certificate

### Risks
- The optimum is affine-orbit specific and does not solve global coordinate minimality for the combinatorial type.

## Limitations

- Rejected because current published coverage is exact; correctness is not in doubt.
- The later covering record postdates the audited record, so this audit does not assert that it had historical priority.
- The affine optimum does not apply to non-affinely-equivalent realizations.

## Disposition

**FAILED**
