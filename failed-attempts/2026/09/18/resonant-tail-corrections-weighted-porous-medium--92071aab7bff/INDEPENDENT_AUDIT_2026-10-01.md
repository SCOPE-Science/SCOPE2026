# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260918-92071aab7bff`

## Correctness — PASS

The second-order trichotomy is mathematically coherent. In logarithmic radius, the exact relative-error equation linearizes to \(etaarepsilon_t+arepsilon=A_0e^{-rt}\) plus lower-order terms, with forced rate \(r=D/(p-1)\) and homogeneous rate \(h=1/eta=D/(m-p)\). Their crossing is exactly \(m=2p-1\); variation of constants yields the universal forced power below, a resonant logarithm at equality, and a profile-dependent homogeneous mode above. The radial-Laplacian factor \(s(s-N+2)\) explains the independent harmonic cancellation. The assigned symbolic verifier checks these identities, and a later published full proof independently supplies the required stable-manifold remainder control.

### Correctness sources

- assigned RESULT.md
- artifacts/verify_tail_resonance.py
- current published full proof SCOPE-far-field-resonance-weighted-porous-medium--7d98f252f0ca

### Correctness risks

- The conclusion depends on the source paper's far-field stable-manifold description.
- Exceptional vanishing homogeneous coefficients require higher-order analysis.

## Originality — FAIL

Current published coverage is decisive. A later published finding dated 2026-09-19 gives the same weighted porous-medium far-field theorem with the same threshold \(m=2p-1\), the same universal/profile-dependent trichotomy, the same resonant logarithm, and the same harmonic surface \(m\sigma/(p-1)=N-2\); it additionally supplies a fuller proof and identifies the exact singular harmonic profile. Under the required current-coverage rule, the audited final claim is therefore covered. Because the covering result postdates this 2026-09-18 record, this audit does not determine historical first-discovery priority.

### equivalent_formulations

Searches:
- Resultary: porous medium weighted absorption second-order tail resonance m 2p minus 1 universal correction

Evidence:
- The 2026-09-19 finding is an exact theorem-level semantic match.

Reasoning:
The later notation swaps labels for the leading-tail exponent and correction rate, but after translation the formulas, parameter surfaces and implications coincide.

### broader_coverage

Searches:
- current published far-field-resonance theorem
- Iagar–Munteanu arXiv:2609.20397

Evidence:
- The later theorem strictly contains the audited trichotomy and also proves an exact singular profile on the harmonic surface.

Reasoning:
This is direct broader coverage, not merely shared methodology.

### exact_database_or_table

Searches:
- current Resultary porous-medium records

Evidence:
- No table comparison is needed because exact theorem-level coverage exists.

Reasoning:
The database/table check is inapplicable once a full published theorem duplicates the claim.

### claim_vs_prior_implication

Searches:
- statement-by-statement implication comparison with the 2026-09-19 result

Evidence:
- Both have the same forced coefficient below \(2p-1\), logarithmic coefficient at equality, free homogeneous mode above, and vanishing forcing on the radial-harmonic surface.

Reasoning:
Every originality-bearing scientific assertion in the audited statement is implied by the later theorem.

### source_inspections
- **Far-field resonance in dominating weighted porous-medium absorption** — https://github.com/Resultary/2026/tree/main/2026/9/19/SCOPE-far-field-resonance-weighted-porous-medium--7d98f252f0ca. Trigger: Exact current semantic match. Material read: Complete published RESULT.md, including proof and limitations. Method: Full statement-and-proof implication comparison. Assessment: DECISIVE CURRENT COVERAGE. Evidence: The theorem gives the identical \(m=2p-1\) trichotomy and harmonic cancellation, with stronger exact information on the cancellation surface.
- **A porous medium equation with dominating weighted absorption: three types of self-similar solutions** — https://arxiv.org/abs/2609.20397. Trigger: Primary source for the universal leading tail and stable manifold. Material read: Accessible abstract/metadata; full arXiv/OA text was not obtainable in this run and the authorized route was unavailable. Method: Background-scope comparison only. Assessment: Background source; originality failure does not depend on excluding it because current exact coverage is already decisive. Evidence: It establishes the leading-tail setting refined by both records.
- **Assigned resonance verifier** — artifacts/verify_tail_resonance.py. Trigger: Algebraic identities. Material read: Complete source file. Method: Line-by-line symbolic inspection and independent algebra. Assessment: Supports correctness but cannot restore originality. Evidence: It verifies the rate crossing, denominator identity and radial-curvature coefficient.

### checked_sources

- https://github.com/Resultary/2026/tree/main/2026/9/19/SCOPE-far-field-resonance-weighted-porous-medium--7d98f252f0ca
- https://arxiv.org/abs/2609.20397
- artifacts/verify_tail_resonance.py

### residual_risks

- The covering publication is later than the audited record; current coverage does not settle historical priority.

## Scientific value — PASS

The theorem identifies a natural second-order phase boundary in a family whose leading tail is universal, and distinguishes a genuine resonance from an independent geometric cancellation. It remains mathematically worthwhile even though it is now covered.

### Value sources

- current full far-field resonance theorem
- source universal-tail problem

### Value risks

- Scientific rejection is solely originality-based.

## Limitations

- Correctness and scientific value pass; current originality fails decisively.
- The exact covering publication is dated one day later, so historical priority is not adjudicated.
- The theorem concerns bounded radial similarity profiles, not general large-time PDE convergence.

## Disposition

**FAILED**
