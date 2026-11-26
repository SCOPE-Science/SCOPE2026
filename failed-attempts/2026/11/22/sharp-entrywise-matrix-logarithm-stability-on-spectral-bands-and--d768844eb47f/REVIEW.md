# Independent mathematical audit

## correctness

PASS

The domain is the real symmetric Loewner band, with maximum absolute entry on both inputs and outputs. Independently, center each resolvent at m=(r_a+r_b)/2: R=mI+((r_a−r_b)/2)M with M a symmetric spectral contraction. Each row of M has Euclidean norm at most one, hence absolute row sum at most √n. This gives exactly q=r_b+c_n(r_a−r_b). The resolvent identity bounds the two-input difference by the integral of q² times ||A−B||_max. The displayed P is the positive rank-one projector onto the normalized sum of e_1 and the uniform unit vector; the resolvent at aP+b(I−P) is entrywise nonnegative with the required first row sum. The all-ones direction attains its derivative integral in the (1,1) entry. Moving inside the band by ε and taking a perturbation h<ε/n gives admissible distinct pairs and recovers the boundary derivative in the double limit, also for n=1. Integration of q² gives the three claimed terms. At fixed r>1 the leading coefficient is positive by a nonzero square integral; at b/a=1+x/√n the scaled integrand is dominated by a multiple of (1+t)^−2 and tends to [1/(1+t)+x/(2(1+t)^2)]², giving the claimed polynomial integral. These are bounded-critical and fixed-band regimes, not an exhaustive two-rate dichotomy for intervening widths. RESULT.md lines 28–84 prove the claims; checker.py and VERIFICATION.md were read but the 625 reported numerical comparisons were not rerun.

## originality

FAIL

A distinct indexed theorem gives exactly this finite-band modulus and the same rank-one witnesses after the affine spectral reversal X=I−A/b. Its applicability is missed by asking whether log itself has nonnegative coefficients: the transformed scalar function is g(x)=−log(1−x). The stated limits are direct limiting evaluations of the covering theorem's exact coefficient. This is demonstrable mathematical coverage, not an inference about publication order from two same-day catalogue entries.

## value

FAIL

The stability question and critical scale are natural, but the exact band law and witnesses are a parameter and function substitution into a distinct published indexed theorem. The residual dimension formulas are direct leading-term evaluations, with no surviving independent exact invariant or new mathematical gap resolved in the frozen finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
