# Independent mathematical audit

## correctness

PASS

Within each resident group with equal susceptible and vaccinated generators, sum the two DFE balances to see that its total distribution and hence the physical-location denominators are invariant under vaccination changes. The susceptible difference satisfies the displayed positive-right-hand-side equation: the nonsingular M-matrix inverse is nonnegative, since the transpose is strictly diagonally dominant from positive death and nonnegative vaccination. Thus susceptible counts, and their effective-susceptibility convex combinations with invariant totals, cannot increase. The infectious transition matrix is fixed and inverse-positive, so Perron monotonicity applies. No equality with infectious mobility is used. In the separate fixed toy example the independently reconstructed population and infection matrices agree with the frozen ones; both physical-location denominators remain positive. The background next-generation matrix lies strictly below threshold by the stated infinity norm bound. Relative to that background the perturbation is rank one. At a spectral parameter above the background spectral radius, the corresponding scalar from the nonnegative resolvent of the background next-generation matrix is decreasing, and equals one at the perturbed Perron root. Evaluating at one gives the threshold sign, including equality; a determinant sign without this perturbation argument would not suffice. For an independent integer expansion of RESULT.md's frozen matrix, put L=31-19t and Q=31+19t and clear its four rows of W-F by 40L, 20Q, 20L, 10Q; a cofactor expansion gives 80L times the displayed P. Endpoint derivative signs and convexity of P' give strict decrease on [0,1]; exact bracket signs at 9/20 and 23/50 and a positive denominator give one simple crossing. The irreducible next-generation matrix, with the primary model's DFE theorem, supplies the stated local threshold, not a global outcome claim. The packaged verify.py and VERIFICATION.md were inspected, not executed; the comparison and exact frozen-matrix check, not the recorded script run, are the review evidence.

## originality

PASS

The model, next-generation threshold machinery, and broad possibility of offsetting protection through changes in behavior are not new. The supported contribution is the precise fixed-parameter sufficient condition for comparative monotonicity in this model together with a certified, strictly positive finite example that demonstrates why dropping the condition does not preserve the guarantee. The classical resolvent and Perron arguments are credited rather than claimed novel. No novelty is asserted for the underlying qualitative public-health idea; historical overlap with related earlier vaccination models remains possible.

## value

PASS

A condition under which the uptake comparison is reliable despite heterogeneous efficacy, contacts, ongoing vaccination and infectious movement is useful for interpreting a spatial model. An exact admissible counterexample shows that the guarantee cannot simply be carried over once the mobility assumption changes; a complete single-parameter threshold analysis is stronger than one simulated reversal. The value is limited to model sensitivity and interpretation, not empirical vaccine advice or a general nonlinear epidemic prediction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
