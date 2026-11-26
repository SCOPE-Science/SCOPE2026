# Independent mathematical audit

## correctness

PASS

An order-three multiplicative character, extended as zero at zero, gives B_a(u)=1+omega^(-a)chi(u)+omega^(-2a)chi(u)^2, equal to three on the desired nonzero coset and zero on the other two. On permitted starts the product counts the word with weight 81. Summing first over the entire field, the empty-support term is p and one-position terms vanish. On support size k≥2 the polynomial has k distinct roots and exponents in {1,2}, so not a constant times a cube; the distinct-root Weil bound is (k-1)sqrt(p) for each unit-modulus-weighted term. The counts at k=2,3,4 give 24+64+48=136. At each excluded start exactly one argument is zero, so B_a(0)=1 bounds the total subtraction by 4 times 27. Thus 81N≥p-136sqrt(p)-108, positive at 19000 by squaring 19000-108>0 and increasing thereafter. The independent finite code uses trial division, verifies primitive roots using all prime divisors of p-1, constructs cosets by explicit cubing and multiplication (not discrete-log or Euler color labels), and analyzes every x=1,…,p-4. Replay: python3 /workspace/branches/074f9253-f40d-4057-92d4-e86062111ed1/direct_cube_coset_check.py 19000. The accompanying full-run.txt matches all 39 listed exceptions out of 1072 eligible primes; it records exactly (0,2,2,0) absent with g=2 at 547, all 81 at 571, and last all-cubic failure at 379. Combined with the infinite bound this gives 571 as the first eligible prime beyond the last failure, not an assertion that every admissible prime below 571 fails. Replacing the primitive root multiplies the color index by a unit mod 3, leaving color zero fixed and either fixing or interchanging the other two colors. Frozen checker and verification evidence inspected; uploaded code not executed.

## originality

PASS

Available sources establish related residue runs, distributions or word thresholds, not this full 81-word classification and sharp cutoff. The classical character-sum argument is prior machinery; the supported distinct result is the exact four-position classification. Published priority remains bounded by the inspected sources.

## value

PASS

Complete residue-color words are a natural strengthening of classical consecutive-power runs, and the exact uniform cutoff resolves when every local four-argument cubic condition is simultaneously available as an existence assertion for each specified word. The last obstruction is mixed rather than all-cubic, so the cutoff is not a restatement of the classical run question or a tiny improvement to the Weil estimate. The exhaustive classification is connected to an infinite theorem, with a sharp finite witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
