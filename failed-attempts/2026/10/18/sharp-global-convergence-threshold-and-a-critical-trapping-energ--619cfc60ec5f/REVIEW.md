# Independent mathematical audit

## correctness

PASS

The vector field is globally Lipschitz. The (y,z) linear subsystem is Hurwitz with bounded forcing; the displayed quadratic Lyapunov part has determinant a+h(b−h)>0 in the strict regime, and its critical sum-of-squares form has compact sublevels on the positional cylinder. At equality put S=z+by/a, W=y−c sin(dx); then S′=−W and W′=aS−b(1+cos(dx))y, which together with the cosine potential gives E′=−b(1+cos(dx))y². On an invariant trajectory of zero dissipation, a nonzero y would force constant x on an interval, so y, z, and sin(dx) must vanish. LaSalle and connectedness select one of two equilibrium phases; continuity confines the late-time lift to one component of the inverse image of a small phase interval. At each even plane E≥2c², so a strictly lower initial energy prevents hitting either plane and even excludes those boundary equilibria as limits. Below threshold the Routh signs give one unstable eigenvalue at even equilibria and two at odd ones. Substitution of iω allows a nonzero imaginary root only at b=cd for odd parity; hence the strict subthreshold equilibria are hyperbolic. Their global stable manifolds are lower dimensional, and their countable union is null. The verification note and supporting Python were inspected, not executed; the finite tests are not needed for these conclusions.

## originality

FAIL

Distinct indexed record e9d0dcac064d states the same exact-system if-and-only-if theorem and proves the same subthreshold nullity. Its Lyapunov function is exactly −V_b in the frozen notation, not a different invariant. The critical energy differs by an additive constant after reversing sign, and the strip is a direct sublevel consequence. The overlapping public record's displayed date is later than the frozen path date; equivalence and implication are established here, not historical priority, authorship, or provenance.

## value

FAIL

The closed global dichotomy is a useful result, but is already covered. The remaining energy normalization and strip check use the same functional, its value on the two planes, and the known convergence theorem directly. They do not supply a distinct substantive boundary, invariant, or basin classification to retain on their own.

The dated certificate retains the supplied scientific assessment, sources and limitations.
