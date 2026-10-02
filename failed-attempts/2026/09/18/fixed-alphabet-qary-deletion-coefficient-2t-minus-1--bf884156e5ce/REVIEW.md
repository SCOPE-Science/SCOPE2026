# Review status

Fresh independent audit: **FAILED**.

Independent audit failed on originality and value. The theorem is correct, but an earlier SCOPE record already states the same fixed-alphabet q-ary deletion bound.

- Correctness: **PASS** — The q-ary extension argument is mathematically coherent, and the local finite verification was rerun independently during this audit. It reproduced 42 overlapping-window probability cases, 2,783,928 q-ary local-bubble cases, and 32,642,112 offset comparisons. The exhaustive local check establishes only the q-ary bubble/probability lemmas; the all-\(n\) code bound rests on the analytic adaptation of the hashing, exceptional-alignment, witness, and bipartition arguments. Those adaptations change only fixed alphabet-dependent constants for fixed \(q,t\), yielding the stated \((2t-1)\log_q n+O_{q,t}(\log\log n)\) upper bound.
- Originality: **FAIL** — The exact theorem is already present in an earlier SCOPE record, `fixed-qary-deletion-codes-2t-minus-1--0b8ba422fcea`, whose RESULT states the same fixed-\(q\), fixed-\(t\) coefficient \(2t-1\). The current record itself acknowledges that earlier provenance. Under the required implication/duplicate standard, a separately written corroborating derivation is not an original second discovery of the theorem.
- Scientific value: **FAIL** — The theorem itself is mathematically valuable, but this later record does not fill a new mathematical gap: it reproduces an already-published SCOPE theorem. A corroborating derivation and finite local checker are useful evidence, yet correctness and reproducibility alone do not satisfy the research-value axis for a duplicate finding.

Full evidence, source comparisons, limitations, and residual risks are recorded in `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.

The historical same-model assessment remains preserved in `AUDIT.json` and is not treated as independent validation.
