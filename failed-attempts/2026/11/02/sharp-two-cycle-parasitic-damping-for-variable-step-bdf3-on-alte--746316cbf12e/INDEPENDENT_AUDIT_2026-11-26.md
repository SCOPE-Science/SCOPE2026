# Independent mathematical audit

## correctness

PASS

A fresh exact derivative-moment solve on 1,t,t^2,t^3 gives the increment transfers on (r,1,r) and (1,r,1). The resulting characteristic traces and determinants agree for the two orders of the products and under r↔1/r. For w=5z, all three real monic quadratic Schur expressions have strictly positive numerators and a positive denominator for every r>0; the limiting characteristic polynomial is z(z+1/5). At fixed ratio, the product powers decay geometrically even if a Jordan block occurs; the intervening one-step transfer is fixed and finite, so the increments are absolutely summable. Neither a ratio-uniform norm bound nor stability at nonzero test-equation eigenvalues follows. The frozen verifier was inspected, not executed. Independent replay: python3 /workspace/reproduction/1.py (SymPy); passed the exact identities, reciprocity and limit checks.

## originality

FAIL

A distinct published Resultary record states the complete strict all-ratio 1/5 Floquet bound and sharp supremum for the same recurrence, and gives the same reduced trace and determinant. Passing from values to differences quotients out the constant mode; it does not produce different multipliers or a distinct theorem. The matched record additionally resolves the real/conjugate regimes. The shared calendar date does not establish order or priority; this is a positive finding of equivalent coverage, not a priority assignment.

## value

FAIL

The sharp uniform period-two damping factor is a useful structural fact: it separates asymptotic cancellation from a possible large one-step transient and from general adjacent-ratio restrictions. As a separate submission, however, this exact invariant and its consequences supply no further mathematical payoff over the matched, more informative classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
