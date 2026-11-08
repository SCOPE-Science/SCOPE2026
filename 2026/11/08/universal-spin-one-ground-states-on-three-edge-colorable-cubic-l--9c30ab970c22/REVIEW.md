# Scientific review: universal spin-one cubic-line-graph ground states

## Correctness — PASS

For any three-edge-colorable simple cubic base graph, the bilinear exchange interactions of its line graph partition exactly into triangles indexed by base vertices, while every spin appears in exactly two triangles. The complete ten-triple local energy table reduces to six positive-field affine terms. A pre-existing proper three-edge-coloring makes any minimizing triple consistent at every base vertex, proving **attainment** of the lower bound at arbitrary field and anisotropy, rather than merely an inequality. Strictly minimizing compositions correspond bijectively to perfect matchings, labeled proper edge-colorings or uniform states. On the two stated coexistence sets, local minimizer supports correspond bijectively to even-cycle packings or ordinary matchings, proving both exact degeneracy formulas. The standard-library verifiers enumerate the cuboctahedron, tetrahedral and complete bipartite cubic examples independently of the general proof. No infinite statement is inferred from the tests alone.

## Originality — PASS on the inspected evidence, with residual priority risk

The nearest direct source is Hwang, Park and Kwak (2016): their zero-temperature \(h/J=4\) kagomé Blume–Capel field threshold at the examined anisotropy is **already known**. Their paper explicitly identifies the simultaneous nonzero anisotropy/field problem as future work. Xu and Moore (2007) already identify the \((-1,0,+1)\) classical kagomé constraint for \(0<D<J\) at zero field, so it is not claimed as new. Barry and Muttalib (2002) solve a **triquadratic** rather than bilinear interaction model, and Rousochatzakis, Läuchli and Mila (2007) address quantum Heisenberg kagomé-like clusters. An existing Potts line-graph result shares the three-edge-coloring method but uses equality-indicator interactions and yields a different envelope and matching weight. The new joint statement is not implied by those particular field thresholds, special classical constraints, or distinct Hamiltonians. Residual risk: an unindexed equivalent derivation of the full classical field/anisotropy envelope or the two boundary graph-polynomial identities may exist.

## Mathematical value — PASS

The result supplies a complete exact two-control zero-temperature classification for an infinite family of frustrated kagomé-like cluster graphs, not a small numerical correction. It identifies six physically distinct saturation/occupation patterns, shows how their open-region multiplicities encode perfect matchings and edge colorings, and connects two separate coexistence processes to **different natural graph invariants**: even-cycle packing weights and the all-matching generating function. The 12-spin cuboctahedron is a physically motivated member, with independent exact 69/108 boundary counts and 1/9/24/9/9/1 open-phase counts. This precise structure can support low-temperature entropy and magnetization studies, without falsely asserting thermodynamic-limit phase transitions.

## Closest literature and scientific limits

- J. H. Barry and K. A. Muttalib, *S=1 kagomé Ising model with triquadratic interactions*, arXiv:cond-mat/0204632 (2002); distinct exchange term.
- C. Xu and J. E. Moore, *Global phase diagram of the spin-1 antiferromagnet with uniaxial anisotropy on the kagome lattice*, arXiv:cond-mat/0701635 (2007); supplies a covered zero-field three-color constraint but not the full claimed finite-graph field envelope.
- I. Rousochatzakis, A. M. Läuchli and F. Mila, *Highly Frustrated Magnetic Clusters: The kagomé on a sphere*, arXiv:0711.3231 (2007); quantum magnetic-cluster context.
- C.-O. Hwang, S. Park and W. Kwak, *Study of the Antiferromagnetic Blume-Capel Model on kagomé Lattice*, J. Phys. Conf. Ser. 750 (2016) 012016; known zero-anisotropy critical field and explicit limitation regarding combined anisotropy and magnetic field.

The theorem excludes non-three-edge-colorable cubic graphs and nonuniform couplings. It does not provide the full boundary degeneracy on every tie curve, a positive-temperature phase diagram, or independent validation. The comparison cannot establish absolute historical uniqueness.

Self-review: passed. Independent audit: not yet performed.
