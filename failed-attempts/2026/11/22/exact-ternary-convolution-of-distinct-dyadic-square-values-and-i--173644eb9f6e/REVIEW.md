# Independent mathematical audit

## correctness

PASS

I reconstructed the all-depth proof. The odd squares fill the 1 mod 8 class (odd-root lifting); the even squares are exactly the injective image 4Q_{k-2}. At k>=5 the even classes 0 and 4 mod 8 contain A and B values. Partitioning ordered triples by the number of odd summands gives division by four in the all-even case; otherwise the full odd coset gives a uniform count per target in its allowed mod-8 class. For k>=6, induction on s_j gives A<=B=u/4 and A+B=s_{k-2}<=u/2; nonrecursive classes other than 3 are strictly below u^2 and the recursive ones are bounded by s_{k-2}^2. The first two summands determine the third, with repeats and zero correctly included. Parseval has the stated factor 2^{-k}; scaling the energy recurrence contracts by 2^{-10} and yields 485/9427968. A new verifier used weighted unordered triples at low depth and carry-free polynomial cubing at high depth, matching all 8190 targets at k=1..12, the base arrays, maximum classes, and energies. Replay: python3 /workspace/reviews/reproduce.py 5; output /workspace/reviews/reproduce-output.txt. The finite run is corroboration, not the all-depth proof.

## originality

FAIL

The closest same-object result gives more than an absolute-first moment: it explicitly evaluates the full transform as a recursive term plus eight exceptional coefficients, including the parity values and their limits. On that eight-point support, write z=exp(-2πij/8) and C=A+Bz^4. The prior formulas give the correction to the cube as (C+uz)^3-C^3 = 3u(A^2+B^2)z+3u^2 A z^2+u^3 z^3+6uAB z^5+3u^2 B z^6, using z^8=1. Its inverse transform simply reads these five coefficients and divides by u. The recursive term is the old triple convolution stretched by four. Thus the alleged explicit refinement is an eight-term coefficient extraction from the prior explicit formula, not merely an observable that could in principle be computed with an unrestricted inverse DFT. The maximum is an immediate comparison using the prior square counts, and squaring the same coefficients and summing, with the prior parity asymptotics, gives the moment constant by a geometric sum. The earlier text need not have stated any of these exact final numbers verbatim for this overlap to be decisive.

## value

FAIL

The distinct-value distribution is a natural object. The exact law and energy here, however, amount to a direct fixed-size postprocessing of already evaluated same-set transform data; the maximum then uses immediate cardinality bounds. No separate structural or independently unknown exact result survives this comparison. There is no justified repair by renaming the specialization or adding a fresh certificate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
