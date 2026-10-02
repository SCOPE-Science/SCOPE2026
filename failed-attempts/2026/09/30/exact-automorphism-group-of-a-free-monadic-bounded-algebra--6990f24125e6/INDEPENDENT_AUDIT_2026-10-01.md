# Mathematical audit — 2026-10-01

Record: `SCOPE-20260930-6990f24125e6`

## Correctness — PASS

Akishev and Goldblatt's finite graph model gives one block \(G_J\) for every subset \(J\) of an \(m\)-set, with \(m\) unmarked vertices, \(|J|\) marked vertices, and common successor set exactly the marked vertices. Boolean-algebra automorphisms permute atoms and preservation of the distinguished set and existential operator recovers precisely marked directed-graph automorphisms. Blocks can mix exactly when \(|J|\) agrees; a block with \(|J|=k\) has internal group \(S_m\times S_k\), and arbitrary permutation of the \(\binom{m}{k}\) isomorphic blocks gives the stated wreath product. The exact order follows. Stirling applied to the three logarithmic sums gives the claimed leading expansion. The package verifier correctly brute-forces rank one and checks small exact orders.

### Correctness sources

- Akishev–Goldblatt, Monadic Bounded Algebras, Section 8 full primary text
- assigned RESULT.md
- artifacts/verify.py and verify_output.txt

### Correctness risks

- The asymptotic is only to error \(O(2^m\log m)\).

## Originality — FAIL

The exact group decomposition is mechanically implied by the published Section 8 graph decomposition together with the standard automorphism theorem for a disjoint union of isomorphic connected relational blocks: each multiplicity class contributes a wreath product of the block automorphism group with the symmetric group on the copies. Akishev and Goldblatt explicitly provide all data needed to identify the block automorphism group as \(S_m\times S_k\) and the multiplicity as \(\binom{m}{k}\). The order formula is immediate multiplication, and the displayed asymptotic is routine Stirling/entropy bookkeeping. Under the required implication-based originality bar, absence of the formula verbatim from the source does not preserve originality.

### equivalent_formulations

Searches:
- Resultary: free monadic bounded algebra automorphism group wreath product Akishev Goldblatt
- Akishev–Goldblatt Section 8 free-algebra graph construction
- web searches for automorphism group of the free monadic bounded algebra

Evidence:
- Resultary returns only the audited formula as an exact textual match.
- The primary source already decomposes the free graph into all blocks \(G_J\) with the exact marked/unmarked structure and common successor sets.

Reasoning:
The relevant equivalent formulation is the automorphism group of a disjoint union of relational blocks, for which the wreath-product decomposition is standard.

### broader_coverage

Searches:
- Akishev–Goldblatt full Section 8
- standard automorphisms of disjoint unions of isomorphic structures

Evidence:
- The source supplies the complete component isomorphism types and multiplicities.
- General disjoint-union automorphism theory strictly covers the group-decomposition step.

Reasoning:
No additional nonstandard algebraic theorem is needed once the published representation is read.

### exact_database_or_table

Searches:
- current Resultary algebra/automorphism findings

Evidence:
- No finite table is relevant; theorem-level implication already settles coverage.

Reasoning:
The exact orders at small rank are consequences of the general group formula rather than independent database values.

### claim_vs_prior_implication

Searches:
- claim versus published graph construction plus standard wreath-product theorem

Evidence:
- For each \(k\), there are \(\binom{m}{k}\) mutually isomorphic blocks, each with free permutations of its \(m\) unmarked and \(k\) marked vertices; this is exactly \((S_m\times S_k)\wr S_{\binom{m}{k}}\).

Reasoning:
The final claim is a direct standard corollary, even though Akishev and Goldblatt did not print it.

### source_inspections

- **Monadic Bounded Algebras** — https://homepages.ecs.vuw.ac.nz/~rob/papers/mba.pdf. Trigger: Primary construction of the free finite algebra. Material read: Relevant full Section 8 and the pages defining \(G_J\), the disjoint union \(G_r\), and the complex-algebra representation. Method: Primary full-text structural comparison. Assessment: DECISIVE COVERING INGREDIENT. Evidence: The source explicitly specifies the block vertex sets, marked points, successor sets, all subset-indexed blocks, and the disjoint-union free representation.
- **Assigned small-rank verifier** — artifacts/verify.py. Trigger: Exact order formula sanity check. Material read: Complete source and output. Method: Line-by-line inspection. Assessment: Correct corroboration only. Evidence: The brute-force rank-one automorphism count is 64 and agrees with the formula.

### checked_sources

- Akishev–Goldblatt Section 8 full text
- standard disjoint-union automorphism/wreath-product theorem
- current Resultary semantic search
- assigned RESULT.md

### residual_risks

- No claim is made that the exact group formula was previously printed verbatim; the failure is implication-based.

## Scientific value — FAIL

The automorphism group of a free algebra is a natural invariant, but here its exact answer is mechanically determined by the published explicit component decomposition and a textbook wreath-product rule. The order formula and first asymptotic then require only routine multiplication and Stirling expansion. That falls below the required value bar for a new finding.

### Value sources

- published free-graph decomposition
- standard wreath-product automorphism rule

### Value risks

- Failure of value is not a correctness defect.

## Limitations

- Correctness passes.
- Originality and scientific value fail because the result is a standard corollary of the published block model.
- No historical-priority claim is made about whether anyone previously wrote the formula explicitly.

## Disposition

**FAILED**
