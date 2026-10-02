# Independent mathematical audit — 2026-09-30

## Outcome

**FAILED** for the final finding as stated.

## Correctness — UNRESOLVED

The committed data and logs are internally consistent, and an independent high-precision reconstruction from the five cubic defining polynomials reproduced all first-2000 quotient tallies, maxima \(B\), and the reported minimum-\(\theta\) indices/values; the four quadratic periodic rows also agree with their exact classical periods. However, the RESULT claims exact Sturm-chain certification of every accepted digit and theta bracket, while the referenced generator/checker source files `poly_cf.py`, `verify_poly.py`, and `qquad.py` are absent from the assigned Git tree. The surviving `VERIFY_OK` log is not a substitute for inspecting and replaying that exact certificate. Thus the numerical table is strongly corroborated but the full exact-certification claim cannot be independently closed from the actual package.

Checked sources:
- committed `artifacts/table.json`, `artifacts/quads.json`, `artifacts/verify.log`, `artifacts/poly_cf.log`; independent 4000-digit continued-fraction reconstruction

Residual risks:
- The exact verifier/generator sources named in RESULT are missing from the assigned tree.
- High-precision agreement alone is not an exact proof that no quotient boundary was crossed or that every stored theta interval is rigorous.

## Originality — PASS

The inspected literature discusses statistical behavior of continued fractions of algebraic numbers and prior finite experiments, but no exact nine-number \(N=2000\) table with this combination of quotient counts, \(\chi^2\), theta minima and the stated finite extremal was found. This is only best-of-knowledge originality.

### equivalent_formulations

Searches: Resultary semantic search for the nine-number Gauss–Kuzmin/theta table; Sibbertsen–Lampert–Müller–Taktikos, arXiv:2208.14359

Evidence: The exact record was the only matching published-result hit. The paper surveys and performs finite distribution tests for algebraic numbers, but not the same committed nine-number table.

Reasoning: Equivalent formulations as empirical continued-fraction digit-distribution tests and convergent approximation-constant tables were checked; no exact equivalent table was found.

### broader_coverage

Searches: arXiv:2208.14359 full text; OEIS A002945 and A072117 cited by the record

Evidence: The literature gives broader statistical framing and some pre-existing quotient prefixes, especially for \(\sqrt[3]{2}\) and the plastic constant.

Reasoning: Broader experiments cover related algebraic numbers and sample sizes, but the inspected statements do not imply the exact combined table or all stored theta minima.

### exact_database_or_table

Searches: OEIS searches/prefix references for \(\sqrt[3]{2}\) and plastic constant; Resultary exact-table search

Evidence: Some quotient prefixes are already databased; no inspected database contains the entire nine-row derived-statistics table.

Reasoning: The prefix component is partly known, while the combined finite statistics were not located as a pre-existing exact database row.

### claim_vs_prior_implication

Searches: Comparison with metric Gauss–Kuzmin/Khinchin statements and finite empirical studies

Evidence: Metric theorems concern almost-everywhere asymptotics and do not determine the first 2000 digits of named cubics.

Reasoning: The finite table is not a corollary of Gauss–Kuzmin or Khinchin theory for generic reals.

### source_inspections

- **Do algebraic numbers follow Khinchin’s Law?** (https://arxiv.org/abs/2208.14359): trigger=Same question of finite continued-fraction digit distributions for algebraic numbers.; material read=Accessible full arXiv HTML including literature discussion, finite-algebraic experiments and Gauss–Kuzmin setup.; method=Primary full-text inspection.; assessment=RELATED, PARTIALLY OVERLAPPING EXPERIMENTAL THEME, NOT THE SAME TABLE.; evidence=The paper discusses earlier chi-square tests and finite samples for algebraic numbers, including cubics, but the audited nine-number certified table was not found.
- **OEIS A002945** (https://oeis.org/A002945): trigger=Pre-existing continued-fraction data for \(\sqrt[3]{2}\).; material read=Sequence identification as cited in the record.; method=Database comparison.; assessment=PARTIAL COVERAGE.; evidence=A prefix of the quotient sequence is pre-existing; this does not by itself supply the audited GK/theta statistics.
- **Committed table and logs** (artifacts/table.json; artifacts/quads.json; artifacts/verify.log; artifacts/poly_cf.log): trigger=Actual package evidence.; material read=Complete small logs/quadratic table and the available committed table material; referenced source scripts were absent.; method=Package inspection plus independent numerical reconstruction.; assessment=Strong numerical corroboration with a reproducibility gap.; evidence=Independent reconstruction reproduced the five cubic summary statistics, but the exact symbolic verifier could not be read or replayed.

### checked_sources

- arXiv:2208.14359
- OEIS A002945
- OEIS A072117
- Resultary semantic search
- actual committed data/logs

### residual_risks

- Finite continued-fraction computations are widespread and grey-literature overlap is plausible.
- The missing exact checker source prevents a stronger correctness audit but does not itself prove prior coverage.

## Scientific value — FAIL

The final object is a hand-picked nine-number, fixed-\(N=2000\) table of directly computable continued-fraction statistics. The quadratic rows and the \(\varphi\) minimum-\(B\) extremal are classical or predetermined, while the cubic rows are raw finite samples whose exact cutoff is not independently motivated. The record does not establish a structural boundary, natural complete classification, or a precise finite invariant with a demonstrated future mathematical need. Under the required value bar this is an arbitrary finite slice rather than a substantive gap.

Checked sources:
- arXiv:2208.14359; OEIS prefix records; audited RESULT

Residual risks:
- A differently motivated use of the raw cubic data could be worthwhile, but that motivation is not part of the final claim being audited.

## Limitations

- Exact symbolic certification is unresolved because the source scripts named in RESULT are absent from the assigned Git tree.
- Independent high-precision computation strongly corroborates the numerical rows but is not promoted to an exact certificate.
- Scientific rejection rests independently on the value axis; the missing-source defect is not being mislabeled as a scientific falsehood.
