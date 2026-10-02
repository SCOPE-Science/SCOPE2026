# Legendre degree-parameter parameterized Galois trichotomy

## Context

The Legendre equation with degree parameter is a classical Fuchsian equation with
three regular singularities. Its unparameterized differential Galois group is a
textbook Kovacic exercise, but its parameterized Picard-Vessiot (PPV) group,
which records differential-algebraic relations among solutions with respect to
the parameter derivation, was not recorded. Deciding the PPV trichotomy
(reducible Borel, imprimitive dihedral, or Zariski-dense) together with an
isomonodromic versus non-isomonodromic verdict is the admitted target.

## Definitions

Let C be algebraically closed of characteristic 0 and
F = C(t,x) with commuting derivations dx(x) = 1, dx(t) = 0,
dt(x) = 0, dt(t) = 1.
Consider the Legendre degree-parameter operator

L(Y) = (1-x^2) dx^2 Y - 2x dx Y + t(t+1) Y = 0, nu := t(t+1),

i.e. dx Z = A Z for its companion matrix. Put t transcendental over C
(generic t); integer values t in Z are the exceptional locus.
The unparameterized Picard-Vessiot theory is taken over K = C(t) in x;
the parameterized theory adds dt with dx-constants C(t).
With p = -2x/(1-x^2) and q = nu/(1-x^2), the normalized Riccati equation
for z'' = r z is v' + v^2 = r with

r = p^2/4 + p'/2 - q = nu/(x^2-1) - 1/(x^2-1)^2.

The PPV group G is a linear dt-differential-algebraic subgroup of SL2 over C(t).

## Result

Generic (t transcendental): exactly case (C) of the trichotomy holds.
The normalized equation admits no rational Riccati solution
(Kovacic cases 1, 2, 3 all fail), so the unparameterized PV group is SL2.
Nontrivial unipotent local monodromies at x = +/-1 independently exclude
the dihedral case (B). The trace Tr(M_infinity) = 2cos(2 pi t) is
nonconstant in t, so the family is non-isomonodromic and the PPV group is
SL2 as a dt-differential-algebraic group with defining dt-ideal (det-1)
and no further dt-equations, up to SL2(conj). The irreducibility witness
is the Riccati equation v' + v^2 = r having no solution in C(t,x).

Integer exceptional set (t in Z): the trichotomy collapses to case (A).
The Rodrigues polynomial P_n gives a rational Riccati solution
(e.g. w = 1/x at t = 1, v = (2x^2-1)/(x^3-x) in normalized form),
the system gauges to upper-triangular Borel form, and the PV group is
the unipotent Ga inside a Borel.

## Proof and evidence

Normal form: symbolic verification confirms r from p,q agrees identically
with the closed form nu/(x^2-1) - 1/(x^2-1)^2. Partial fractions give
double poles at x = +/-1 with coefficient b = -1/4 (alphas 1/2,
E = {2}) and ord_infinity r = 2 with b_inf = t^2+t,
sqrt(1+4 b_inf) = 2t+1, alphas {t+1,-t}, E_inf = {2} for transcendental t.
Case 1 needs d = alpha_inf - 1 in N0, i.e. t or -t-1, impossible for
transcendental t. Case 2 needs d = (2-2-2)/2 = -1, impossible.
Case 3 needs every sqrt(1+4b) rational, but 2t+1 is transcendental.
Hence no Liouvillian solution; with Wronskian 1/(1-x^2) in F the PV group
is SL2. Original-equation exponents at x = +/-1 are {0,0} (indicial
rho^2 = 0) giving nontrivial unipotents, which no infinite dihedral
subgroup of SL2 contains; at infinity exponents {t,-t-1} are
non-resonant with Tr(M_inf) = 2cos(2 pi t), evaluated 1.618/0.618/-0.618
at t = 0.1/0.2/0.3 with nonzero t-derivative. By Arreche density the PPV
group is Zariski-dense in SL2; by Cassidy-Singer a dense dt-subgroup is
SL2 or conjugate to SL2(C), the latter iff isomonodromic (zero-curvature
Lax matrix B). Moving trace contradicts Schlesinger constancy, so no such
B exists and G = SL2 with dt-ideal (det-1). Integer case: Rodrigues
P_0..P_3 residuals zero; t = 1 Riccati residuals zero as above;
upper-triangular gauge gives PV group Ga. All computations reproduced by
output/artifacts/verify_legendre.py.

## Limitations

Algebraic non-integer t (especially t in 1/2+Z, where 2t+1 in 2Z makes
E_inf larger and Kovacic cases 1-2 can succeed) are outside the claimed
trichotomy and not resolved here. The isomonodromy argument uses analytic
continuation in t (specialization to a complex disc), standard but not
purely differential-algebraic. Lax-pair nonexistence is deduced via
monodromy rather than a direct rational-B pole analysis.
PPV existence and conjugacy use the standard base change to the
differential closure of C(t).

## Reproducibility

Run python3 output/artifacts/verify_legendre.py with sympy installed.
It prints r, pole data b_1 = b_-1 = -1/4, b_inf = t^2+t, case-1 options,
case-2 degree -1, Wronskian check 0, indicial data, infinity exponent
confirmations, Rodrigues residuals, and the moving-trace values.

## References

Kovacic algorithm and criterion; Arreche Zariski-density of PPV groups;
Cassidy-Singer classification of Zariski-dense dt-subgroups of SL2 and
isomonodromy (zero-curvature) criterion; Schlesinger isomonodromy implies
constant monodromy; Fuchsian local theory (exponents to monodromy
eigenvalues in the non-resonant case); DLMF 14.2 Legendre differential
equations; Arreche arXiv:1208.2226 parameterized Kovacic algorithms.
