# Independent mathematical audit

## correctness

PASS

Eliminating x gives F=(y+1)^2(9y^2+4y+4). For p>=5 the double root is disjoint from the simple quadratic branches, whose discriminant is -2 times a square. At 3, u=y+1 gives v_3(F)=2v_3(u)+v_3(u-alpha) with v_3(alpha)=2; the two balls separate for k>=7, with counts 81 and 3^(k-max(3,ceil((k-2)/2))). At 2 and k>=2 the two x-candidates have equal squares; divisibility of F by 2^(k+2) is therefore the correct test. Even y contributes only at k=2,3, and odd y must satisfy v_2(y+1)>=ceil((k+2)/2); k=1 was checked directly. Coprimality and the positive-box hypothesis match Kabluchko–Marynych Theorem 3.1. Independently, for M<p<=N the large-prime tail is bounded by a constant times sum_{p>M}p^(-2), and for p>N each fixed y has O(1) prime divisors of F(y) above N, each allowing at most one x in the box. CRT and these tail bounds justify the independent local law. Tail summation gives the fixed-prime cutoff 3/2 from R_{p,k} comparable to p^(k/2); globally the k=1 term alone diverges at t=1, and the summed higher levels are bounded by a constant times sum_p p^(2t-3) for 0<=t<1. Independent finite replay testing both original congruences agreed at 2^1–2^16 and 3^1–3^11, with direct square enumeration at 2^1–2^8 and 3^1–3^5; in particular R_{2,8}=16 and R_{3,7}=162. The frozen numerical density is a truncated product, not a certified decimal for the limiting probability. No finite-box moment convergence is proved.

## originality

PASS

The supported increment is the explicit pair-specific prime-power spectrum, especially the exceptional binary and ternary branches, and the resulting exact local and global moment comparison for this law. General GCD convergence and the prime-level Euler product method are existing results, not part of that increment.

## value

PASS

The intersection of two fixed translated singular curves is a natural exact local invariant. The formula resolves both small-prime mechanisms across all precisions and determines the full limiting GCD law rather than just its probability at one. The distinct local and global moment thresholds give a concrete use for the all-power information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
