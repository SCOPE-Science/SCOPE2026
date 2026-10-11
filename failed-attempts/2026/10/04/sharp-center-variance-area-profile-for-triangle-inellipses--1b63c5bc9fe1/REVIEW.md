# Independent mathematical audit

## correctness

PASS

The classical prescribed-center formula gives \(\eta=\sqrt{27xyz}\) after setting \(x=1-2t\), \(y=1-2u\), \(z=1-2v\), with \(x,y,z>0\) and sum one. The spread constraint is equivalent to \(xy+yz+zx=(1-r^2)/3\), \(r=\sqrt{2D}\). Thus fixed spread fixes the first two elementary symmetric polynomials and the area optimization is exactly extremization of \(xyz\). Interior extrema have two equal variables by the Lagrange equations; substituting the two branches yields \((1+r)\sqrt{1-2r}\) and \((1-r)\sqrt{1+2r}\), with the first feasible only for \(r<1/2\). For larger \(r\), approaching the boundary makes the infimum zero. Squaring the upper branch immediately gives \(\eta\le1-r^2=1-2D\), and expansion at zero proves sharpness of coefficient two. The verifier independently checks the determinant formula, branch values and stability numerically.

## originality

FAIL

The classical source already gives the complete area of the unique inellipse as an explicit function of the center's barycentric coordinates: \(\operatorname{Area}(E)=\pi\Delta\sqrt{(1-2t)(1-2u)(1-2v)}\). That is stronger pointwise information than the audited fixed-spread envelope. Once the spread is fixed, the remaining optimization is the elementary symmetric-polynomial problem of extremizing \(xyz\) at fixed \(x+y+z\) and \(xy+yz+zx\), whose Lagrange equations force two equal variables. Under the required implication-level standard, the printed profile and stability coefficient are therefore routine corollaries of the classical full-center formula rather than independent originality.

## value

PASS

A sharp area envelope at fixed displacement of the inellipse center and the globally optimal quadratic stability coefficient are natural geometric summaries of the full center formula, including a genuine boundary phase transition. The result is rejected for prior implication, not because the profile is an unmotivated statistic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
