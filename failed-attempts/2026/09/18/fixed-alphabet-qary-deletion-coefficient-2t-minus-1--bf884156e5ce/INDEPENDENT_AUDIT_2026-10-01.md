    # Independent mathematical audit — 2026-10-01

    ## Record

    **Corroborating derivation of the fixed-alphabet q-ary deletion coefficient 2t-1**

    Disposition: **FAILED**.

    ## Correctness — PASS

    The q-ary extension argument is mathematically coherent, and the local finite verification was rerun independently during this audit. It reproduced 42 overlapping-window probability cases, 2,783,928 q-ary local-bubble cases, and 32,642,112 offset comparisons. The exhaustive local check establishes only the q-ary bubble/probability lemmas; the all-\(n\) code bound rests on the analytic adaptation of the hashing, exceptional-alignment, witness, and bipartition arguments. Those adaptations change only fixed alphabet-dependent constants for fixed \(q,t\), yielding the stated \((2t-1)\log_q n+O_{q,t}(\log\log n)\) upper bound.

    ## Originality — FAIL

    The exact theorem is already present in an earlier SCOPE record, `fixed-qary-deletion-codes-2t-minus-1--0b8ba422fcea`, whose RESULT states the same fixed-\(q\), fixed-\(t\) coefficient \(2t-1\). The current record itself acknowledges that earlier provenance. Under the required implication/duplicate standard, a separately written corroborating derivation is not an original second discovery of the theorem.

    ### Equivalent formulations

Searches: fixed q-ary deletion coefficient 2t-1; q-ary t deletion redundancy (2t-1) log n; earlier SCOPE record fixed-qary-deletion-codes-2t-minus-1--0b8ba422fcea

Evidence: The earlier SCOPE RESULT was inspected directly at the assigned repository commit and states the same asymptotic theorem.

Reasoning: The two records differ in exposition and some bookkeeping choices, but their final mathematical theorem is equivalent.

### Broader coverage

Searches: En Gad Polynomially larger deletion codes arXiv:2609.19493; fixed q-ary deletion codes 2t-1 earlier SCOPE

Evidence: En Gad supplies the binary theorem; the earlier SCOPE record supplies the fixed-alphabet q-ary extension in full.

Reasoning: The earlier SCOPE theorem covers the current final claim exactly, so no narrower wording in the corroborating record restores originality.

### Exact database or table

Searches: SCOPE repository path 2026/09/18/fixed-qary-deletion-codes-2t-minus-1--0b8ba422fcea; published-record semantic query: q-ary deletion coefficient 2t-1

Evidence: Direct inspection of the earlier published SCOPE record is decisive. The semantic record-search service returned no usable result, but that limitation is immaterial because the exact repository duplicate was read.

Reasoning: This is an exact same-theorem repository match, stronger than a failed or incomplete literature search.

### Claim versus prior implication

Searches: earlier SCOPE RESULT fixed-qary-deletion-codes-2t-minus-1--0b8ba422fcea; current corroborating RESULT

Evidence: Both state existence of fixed-alphabet q-ary t-deletion codes with redundancy coefficient \(2t-1\) and a logarithmic-logarithmic remainder.

Reasoning: The current theorem is not merely implied by the prior record; it is the same theorem. Originality therefore fails decisively.

    ## Source inspections

    - **Fixed-alphabet q-ary deletion codes attain the 2t-1 coefficient** (SCOPE record 2026/09/18/fixed-qary-deletion-codes-2t-minus-1--0b8ba422fcea): trigger — the current record's provenance correction identifies it as earlier priority; material read — complete RESULT.md at repository commit 92c7f26b45ce94be6cda0eafed44298c598d7b47; assessment — COVERING exact duplicate theorem. Evidence: The earlier record states the same fixed-\(q\), fixed-\(t\) asymptotic redundancy bound and gives a complete q-ary adaptation.
- **Polynomially larger deletion codes by linear hashing of substring counts** (arXiv:2609.19493): trigger — binary source theorem and motivating open extension; material read — abstract and lawful public rendering of the binary coefficient theorem and hashing mechanism; assessment — PRIOR_BINARY_RESULT; not itself the decisive duplicate. Evidence: The source proves coefficient \(2t-1\) for binary codes; the exact q-ary duplicate is supplied by the earlier SCOPE record.

    ## Checked sources

    - earlier SCOPE record fixed-qary-deletion-codes-2t-minus-1--0b8ba422fcea
- arXiv:2609.19493
- arXiv:2306.02868
- arXiv:2210.14006

    ## Residual risks

    - No originality uncertainty remains inside SCOPE: the exact earlier theorem was directly inspected. External priority remains time-sensitive but cannot change the internal duplicate finding.

    ## Scientific value — FAIL

    The theorem itself is mathematically valuable, but this later record does not fill a new mathematical gap: it reproduces an already-published SCOPE theorem. A corroborating derivation and finite local checker are useful evidence, yet correctness and reproducibility alone do not satisfy the research-value axis for a duplicate finding.

    ## Limitations

    The q-ary derivation is mathematically sound as checked, but this record is rejected as a research finding because the same theorem appears in an earlier SCOPE record. The local exhaustive check does not by itself prove the all-length theorem.

    This document records a mathematical assessment of the stated claim and its literature context. It does not convert historical same-model review evidence into independent evidence.
