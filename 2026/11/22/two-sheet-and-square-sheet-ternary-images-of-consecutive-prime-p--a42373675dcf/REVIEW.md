# Independent mathematical audit

## correctness

PASS

For every s>=1, j*binomial(3^s,j)=3^s*binomial(3^s-1,j-1) gives v_3(binomial)>=s-v_3(j). On x=3v the linear term after division of G_s(3v)-1 by 3^{s+1} is v, and for 2<=j<3^s one has j-1-v_3(j)>=1. Thus the normalized map changes any difference v-w by a unit factor and induces permutations on every finite level, giving surjectivity by inverse limits. The involution x↦-1-x gives the same regular image on x≡-1 mod 3. On x=-1/2+3v, the binomial expansion retains only even powers of 6v. Dividing out 3^{s+2}v^2 gives constant 2c_s(3^s-1)≡1 mod 3; for even j>=4 one has j-2-v_3(j)>=2, so the remaining coefficients lie in 9Z_3. Its square root congruent to 1 mod 3 exists by Hensel and changes by a multiple of 9(v-w), by division by the unit sum of the roots. Multiplication of v by the root therefore gives another bijective isometry, proving that the third sheet is exactly a square image. Since (3^s-1)/2≡1 mod 3 and 4 has order 3 modulo 9, c_s≡7 mod 9; the regular sheet is 1 mod 9. At n=1 all three inputs have one output. At n>=2, the regular normalized coordinate is read to max(0,n-s-1) digits out of n-1 and has two sheets. In the critical branch with L=n-s-2>0, square zero requires divisibility of the coordinate by 3^{ceil(L/2)}, while a nonzero square of valuation 2j has two simple unit roots modulo 3^{L-2j}, with 3^j lifts each. Each normalized root has 3^{s+1} lifts in the original critical residue branch; for L<=0 the whole branch is one fiber. Square units give 3^{L-2j-1} targets at each admitted valuation, establishing Q(L) and I_s(n). The square set has measure (1/3)sum_{j>=0}3^{-2j}=3/8, giving the stated total density. Read RESULT.md lines 38–85, VERIFICATION.md and check.py. The described 34 complete finite comparisons are supplementary; no uploaded script was executed and the verdict rests on the all-level proof.

## originality

PASS

The inspected sources give very close square-sheet analogues, but with another polynomial, another prime, or the opposite parity and sign. The distinct claim supported here is the full ternary image and finite fibers for all positive s of the odd-exponent consecutive difference; neither general square-root counting nor the elementary s=1 quadratic alone is claimed as new.

## value

PASS

The map is a natural finite difference of a prime-power map evaluated at its own prime, where singular lifting prevents the regular analysis from giving the full congruence count. The all-exponent classification identifies three input branches, proves that the two regular branches coincide in the target but are separated from the square branch, and gives exact multiplicities at every depth. This makes attainment and the number of solutions to an arbitrary finite congruence explicit, including the exceptional high-valuation targets; it is more than the elementary s=1 quadratic or an image-size sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
