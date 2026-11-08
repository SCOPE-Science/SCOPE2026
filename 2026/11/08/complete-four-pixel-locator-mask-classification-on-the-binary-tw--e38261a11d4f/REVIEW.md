# Self-review

## Correctness — PASS

The domain is exactly sixteen binary cells and fifteen four-element masks, each with sixteen translated views. Both complete, terminating implementations individually cover all \(2^{16}\) arrays and agree that twelve masks have an identical successful set of 64 arrays and the other three have no successes. Membership is tested by an exact sixteen-label equality, not sampling. Four 16-element translation orbits and two 32-element enlarged symmetry orbits are independently checked. The all-zero-word argument gives a separate impossibility proof for the three two-column masks. Boundary conditions (cyclic rows and columns, ordered sites, mask span) are explicit.

## Originality — PASS, qualified

The closest inspected source, Horan–Stevens (2015), gives existence/construction/decoding conditions for selected nonrectangular windows, not the exhaustive small-torus classification, simultaneous validity for all twelve masks, or their full solution and symmetry-orbit counts. Alhakim–Butler–Graham (2014) treats one-dimensional sparse comb indexing, which is not the two-row toroidal indexing model. The checked mathematical records and targeted public searches revealed no implying exact result. An unindexed small-instance computation or uninspected appendix could still anticipate the result, so no absolute priority claim is made.

## Value — PASS

A four-pixel binary window has exactly sixteen possible readings, so sixteen toroidal sites are the information-theoretic minimum for complete localization. The two-by-eight torus is the natural minimum-size two-row test case with a three-column field of view. The unexpected shape-invariance (twelve ostensibly different masks all selecting the *same* arrays, including disconnected patterns), complete four-translation-orbit classification, and sharp obstruction for the other three masks give a concrete finite design rule for mask-robust spatial tags beyond mere construction of one example.

## Closest literature and limitations

Horan and Stevens, arXiv:1505.04065v1 (May 15, 2015), Sections 2–3, Theorems 3.5 and 3.9–3.11, is the closest source inspected in substantive detail. Alhakim, Butler and Graham, *De Bruijn Sequences with Varying Combs* (2014), is a different one-dimensional model; its appendix lists small comb counts but does not certify this two-dimensional statement. General historical priority is qualified. There is no higher-size or nonbinary claim.

Self-review: passed. Independent audit: not yet performed.
