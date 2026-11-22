# Scientific review

## Correctness — PASS
The result is an exact dichotomy for real Haar orthogonal projectors on paths of length a power of two. Ancestor-closed masks correspond to contiguous dyadic conditional averages, which contract variation by a step-decomposition proof, with sharp norm one unless the mask is empty. For a missing parent, the midpoint step of its retained child produces an interior jump of one and a sibling-interface jump of one half while all higher retained contrasts are constant on the parent. A single root-child projector attains the lower bound \(3/2\). The independent integer-matrix enumeration in the supplied checker corroborates all masks through depth four and exact extremizers through depth nine. The theorem itself follows from the analytical argument for every depth; no finite search is treated as an infinite proof.

## Originality — PASS, subject to historical-priority uncertainty
The closest primary sources are Durand–Froment (2003) on TV-minimizing wavelet reconstruction, Steidl et al. (2003/2004) on multiscale soft shrinkage and TV diffusion, Bechler et al. (2006/2007) on higher-dimensional BV stability and one-dimensional greedy failure, Cartis–Thompson (2013) on best Euclidean rooted-tree approximations, and Cohen et al. (1999) on dyadic averages in two dimensions. Those statements do not imply the exact necessary-and-sufficient contraction criterion or the dimension-free sharp \(3/2\) gap for arbitrary *fixed* one-dimensional Haar masks. Related prior published technical statements concern global Haar shrinkage Lipschitz norms or Haar transformations in different endpoint geometries, not mask-by-mask contraction rigidity. Full text of Wojtaszczyk's 2003 paper on BV in dimensions at least two remained inaccessible; an obscure prior one-dimensional analogue is a residual risk, not a claim of definitive uniqueness.

## Value — PASS
Wavelet approximation commonly selects arbitrary collections of detail coefficients; their Euclidean orthogonality alone does not control adjacent-edge variation. The classification gives an explicit combinatorial design law for non-amplifying projections and proves that violating it incurs at least a 50% sharp variation penalty, independent of resolution. This separates exact stability of tree-structured reconstruction from the potential pseudo-Gibbs behavior of unstructured coefficient masks and offers a precise constraint for variation-aware wavelet selection.

## Scope and limitations
This is a finite, real, one-dimensional path-seminorm theorem with fixed masks and the constant coefficient retained. It does not assert a closed formula for arbitrary unstable masks, and it does not cover weighted, cyclic or higher-dimensional variation. The review is not independent validation.

Self-review: passed. Independent audit: not yet performed.
