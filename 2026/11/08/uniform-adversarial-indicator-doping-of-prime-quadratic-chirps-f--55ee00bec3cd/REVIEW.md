# Independent mathematical audit

## correctness

PASS

Expanding g(x+u) conjugate(g(x)) into chirp/chirp, chirp/indicator, indicator/chirp and indicator/indicator yields p zeta^(au^2) on v=2au plus 2k+C_u prime-root summands with nonnegative integer coefficients. For prime p, a vanishing p-root sum must have equal exponent counts, so p must divide the total number of summands, congruent to L_u modulo p even on the chirp line. With 0<L_u<=3k<p no zero is possible. Off the line, every nonzero cyclotomic algebraic integer has norm a nonzero integer and its p-2 other conjugates are <=L_u, giving |A|>=L_u^(-(p-2)); on line triangle inequality gives p-L_u>=1. Weyl characters diagonalize the Hermitian-matrix lifting, yielding sqrt(p)|A| singular values, with ||g||^2<=p+3k. Independently reconstructed residue counts for p=5,7,11 all supports k<p/3 with a=1,2 and all pixels, and exactly checked each of three boundary zeros (all p residue classes once). Finite checks corroborate but do not prove infinite p.

## originality

PASS

The cyclotomic vanishing criterion and Gabor-lifting diagonalization are classical inputs, not original findings. The full published single-impulse quadratic-chirp theorem covers k=1 and all odd cyclic lengths but not arbitrary adversarial support k growing linearly with prime p. A fresh statement-level search found no covering theorem for the modulus-by-overlap condition and position-free 3k<p guarantee, with bounded-priority uncertainty.

## value

PASS

An all-position adversarial construction of full Gabor phase retrieval from a natural quadratic chirp, tolerating a positive fraction of perturbed entries, is a substantive stability/design question. The explicit overlap-sensitive modular certificate explains which support geometry matters and produces exact boundary cancellation witnesses; it is not merely a renamed k=1 identity. Quantitative if conservative singular-value control makes the result useful for robust finite tomography.

The dated certificate retains the supplied scientific assessment, sources and limitations.
