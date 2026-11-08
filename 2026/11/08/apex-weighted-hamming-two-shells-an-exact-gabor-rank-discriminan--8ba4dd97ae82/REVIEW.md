# Scientific review: apex-weighted Hamming two-shell Gabor lifting

## Correctness — PASS
The proof defines the exact Boolean group, normalization, projector family, and complex-linear Hilbert–Schmidt lifting map. Walsh–Weyl orthogonality yields singular values \(\sqrt N|A_z(u,v)|\) with their full multiplicity. The support-difference analysis leaves precisely Hamming-shift weights zero, two, and four; each is evaluated in closed form with all Walsh characters accounted for. The resulting zero counts are additive across disjoint Weyl labels, giving the exact rank and its maximizing conditions. The universal weak law follows uniformly because all non-weight-four positive modes form only \(O(n^{-2})\) of the positive spectrum. Exact Gaussian-integer checker results hold for dimensions 4–7 over seven rational parameters per dimension; a direct complex Gram spectral check holds at dimension 4. These finite checks corroborate, but do not replace, the algebraic proof.

## Originality — PASS under bounded source comparison
The closest primary predecessors are Bojarovska–Flinth, arXiv:1503.05800 (2015), and Goldberger–Kang–Okoudjou, arXiv:2106.01509 (2021). Their general Gabor linearization and Weyl-ambiguity spectral identity are known and fully credited; neither inspected theorem evaluates this Boolean two-shell apex family. Indexed complete rank discriminants for near-constant *cyclic* windows do not imply the Boolean subgroup parity defect or the complex apex vertical/circle rank loci. Hamming-shell Walsh-band concentration and positive-definite Turán optimization also involve different operators, despite related combinatorics. The full mathematical comparisons, source inspections, and identified source IDs are recorded in `AUDIT.json`. A stronger unlocated association-scheme/Gabor statement could implicitly contain the classification; bounded searches are not a guarantee of historical priority.

## Mathematical value — PASS
This is a complete sharp family classification for a natural Hamming-geometry Gabor measurement design. It determines the precise maximal matrix-information dimension and all complex parameter values at which information drops, including additive losses where geometric exceptional loci intersect. It also proves a nontrivial parameter-uniform two-atom law for the overwhelming positive singular spectrum. The unavoidable parity obstruction is explicit and prevents overinterpretation as pure-state phase retrieval. The rank and spectral classification is useful independently of a noisy-reconstruction theorem.

## Limitations and closest literature
The result covers the unnormalized apex-weighted binary Hamming weight-two shell; it does not extend to larger radii, imply generic pure-state phase retrieval, or quantify noise stability. The classical spectral reduction is not claimed as a discovery. Independent mathematical audit and validation have not been performed.

Self-review: passed. Independent audit: not yet performed.
