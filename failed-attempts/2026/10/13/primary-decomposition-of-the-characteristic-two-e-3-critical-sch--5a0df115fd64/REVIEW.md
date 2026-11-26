# Independent mathematical audit

## correctness

PASS

In characteristic two, f₄=f₁+f₂+f₃ and Euler's identity gives e₃=Σ xᵢfᵢ, so adjoining e₃ does not change the derivative ideal. Xie's exact dimension gives height three; the three quadrics in the polynomial ring form a complete intersection, unmixed of degree eight. The four axes have length two generically by Xie and already exhaust the degree. For fixed i and distinct remaining indices a,b,c, f_a+f_b=(x_a+x_b)(x_i+x_c); the second factor is a unit at the axis prime P_i. These identities force the three off-axis coordinates to coincide in R_{P_i}/I. Then f_i gives the square of their common coordinate, and conversely all partials vanish when the three equal coordinates have square zero. The quotient by the contracted ideal Q_i is K[x_i,t]/(t²), whose zero divisors are nilpotent (an element with nonzero constant-in-t part is regular), so Q_i is P_i-primary. The contraction equals the isolated component at P_i, and distinct axis primes give an irredundant intersection. Unmixedness leaves no embedded component; inverting x_i eliminates the other three components, also verifying the claimed saturation. An independent exact SymPy 1.14.0 elimination replay over GF(2) checked all four saturations, the full ideal intersection, and the Euler membership. The algebraic argument proves the field-level statement; the finite ideal identity also persists by flat field extension.

## originality

FAIL

The exact four-variable affine result is a routine consequence of the predated and cited Xie theorems and their proof. Crucially, Xie's §4.1 supplies not merely an abstract generic length: it identifies the embedded off-support differences and the remaining t^Q ideal in the resulting local coordinate. At n=4,d=3,p=2 these are exactly the localizations of the stated Q_i. The dimension theorem and three visible quadrics then give a degree-eight unmixed complete intersection; the four known length-two axes exhaust degree, and contracting the four primary local ideals gives precisely the claimed intersection. Xie's remarks about general unresolved primary decompositions are accurate, but this special case is covered by a short standard deduction. This is established prior implication, not a verdict based on an inaccessible source or a later duplicate.

## value

FAIL

An explicit primary decomposition of a critical scheme and control of its cone vertex are natural objectives. Here, however, all four embedded generic ideals are already furnished by the prior local-coordinate theorem, and the three-quadric complete-intersection degree forces the entire global scheme, leaving only routine contractions. The exact computational replay is useful as an illustration but is not a surviving distinct valued finding; no broader new case, obstruction or method is proved in the frozen record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
