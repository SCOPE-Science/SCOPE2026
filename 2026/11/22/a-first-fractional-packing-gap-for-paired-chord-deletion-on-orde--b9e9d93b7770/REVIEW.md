# Scientific review

## Correctness — PASS

The claim defines the precise single-pair erasure channel and set-valued deletion shadows. An exhaustive induction-based recurrence on the subsets of at most 15 outputs counts both optimal disjoint-shadow families and all optimal codebooks; a separate maximal-clique method confirms the same cardinalities and multiplicities. A concrete seven-source matching code and exact half-unit primal/dual LP certificates establish the matching size 7 and fractional optimum 15/2 without floating-point error. All certificate constraints and symmetry counts were reconstructed and checked by the standalone program.

## Originality — PASS (qualified)

Pilaud–Rué (arXiv:1307.6440) treats ordered chord-diagram crossings, not the entire matched-pair erasure channel. Gabrys et al. (ISIT 2014, DOI:10.1109/ISIT.2014.6875337) treat standardized deletion of a single permutation entry, not two matched endpoints together. General deletion coding methods therefore do not directly imply the 105-to-15 incidence certificate or classification of all 278 maxima. Sala–Gabrys–Dolecek (ISIT 2014, DOI:10.1109/ISIT.2014.6875338), on multipermutation deletions, remains a material priority risk because only its abstract, not the full article, could be inspected. No exhaustiveness claim about world literature is made.

## Mathematical value — PASS

Erasing an unknown paired chord from an ordered matching is a natural contraction channel in chord diagrams and paired-endpoint information. Exact zero-error code capacity, an explicit strictly fractional packing relaxation and a complete equality census at the first four-pair boundary supply a nontrivial, reproducible benchmark. No extension beyond four pairs is asserted.

## Limitations

Results are finite and concern whole-pair deletion only, not arbitrary two-vertex deletion. There is a fractional integrality gap but not an integer-rounding failure: \(\lfloor15/2floor=7\). Earlier inaccessible or unindexed exact finite results could supersede the priority assessment. The checker verifies a finite mathematical certificate, not an independent scientific review.

Self-review: passed. Independent audit: not yet performed.
