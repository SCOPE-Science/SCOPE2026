# Self-review

## Correctness (PASS)

The graph has precisely four index layers, six prescribed edge types and no degenerate edge duplications for \(n\ge3\). Both exhaustive implementations independently reconstruct all graph edges and graph distances using different algorithms; they directly test injectivity of *all* edge-distance signatures for every subset of sizes two through four and every \(n=3,\ldots,12\). The resulting counts agree coefficient-for-coefficient. Positive four-set counts guarantee upper bounds; zero two-/three-set counts guarantee the lower bounds, and every one-set extends to a pair. The orbit checker tests each natural symmetry image and partitions all \(160\) minimum triples of \(DGP(10,1)\). The remaining infinite tail is attributed to the published Theorem 1, whose scope is exactly \(n\ge13\). The finite certificate relies on code inspection and reproduction and is not a claim of a paper-independent formal verification.

## Originality (PASS, provisional)

The closest same-graph original work [1], read through the relevant graph definition, lemmata, tables and Theorem 1, states the residue formula only for \(n\ge13\). Even the \(2\bmod4\) constructive lemma starts at \(n=14\). It neither enumerates initial-order three- or four-vertex bases nor supplies their symmetry orbits. The related later paper [2] computes Wiener-family indices, which do not imply these edge-signature injections. Searches for alternate graph nomenclature, small-order tables, basis counts and parameter-specific implications did not locate a covering result. Residual risks include unindexed theses, code databases and unpublished computational tables. Failed discovery alone is not a priority proof.

## Mathematical value (PASS)

The missing initial cases of a published infinite-graph theorem form a natural finite cutoff, not an arbitrary slice. The smallest index congruent to two modulo four, \(n=6\), does **not** satisfy the extrapolated three-sensor law, whereas \(n=10\) does. The sharp onset matters for applying the theorem without its published size restriction. Exact four-set census and six symmetry families of the \(160\) exceptional optimal sensor arrangements supply reproducible boundary structure beyond simply checking a few examples.

## Closest sources and limitations

[1] Iqbal et al., *On the Edge Resolvability of Double Generalized Petersen Graphs*, 2022, DOI 10.1155/2022/6490698, Theorem 1 restricted to \(n\ge13\).

[2] Iqbal et al., *Wiener polarity and Wiener index of double generalized Petersen graph*, 2023, DOI 10.1016/j.jksus.2023.102680, different invariant.

The claims for \(n\ge13\) rely on [1]. The exhaustive enumeration is finite, priority clearance is provisional, and no external validation has been conducted.

Self-review: passed. Independent audit: not yet performed.
