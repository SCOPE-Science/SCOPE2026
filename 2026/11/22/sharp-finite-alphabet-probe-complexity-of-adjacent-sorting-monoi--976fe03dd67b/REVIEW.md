# Scientific review: sharp sorting-monoid probe complexity

## Correctness — PASS

The proof specifies all quantifiers and the comparison action, derives the classical normal form and its faithful binary thresholds, constructs \(\lceil(n-1)/(m-1)\rceil\) explicit probes, and proves the matching lower bound from the longest element versus its \(n-1\) distinct adjacent coatoms. The pivotal observation is that a sorted input has no more than \(m-1\) strict coordinate increases. Each coatom differing from the sorting function requires a strict increase at its own position; therefore one probe detects no more than \(m-1\) of the \(n-1\) pairs. A standalone exhaustive small-case checker validates the constructions and critical coatom identities. The all-dimensional conclusion depends on the proof, not on enumeration.

## Originality — PASS (subject to historical priority risk)

The paper by Militaru proves braid/idempotent poset-sorting solutions, but not a nonadaptive probe-complexity formula; Sections 1–3 were inspected. Mazorchuk–Steinberg establish faithful actions, classical normal forms, and sharp *linear representation dimension*, which are deliberately excluded from the novelty claim. Their Sections 2 and 7 were inspected; minimal faithful representation dimension and minimal faithful set-action degree are different from the minimum number of evaluations in the fixed chain-product action. Searches in mathematical research records and publicly indexed literature for comparator probes, 0-Hecke separation, alphabet levels, and network test suites did not identify the exact claimed parameter-dependent formula. Piestrak (1990) studies sorting-network fault detection; its full text could not be inspected and remains a specific historical risk. A negative search is not a proof of universal novelty.

## Value — PASS

The optimum is a natural nonadaptive function-identification invariant, with a sharp alphabet-versus-query tradeoff and an explicit optimal design. Its lower bound is structural rather than brute-force: each symbol level can resolve only one strict boundary in the output and hence at most one corresponding top coatom. The result applies for all word lengths and finite alphabet sizes and is not merely an arbitrary isolated numeric cutoff.

## Remaining limitations

The statement is restricted to the given adjacent comparator action with observable full outputs and no noise. Only finite ranges are computationally checked, while the proof supplies the infinite part. Historical priority under alternative semigroup-testing terminology may need independent examination. No external or independent certification is asserted.

Self-review: passed. Independent audit: not yet performed.
