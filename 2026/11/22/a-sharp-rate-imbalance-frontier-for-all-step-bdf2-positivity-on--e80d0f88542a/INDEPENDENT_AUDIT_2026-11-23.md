# Independent mathematical audit

## correctness

PASS

Reconstructed the analytic all-index proof in RESULT.md. The complementary stationary/centered projections give M_n=Π+z_n(I−Π), with unit row sums, off-diagonal sign set by 1−z_n, and diagonal lower condition z_n≥−min(a,b)/max(a,b). For 0<r<1/2 the real roots are (2∓√(1−2r))^−1 and the stated BE-started coefficients have the larger-root coefficient exceeding the subtracted one by one; thus z_n>0. At r=1/2 the repeated-root solution is 2^−n(1+n/3)>0. The first-difference recurrence then proves strict decrease in this regime. For r>1/2, matching z₀ and z₁ gives the stated trigonometric solution. Using |sin(nθ)|≤n sinθ bounds |z_n| by 2^−n(1+n/3), hence z_n<1 for n≥1 and |z_n|≤5/192 for n≥7. Independently checked the shifted polynomials from the recurrence and the four quadratic discriminants (−1843840, −101573568, −5495631872, −124090302464 in index order). The split about t=2 for P₃ and the positive higher coefficients in P₄–P₆ give strict positivity, so z₃,…,z₆>−29/1000>−(17−12√2). For n=2 the rational derivative has its only positive zero at r=3+3√2, a strict minimum with z₂=−(17−12√2); n=0,1 cannot tie. Reciprocating proves the claimed rate boundary and its unique normalized equality step for one diagonal. For fixed positive rates the real-root regime is safe and the complex-root bound also gives uniform |z_n|≤5/[3(3+2r)] for n≥2 as r→∞; z₁→0 separately. The exact 40:1 witness has r=7 and z₂=−1/34, hence (M₂)₁₁=−3/697. Inspected VERIFICATION.md, verify.py and the recorded output; did not execute the uploaded script. Its checks are finite support, not the all-index proof. Scope is constant step, irreducible two-state row generator, BE startup from one initial law and exact arithmetic.

## originality

PASS

Credit the scalar sign boundary and phase representation, standard stationary projection, and multistep monotonicity framework. The supported claim is the sharp quantitative global negative envelope, uniquely at the second step, and the consequent necessary and sufficient all-step imbalance frontier for the precise BE-started history. The nearest arbitrary-history classification includes classical BDF2 as a parameter value but demonstrably has different quantifiers.

## value

PASS

The sharp rate-ratio criterion answers a natural question not resolved by generic step restrictions: can a standard BE-started integrator preserve every initial probability for every step on the simplest irreducible exchange? It shows how a signed centered mode is compatible with positivity because of the stationary mass, gives an exact obstruction at the second step, and distinguishes intermediate failures from eventual large-step safety. This is an exact model-specific invariant and explanation, not a claim for general Markov generators.

The dated certificate retains the supplied scientific assessment, sources and limitations.
