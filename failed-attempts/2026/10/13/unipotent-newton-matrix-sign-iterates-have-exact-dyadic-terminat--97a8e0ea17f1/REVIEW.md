# Independent mathematical audit

## correctness

PASS

For X=I+N unipotent, sign(X)=I by analytic functional calculus since the scalar sign is identically 1 near the eigenvalue 1. All iterates stay unipotent. With C(X)=(X-I)(X+I)^(-1), one exact Newton step gives C(X_next)=C(X)^2 by factoring X+X^(-1) +/- 2I. C(X_0)=N(2I+N)^(-1), so C(X_0)^j vanishes exactly when N^j does: the second factor commutes and is invertible. This proves the precise termination index including n=1 and n=2. The exact first error is N^2(I+N)^(-1)/2, whose action on e_3 is M^2 e_1/2. Initial spectral and Frobenius norms are respectively M and M sqrt(n-1) for n>=3, giving the two bounds. In dimension 3 the first error is exactly M^2 E_13/2 and its square is zero, proving both ratios and the next-step identity. For n<=2 any such nilpotent has square zero, so the transient dimension is minimal. Expanding the inverse Cayley map also confirms the leading coefficient 2^(1-2^k) until termination.

## originality

FAIL

This is a direct specialization of the established exact Newton rational map, not just of asymptotic convergence theory. Conjugating that map by (z-1)/(z+1) gives squaring, so on a nilpotent argument the claimed if-and-only-if termination is the nilpotency index test. The same one-step formula on I+MJ_n gives the two amplification ratios by reading its (1,3) entry, and in dimension 3 that is the whole error. These routine consequences exhaust the stated contribution. No publication of the exact frozen wording or its paired presentation is alleged.

## value

FAIL

The example is a valid teaching illustration of why eigenvalues alone do not control a nonnormal error. But the chosen shift makes the phenomenon an immediate first-step entry evaluation, and the stopping count is the routine vanishing of powers of a nilpotent matrix under the known map. The conjunction adds no independently useful invariant beyond those exact evaluations. Increasing the unrestricted scale M is not a separate transient mechanism.

The dated certificate retains the supplied scientific assessment, sources and limitations.
