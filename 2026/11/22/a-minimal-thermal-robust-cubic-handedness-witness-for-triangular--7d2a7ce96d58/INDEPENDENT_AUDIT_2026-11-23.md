# Independent mathematical audit

## correctness

PASS

The frozen algebra is correct when the index rates are taken as defined, but its proof swaps the physical names of the two turns. This matters for a signed handedness witness. The complete replacement RESULT.md in repairs/2 fixes the convention: with Z=X+iY and positive angles anticlockwise, u advances the index and is anticlockwise, and d is clockwise. No checker or other supporting file needs a mathematical change. The stationary generator on z^n U^{-n} gives the three denominators kappa+3s/2+i sqrt(3) delta/2, 2kappa+3s/2-i sqrt(3) delta/2, and 3kappa; the product of the first two is A+iB with A>0 and B=sqrt(3) kappa delta/2. Thus the stated sign carries through also when exactly one rate vanishes. The radial second moment follows separately from the stationary |z|^2 balance and Re E[z U^{-1}]. Threefold invariance forces the first two pure moments to vanish, and circular independent noise contributes no positive-degree pure moments. In the repaired support proof a finite stationary history in a permitted cyclic order with two switches in open time windows can approximate any three positive weights, with old history uniformly negligible; this also covers one-way switching. The three triangle reflections all have form z->omega^k conjugate(z) and would force a real cubic. Isotropic Gaussian deconvolution preserves this obstruction for arbitrary reflection axes, including affine ones. The two-heading segment has an affine reflection, which survives convolution. The diagnostic script was inspected, not executed; the result is a population moment, not a finite-sample detection guarantee.

## originality

PASS

For the repaired claim the change is to the turn convention and supporting proof, not to the signed formula in index coordinates or to the model. The closest known fourth-order trapped witness uses four headings and the relevant independent-redraw and preferred-turn sources solve different dynamics. The contribution is the sharp reflection obstruction at the minimal heading count, not the use of generator moments or circular convolution.

## value

PASS

The observable is motivated by the loss of handedness information in the first two pure spatial moments. The repaired statement shows when unobserved angular bias leaves no reflection whatsoever and gives a signed spatial-only witness which remains exact under arbitrary finite independent isotropic translational diffusion. Two headings cannot produce the phenomenon even with asymmetric jumps, so the triangle tests the natural minimal case, not an arbitrary cutoff. Thermal invariance of the expectation does not ensure practical precision at high noise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
