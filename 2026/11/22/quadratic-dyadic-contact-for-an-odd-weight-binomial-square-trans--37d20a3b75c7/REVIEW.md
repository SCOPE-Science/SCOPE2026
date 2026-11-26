# Independent mathematical audit

## correctness

PASS

The valuation can be checked directly on finite sums. Divide F_n(t)−1 by n²; the j-th term is (2t)^j/j² times the product of (1−n/i)² for 1≤i<j. For 8|n its valuation is at least j−2ν₂(j)−2Σ_(r≥4)⌊(j−1)/2^r⌋. At j≥9 this is at least (j+1)/4>2, using ν₂(j)≤j/4, and hence zero modulo 8. At j≤8, only j=1,2,4,8 can contribute; the product can be replaced by 1 modulo 8 after including each prefactor (the nonconstant coefficients have sufficient powers of 2). These four terms are always present for the allowed n and give 2t+t²+t⁴+4t⁸≡2t+6≡4 modulo 8. Thus the normalized difference has valuation exactly 2, for positive and negative admissible weights. This also verifies the leading-term argument in the frozen proof; its coefficient bounds grow with j and justify its restricted series. Each r≥3 occurs and has frequency 2^(−(r−2)) conditional on 8|n. A separately written exact-integer replay matched 40 signed-weight cases at n=8,16,24,40,64 and reproduced F_4(3)=6145 with difference valuation 11. The replay is finite and is not the proof; see /workspace/branches/217d5353-dfe9-4245-acd8-da9282aa4d88/replay.py and replay.log. The source checker was inspected, not executed.

## originality

PASS

Credit the known central Delannoy contact and image results at t=1. The supported distinct claim is the exact all-index valuation on 8|n for an entire signed weight class t≡3 modulo 4, where the leading order changes from cubic to quadratic.

## value

PASS

The weight is a standard polynomial deformation of a sequence with known cubic dyadic contact. The first coefficient after normalizing by n² selects the residue class of the weight, and the cut at 8|n is material, as the n=4 witness shows. The exact law determines a full local valuation spectrum and its conditional frequencies; it is more than recomputing the classical sequence or verifying a finite congruence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
