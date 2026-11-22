# Mathematical review

## Correctness — PASS

The stated object is a Minkowski sum of independent unit segments in \(\mathbb R^3\), sampled from the normalized spherical density \(1+\varepsilon P_2\). The geometric determinant formula fixes the normalization. Exact uniform-sphere projections yield the bounded canonical pair kernel \(g\) and triple kernel \(h_3\). Under the perturbed triangular law, counting shared indices gives \(\operatorname{Var}(\sum h_3)=O(n^3+n^4\varepsilon^2+n^5\varepsilon^4)\); this proves negligible residual error in **both** claimed regimes. The Funk–Hecke operator's degree-two eigenvalue is \(-\pi/64\), and the density changes exactly one normalized quadratic harmonic mean to \(\varepsilon/\sqrt5\). The triangular-array CLT, canonical spectral-tail estimate, and square-sum identity produce the noncentral five-degree chi-square law. Exact chi-square moments give the variance and sharp support edge. Under larger vanishing anisotropy, the exact linear projection and the ordinary CLT yield the Gaussian variance \(\pi^2/20480\). Exact symbolic integrals for six even degrees and numerical quadrature and determinant checks corroborate the normalization; finite tests are not offered as infinite proofs.

## Originality — PASS, provisional priority

The complete published isotropic random-zonotope variance and chi-square theorem is a **strict special case** \(c=0\), not a theorem for moving angular densities. The published planar radial-noise crossover varies segment lengths, and its independent Gaussian-plus-chaos transition does not imply the coupled noncentral five-dimensional harmonic sector in the spatial angular perturbation. Schneider's publicly available abstract states fixed-law expectations and a central limit theorem; the full text was unavailable in this comparison and is a material priority risk, although the directly inspected isotropic result explicitly reports that its CLT nondegeneracy condition excludes the isotropic case. The noncentral local-alternative technique is standard in statistics; only the explicit geometric spectrum, critical angular scale, full noncentral law and sharp variance/support consequences are claimed as new. Searches for the precise angular density, dimension, eigenvalue and reduction yielded no covering published published-finding corpus result, but absence from a search index cannot prove worldwide uniqueness.

## Mathematical value — PASS

The uniform-sphere volume statistic has no first Hoeffding projection; under a small anisotropic perturbation that projection is restored. The theorem classifies **all** vanishing quadrupolar angular perturbations into a non-Gaussian, noncentral crossover, and Gaussian regimes at a sharp scale. Its exact dimension-five noncentral mode and moving sharp upper endpoint reveal how geometric isotropy breaks; this is not a mere fixed-distribution CLT or parameter substitution. The result is deliberately confined to a naturally motivated single harmonic perturbation instead of claiming unproved general anisotropy universality.

## Closest literature and residual limitations

- Schneider (arXiv:2202.06774, first posted 2022-02-14): public abstract available, full paper inaccessible in this run; fixed-law CLT is a plausible broader tool, not independently demonstrated to contain this moving law.
- Breiding–Bürgisser–Lerario–Mathis (arXiv:2109.14996): determinant and zonoid background, not the asserted critical law.
- *Second-order volume fluctuations of isotropic three-dimensional random zonotopes* (published published-finding corpus 2026): full `RESULT.md` read; \(c=0\) covered and credited.
- *A critical radial-noise crossover for areas of random planar zonotopes* (published published-finding corpus 2026): full `RESULT.md` read; angular spatial law and noncentral mode not covered.

Other potential unindexed equivalent local-alternative results remain an originality risk. The exact finite-size centering is not simplified into a polynomial in anisotropy, and no independent audit is claimed.

Self-review: passed. Independent audit: not yet performed.
