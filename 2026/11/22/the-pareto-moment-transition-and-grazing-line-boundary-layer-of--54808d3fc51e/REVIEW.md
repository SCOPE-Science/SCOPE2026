# Independent mathematical audit

## correctness

PASS

The conditioned invariant line measure makes the absolute offset S uniform. The half-length is sqrt(1-S²) minus sqrt((r²-S²)_+); the inner and outer branches are respectively increasing and decreasing. For q=w/2 on the two-root interval, the inner equation is inverted by adding and subtracting the two square roots, giving sqrt(1-S_-²)=(q+(1-r²)/q)/2. This gives both survival pieces (the central equality affects a null point), the maximum, and the mean by integrating the two disk chords. For fixed S<1 rationalization gives the stated weak limit, with domination by 2/sqrt(1-S²) even on the outer branch, proving the p<2 limit. At y=(1-S)/δ the limiting profile is H(y)=sqrt(2y)-sqrt(2(y-1)_+); for y≥1 the prelimit profile is bounded by 2/sqrt(y) up to y=1/δ and is set to zero beyond it. Its p>2 integral uses y=1/(2z²)+1/2+z²/8 on the descending branch z=H(y), giving the claimed coefficient. The two limiting roots at fixed 0<t<sqrt(2) are strict crossings; finite-δ monotonicity gives convergence of both roots and exact uniformity between the prelimit roots conditional on exceedance. For t≥sqrt(2) there is no exceedance because the scaled maximum is sqrt(2-δ). I independently verified the critical constant without elliptic integrals: let m=1-r², u=1-S², W_m=(sqrt(u)-sqrt((u-m)_+))², and g(u)=(1-u)^(-1/2)-1. The second moment is (2δ²)^(-1) times the integral of W_m(1+g) from 0 to 1. The unweighted integral divided by m² is 3/8-(1/2)log z+z⁴/8 for z=sqrt(m)/(1+sqrt(1-m)), by scaling u=mx and inverting sqrt(x)-sqrt(x-1). The weighted correction divided by m² is ∫g/(4u) du=(1/2)log 2, with error O(m log(1/m)): on u≤2m use g=O(u) and W_m/m²=O(1/u); elsewhere the kernel differs from 1/(4u) by O(m/u²). With m=2δ-δ² this gives (1/2)log(1/δ)+log(2sqrt(2))+3/4 with the stated remainder.

## originality

PASS

Bounded comparison supports the distinct thin-annulus moment transition, finite critical constant, and marked grazing law for total material intercept. The invariant-offset model and ordinary disk chord formulas are classical inputs, not new. Related works on nonconvex polygon chords and other geometries do not establish prior coverage on the evidence read.

## value

PASS

A thin annulus is a natural test of local-thickness approximations in line-intercept geometry. The limit has a finite first moment but divergent second moment; the exact critical finite part and supercritical coefficients tell where and by how much that approximation fails. The marked law identifies the offsets generating the rare long intercepts, not just a tail exponent.

The dated certificate retains the supplied scientific assessment, sources and limitations.
