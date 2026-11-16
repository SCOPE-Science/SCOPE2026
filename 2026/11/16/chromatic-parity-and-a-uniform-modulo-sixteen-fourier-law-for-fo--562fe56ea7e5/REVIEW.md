# Scientific self-review

## Correctness — PASS

A full reconstruction checks translation orthogonality, the root-zero orbit bijection, parity of each nonroot colour bit under the full three-element nonzero-colour permutation group, and the modular lifting from \(P_G(4)/4\) to each balanced coefficient. The complete-bipartite computation uses the standard Stirling-number expansion and verifies the parity recurrence \(S(m,3)\equiv m\pmod2\) for \(m\ge2\). The resulting operator rank follows from character diagonalization on a finite abelian group. The standalone integer checker corroborates 16,932 coefficients on all labelled graphs through four vertices, 28,224 balanced biclique coefficients and 99 independent direct sums. No finite check substitutes for the universal proof.

## Originality — PASS under bounded comparison

The Greene–Zaslavsky chromatic linear-coefficient identity and the unsigned biclique colouring formula are prior work. The inspected portions of Gebhard–Sagan’s 1999 preprint discuss unique-sink acyclic orientations and coefficient identities, not arbitrary signed character sums. Tarsi's full 1999 article discusses a distinct graph-polynomial-weighted colour sum; its Theorems 1.1–1.4 do not state the present uniform \(\pmod{16}\) law. The closest indexed first Fourier-band study on complete bipartite colourings addresses sampling Gram spectra, not all convolution multipliers; only its indexed abstract could be inspected. Searches did not locate a published full-character congruence with this conclusion. This is bounded evidence, not a proof of historical uniqueness. The residual risk is an uncatalogued treatment of character-weighted colourings or a more general modular group-action theorem implying the result.

## Mathematical value — PASS

The exact full Fourier support of a graph-colouring indicator is a natural deconvolution question. The theorem converts a graph-polynomial parity invariant, also interpretable by acyclic unique-sink orientations, into an exact rank test for a whole class of colour-constrained convolution operators. The biclique theorem uniformly handles arbitrarily large and unbalanced part sizes and proves a frequency-independent nontrivial modulo-sixteen restriction, stronger than ordinary translation-forced zeros. The result is structural, not a numerical tolerance test or arbitrary small parameter slice. It does not claim exact nonzero singular-value multiplicities or a paper-sized development.

## Closest sources and limitations

Gebhard–Sagan, arXiv:math/9907078v1, examined primary PDF text through Section 3; Tarsi, DOI:10.5802/aif.1707, full PDF pp. 1–5; OEIS A212084; and the indexed 2026/11/1 first-Fourier-band record. All limits and the unexamined plausible first-band full text are disclosed in RESULT.md. Independent assessment has not been performed.

Self-review: passed. Independent audit: not yet performed.
