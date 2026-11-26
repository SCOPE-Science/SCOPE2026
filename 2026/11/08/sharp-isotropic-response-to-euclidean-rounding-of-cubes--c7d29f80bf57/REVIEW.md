# Independent mathematical audit

## correctness

PASS

The outside coordinates of a point are determined by the coordinatewise Euclidean projection to the cube. For exactly k excess coordinates their vector ranges over a positive-orthant k-ball. Thus V has normalized coefficients 1,d,πd(d−1)/8 through order two. The contribution to S from a stratum uses the inside-square mean (d−k)/3 and k outside squares (1+u_i)^2. The face linear-in-excess term contributes 3 to the normalized quadratic coefficient, and k=2 contributes π(d+4)(d−1)/8. Symmetry gives L²=S/(dV^(1+2/d)); the binomial expansion cancels the linear term and gives −(d−1)(4−π)/48. Erosion is exactly a homothetic cube, so the signed profile is C¹ but lacks a second derivative at zero. In d=3 the edge region integrates ∫u_1=t³/3 on a quarter-disk and the corner region integrates ∫u_1=πt⁴/16 on an octant, consistent with independent sums of the volume and moment polynomials. An exact scaled-integer coefficient convolution, adding (5i−3j)v_i s_j to the coefficient of t^(i+j−1) and using a formal variable for π, reproduced the five-term derivative certificate in RESULT.md lines 82–97. Rational bounds 3.1<π<22/7 give all signs; the derivative is strictly negative for positive t. Leading terms give the ball limit, which is not attained at finite radius.

## originality

PASS

The supported distinct content is the explicit signed onset for every d and the exact strict outer-radius profile in d=3, not the use of parallel-body stratification, volume polynomials or covariance invariance themselves.

## value

PASS

Euclidean rounding is a canonical deformation of the cube. The vanishing linear term and explicit negative quadratic term distinguish covariance response from volume growth and exhibit a loss of twice differentiability in the signed family. The exact dimension-three profile establishes strict behavior across all outer radii rather than just an endpoint ordering or a near-cube approximation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
