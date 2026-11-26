# Independent mathematical audit

## correctness

PASS

Using diag(1,-1,-1,-1), beta is effective (2E2+2E3+2D4+D2+D6), its six pairings are (2,1,1,2,1,1), and its anticanonical degree and one-point virtual dimension are both 8. The toric I-term with z prefactor is Q^beta z^(-7)/4 times [1-z^(-1) sum_i H_{D_i.beta} D_i+O(z^(-2))]. The divisor sum is (7/2)H-(1/2)E1-(3/2)E2-(3/2)E3. There is no positive-degree z^0 correction: for anticanonical degree 1 a nonnegative pairing vector would have to be a coordinate unit vector, but each unit vector violates at least one of k1+k2=k4+k5 and k2+k3=k5+k6, the two displayed divisor relations. A negative pairing gives a numerator factor D_i at m=0 and lowers the leading z-degree by at least one; degree at least 2 cannot contribute to z^0 either. Fano excludes nonzero effective classes of anticanonical degree 0. Thus after the standard classical divisor factor the small J coefficient of z^(-8), paired with H in the one-point insertion convention, is -7/8. H is self-dual, and 1/(z-psi) gives psi^7 at z^(-8). The result was checked by this derivation, not by trusting historical audit assertions; both named arithmetic scripts are present under source artifacts in this frozen package, even though the result's historical path note says they were absent from an earlier tree.

## originality

FAIL

The exact decimal-free value is not independently tabulated in the inspected sources, but follows mechanically from the established explicit toric I=J formula, with elementary checks of two divisor relations and a first-order product expansion. The record adds no new mirror theorem, correction term, or enumerative mechanism.

## value

FAIL

The surface and descendant theory are natural, but this one coefficient is a routine one-step specialization of an explicit prior formula. The record identifies no independent reason to need this particular coefficient, no unresolved boundary, and no new computation beyond substitution and arithmetic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
