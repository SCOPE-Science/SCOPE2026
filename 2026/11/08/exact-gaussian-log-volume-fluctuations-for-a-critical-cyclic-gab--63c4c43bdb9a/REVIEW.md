# Scientific review: exact log-volume fluctuations for a critical cyclic Gabor basis

## Correctness — PASS

The exact domain is every integer \(p\ge3\), standard circular complex-Gaussian coordinates with variance \(1/(2p)\), and the square family of two adjacent cyclic translations and all even modulations in dimension \(2p\). Fourier orthogonality gives exactly \(p\) two-by-two blocks, including the swapped boundary vector. Their Gram determinants give the stated product formula. Independently distributed Gaussian radii and Haar directions yield exact log-moment values; conditioning on the common Haar direction shows angular log factors on adjacent edges are uncorrelated. The fixed-size mean and variance follow without approximations. The bulk determinant increments are stationary one-dependent with finite moments, and the exceptional boundary contributes \(o_{\mathbb P}(\sqrt p)\), completing the central limit theorem. The saved checker passed 254 deterministic-factorization and moment sanity checks. The finite tests do not certify the infinite limit.

## Originality — PASS relative to inspected literature

The closest structural antecedent is Asipchuk, De Carli, and Rodriguez, *Block-equivalent finite Gabor frames* (arXiv:2605.16139, first submitted 2026-05-15). Its Theorem 1.1 and structural lemmas explain subgroup-induced block decomposition, but not the exact distribution of determinants of blocks linked by reused Gaussian coordinates, their exact covariance contribution, or the log-volume central limit theorem. Salanevich (arXiv:1902.01062) studies extreme singular values, and Salanevich–Strachan (arXiv:2509.01325) studies random frame bounds and erasures, not the claimed log-determinant law. Comparisons against relevant published mathematical statements revealed no stronger implication or equivalent theorem. The Gaussian radial law and one-dependent limit theorem themselves are classical and are not claimed as new. Specialized unpublished or differently indexed random-Gabor determinant results remain a publication-priority risk.

## Mathematical value — PASS

A square Gabor frame has no redundancy, so its determinant quantifies the volume of the associated analysis map. The chosen half-modulation/two-translation pattern is a minimal natural subgroup example with nontrivial two-dimensional blocks. Unlike an independent-block approximation, repeated random window entries create an exact additive fluctuation penalty. The result calculates the logarithmic volume's finite-size mean and variance, identifies that correlation penalty, and proves Gaussian fluctuations in growing dimension. It answers a quantitative random-frame question without claiming a condition-number bound. The special mask, Gaussian input law, and log-volume invariant limit the scope.

## Closest sources and limitations

[1] O. Asipchuk, L. De Carli, L. Rodriguez, *Block-equivalent finite Gabor frames*, arXiv:2605.16139 (2026).

[2] P. Salanevich, *Extreme Singular Values of Random Time-Frequency Structured Matrices*, arXiv:1902.01062 (2019).

[3] P. Salanevich and N. Q. D. Strachan, *Robustness to noise and erasures of Gabor frames in finite dimensions*, arXiv:2509.01325 (2025).

Log-volume is not the smallest singular value. The scope is restricted to standard circular Gaussians and one explicitly described critical-frequency mask. Independent publication-priority verification has not occurred.

Self-review: passed. Independent audit: not yet performed.
