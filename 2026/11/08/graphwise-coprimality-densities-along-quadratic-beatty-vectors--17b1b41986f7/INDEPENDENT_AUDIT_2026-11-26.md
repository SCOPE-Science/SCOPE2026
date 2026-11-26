# Independent mathematical audit

## correctness

PASS

The repaired RESULT proves a power-saving estimate, not just the frozen limit. For either type of edge, a common positive divisor d gives 1<=k<=O(X/d) and ||kρ||<=O(1/d), where ρ is an irrational square root of a positive rational. The frozen proof's wording about all quadratic irrationals being of that form was overbroad; only these specific ratios are needed and the repair restricts the elementary rationalization accordingly. It gives ||kρ||>=c/k, hence d=O(sqrt X), and circular separation Ω(d/X) gives O(X/d²+1) possibilities for each d, with at most one n per k. This holds for composite d also; summing over integers d>Y bounds the union event of an endpoint gcd exceeding Y by O(X/Y+sqrt X). Independently, the norm of h·α minus its nearest integer is a nonzero integer in the degree D=2^(s−1) multiquadratic field, with all other conjugates O(H), so ||h·α|| is bounded below by a constant times H^(1−D). Erdős–Turán–Koksma and the geometric sum bound then give uniform translated-box discrepancy O(T^(−γ)), γ=1/(2D); the correctly scaled fractional parts on n=b0+Mt give X/M^s+O((X/M)^(1−γ)+1) uniformly for M<=X. Replacing the product of full edge Möbius sums by divisors <=Y differs only on the gcd tail and costs O(X^ε(X/Y+sqrt X)) by the divisor bound. A tuple of edge divisors has modulus <=Y^e and main density the inverse product of incident lcms; summing the residue errors costs O(X^(1−γ)Y^(e(s+1))). The absolute main series has local nonempty terms <=p^(−2); weighting one marked edge divisor by its square root leaves terms <=p^(−3/2), proving truncation cost O(XY^(−1/2)). The local signed sum equals the independent-set factor by inclusion-exclusion on edges, and the factors are positive and 1+O(p^(−2)). Taking θ=γ/(2e(s+1)), Y=floor(X^θ), ε=θ/4 makes all errors O(X^(1−θ/2)); the stated δ and K3 example follow. Edgeless graphs are exact and nonintegral X differs only by the floor in the main term. The frozen verify.py and the repaired scientific verification notes were inspected, not executed; numerical examples check neither the theorem nor the exponent.

## originality

PASS

The frozen qualitative graphwise limit is mathematically covered: Champagne's Lemma 4.3 supplies the required upper-density tail for both types of slope pairs, and ordinary residue equidistribution plus CRT and a finite union over edges give the limit and factor. The repaired contribution is only the full-count power saving for arbitrary fixed graphs along the same thin sequence. The closest primary quantitative results cover the large-prime tail, or give an even stronger full count for a single edge incident to n, but do not provide an effective count for simultaneous constraints on several edges or several linear floor coordinates. The replacement proof supplies that by combining all-divisor tails with effective residue discrepancy and a bounded-modulus edgewise sieve. No first-priority or exponent optimality claim is made.

## value

PASS

The repair supplies an explicit algebraic-rate discrepancy from the graphwise density for a thin deterministic set with potentially overlapping coprimality constraints, rather than another proof of the already implied qualitative limit. The all-divisor tail and bounded-modulus Möbius truncation address the substantive obstacle that pairwise power bounds and a fixed-prime limiting sieve do not estimate the full graph count. Although not optimized, the explicit saving works for arbitrary fixed edge incidence and includes simultaneous floor–floor constraints.

The dated certificate retains the supplied scientific assessment, sources and limitations.
