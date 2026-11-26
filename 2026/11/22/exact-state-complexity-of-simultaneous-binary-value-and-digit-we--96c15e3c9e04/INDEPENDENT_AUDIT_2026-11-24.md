# Independent mathematical audit

## correctness

PASS

For odd u>1, positions of exponents 0 and 1 modulo the order of 2 supply (1,1) and (2,1). Their difference gives (1,0), and subtracting that from (1,1) gives (0,1); finite additive orders let one reduce coefficients and realize all pairs at a common sufficiently large length. For u=1 use a sufficiently long fixed block that realizes each weight residue. Fixing the low t bits supplies the modulo-2^t target and leaves a solvable joint condition modulo u and k on the prefix. Thus all mk residue pairs are reachable at one common length, and at all greater lengths by leading zeros. Suffixes of length >=t forget all but (r mod u,p); fixed-length reachability and invertibility modulo u separate different such pairs. For each j<t the only possibly accepting suffix is exactly the j-bit encoding of a mod 2^j (empty for j=0). Its predecessor test fixes r modulo m/2^j and p modulo k. In descending j this test can split at most one block because all earlier tests use coarser numerical congruences and the same specified weight coordinate on that set. Adding m/2^(j+1) to an inside r changes the current test but not the older ones, giving exactly one split. Hence the explicit quotient has ku+t classes for all targets, with modulus one and t=0 included. The two odd-part/weight transitions are permutations; some common power of their average is entrywise positive by the fixed-length argument, so that finite chain converges exponentially to its uniform law. Prescribing the low t bits and applying CRT yields 1/(mk). Independent bounded replay `python3 /tmp/opencode/modular-review.py` checked reachability and minimized by backward pair distinguishability for all 780 targets at 1<=m<=12, 1<=k<=4; the frozen three check scripts and captured output were inspected, not executed. The full replacement leaves theorem and proof intact, but marks the density as a known consequence and credits exact covered state-complexity subcases; the known-consequence derivation was independently checked at X=2^n, with redundant moduli handled by summing. Scope remains MSD-first binary words, leading zeros and epsilon, one joint target, complete one-way DFA.

## originality

PASS

Pass the distinct general joint-congruence minimal-state and quotient claim, not the standalone density theorem or covered divisibility and affine Thue–Morse subcases. Gelfond's classical theorem actually implies the entire exponential-density part; the repaired Finding and literature section explicitly credit it and present the direct Markov proof as complementary. The literature section also credits the nonzero-a translated Thue–Morse subcases and updates the two-way-automaton comparison. No inspected broader result implies the general one-way input-popcount/target quotient. This is a best-of-knowledge verdict, not priority certification.

## value

PASS

The two numerical tests form a natural common-input product for one-way binary recognition, but the quotient has ku+t states rather than the separate-minima product k(u+t) in general. The uniformity across every numerical and digit-weight target, and the one-new-class-per-short-suffix mechanism, explain where all but t of the low-bit distinctions disappear. This is a usable exact construction and lower bound for joint recognition, not a parameter substitution into a multiplication theorem. The density appears only as classical context with a direct alternative proof and is not used as the novelty or value basis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
