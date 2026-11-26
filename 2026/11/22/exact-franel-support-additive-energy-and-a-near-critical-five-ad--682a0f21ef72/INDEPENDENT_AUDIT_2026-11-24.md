# Independent mathematical audit

## correctness

PASS

Lucas factorization of the cubed binomial sums gives residues (1,2,0,1,1) for one digit and exactly the alphabet {0,1,3,4}. For equality of ordinary integers, the difference of digit pair-sums plus the incoming signed carry must be five times the outgoing carry. Starting at zero, only -1,0,1 occur; zero terminal carry is necessary and sufficient by telescoping. The pair-sum multiplicities (1,2,1,2,4,2,1,2,1) give carry rows (17,28,6), (8,36,8), (6,28,17), hence reflection-even trace 59 and determinant 380. The middle entry starts at 1,36, giving the required resolvent and root expansion, with the polynomial negative by 484/25 at 256/5. The contiguous digit sum range 0..8 yields overlapping translated prefix intervals and hence the full integer sumset at every depth, including depth zero. The independent residual tail in the continuous sum lands on either side of 1 with probability 1/2 by non-atomicity and reflection; hence grid masses are the averages of neighboring truncated masses. Their square sum is between one half and one times E_r/256^r. This proves the five-adic grid exponent and violates the uniform L² bound obtained by applying cellwise Cauchy–Schwarz to a putative density. /workspace/evidence/reproduce_other_checks.py independently verified direct Franel residues through n=200, prefix-sum histograms and grid energy bounds through r=8, and the reported dimension decimal. The analytic bounds, not these finite checks, prove the limiting assertion.

## originality

PASS

Support congruences, interval coverage, and the matrix method are not the supported novelty. The reviewed contribution is the evaluated exact sequence for ordered additive collisions on the mod-five Franel support and its computed grid dimension and strict L² obstruction.

## value

PASS

The support is specified by a natural divisibility invariant and its interval sumset is a good case in which to ask whether representations are nevertheless concentrated. The exact all-depth energy quantifies an exponentially growing excess over the uniform-distribution bound. The eigenvalue also resolves a near-threshold L² regularity question for the natural equal-weight convolution, without claiming singularity or a new general algorithm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
