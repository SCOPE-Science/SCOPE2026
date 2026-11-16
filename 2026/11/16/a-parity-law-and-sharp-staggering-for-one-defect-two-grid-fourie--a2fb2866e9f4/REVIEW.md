# Scientific review

## Correctness — PASS

The two regular grids diagonalize simultaneously under a unitary \(q\)-point DFT in the site index. Every residue class has precisely two Fourier rows, giving an explicit \(2\times2\) Gram block with diagonal one and coherence \(|\cos(\pi d_r\theta)|\). The exceptional displacement is \(d_b=m\) and every other displacement equals one. This proves the full claimed spectrum and the exact rank-loss set without asymptotic assumptions. The norm ratio reduces to minimizing the maximum of two cosines. For odd \(m\), the half-step makes both vanish and is the only zero of the first. For even \(m\), putting \(u=|\cos(\pi\theta)|\) and splitting at \(u_*=\sin(\pi/(2(m+1)))\) yields strict minimax inequalities on either side. The simple Taylor expansion at every \(r/m\) proves the blow-up coefficient. The independent full-matrix checker gave `CHECKS_PASSED 1597`; finite tests are not treated as proofs of the infinite claims.

## Originality — PASS, subject to historical priority

Batenkov–Goldman (arXiv:2107.09326v1, inspected introduction, main singular-value bounds and Section 7) address clustered Vandermonde and prolate singular values rather than one substituted frequency in an equally populated pair of cyclic sampling grids. Lai–Sheynis (arXiv:2309.14625v1, inspected introduction and theorem on multi-tiling fibers) supply general qualitative Riesz criteria; such criteria do not contain the exact two-cosine minimax or the odd/even replacement-height classification. Guo et al. (DOI:10.1016/j.sigpro.2020.107856) investigate optimal recovery under periodic nonuniform sampling; an accessible abstract and introduction concern numerical pattern choice, not the present all-size classification. Two closely related public results were read in full: `1e706b439add` solves the scalar minimax for *consecutive* displacement frequencies and includes the \((1,2)\) specialization already; `89421d123299` solves a fixed three-displacement planar tile. Neither proves arbitrary \((1,m)\) sampling spectra, even/odd dichotomy and exact defect-rank counts. The contribution does not claim new DFT block diagonalization or novelty of the \((1,2)\) scalar case. A general two-grid aliasing paper could implicitly contain these statements; historical priority is provisional.

## Value — PASS

A single out-of-band harmonic is a natural minimal error in an otherwise contiguous Fourier interpolation design. This theorem completely determines whether a fixed two-grid acquisition geometry can be made orthogonal, the unavoidable stability price when it cannot, all attaining shifts, and the exact singular-offset failure law, uniformly in the number of samples and in the affected Fourier residue. This distinguishes odd and even replacement gaps and gives a quantitative acquisition rule rather than an isolated numerical matrix identity.

## Scope and risks

No optimization over arbitrary sampling nodes, multiple band outliers, or weights is claimed. Current evidence is not an independent literature-priority certification. The numerical checker cannot independently validate the all-integer proof. The general aliasing block reduction is standard and acknowledged.

Self-review: passed. Independent audit: not yet performed.
