# Independent mathematical audit

## correctness

PASS

The observed DC component fixes the mean; the only real invisible modes are sine and cosine at k. Cyclic differentiation is invertible on that span, coprimality permutes its sample phases, and even n makes y_(j+n/2)=−y_j. The usual triangle inequality shows strict uniqueness if the mass on every s-set is strictly below half. For necessity, choose a maximum phase and a top set containing a nonzero antipodal pair, which is possible for s≥2, and take a gradient supported at the selected nonzero sites with signs opposite y and total zero (each sign class is weighted by the size of the other). This integrates to a cyclic signal and gives the directional TV change ||y||_1−2||y_S||_1, including nonuniqueness or nonoptimality at equality. For s≤1 a top magnitude is strictly less than half: its antipode contributes equally and other magnitudes are nonzero. For fixed signs and ordering the ratio is a quotient of two linear trigonometric forms; the derivative numerator is constant and the denominator positive. Nonidentical absolute ties and sample zeros are at multiples of π/n, while shifting by 2π/n only permutes samples. Therefore the two grids give the global maximum, including breakpoints and constant pieces. The top-s variational identity and uniform Riemann sums yield the upper-p fraction of the |cos| mass, sin(πp/2) (including p=0,1); monotonicity and comparison at p=1/3±δ give the first-failure limit. At n=6 both grids have top-two fraction 1/2. Replay from the frozen proof, RESULT.md lines 37–68; the floating-point checker was inspected, not executed, and its sampled ceil(n/3) observation is not needed or credited as the stated theorem.

## originality

PASS

Credit the previous cyclic differentiation/Fourier reduction and standard sparse-gradient nullspace methodology. The supported distinct part is the exact two-grid evaluation of top-s mass for this deterministic primitive conjugate-pair erasure, with a realizable cyclic-gradient failure witness and a sharp one-third limit. A near-complete Fourier set under deterministic erasure is not the probabilistic recovery regime of the inspected Fourier theorems.

## value

PASS

Asking how sparse gradients must be for uniform uniqueness after minimal real Fourier information is removed is a natural deterministic recovery question. The exact finite criterion is independent of the primitive missing frequency, and the one-third boundary and explicit feasible witnesses quantify a nontrivial uniform obstruction even though almost all measurements are kept.

The dated certificate retains the supplied scientific assessment, sources and limitations.
