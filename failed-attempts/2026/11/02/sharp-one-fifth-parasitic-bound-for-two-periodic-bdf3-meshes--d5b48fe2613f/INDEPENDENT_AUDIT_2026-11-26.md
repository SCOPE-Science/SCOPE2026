# Independent mathematical audit

## correctness

PASS

Reconstructed the interpolation derivative on nodes (0,-1,-1-1/r,-2-1/r) with the current step as scale. The constant-cancelling substitution d_n=y_n-y_{n-1} yields the stated A(r),B(r). Multiplying the two difference maps gives trace (-r^4+r^3+5r^2+r-1)/K and determinant r(r+1)^2/K, K=(r^2+5r+5)(5r^2+5r+1). For 5M the three quadratic disk tests have numerators 6r(10r^2+21r+10), 2(5r^4+25r^3+38r^2+25r+5), and 5r^4+5r^3+r^2+5r+5 over K, all positive. At both ends of the ratio range the trace tends to -1/5 and the determinant to zero. For fixed r the period powers decay summably, the intervening step maps are fixed, and y_n converges. The initial triple (0,0,1) produces y_3=1+A(r), so the bound is not uniform in the startup response. This was checked algebraically; the frozen Python verifier was inspected, not run. The result is for y'=0 on exact alternation, not for general variable meshes or stiff equations.

## originality

FAIL

A distinct indexed finding already contains the same all-positive-ratio sharp parasitic spectral law. The multiplication in value coordinates rather than difference coordinates changes only the inclusion of the constant mode. This is demonstrable coverage; the shared catalogue date does not establish priority. The explicit startup example is an elementary consequence of the step coefficients and does not make the frozen core distinct.

## value

FAIL

A sharp all-ratio damping rate for this natural mesh family is useful, but that exact invariant is already available in the matching indexed finding. The frozen representation and the one-update startup example do not provide a distinct substantive advance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
