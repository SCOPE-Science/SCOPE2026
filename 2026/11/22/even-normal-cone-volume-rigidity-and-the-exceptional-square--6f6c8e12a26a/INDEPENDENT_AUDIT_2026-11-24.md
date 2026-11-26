# Independent mathematical audit

## correctness

PASS

The support-line formula gives L_j(r)=kappa(1-r_j)/(1-r_j+c r_j), since the supports of the two summands add to one. At c=1 the shifted supports would lie in a cyclic eigenspace with eigenvalue strictly between the k=1 and k=2 values, so the shift vanishes. At c≠1 write D=1-r+c r and c=(1-lambda)^2/lambda^2: the transformed x is lambda D/(1-lambda), and lambda^2 D+(1-2lambda)(1-r)=(1-lambda)^2 verifies the reciprocal substitution with positive x. In the recurrence proof the reciprocal first moment makes adjacent characters orthonormal in the 1/x-weighted inner product. The multiplier identity follows from -mu_k=4 sin((k-1)alpha) sin((k+1)alpha) and cotangent subtraction; the cotangent differences telescope to 2 cot(alpha). Equality in the resulting Bessel sum would force both s_2=s_4=1, impossible for distinct characters on a grid with strictly positive weights. Weighted Cauchy–Schwarz is therefore strict for nonzero higher-mode part h. Expanding the weighted square of x minus its constant and first-harmonic parts then gives B(x)≤kappa N, with equality only if both parts beyond the constant vanish. The recurrence imposes equality and x=1. At N=4 opposite equations give x_0=x_2, x_1=x_3 and x_0 x_1=1. For polygons, opposite sides of each rectangle have equal length; comparing opposite proportionality equations forces equal opposite supports, and the atom formula and converse follow. The frozen NumPy script was inspected, not executed; recorded samples cannot prove strictness at every positive weight, which follows analytically.

## originality

PASS

The material contribution supported here is rigidity without imposing symmetry on the summands or on the positive solution in the regular even fan, and the sharp distinction between the square and higher even orders. Monahan's odd-period method and known centered symmetric uniqueness are inputs/overlaps, not claimed novel; the elementary rectangular boundary is not a general new uniqueness theorem.

## value

PASS

The result resolves a natural exceptional case at the even-parity boundary of the weighted Fourier argument. It proves a global discrete uniqueness result in positive supports without assuming central symmetry of the unknown, and identifies exactly where a fixed regular sum can have nonhomothetic proportional-cone-volume summands in the even regular case. The square family explains why the boundary cannot simply be removed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
