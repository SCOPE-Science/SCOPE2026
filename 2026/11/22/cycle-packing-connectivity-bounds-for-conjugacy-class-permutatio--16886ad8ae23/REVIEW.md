# Self-review

## Correctness: PASS

The critical extension lemma starts with pairwise disjoint prescribed source and target labels, assigns the resulting directed edges to cycle slots of capacity \(\lfloor\ell_j/2\rfloor\), then fills and closes each cycle with unused labels. Every required edge remains present, and the chosen source positions are increasing, so the exact target word appears as a subsequence. The cell structure agrees with the complete injective-word complex through dimension \(c(\lambda)-1\), yielding connectivity through dimension \(c(\lambda)-2\) by relative CW approximation and the classical sphere theorem. In the involution case a transposition is a forced inversion, proving exact sharpness of this *skeletal* threshold. Exhaustive finite coverage through eight labels and constructive twelve-label checks corroborate the proof. Risk: the theorem does not determine higher homology or sharpen connectivity beyond the stated range.

## Originality: PASS, subject to independent priority check

The nearest recent work (Govc, November 8, 2026) establishes freedom of fundamental groups for arbitrary permutation complexes, not the universal short-word skeleton for all conjugacy classes. The foundational work of Chachólski–Levi–Meshulam studies arbitrary generating families and two-permutation cases; the complete injective-word sphere theorem applies to the **ambient** complex but has no consequence for conjugacy-class subcomplexes without the newly proved extension lemma. Elizalde–Hanlon–Hersh treats relative-order pattern avoidance, a different family of subcomplexes. Search comparisons and inspection of these relevant primary texts found no direct or dominating published theorem. Residual risk: equivalent statements could appear in unindexed combinatorial subsequence literature.

## Mathematical value: PASS

The cycle-type formula provides a uniform, computable **topological connectivity bound** for every symmetric-group conjugacy class, including families with growing vanishing ranges. It upgrades qualitative freedom of fundamental groups to simple connectivity and higher connectivity when the cycle packing capacity grows. The fixed-point-free involution class offers a natural infinite family with a provably sharp exact-word skeleton cutoff. The result is not a numerical recomputation or an arbitrary finite slice; it is a structural theorem spanning every partition of every degree.

## Scope and references

The claim is for exact-letter subsequences in the full conjugacy class, regular injective-word CW models, and the stated connectivity degrees only. It does not assert a complete homotopy classification, sharp connectivity for every cycle type, or novelty certification. Scholarly sources: Govc, arXiv:2611.11362v1; Chachólski–Levi–Meshulam, arXiv:1908.03394; Elizalde–Hanlon–Hersh, arXiv:2610.07303v1; Björner–Wachs (1983); Farmer (1978/79).

Self-review: passed. Independent audit: not yet performed.
