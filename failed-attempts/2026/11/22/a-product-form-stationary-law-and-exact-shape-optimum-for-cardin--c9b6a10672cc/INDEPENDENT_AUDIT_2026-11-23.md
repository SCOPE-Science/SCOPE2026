# Independent mathematical audit

## correctness

PASS

Independently reconstructed the full invariant distribution using the chain of positions at redraws, avoiding any generator-core assumption. Put a=v/γ for one axis. From the normalized measure (dx+aδ₀+aδ_L)/(L+2a), a positive clipped flight of exponential duration has interior density [1−exp(−y/a)+exp(−y/a)]/(L+2a): the second term comes from the lower atom. It cannot leave an atom at 0 and has mass 2a/(L+2a) at L. Reflection gives the negative flight, and the fair-sign average preserves the original scalar measure. Every axis update therefore preserves the product, and so does the arbitrary-weight mixture. The mean occupation of each flight is obtained by integrating over ages s with density γ exp(−γs), since the durations are independent and exponential; the same signed-flight pushforwards give the heading-resolved law at an ordinary stationary time. This checks both wall and corner normalizations. A specified succession of long positive runs has positive probability independent of the initial state and resets every coordinate to the upper corner, proving fixed-time minorization and uniqueness. The outward-heading occupation gives force Nζv_i(w_i/2)·2a_i/(L_i+2a_i) on that face; division by V/L_i gives the stated P_i. Integrating force gives the log work potential. In log-lengths the fixed-volume constraint is affine and the Hessian strictly positive; the strictly increasing scalar product ∏ℓ_iλ/(D_i−λ) runs from zero to infinity, guaranteeing a unique stationary point and hence global minimum. No Monte Carlo assertion was used as proof.

## originality

FAIL

The exact hard-box formulas are correct, and neither of the two cited active-particle papers was found to state the combined box result in this form. Nevertheless, its central product and weight-invariance claims are direct random-coordinate lifts of the previously solved scalar clipped Laplace jump kernel. The precise implication is given below, including how the heading law, pressure and shape follow. The objection is prior mathematical coverage by a standard construction applied to an already solved kernel, not a claimed verbatim duplicate, nor an inference from search failure.

## value

FAIL

There is a clear physical motivation, and the formulas are useful as a benchmark or explanatory example. But this package, as a finding, adds no independent nonmechanical invariant to the known clipped single-coordinate law: the Cartesian product is preserved by each chosen update, the same flight law supplies its stationary occupation, and the optimization is of the resulting separable log potential with one scalar volume constraint. The record does not identify a further obstruction, a new shape regime, or another substantive question not already settled by those routine steps. The verdict is about research value of this exact package, not the general problem of hard-wall active-particle stationarity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
