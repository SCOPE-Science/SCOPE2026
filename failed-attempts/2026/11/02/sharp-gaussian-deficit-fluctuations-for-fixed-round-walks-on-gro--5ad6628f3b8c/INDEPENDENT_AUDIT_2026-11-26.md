# Independent mathematical audit

## correctness

PASS

At the start of stage i the unseen count is R=U_{i−1}+1. A single specified label escapes the q draws with probability a_i=(1−1/i)^q, while two specified labels both escape with probability (1−2/i)^q. This gives the conditional mean, the exact mean sum, and the centered regression/covariance by telescoping the a_i. Centered innovations are martingale differences bounded by q; their conditional variance is R p_i(1−p_i)+R(R−1)b_i, with p_i=q/i+O(i⁻²) and b_i=−q/i²+O(i⁻³) for fixed q. Orthogonality gives Var(U_i)≤q²i, hence R/i→1/(q+1) in L² and conditional variance →q²/(q+1)² in L¹ by boundedness. The normalized weighted sum of brackets converges in L¹ to q²/((q+1)²(2q+1)), using the Riemann sum of (i/n)^(2q) and the bounded weighted Cesàro error; the normalized bounded increments give conditional Lindeberg. The same second-moment calculation gives the sharp variance and time-correlation limit. Bounded differences applies to qn independent draws since replacing one changes the number of distinct labels by at most one. For q=2 let S=Σ_{j=0}^{n−1}j² and J=Σ_{m=0}^{n−2}m²Σ_{j=0}^m j². The joint absence formula gives Var=S/n²−S²/n⁴+2J/[n²(n−1)²]. Clearing by 180n⁴(n−1)² in comparison with the claimed factorization gives polynomials of degree at most eight. Independent exact-integer arithmetic gave equality at all nine points n=2 through 10, proving the polynomial identity with this degree bound. The asymptotics fix q (a horizon-dependent q in the finite formulas must still be common to all stages of that horizon). Uploaded checker inspected, not executed.

## originality

FAIL

The exact mean is already a constant-duration specialization of Kijima–Shimizu–Shiraga. More decisively, the headline Gaussian limit is for the output count of a standard uniform random recursive circuit in different coordinates, already the subject of binary and f-ary output CLTs. The vertex shift below proves exact equivalence for uniform with-replacement parents, and even uniform distinct parents with fixed seed size change the centered count by o(√n) in L². Prior full-text access was incomplete, so this does not claim the exact variance constant or q=2 finite factorization was printed in those papers. The failure is based on the prior Gaussian coverage and the mathematical equivalence, not on unavailable papers.

## value

FAIL

The principal contribution is an already studied output-count CLT restated as walk coverage. Exact regression follows from the affine single-label escape identity, and the q=2 factorization is useful for checking a finite calculation but does not by itself establish an independently useful new regime or invariant beyond the equivalent model's elementary two-label calculation. The assessment does not deny the utility of fluctuation analysis in genuinely different growing network models.

The dated certificate retains the supplied scientific assessment, sources and limitations.
