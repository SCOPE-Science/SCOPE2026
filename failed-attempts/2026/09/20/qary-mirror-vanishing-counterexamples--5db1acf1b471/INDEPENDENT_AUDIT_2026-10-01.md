# Independent mathematical audit — SCOPE-20260920-5db1acf1b471

Final disposition: **FAILED**.

## Correctness
**PASS** — The projective-line multiset proof is correct. For a full-length \([2d+1,2,d]_q\) code, nonzero scalar classes correspond to points of \(\operatorname{PG}(1,q)\) and have weight \(2d+1-m(P)\). Minimum distance \(d\) forces a unique multiplicity \(d+1\); a full-weight word forces an empty point; the forbidden weights \(d+1,\ldots,d+t\) force every remaining multiplicity to be at most \(d-t\). The residual mass \(d\) must therefore fit on \(q-1\) points, giving \(d\le(q-1)(d-t)\). Conversely that capacity condition is sufficient by distributing the residual multiplicities. This proves the iff threshold.

## Originality
**FAIL** — The substantive counterexample half is already published in a September 18 record: for every \(q>2\) and \(d\ge2\) it constructs the same \([2d+1,2,d]_q\) family with the maximal gap \(t=d-\lceil d/(q-1)\rceil\), hence automatically supplies counterexamples for every smaller \(t\). The only additional half is necessity, but that is a direct capacity count in the classical projective-multiset model, where codeword weight is \(n\) minus hyperplane multiplicity. Under an implication-based originality bar, the final iff theorem is therefore a routine completion of already-published sufficiency using standard code geometry, not an original theorem.

### Equivalent formulations
The assigned sufficiency half is exactly covered; the necessity half becomes an elementary multiplicity-capacity statement in the standard geometric representation.

### Broader coverage
Combining these prior ingredients mechanically yields the full assigned iff threshold.

### Exact database or table
Exact wording `if and only if` is absent there, but special cases/corollaries count as coverage when the missing direction is a routine consequence of the standard representation.

### Claim versus prior implication
The final statement is mechanically implied by prior construction plus classical geometry.

## Value
**FAIL** — The sharp threshold is a clean summary, but after the earlier maximal-gap construction is known, the remaining impossibility direction is a one-line pigeonhole/capacity deduction from the textbook projective-line representation. It adds no nontrivial structural mechanism or motivated boundary beyond what the existing construction and standard model already make mechanically available.

## Source inspections
- **Nonbinary counterexamples to the literal mirror-vanishing extension** (https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-qary-counterexamples-mirror-vanishing--7d5d46a2a226): complete published RESULT.md Method: published-record full-text inspection. Assessment: COVERS_THE_ENTIRE_SUFFICIENCY_HALF. Evidence: It constructs \([2d+1,2,d]_q\) counterexamples for every \(q>2,d\ge2\) with \(t=d-\lceil d/(q-1)\rceil\), including the same smallest ternary example.
- **A Mirror Vanishing Band for Weight Distributions of Binary Linear Codes** (https://arxiv.org/abs/2609.20344): complete seven-page primary preprint Method: authorized full-text inspection after open full text was unavailable. Assessment: BINARY_SOURCE_AND_BOUNDARY_CONTEXT. Evidence: The paper proves the binary mirror band, explains reliance on binary disjoint-support decomposition, and states that a nonbinary version requires additional conditions.
- **On strongly walk regular graphs, triple sum sets and their codes** (https://doi.org/10.1007/s10623-022-01118-z): primary web text describing generator columns as projective-point multisets and codeword weight as the complement of hyperplane multiplicity Method: primary full-text web inspection. Assessment: STANDARD_GEOMETRIC_INPUT. Evidence: The exact weight-versus-hyperplane-multiplicity identity makes the assigned necessity direction a direct capacity count in dimension two.

## Checked sources
- https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-qary-counterexamples-mirror-vanishing--7d5d46a2a226
- https://arxiv.org/abs/2609.20344
- https://doi.org/10.1007/s10623-022-01118-z

## Residual risks
- No correctness defect is asserted; rejection is implication-based coverage and routine value.
- The recent binary source itself does not contain the sharp nonbinary threshold; the coverage comes from the earlier counterexample record plus classical code geometry.
