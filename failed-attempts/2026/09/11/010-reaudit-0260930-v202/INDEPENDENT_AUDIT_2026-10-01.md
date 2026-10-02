# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260911-010`

## Correctness — PASS

Within the record's explicit hypotheses, the stated degree inequalities are correct. The actual `artifacts/verify_cell.py` was read completely and its integer enumeration matches the Donaldson-basis cell bookkeeping. Once every cycle component is invariant and a positive closed current has generic Lelong number at least one along each component, Siu decomposition gives degree at least the sum of the component volumes. Camacho–Sad then supplies the listed componentwise self-intersection sum. The record also explicitly distinguishes the alternative total-square convention; the verifier checks that alternate convention in its sample gap section.

## Originality — FAIL

The central degree obstruction is mechanically implied by standard ingredients once the record assumes a directed positive closed current with Lelong number at least one along every cycle component: Siu decomposition immediately yields the positive degree lower bound, and Camacho–Sad converts invariant-curve indices into self-intersections. The remaining \(b_2=2\) class enumeration is finite bookkeeping. No new theorem is needed to obtain the advertised positive gap under those hypotheses.

### equivalent_formulations

Searches: class VII b2=2 Teleman cycle Gauduchon directed current Camacho Sad degree obstruction; equivalent Siu decomposition positive current degree formulation

Evidence: The semantic search found the audited record but no separate exact statement; the mathematical reformulation reduces directly to standard Siu decomposition plus Camacho–Sad.

Reasoning: Changing notation from degree minus Camacho–Sad sum to an explicit gap does not change the implication.

### broader_coverage

Searches: Kurnosov–Spicer 2026 class VII foliations; standard Siu decomposition and Camacho–Sad index theorem

Evidence: The cited recent class-VII paper supplies related foliation lemmas; the positivity step itself is a standard general theorem about positive currents.

Reasoning: The broader standard results already imply the degree inequality for any such invariant cycle, making the fixed cell a specialization.

### exact_database_or_table

Searches: fixed b2=2 Donaldson class enumeration

Evidence: No external exact table is required: the two-coordinate integer constraints are directly enumerable and are reproduced by the package script.

Reasoning: This check is genuinely inapplicable as a novelty source because the headline obstruction follows from general theorems rather than a hidden database.

### claim_vs_prior_implication

Searches: implication from Siu decomposition plus Camacho–Sad

Evidence: Under generic Lelong number at least one, the cycle contribution alone has degree at least its total Gauduchon volume; the residual current is nonnegative.

Reasoning: This directly implies positive degree and excludes a negative transfer identity, so the headline obstruction is a corollary of the assumed setup.

### source_inspections
- **Assigned cell verifier** — artifacts/verify_cell.py. Trigger: Finite Donaldson-basis and gap bookkeeping. Material read: Complete source file. Method: Line-by-line inspection of integer enumeration and the symbolic degree-gap cases. Assessment: Supports correctness of the finite cell bookkeeping but shows the gap step is elementary once assumptions are fixed. Evidence: The script enumerates the cell classes exactly and then checks only the algebraic gap identities.
- **Class VII surfaces with b2=3 and two foliations are Kato** — https://arxiv.org/abs/2608.29047. Trigger: Closest recent source cited for foliation numerics. Material read: Accessible abstract/html search material and cited-lemma context. Method: Primary-source comparison. Assessment: Related class-VII machinery, but not needed to establish novelty of the final positivity deduction. Evidence: The final degree lower bound comes from the record's strong current/Lelong assumptions plus standard positivity.

### checked_sources

- assigned RESULT.md and artifacts/verify_cell.py
- arXiv:2608.29047
- standard Siu decomposition
- Camacho–Sad index theorem
- Resultary semantic search

### residual_risks

- The audit does not claim the surrounding class-VII shell problem is routine; it assesses only the narrow final claim under its stated assumptions.
- The result uses two Camacho–Sad aggregation conventions; the primary componentwise convention and alternate total-square convention must not be conflated.

## Scientific value — FAIL

The shell problem is important, but the audited final claim imposes assumptions strong enough that the advertised obstruction is essentially the immediate positivity of the cycle contribution. The finite \(b_2=2\) bookkeeping does not turn that routine deduction into an independently valuable new invariant or boundary theorem under the required value bar.

## Limitations

- The rejection concerns the narrow final obstruction under its stated Lelong/current hypotheses, not the broader global spherical shell problem.
- The verifier's sample gap uses the total-square convention for the two-component case, while RESULT separately states the componentwise sum convention.
- The record's reproducibility path names `output/artifacts/verify_cell.py`; the actual package path is `artifacts/verify_cell.py`.

## Disposition

**FAILED — not a validated finding.**
