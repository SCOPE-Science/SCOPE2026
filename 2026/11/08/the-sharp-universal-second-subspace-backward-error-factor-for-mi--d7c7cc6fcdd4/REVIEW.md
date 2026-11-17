# Independent mathematical audit

## correctness

PASS

Normalize B=A/||A|| with spectrum in [0,1]. Positive affine p(t)=2(1+sqrt2)-4t has |t-p(t)^(-1)| <=E by strict concavity, endpoints -E and interior +E, so trial x=p(B)b/||A|| proves the universal bound via functional calculus. For spectral values (0,1/sqrt2,1) and weights (sqrt2-1,sqrt2,1), independently expanded Q(a,c)=||A(aI+cA)b-b||²-E²||(aI+cA)b||² and verified positive-definite quadratic matrix with leading 3-sqrt2 and det (3sqrt2-4)/8>0, zero at (2(1+sqrt2),-4), proving all competitors have error >=E and attainable equality. SPD approximation follows continuity of strictly positive Q_{E-delta} for each delta>0. No randomized check supplies unrestricted proof.

## originality

PASS

Best-of-knowledge originality: The scalar contact polynomial gives upper bound but does not alone force lower bound against all x in K2; the exact positive-semidefinite residual quadratic with three nonzero weights and unique zero supplies that missing implication.

## value

PASS

A sharp attained finite-step bound for the actual Krylov optimization where motivating general result gives only 1 at k=2; three-point spectral-weight witness proves sharpness for genuine matrix systems rather than merely scalar approximation, with SPD limiting sharpness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
