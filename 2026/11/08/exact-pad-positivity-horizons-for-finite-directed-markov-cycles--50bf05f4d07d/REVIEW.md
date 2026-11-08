# Self-review

## Correctness — PASS

**Exact domain.** The claim covers the unit-rate homogeneous row-conservative directed cyclic generator \(Q_n=P_n-I_n\) in each integer dimension \(n\ge2\), for every real \(h\ge0\), and only the two-stage Gauss endpoint rational map. The denominator's roots are in the right half-plane, ensuring all matrix inverses exist. The map exactly preserves mass, so positivity is the only relevant stochasticity condition.

**Proof reconstruction.** For two and three states, complete rational entries establish positivity with a manifestly positive discriminant or positive coefficients. For dimensions four through seven, exact elimination and Descartes' one-sign-change rule give a unique root of the neighboring-entry sign polynomial. All *other* entries have nonnegative-coefficient numerators for dimensions four and five; for dimensions six and seven the exact transformed-polynomial positivity certificate covers the interval through the root, which lies below four. For dimension at least eight, the coefficient of degree seven in the stability function is negative and the unique seven-edge path gives the leading entry sign. For arbitrary cycle dimension the cyclic group-inverse identity and rational-map Laurent expansion establish the negative nearest-neighbor asymptotic for \(n\ge4\). Each step is an analytic argument, not extrapolation from tests.

**Reproduction.** The included Python/SymPy program passed 182 exact assertions involving the actual constructed matrices, rational sign brackets, polynomial positivity certificates, Taylor coefficients, and selected group-inverse checks. The bounded script does not purport to certify the unbounded quantifiers by enumeration. No other-run verification artifact is used.

## Originality — PASS, with residual precedence risk

**Equivalent forms.** Prior published records on the same Gauss rational map and on stochastic positivity were compared at the level of matrix class, all-step quantifier, and exact critical polynomial. The closest published conservative Markov result establishes *local* positivity in all dimensions at most seven, not the exact full-step positivity windows for the cyclic family. An existing symmetric-cycle Gauss result does not imply the directed-cycle result, because the matrices and spectrum are different. A directed-cycle Radau IIA classification uses a different rational map, with different thresholds and a different large-step sign.

**Broader coverage and databases.** General absolute-monotonicity/positivity obstructions and the eight-state pure-birth Padé result provide the \(n\ge8\) local-failure component already; it is explicitly attributed and not treated as new. No inspected source provided globally sharp values of \(H_4,H_5,H_6,H_7\) or the two/three-cycle unconditional contrast. An unidentified equivalent result in specialist Padé, circulant, or positivity literature remains possible. Inaccessible 2026 rational-propagator full text is a specifically noted residual risk.

## Mathematical value — PASS

The uniform directed-cycle generator is a canonical irreducible conservative test problem for Markov discretizations; exactly characterizing its fourth-order Gauss positivity provides an interpretable boundary between unconditional, finite-horizon and immediately failing stochasticity. The four complete sharp algebraic cutoffs are intrinsic answers to the nonnegativity problem—not arbitrary numerical samples—and the dimension transition complements general absolute-monotonicity results without claiming stronger generality than proved. This is useful for method-selection and checking step-size safety on cyclic transport test problems, while explicitly excluding nonlinear/general-generator conclusions.

Self-review: passed. Independent audit: not yet performed.
