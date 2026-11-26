# Independent mathematical audit

## correctness

PASS

Interlacing gives k + max |K(g_i)| for the three cyclic gaps. At the candidate level each gap lies in [d,2d] or [1-2d,1-d]; fewer or more than one long gap cannot sum to 1, and equality with one long gap requires (d,d,1-2d) cyclically. At those gaps the off-diagonal matrix is sign-conjugate to the matrix with all off-diagonals -p, giving k+p twice and k-2p once. The Sobolev evaluation-map squared norm is the top Gram eigenvalue. Differentiation on compact subarcs follows from the uniform Dirichlet test; the Laplace sine representation has positive integrand on the open half-circle, with partial geometric sums dominated by C e^{-u} uniformly away from zero angle. In the sum at 1/6 and 1/3 odd harmonics cancel, and the remaining coefficient at 2m is 2 cos(2 pi m/3); this gives the exact strict sign for 2s>1. Locally uniform convergence to the log-sine kernel traps the critical root by sign. For H_s=K_s(2 pi)^{2s}/2, H_s(t)+H_s(2t) has value -4^{-s}(1+o(1)) and derivative -3 pi sqrt(3)+o(1) at t=1/6, with uniformly convergent derivatives near the limiting root. The shift thus costs one third of the leading gain over equal spacing, leaving the normalized coefficient 2/3. Independently replayable `python /workspace/branches/audit_checks.py sobolev` checks the polylog roots, the s=1 normalization, the critical root (~0.1194571600), and both large-s coefficients (s=15: 0.06125876625 and 0.66666666591); these are corroboration, not proof. The frozen checker was inspected, not executed. The endpoint s=1/2 is a node-location limit only.

## originality

PASS

The exact s=1 design is covered and expressly excluded from novelty in RESULT.md. The supported distinct claim is the general circular criterion, all real s>1/2 for the specified Sobolev scale, and the sharp limiting design and gain laws. The closest examined sources do not establish or imply that extension.

## value

PASS

Solves the natural worst-case simultaneous sample-energy minimization for three equally weighted sensors across an entire fractional scale, not only a parameter instance. The kernel theorem isolates why clustered sites can beat equal spacing and gives equality rigidity, and the two asymptotic coefficients quantify precisely how the improvement vanishes. It does not make claims about recovery-error-optimal points.

The dated certificate retains the supplied scientific assessment, sources and limitations.
