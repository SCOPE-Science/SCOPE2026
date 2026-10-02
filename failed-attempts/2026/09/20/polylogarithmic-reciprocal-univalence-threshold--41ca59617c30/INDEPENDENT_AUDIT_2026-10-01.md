# Independent mathematical audit — 2026-10-01

## Final claim assessed

An exact area-theorem Hilbert envelope lowers a polylogarithmic reciprocal univalence threshold

## Correctness — PASS

PASS. The multiplier criterion follows from Bieberbach's bound for the first reciprocal coefficient, the area theorem for the remaining reciprocal coefficients, and weighted Cauchy--Schwarz. The class-U functional identity gives the second square-summability condition. For the polylogarithmic multiplier, direct high-precision evaluation independently gives the unique root \(\sigma_*=1.413519504297085\ldots\), with the stated signs at \(1.413519\) and \(1.413520\). The saved script is consistent with this calculation but is not the proof.

## Originality — FAIL

FAIL. A distinct published 20 September 2026 record, 'A quantitative bracket for the polylogarithmic reciprocal-smoothing threshold', proves the same universal upper threshold \(s_*=1.41351950\ldots\) by retaining the exact area-theorem tail, and additionally proves the stronger lower bracket \(\tau_{\mathcal U}\ge1\). The two records were later reconciled into the public repository in the same commit and expose only the same calendar publication date, so sub-day priority cannot be independently established. Under the audit requirement to compare against published records and certify originality rather than assume it, the central threshold claim cannot pass originality.

### equivalent_formulations

Searches: Resultary semantic search: polylogarithmic reciprocal univalence threshold exact Hilbert envelope sigma 1.413519; published record SCOPE-polylog-reciprocal-u-threshold-bracket--9391b8ab7b89

Evidence: The complete comparison record states the identical numerical upper root and uses the same exact square-summable reciprocal tail.

Reasoning: The target conclusion is the same universal class-U tail bound, with the comparison record additionally supplying a lower bound.

### broader_coverage

Searches: Ali--Obradović--Ponnusamy 2013 Theorem 1.6 and Corollary 1.7; published 20 September quantitative bracket record

Evidence: The 2013 source proves only \(\sigma\ge3/2\); the distinct 2026 record improves it to the same root as the assigned finding.

Reasoning: The later published bracket directly dominates the assigned polylogarithmic corollary.

### exact_database_or_table

Searches: Published-record exact search for 1.4135195 polylogarithmic reciprocal smoothing

Evidence: The distinct 20 September record is an exact theorem-level match.

Reasoning: This is not a numerical-table issue; direct published theorem coverage is decisive.

### claim_vs_prior_implication

Searches: Complete RESULT.md of the distinct bracket record; 2013 primary full text

Evidence: The comparison record explicitly states \(1\le\tau_{\mathcal U}\le1.41351950\ldots\), while the assigned record's principal corollary is the same upper endpoint.

Reasoning: The central claim is already covered in the published corpus; unresolved sub-day ordering prevents a truthful originality certification.

## Scientific value — PASS

PASS. Lowering the published universal \(3/2\) bound for an explicit open problem and identifying the exact Hilbert-space envelope is mathematically worthwhile. The failure is originality certification, not mathematical usefulness.

## Source inspections

- **Necessary and sufficient conditions for univalent functions** — https://doi.org/10.1080/17476933.2011.599116. Material read: Primary full text through Theorem 1.6, Corollary 1.7, and the final open problem. Assessment: MOTIVATING_SOURCE_WITH_WEAKER_BOUND. Evidence: Corollary 1.7 gives the universal \(\sigma\ge3/2\) conclusion and the paper asks for the smallest parameter.
- **A quantitative bracket for the polylogarithmic reciprocal-smoothing threshold** — https://github.com/Resultary/2026/tree/main/2026/9/20/SCOPE-polylog-reciprocal-u-threshold-bracket--9391b8ab7b89. Material read: Complete published RESULT.md and metadata. Assessment: DECISIVE_OVERLAPPING_PUBLISHED_COVERAGE. Evidence: It proves the same \(1.41351950\ldots\) upper threshold and a stronger lower bracket.

## Limitations and residual risks

The calculation is correct, but the target polylogarithmic upper threshold is already present in a distinct published record from the same date. The available repository metadata do not resolve sub-day priority. The exact universal tail threshold remains open.

- The public records expose only a calendar publication date and were reconciled in the same later repository commit, so fine-grained priority between the two 20 September findings cannot be recovered. This uncertainty is the reason originality is not certified rather than a claim of proven copying.

## Disposition

**failed**
