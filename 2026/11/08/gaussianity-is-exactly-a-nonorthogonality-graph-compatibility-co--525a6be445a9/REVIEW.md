# Self-review

**Correctness — PASS.** A spanning word of projection normals yields a strict block contraction; a pullback representation supplies the unique stationary distribution and all finite moments. Gaussian-mixture fourth-moment rigidity, symmetry of covariance eigenspaces, and a constructive orthogonal-component Gaussian establish the exact iff graph criterion. Conditional Gaussian variance-mixture arguments prove the fourth-cumulant identity and strict non-Gaussianity. `verify.py` confirms 140 exact rational assertions, including a three-row overdetermined covariance and fourth-moment calculation. Computational checks supplement the proof.

**Originality — PASS, qualified.** Bergou et al. (arXiv:2308.16904) study Kaczmarz convergence with data perturbed once; Agaskar et al. (GlobalSIP 2014) give a noise-free exact MSE analysis. Yoon et al. (arXiv:1905.09427) study switching-noise covariance enclosures, not an exact graph criterion. Chen and Ip (2014, DOI 10.1080/00949655.2014.968159) already establish a two-coordinate incompatible-Gibbs random-scan mixture, which is not claimed as new. The asserted distinction is the arbitrary overcomplete oblique-row Gaussianity iff graph condition and non-Gaussian fourth-cumulant consequence. A specialized equivalent result may exist and remains a precedence risk.

**Value — PASS.** Invariant covariance alone does not establish Gaussian uncertainty in repeated noisy linear-system solution. The theorem gives a complete classification for all finite spanning row systems and an exact three-row witness, with a computable fourth-cumulant lower bound useful for detecting failed Gaussian error approximations.

**Limits.** Fresh iid Gaussian measurements, strictly positive sampling probabilities and normalized full projections are essential. The work does not cover fixed dataset noise, correlated row schedules or relaxed updates. Independent scientific validation is outstanding.

Self-review: passed. Independent audit: not yet performed.
