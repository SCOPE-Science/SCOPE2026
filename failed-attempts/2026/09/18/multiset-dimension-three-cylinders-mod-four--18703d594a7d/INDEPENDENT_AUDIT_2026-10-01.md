# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260918-18703d594a7d`

## Correctness — PASS

The piecewise cycle-distance calculation gives the stated normalized-code collision families and translation separations. The vertical-lift lemma is exact: adding the path coordinate shifts all three sorted distances equally, so a repeated cycle gap code can collide between layers exactly when the translation difference is at most \(m-1\). Maximizing the antipodal-family separation gives \(\lfloor L/3\rfloor\), and \(L\ge3m\) yields a three-landmark resolving set. The 2025 primary paper independently supplies the standard lower facts that no connected graph has multiset dimension two and that dimension one characterizes paths. The package checker is finite corroboration only.

### Correctness sources

- assigned RESULT.md and artifacts/check.py
- Marcelo–Tolentino–Garciano–Buot 2025 full PDF

### Correctness risks

- The sharp capacity statement is only for the antipodal boundary family.

## Originality — FAIL

A later published SCOPE theorem strictly covers the entire audited congruence family. It proves \(\operatorname{md}(P_m\square C_n)=3\) for all \(n\ge6m+3\), plus boundary cases \(n=6m+2\) when \(m\) is even and \(n=6m\) when \(m\) is odd. For \(n\equiv2\pmod4\) and \(n\ge6m\), these cases exhaust the audited range: if \(m\) is even the first allowed circumference is \(6m+2\), while if \(m\) is odd the first is \(6m\); every later congruent value is at least \(6m+3\).

### equivalent_formulations

Searches:
- Resultary query for cylindrical multiset dimension six times height
- full comparison with the 2026-09-19 q-separated three-point theorem

Evidence:
- The later theorem states the uniform tail and the two boundary families needed to cover every audited congruence case.

Reasoning:
The later theorem uses a more general q-separated lifting mechanism; the audited antipodal construction is a special covered range.

### broader_coverage

Searches:
- 2026-09-19 SCOPE cylinder theorem
- Marcelo et al. 2025 full article

Evidence:
- The later theorem improves the old \(8m+1\) range to a substantially broader six-times-height region.

Reasoning:
It strictly dominates the audited single congruence class.

### exact_database_or_table

Searches:
- Resultary exact/semantic searches
- 2025 cylindrical graph paper

Evidence:
- No table lookup is needed after locating a theorem that covers every parameter pair in the audited claim.

Reasoning:
The decisive comparison is theorem implication, not an exact database row.

### claim_vs_prior_implication

Searches:
- parity and congruence implication check

Evidence:
- For even \(m\), \(6m\equiv0\pmod4\), so the first \(2\pmod4\) value is \(6m+2\); for odd \(m\), \(6m\equiv2\pmod4\). Remaining values differ by four and lie in the later theorem's uniform tail.

Reasoning:
Thus the entire audited range is a corollary of the later theorem.

### source_inspections
- **Three-point multiset bases for cylindrical grids at circumference six times the height** — https://github.com/Resultary/2026/tree/main/2026/9/19/SCOPE-multiset-dimension-cylinders-six-times-height--fb793a108374. Trigger: Highest-overlap Resultary theorem. Material read: Complete RESULT.md including q-separated lifting lemma, residue constructions, boundary cases and proof. Method: Full parameter implication comparison. Assessment: DECISIVE CURRENT COVERAGE of every audited \(n\equiv2\pmod4\), \(n\ge6m\) case. Evidence: Its tail \(n\ge6m+3\) plus parity boundary cases cover the congruence family exactly.
- **On multiset dimension of cylindrical graphs** — https://doi.org/10.61091/jcmcc126-15. Trigger: Primary pre-existing cylinder theorem. Material read: Full open-access PDF, including abstract, foundational propositions and main-result setup; page image was also inspected. Method: Primary full-text comparison. Assessment: Prior 2025 coverage reaches \(n\ge8m+1\) and leaves the lower range open; it does not itself cover the audited theorem. Evidence: The abstract states the \(8m+1\) sufficient range and the foundational lower-bound facts appear in Section 1.

### checked_sources

- later 2026-09-19 published SCOPE cylinder theorem
- Marcelo et al. 2025 DOI 10.61091/jcmcc126-15
- assigned RESULT.md and artifacts/check.py
- Resultary semantic search

### residual_risks

- The covering theorem postdates the audited record, so historical priority is not decided.

## Scientific value — PASS

The congruence-class theorem is a mathematically useful sharp structural improvement over the original \(8m+1\) range, with an exact collision-capacity mechanism. Current coverage defeats originality but not intrinsic value.

### Value sources

- Marcelo et al. 2025
- later q-separated cylinder theorem

### Value risks

- Value cannot rescue a currently covered claim.

## Limitations

- Scientific rejection is originality-only; correctness and value pass.
- The decisive covering record was published one day later, so this audit does not adjudicate historical priority.
- The coefficient six is sharp only for the audited landmark family, not globally.

## Disposition

**FAILED**
