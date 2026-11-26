# Independent mathematical audit

## correctness

PASS

The complete observation is a length-resolved multiset, so reversal preserves it, and even an unrestricted collision with an admissible word must itself avoid 11 (inspect the length-two all-ones count). The primary unrestricted theorem supplies the lengths with n+1 prime, twice prime or 8. I independently exhausted the other three positive cases by filtering binary masks with w&(w>>1)=0 and constructing an exact packed integer count key (each count fits its field). For n=8,11,15 the populations are 55,233,1597 and the fibers 30,127,826, exactly the reversal orbits. On the negative side, a composite m=n+1 outside twice-primes and 8 either has an odd prime divisor with complementary factor at least 3, or is a power of two with a factorization into factors at least 3. Unless m is 9,12,16, one factor must be at least 5, since products of 3 and 4 give only those exceptions. With a>=5, b>=3, the nonpalindromic block s=01 followed by a-3 zeros has zero endpoints, so inserting the letters of t=1 followed by b-2 zeros in either order yields admissible words. The first inserted bits distinguish the two words; the reversal would start with the different block s reversed. Every substring meeting inserted positions has a uniquely determined first and last inserted position and boundary offsets; for given offsets and span its only varying contribution is the composition of a contiguous t-factor, invariant as a multiset under reversal. Substrings missing all inserted positions lie in a block copy. Thus the collision works for every excluded length. Replay: `python /workspace/audit-replay.py 2`.

## originality

PASS

The supported distinct claim is the all-length universality criterion for the full 11-avoiding source with complete substring compositions. The unrestricted theorem and interleaving identity are prior. The finite exceptional cases can be investigated via unrestricted census data, but admissibility of the infinite family of collision witnesses requires the boundary-safe block and factor split.

## value

PASS

A natural source constraint changes the worst-case identification capability at exactly three lengths and nowhere from length sixteen onward. The theorem tells a researcher when complete composition data suffice and supplies concrete admissible counterexamples otherwise. Its value is in the all-length classification, not a rerun of finite census counts alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
