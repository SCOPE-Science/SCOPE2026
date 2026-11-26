# Independent mathematical audit

## correctness

PASS

With common sum s, let Δ be the second product minus the first. The second and third differences are 2Δ and 3sΔ. Their vanishing implies 2Δ=sΔ=0 (subtract s times the second equation), and the pair-power recurrence P_j=sP_{j−1}−uP_{j−2}, P_0=2, P_1=s, then implies ΔP_j=0 for every j for either product u. Subtracting the two recurrences now proves closure at all degrees. With z=x−a,w=x−b,y=x−a−b, Δ=ab and s=2x−a−b. At odd p the count for the product condition is p^k+k(p−1)p^{k−1}: a=0 contributes p^k and each of k finite valuation classes contributes (p−1)p^{k−1}. At 2^k, k≥2, the zero-product count is (k+2)2^{k−1} and a displacement 2^{k−1} is admissible exactly for the k−2 ordered positive valuation splits summing to k−1, each contributing 2^{k−1}. Multiply by the independent p^k choices of x; at 2 all powers are the first power, giving 8, and the residue singleton gives 1. CRT multiplies exact local counts. The first-sum-only example differs by 2 in its second sum for N>2; the stated a=1,b=N/2 example has agreement at degree two but difference N/2 at degree three when 4|N. Independently ran python /workspace/reproductions/check.py 1, directly enumerating ordered collisions and their complete modular power orbits for each N=1,...,40, all matching. The frozen verifier and its stated finite bounds were inspected, not executed.

## originality

FAIL

The distinct indexed record 9c10273590a0 already gives the exact same dyadic energy, all-higher-moment closure, and degree-three sharpness, and additionally gives the individual dyadic fibres. This covers the difficult local part of the frozen claim. The difference in scope is the odd local factors and all-moduli assembly, not a new dyadic effect: where 2 is invertible, the product is already fixed by the first two sums, the count is the elementary zero-product valuation sum, and CRT combines these counts and the closure thresholds. This establishes material statement-level coverage, not the chronology of two records dated the same day. A full-modulus verbatim duplicate was not found.

## value

FAIL

The exact modular fourth energy and the sharp dyadic cutoff are worthwhile invariants. But the nontrivial dyadic result is already present in a stronger indexed fibre law. The remaining odd-factor count and CRT packaging follow by elementary valuation and product rules and do not form a separately substantial finding on this evidence. This is not a correctness rejection.

The dated certificate retains the supplied scientific assessment, sources and limitations.
