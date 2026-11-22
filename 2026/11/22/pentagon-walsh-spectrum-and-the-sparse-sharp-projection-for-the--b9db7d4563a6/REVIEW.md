# Scientific review: Petersen pentagon convolution

## Correctness — PASS

For the exact fifteen-edge Petersen graph, every pentagon is generated from its canonical simple five-vertex path, and independently from the complements of its six perfect matchings. The twelve resulting masks span the full dimension-six binary cycle space. The sixty-four compressed signed sums have multiplicities \(-12:1,-4:15,0:32,4:15,12:1\); these independently match the complete 32,768-character Walsh transform after the exact multiplicity factor 512. Fourier inversion of the spectral-support indicator has one value \(1/2\), ten values \(1/8\), and six values \(-1/8\), precisely on the stated edge configurations. Translation averaging gives the minimum norm for arbitrary real or complex projections. No finite experiment is used as an infinite proof; the claim is finite.

## Originality — PASS, with residual historical risk

DeVos–Mkrtchyan–Petrosyan (arXiv:0801.3714, 2008-01-24; full accessible paper inspected) prove a cubic-graph characterization using five-cycle two-factors, not the signed edge-character transform. Brouwer's Petersen catalogue and the accessible exposition *The Petersen code* count the twelve pentagons and give the cycle-code weight enumerator but do not give a pointwise character spectrum or the optimal projector. A published coset-leader/tie census concerns syndrome decoding; a published Petersen spanning-tree spectrum concerns 2,000 trees rather than twelve pentagons. These results do not logically entail the exact 64-character table or the seventeen-point signed projection kernel. A comprehensive older specialized coding-theory source could still contain the same character table, and the Holton–Sheehan monograph was not read in full; neither search nor this review establishes absolute priority.

## Value — PASS

The twelve shortest cycles of the Petersen graph constitute the minimum-weight orbit of its canonical \([15,6,5]\) binary cycle code, with intrinsic interest in graph cycles and error correction. The theorem quantifies precisely the recoverable Walsh frequencies and produces a striking geometrically supported **signed** range projector: its nontrivial coefficients discriminate hexagons from disjoint pentagon pairs. The sharp \(5/2\) endpoint amplification distinguishes this Fourier range from contractive subgroup projections and can serve as an exact benchmark for inverse problems on graphical codes. A natural finite, complete invariant suffices here; no larger-family application is claimed.

## Boundaries and reproducibility

The standalone `verify.py` uses only the Python standard library. The two finite signed-sum computations share the same graph definition but use different transformations; the independent perfect-matching construction cross-checks the shortest-cycle set. Exactness and the limits of the bounded source comparison are disclosed in `RESULT.md`.

Self-review: passed. Independent audit: not yet performed.
