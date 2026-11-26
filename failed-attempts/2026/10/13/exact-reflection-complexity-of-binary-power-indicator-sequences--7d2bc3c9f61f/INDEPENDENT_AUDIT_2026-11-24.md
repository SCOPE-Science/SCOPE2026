# Independent mathematical audit

## correctness

PASS

The frozen display adds min(h,ceil(s/2)); it does not multiply that term by n. The first gap between ones uniquely fixes its power index k, so counting allowed starts gives exactly c_k(n). One-one factors lose floor(n/2) classes under reflection, while factors with at least three ones cannot have a factor reversal because their successive gaps strictly increase. For two ones, both orientations require each flank to be no longer than P_k, the available leading zeros; the admissible left-flank interval is reversed by ell→n−d_k−1−ell, giving floor(B_k(n)/2) nontrivial pairs. Strict Q_k>P_k is not needed and is an equality for b=2, k=0. For d_m≤n<d_{m+1}, earlier pairs make no reduction (including the b=2,n=4 palindrome), and the current gap contributes min(h,s)−floor(max(0,min(s,2h−s))/2)=min(h,ceil(s/2)). This proves the block formula and base-2 specialization including n=0–3 by the finite sum. Scaling by d_m gives the stated profile: for b>2 its two endpoint values agree and the peak is at 1+2/b, reached asymptotically by rounding lengths. At b=2 the profile is constant. An independent bounded enumeration agreed for b=2–6 and n=0–60 (305 lengths across bases). The supplied script was inspected but not executed.

## originality

FAIL

The distinct Resultary record e7e8ab2eb348 evaluates precisely the same reflection complexity for every base and length, gives the same base-2 formulas and limiting endpoints, and strengthens the asymptotic result to the full cluster interval. This is mathematical coverage, not an inference about historical priority or provenance from catalogue dates.

## value

FAIL

An exact reflection-complexity profile for this natural family would be worthwhile if distinct, particularly the contrast between convergence at base 2 and oscillation at higher bases. The exact invariant and asymptotics are already covered in the reviewed catalogue. The frozen record leaves no independently useful residual exact claim beyond that coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
