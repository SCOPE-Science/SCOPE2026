# Self-review

## Correctness — PASS

The exact q-ary inverse-list formula is established by a bijection using the unique greedy leftmost embedding, with independently counted initial, internal and terminal gaps. The proof explicitly covers arbitrary deletion counts and treats distinct parents rather than embeddings. Strict monotonicity follows from positive power-series coefficients, and the support threshold follows from the exact binomial count. The standalone checker independently enumerated 70,295 receiver configurations, verified 2,260 automaton cases, and checked 2,016 spectrum parameter combinations. These finite checks corroborate the all-length analytic proof, not replace it.

## Originality — PASS (qualified)

The closest full-text comparison is Atashpendar et al. (2018): their initial-mask methodology concerns unrestricted binary supersequences and embedding multiplicities; the present q-ary homopolymer-free all-radius inverse-list spectrum is not stated there. Takemoto and Nozaki (2020) study binary run-length-limited single-insertion/deletion codes, while Benerjee and Banerjee (2023) study homopolymer-free **Hamming** code bounds. The checked indexed summaries concern different read-deletion channels, unconstrained descendant spheres and unrelated universality indices. The binary one-deletion run-limited case is previously covered in a separate record and is not the substantive q-ary all-radius claim. Exact equivalent or implicit regular-language results remain a historical-priority risk; a failed search is not proof of novelty.

## Value — PASS

The exact receiver-to-source list spectrum measures reconstruction uncertainty under a biologically motivated source constraint for arbitrary deletion numbers. Its strict defect hierarchy, all-radius feasible-output distribution, absence of singleton observations, and Gaussian threshold address meaningful structural questions that are not supplied by ordinary source-to-output deletion sphere counts or Hamming packing bounds. It does not claim a deletion-correcting code cardinality.

## Limitations and closest literature

The source alphabet is q-ary with at least three symbols; words are linear, nonempty at the receiver, and only restricted by unequal adjacent source letters. Exact posterior weights depend on deletion-mask multiplicities and are not addressed. Independent verification has not been performed. The closest comparisons are arXiv:1802.00703, arXiv:2012.13536, and arXiv:2305.10741, as analyzed in `AUDIT.json`.

Self-review: passed. Independent audit: not yet performed.
