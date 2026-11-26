# Independent mathematical audit

## correctness

PASS

For d=2m+1 all individual readouts are fair by complementation. The joint success count is the overlap K_a of equal radius-m balls and the covariance is K_a/2^d−1/4. On flipping the next prescribed coordinate, condition on the other bits: the decrement is the rectangular indicator difference at the two thresholds m,m−1, namely 1 exactly when both partial distances are m. Equal partial distances force 2s flipped coordinates with s ones there, so the decrement is binom(2s,s) binom(d−2s−1,m−s)>0 on an even-to-odd step, and zero on an odd-to-even step. Complementing a mask gives K_a+K_(d−a)=2^(d−1). The middle two distances are accordingly an equal plateau for d≡3 mod 4 and a strict drop for d≡1 mod 4. Together with strictness on the other even steps this proves exactly the stated zero and sign classification, also for d=1. Fair Bernoulli variables are independent at zero covariance. The four masks in the proof have distances 2k+1 from the zero mask and 2k+2 between nonzero masks, giving independent pairs. Global bit-complementation annihilates the triple product of centered signs, and the pair and singleton moments already vanish. Thus each triple has all seven nonconstant moments zero and is uniform; no statement about four-way independence is needed. The exact finite test was inspected, not run, and its recorded 2,115 assertions do not prove the all-dimension claim.

## originality

PASS

Pass for the exact all-odd-dimensional sign/zero classification and its explicit four-readout consequence, on the available evidence. The general ball-overlap formula, Boolean autocorrelation formalism, three-bit special case, and antipodal moment argument are not claimed as novel on their own.

## value

PASS

This is a full structural classification for a natural Boolean function on the same random input, with a qualitative parity distinction that independent-noise smoothing or a large-dimension approximation would miss. It gives a direct deterministic design for several exactly independent readouts in every admissible dimension, without additional randomness. The value is the exact family and design, not the isolated d=3 table or the elementary moment test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
