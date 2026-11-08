# Research assessment: Thirty-three vertices mark the first endpoint-neighbor sign loss for TR-BDF2 diffusion on paths

## Correctness — PASS

The explicit partial-fraction reduction, tridiagonal Neumann Green kernel, strict path-order monotonicity lemma, size-32 Bernstein positivity certificate and size-33 rational sign witness jointly cover every \(n\ge2\) and every positive timestep. The separate endpoint limits establish the bounded sign-loss window's existence, not uniqueness. The standalone verifier reproduces the exact-rational inequalities from source and tests small matrices independently. Finite arithmetic alone is not treated as an infinite proof.

## Originality — PASS, with specified source risk

Bonaventura and Della Rocca (2015, arXiv:1510.04303v1) analyze method-wide absolute monotonicity and SSP variants, not the exact path-specific endpoint-neighbor sign boundary in examined sections. Hosea and Shampine (1996) derive the scheme and analyze stability and implementation. No inspected source implies the exact all-step boundary at 32/33. The directly relevant Carroll (1993) one-dimensional parabolic composite-solver paper was identified, but full primary text could not be accessed; its possible coverage remains an unresolved publication-priority risk. Absence from searches is not taken as proof of uniqueness. The exact comparison dimensions are path length, the boundary-adjacent entry and all positive timesteps.

## Value — PASS

Positive neighbor transport is a natural mass-transfer property of Neumann path diffusion. The result identifies the minimum path length for its breakdown under L-stable TR-BDF2, a quantified boundary-layer sign defect not provided by general timestep-conditional SSP results. It provides a complete infinite-family yes/no classification for this exact entry, not an arbitrary table slice.

## Scientific limits and closest literature

The theorem does not classify the full transition matrix, stagewise positivity or the number of negative intervals. It assumes unit edge conductances. Sources: Bonaventura–Della Rocca (2015), arXiv:1510.04303v1; Hosea–Shampine (1996), DOI 10.1016/0168-9274(95)00115-8; Carroll (1993), DOI 10.1016/0377-0427(93)90030-F (uninspected primary text). Other previously published complete-multipartite TR-BDF2 claims do not imply arbitrary path cases of length at least four.

Self-review: passed. Independent audit: not yet performed.
