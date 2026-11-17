# Independent mathematical audit

## correctness

PASS

In a root basis for triangular book K_(1,1,m), the polar constraints are |t|<=1, |w_i|<=1 and |t-w_i|<=1. Fubini integrates (2-|t|)^m over [-1,1] giving anchored polar 2(2^(m+1)-1)/(m+1). Its polar has sections |y|_1<=1, B-1<=z<=1-A with section length 2-|y|_1; integrating over the cross-polytope yields coordinate primal 2^m(m+2)/(m+1)!. Reciprocal primal/dual Gram Jacobians cancel in their product. Hence R_m=(m+2)/(m+1)(1-2^(-m-1)), difference numerator m^2+4m+5-2^(m+2) has signs positive at m=1,2 and negative for every m>=3 by induction; maximum R_3=75/64, and (m+1)(R_m-1)->1. Independent exact Fraction computations for m=1..29 verified both product and difference identities, not used to justify infinity.

## originality

FAIL

The book Mahler formula is an immediate product of TWO PRIOR explicit whole-family volume formulas: Ohsugi–Tsuchiya (2020) determines primal normalized volume of the suspension of a star, which is the same K_(1,1,m); the published 2026-10-18 weighted-book Lipschitz dual theorem covers the entire polar for all 0<t<=2, and its t=1 case is exactly this polar volume. Independently the 2026-10-25 book Lipschitz covariance theorem explicitly gives that very polar volume. These known exact m-formulas algebraically imply the claimed R_m and its elementary finite-difference peak. New wording of the peak is not sufficient to rescue a corollary of stronger prior results.

## value

PASS

The nonmonotone Mahler product of a natural graph family, with a precise three-page optimizer and limiting Hanner benchmark, is a meaningful geometric phenomenon, though already mechanically recoverable from published exact whole-family volume identities. Value is assessed separately from originality and correctness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
