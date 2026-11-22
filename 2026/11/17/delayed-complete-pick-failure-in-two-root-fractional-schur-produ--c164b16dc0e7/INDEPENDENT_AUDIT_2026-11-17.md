# Independent mathematical audit

## correctness

PASS

The normalized complete Pick coefficient test applies to 1-1/K because the first factor has strictly positive Taylor coefficients and the second is a complete-Pick pullback by z->z^2, even though it identifies opposite points. For F_b(t)=(1-t)^(a+b)(1+t)^b, c_n=-[t^n]F_b. The two unit-circle branch points contribute A(b)n^(-a-b-1) and (-1)^n B(b)n^(-b-1), where A=-2^b/Gamma(-a-b) and B=-2^(a+b)/Gamma(-b). For fixed b the (-1)^n term dominates, giving infinitely many negative odd coefficients; for small b, B~2^a b and A->a/Gamma(1-a). The uniform remainder O(n^(-a-b-2)+b n^(-b-2)) yields n^(a+1)c_n -> a/Gamma(1-a)+(-1)^n 2^a x for bn^a ->x, and a split finite-prefix/uniform-margin argument locates first obstruction N_a(b)~[a/(2^a Gamma(1-a)b)]^(1/a). Separate exact rational coefficient recurrence reproduced N_(1/2)(1/100)=403 and N_(1/2)(1/200)=1603; a=1 yields exactly 3. Finite coefficients corroborate but cannot establish infinite signs or uniform transfer bounds.

## originality

PASS

The published sparse resolvent-factor criterion K=((1-t)^alpha(1-tau t^m))^-1 has integer pole power and amplitude tau. At tau=1, m=2 it yields failure at a fixed early index, but does not cover fractional b->0 and N~C b^(-1/a). Published monomial-defect studies place 1-st^m in the numerator, a different perturbation. Bhattacharyya et al 2026 analyze functionals for given Schur factorizations, not when the product remains complete Pick. Thus no checked source implies the delayed sharp witness asymptotic.

## value

PASS

Schur products of individually complete Pick kernels need not retain complete-Pick interpolation. The exact singular-perturbation scale of the FIRST negative reciprocal coefficient quantifies why arbitrarily deep finite checks may fail to detect the defect; parity-dependent two-endpoint asymptotics explain the mechanism.

The dated certificate retains the supplied scientific assessment, sources and limitations.
