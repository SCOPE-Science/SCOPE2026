# Independent mathematical audit

## correctness

PASS

Equilibrium length-bias and uniform sampling in the renewal interval give age survival (1+a/b)^(-alpha), not the interarrival exponent 1+alpha. Brownian scaling and covariance integration give the independent age multiplier and Gaussian covariance (1/3,1/2;1/2,1), with determinant 1/12. The age density gives the stated beta integral and diverges for (3p+q)/2>=alpha, including equality. Conditioning on the Gaussian factors and using the upper bound from the exact Lomax survival justifies dominated convergence for either a one-sided sign-conditioned exceedance or the intersection of absolute exceedances. Quantile substitution for the latter is justified by marginal inversion and sandwiching between fixed scaled thresholds. The two normalized absolute Gaussian powers are positive with equal means one but unequal a.s., giving 0<chi<1. As a separate check, for independent standard normals Z,E with H=(sqrt(3) Z+E)/2, polar coordinates express Q as the integral of cos(theta)^s over [pi/3,pi/2] divided by the integral over [-pi/2,pi/2]. At s=0 this gives 1/6; at s=1 it gives (2-sqrt(3))/4. Increasing s strictly biases the positive-normal law toward larger Z and its tilted Z^2 is chi-square with s+1 degrees of freedom, so Q decreases strictly to zero. Separate bounded quadrature gave Q(0.5)=0.121596581927, Q(1.5)=0.066987298108 and Q(3)=0.028834442811. The frozen checker was read, not executed.

## originality

FAIL

The reset-specific literature examined does not give these formulas verbatim, but both extreme observables reduce exactly to existing random-scale and elliptical tail laws, and the remainder is a beta moment and an elementary evaluation of a standard conditional Student-t tail. This is prior coverage by implication, not a claim that a reset paper printed the same number.

## value

FAIL

The chosen observable is physically intelligible and the numerical benchmark is correct. As a mathematical finding, however, the reverse-motion benchmark is a mechanically implied Student-t tail and the absolute co-exceedance and moment frontier are direct random-scale and beta-integral evaluations. The record does not establish a distinct structural or quantitative consequence beyond these routine specializations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
