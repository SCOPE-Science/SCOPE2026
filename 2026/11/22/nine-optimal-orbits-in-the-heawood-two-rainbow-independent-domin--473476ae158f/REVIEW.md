# Scientific review of the Heawood two-rainbow independent domination theorem

## Correctness: PASS

The theorem has an explicit finite domain: 14 vertices, 21 incidences and all functions into \(\{0,1,2\}\). The component-coloring bijection proves that enumerating \(2^{14}\) zero sets and their induced positive-component flips is exhaustive. The independent C++ implementation visits all \(3^{14}\) assignments directly and tests every condition without invoking the lemma. Both return identical coefficients and the same point-zero distributions. Exact automorphism generation and orbit coverage certify the nine minima orbit sizes. Scripts are embedded, short and replayable. The finite argument does not extrapolate to larger designs.

## Originality: PASS (best-knowledge priority)

The 2017 original preprint introduces the invariant and prism equivalence but supplies neither the Heawood census nor the nine orbits. The 2019 follow-up addresses high-minimum graphs, bounds and complexity. The 2023 exact-value paper treats other graph families using tropical methods and does not imply this Heawood enumerator. The 2020 near-title match studies a distinct rainbow-domination convention. Searches for the equivalent independent-domination polynomial of the Heawood prism and relevant research records also found no covering table. Unindexed computations and a latent stronger theorem remain possible and independent priority clearance is outstanding.

## Value: PASS

The Fano-plane incidence graph is a canonical regular graph where the complete weight spectrum is noncontiguous. Its 868 optimal labelings occur in nine different symmetry classes, not just one generic orbit, and the precise point/line zero distribution is geometric. These details are not obtained from the scalar definition or from general bounds, and the exact component-cut mechanism motivates future comparisons on incidence graphs. The claim is deliberately finite.

## Limitations

Only the Heawood graph is covered. Code-based exhaustive finite proof is a reproducible exact certificate, not an expert-independent formal certification; an external mathematical review and exhaustive historical-priority check have not occurred.

Self-review: passed. Independent audit: not yet performed.
