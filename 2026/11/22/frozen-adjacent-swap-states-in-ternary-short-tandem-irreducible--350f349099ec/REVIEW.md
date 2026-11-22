# Self-review

## Correctness — PASS

The theorem's domain is indexed ternary words avoiding length-one and length-two tandem squares. Each word has a unique first-symbol-plus-sign representation. A direct modular computation proves the local adjacent-swap sign-flip lemma, including endpoints. The forbidden \(abab\) factor is exactly an alternating sign triple; exhaustive case reasoning on first, last and interior maximal runs proves the frozen characterization. Compositions with internal sizes two/four yield the Fibonacci count, including the zero-interior boundary case. The independently implemented checker directly tests all swaps against both restrictions through length nineteen via sign cases and length eleven via literal ternary words. These finite tests are corroboration, not infinite proof.

## Originality — PASS, with residual priority risk

The nearest related findings count unrestricted radius-two adjacent swaps (`4c63e213-834d-46b8-9cf4-6c2ec7a85ae4`), legal Hamming-one substitutions on the same irreducible language (`e1dd2f70-f4bd-485a-8d5a-d12c5312327a`), legal insertion outputs (`63d30c87-2f2e-47dc-b97d-16e4d15b1df7`), adjacent swaps on the larger proper-word language (`8cf86924-31c0-46ab-9f0a-34b750a1f563`), star swaps (`e8f1957b-eebe-4d4d-9432-2cf7b8664505`) and distance-two swaps (`a6393332-ba3a-4f2c-a3ae-dae835b001cd`). None determines exactly which adjacent swaps retain the \(abab\)-avoidance constraint. In particular, `0102101` is movable by a proper-only adjacent swap but frozen here. published-finding corpus searches of these concepts found unrelated constrained-swap and ternary-spectrum records, not a matching count. The relevant 2018 irreducible-word paper enumerates *words*, not adjacent-swap isolates; the full-text-relevant sections of the 2024 unconstrained swap paper omit this language; the 2025 path-color-swapping paper uses weaker properness and is compared explicitly. An earlier unknown equivalent source remains possible. The 2025 publication is supporting literature, not the 2018 guiding source.

## Value — PASS

A restricted adjacent-swap graph is a canonical reconfiguration/Gray-code object for a recognized tandem-irreducible language. The exact all-length isolated-state count provides a decisive Hamiltonian-generation obstruction at every odd length and shows a parity transition with zero isolates at even lengths; the contribution includes an explicit structural classification rather than an arbitrary numerical slice. The Fibonacci family is new to this restricted operation and is not inferred from the already-known total Fibonacci word count. No claims about optimal codebooks, physical mutation rates, or even-length connectivity are made.

## Evidence and remaining limitations

Compared full-text material: Chee et al., arXiv:1801.02310, Sections I–II and named encoder/ranking contributions as available in the author-uploaded public full text; Adamson et al., arXiv:2307.01648, pages one, four and defining/motivating passages; Fuchs et al. (2025), Sections 4.1.1–4.1.2 of the open HTML article. Source-title searches included exact operation, forbidden motifs, and isolated-vertex aliases. No exact-match source was established. No independent audit performed.

Self-review: passed. Independent audit: not yet performed.
