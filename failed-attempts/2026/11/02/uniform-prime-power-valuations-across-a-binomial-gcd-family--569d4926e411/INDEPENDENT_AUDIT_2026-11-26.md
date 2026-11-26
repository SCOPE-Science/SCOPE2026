# Independent mathematical audit

## correctness

PASS

For 0≤t<N=p^a, the digits of N−1−t are the complements of the a digits of t. The two multiples (q−1)(N−1) and q(N−1) split into complementary length-a blocks (q−2,N−q+1) and (q−1,N−q), respectively. Both therefore have digit sum a(p−1) for the full range 2≤q≤N, including q=N. Legendre’s formula gives exact valuation a. Newton interpolation of F(X)=binom(kX,k) at 1 through k+1 gives F(0)≡k+1 modulo a common prime divisor of F(2),…,F(k+1), so p is the only possible prime in the gcd and the gcd is N. Independent exact binomial and factorial-valuation checks agreed across 11 prime powers through N=32, 136 individual terms, and all 11 gcds; replay: branches/4cc28ef1-1243-41ac-b84c-830949427918/bounded-repro.py. The finite replay is not the proof.

## originality

FAIL

The exact gcd was already given for this family. Although the closest earlier gcd statements do not state every valuation as a theorem, the October 18 proof gives the exact all-level residue test, the exact low-block count, and X=N(q−1)+(N−q). In the pure-prime-power case, directly evaluating that test above the block counts exactly v_p(q−1) further carries, with all other levels automatically excluded. The termwise equality is mechanically implied by those available formulas, not by the minimum valuation alone.

## value

FAIL

Termwise valuation is a natural invariant and stronger than a minimum in isolation, but here it is exactly the fixed-block specialization of an earlier argument. The digit-sum presentation is a short verification of that consequence, not a separate new invariant, method of wider demonstrated use, or non-routine refinement. No distinct valuable claim remains to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
