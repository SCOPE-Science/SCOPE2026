# Independent mathematical audit

## correctness

PASS

A zero-diagonal symmetric A remains trace-zero under a diagonal congruence, while Sylvester inertia fixes positive count r and negative count s. Their magnitudes have equal sum S, and separate Cauchy–Schwarz inequalities give nL0 >= (n/(rs))(S−2rs/n)^2+(r−s)^2/n, establishing L0>=(r−s)^2/n² and equality magnitudes 2s/n and 2r/n. Real Fourier constant-diagonal rank-r projections produce hollow matrices realizing equality for every inertia. For weighted complete-graph A=W(J−I)W, G=sqrt(2/n)W^-1 attains the floor; all positive off-diagonal entries plus rank-one spectral equality force uniqueness when n>=3. The explicit diagonal-plus-rank-one W^-1[I+((n−1)^(-1/2)−1)P] transforms A into 2P−I, eigenvalues exactly ±1. This addresses unsmoothed loss only; no performance guarantee for regularized loss or Krylov convergence.

## originality

PASS

Brarda et al. introduce the indefinite bimodal target and fixed-support optimization, but their inspected full published text optimizes a smoothed objective with an anti-zero regularizer and does not establish a sharp zero-diagonal inertia floor or a diagonal-versus-rank-one exact separation. Resultary searches found various SPD condition-number scaling results, not this exact indefinite spectral target. Classical inertia, trace and Schur–Horn ingredients are credited; the combined sharp obstruction, equality and factor-support escape survive on best-of-knowledge evidence.

## value

PASS

The inertia imbalance gives a precise structural obstruction to a natural bimodal eigenvalue target under diagonal factor support, and a rank-one added direction removes it exactly on a nontrivial weighted complete-graph family. Uniqueness of the diagonal optimizer and matching equality constructions determine a sharp support-versus-spectrum boundary. This is a motivated exact result even though its proof uses elementary classical linear algebra and does not establish Krylov acceleration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
