# Independent mathematical audit

## correctness

PASS

The real symmetric unit-mass class is in bijection with q(y)=y²+a y³+b y⁴+c y⁵; Plancherel gives the induced norm 16||q||∞ on [0,1]. Bounded evaluation at three positive nodes gives existence. The extremal set has positive distance from zero; fewer than four alternating contacts allow a sign-correcting perturbation y³h(y), deg h≤2, with strict decrease. All but the possible right endpoint are interior stationary points; q′/y has degree at most three and is positive at zero. Thus precisely three interior extrema and the endpoint occur, with signs +,-,+,-. Signed positive-magnitude interpolation weights annihilate the perturbations at those nodes, proving optimality, uniqueness, and the converse for the ordered algebraic system. Independently replayed the numerical certification in review-work/minimax.py (not the frozen program): exact rational four-node dual bound, disjoint stationary brackets for the trial polynomial and a derivative Lipschitz upper bound give outer decimal displays 0.2029850838641552356566686… and 0.2029850838641552387168094…. The four weighted deficits bound the optimizer's coefficients within 2.052×10⁻¹⁶ of the trial coefficients; Laurent expansion then certifies positive taps and the strict negative symbol witness. For the constrained comparison, the interval nonnegative cubic representation P=(1−y)A²+yB² with linear A,B and A(0)=1 permits dropping the B term. The remaining problem is to minimize the squared uniform norm of f(x)=x(1−x²)A(1−x²), x=√(1−y). The polynomial −(2/5)tan(π/10)T₅(x cos(π/10)) is in this family (odd, f(1)=0, f′(1)=−2), and its two opposite contacts on (0,1) certify optimality because every perturbation is a multiple of x(1−x²)². After the factor 16 this is the stated benchmark and the resulting gain is 24.8944409688…%.

## originality

PASS

Credit the known minimax method, the fourth-difference Fourier-nonnegative optimum, and adjacent unrestricted lower orders and shorter radii. The supported distinct contribution is the exact unrestricted radius-three fourth-difference optimum, including the simultaneous strict tap positivity and spectral negativity and the quantitative comparison. No checked statement supplies these. This is distinct-content assessment, not a global priority claim.

## value

PASS

The single radius is motivated by a concrete open sharp fourth-difference regime in the prior smoothing work and an extra free coefficient beyond five taps. The positive time-domain minimizer is still a genuine average, so its negative Fourier symbol and appreciable sharp improvement separate two naturally used meanings of positivity. This is more than a numerical norm estimate or a restatement of alternation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
