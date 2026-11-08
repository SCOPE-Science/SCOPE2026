# Scientific review

## Correctness
**PASS.** The exact spatial counts follow from a three-root filter on \((1+z)^n\); one- and two-coordinate conditioning gives every Gram entry. On the two regular masks the first-band matrix is a scalar plus one rank-one term, while the exceptional mask separates into a scalar and the coordinate-sum/contrast decomposition. Positivity is explicit for all \(n\ge5\), and two parity-specific cross-multiplications establish strict optimality. The elementary monotonicity step in odd dimensions and the error in the asymptotic expansion were checked separately. The standalone checker reconstructs 18 finite Gram matrices and carries out 408 exact binomial identities, supplementary to the all-parameter proof.

## Originality
**PASS, with residual priority risk.** Rao (2021) treats one Boolean Hamming slice. Cornelissen, Mande, Ozols, and de Wolf (2021) treat modular Hamming weight as a query-complexity function, not a Fourier sampling design. Previously published first-band spectral results for single Hamming shells and Hamming balls do not claim the two-/three-level spectrum of full modulo-three congruence classes or the strict selection of two optimal classes. Exact equivalent and broader-coverage comparisons are recorded in `AUDIT.json`. An unlocated general association-scheme consequence remains possible; a failed search is not uniqueness proof. This report does not assert independent novelty certification.

## Mathematical value
**PASS.** Sampling an entire one-third-density Hamming-weight residue class is a natural deterministic measurement design. The exact spectral classification and strict best-of-three condition-number comparison identify two optimizers, a structural degeneracy, and exponential approach to tightness at fixed approximate density. The result does not extend to degree two, arbitrary subsets, or nonlinear recovery stability. The root-filter identity by itself is routine; the complete sharp conditioning classification is the substantive claim.

## Sources and limitations
Primary comparisons: https://arxiv.org/abs/2111.03213 ; https://arxiv.org/abs/2112.14682 ; https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-q-ary-hamming-shell-fourier-concentration-and-the-arithmet--89a15e26e594 ; https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-first-walsh-band-concentration-spectra-on-boolean-hamming--a2f5ddac5a0f . Full source-inspection detail and residual priority risks are in `AUDIT.json`. Exact computations validate sampled cases but cannot establish infinite-dimension correctness. A separate independent mathematical review has not been carried out.

Self-review: passed. Independent audit: not yet performed.
