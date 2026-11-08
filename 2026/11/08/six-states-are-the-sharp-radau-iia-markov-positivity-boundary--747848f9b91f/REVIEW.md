# Self-review

## Correctness — PASS

The quantifiers separate all finite row-conservative Markov generators in dimensions at most five from an explicit six-state pure-birth generator. The two-stage third-order Radau IIA end-step map has an everywhere-defined denominator on generator spectra and preserves row sums. Its first four nonconstant Taylor coefficients are positive, giving local entrywise positivity through shortest directed paths of length at most four. The six-state absorbing-column entry is exactly \(h^5P(h)/(h^2+4h+6)^5\); differentiation gives one and only one positive zero of \(P\), and explicitly positive remaining entry types on its interval establish the full stochasticity set. The derivative and absorber identities were reconstructed independently with exact symbolic algebra; the packaged dependency-free rational checker agrees with all 36 entries at 14 exact steps. The infinite-dimensional quantifier and exact threshold rely on the proof, not on sampled matrices.

## Originality — PASS, with residual priority risk

The closest explicit published analogue establishes an eight-state Markov positivity obstruction for the *diagonal* \([2/2]\) Padé map, rather than the \([1/2]\) Radau IIA map considered here. Its different Taylor cancellation and higher first wrong-signed coefficient do not imply this six-state cutoff or the polynomial stochasticity interval. Zappavigna–Colaneri–Kirkland–Shorten (2012) analyze diagonal Padé positivity on nonconservative Metzler examples; their examples do not enforce zero generator row sums. Lóczi–Ketcheson (2013) studies generic absolute-monotonicity radii, not sharp conservative state-space dimension and full entrywise stochasticity windows. Brugnano–Iavernaro–Magherini (2013) treats efficient Radau collocation implementation, and Bonaventura–Della Rocca (2015) focuses on TR-BDF2. published-finding corpus semantic searches for the method, aliases, pure-birth chains, Padé order, conservative Markov generators, dimensions and stochasticity windows did not return an equivalent result. A negative search is not proof of priority: unindexed work on subdiagonal Padé applied to Markov generators remains an explicit risk.

## Mathematical value — PASS

The smallest dimension of a Markov generator capable of losing nonnegativity for *arbitrarily small* integration steps is a natural structural invariant of a numerical one-step method. The sharp six-state cutoff for a standard L-stable third-order collocation method and the exceptional disconnected set of safe steps for a concrete six-state CTMC jointly identify a material Markov-positivity failure mode: reducing the step does not necessarily repair stochasticity. The classification is exact, applies to every generator up to the threshold, and is not a routine numerical observation or a mere change of notation from diagonal Padé results.

## Scientific limitations

The cutoff is local for each generator below dimension six; there is no dimension-only step-size bound for unbounded rates. The exact safe-step set concerns the specified pure-birth chain, not all six-state generators. Only end-step stochasticity is addressed; stage values, nonlinear problems, floating point and other numerical methods remain outside the claim. The originality comparison is not exhaustive; no independent scientific audit has been conducted.

Self-review: passed. Independent audit: not yet performed.
