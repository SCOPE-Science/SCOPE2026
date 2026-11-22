# Scientific review — cubic Blaschke composition amplification

## Correctness: PASS

The exact moment-generating function is the Hardy Parseval norm at a radius slightly greater than one. The rational modulus is maximized at positive real radius, giving a uniform logarithmic Laplace estimate with no asymptotic interchange of infinite sums. The expansion \(F(s)=Us+cs^3+O(s^5)\) is verified by exact differentiation; the coefficient \(c=U(U^2-1)/48\) is positive. A concave tangent gives the upper bound. Exponential tilting and two explicit Chernoff estimates localize the weighted coefficient mass within \(O(ns^2)\) of \(Un\), where the tangent deficit is only \(O(n^\theta s^4)\). Both error orders are strictly below \(ns^3\) when \(2/3<\theta<1\). The proof covers all integer degrees and all fixed parameters in the stated open domain, not merely numerical examples.

## Originality: PASS (qualified)

Inspected primary work: Szehr--Zarouf (2017) studies unweighted \(\ell^p\) norms of Blaschke powers; Borichev--Fouchet--Zarouf (2021) gives detailed individual Taylor coefficient asymptotics across the Airy and exponential regions; Lefèvre--Li--Queffélec--Rodríguez-Piazza (2023) treats weighted-Hardy composition boundedness and qualitative algebra phenomena. Their coefficient estimates are a plausible starting point from which a further weighted summation might yield the present result. The assessed statement, however, is a distinct sharp weighted Hilbert-norm logarithmic correction, and the complete comparison did not locate that coefficient or its tilted-moment argument in those texts. The published coefficient results do not state a uniform ready-to-use asymptotic for the exponentially weighted aggregate. Relevant mathematical index searches and own recoverable claims found no matching theorem. This remains a self-review; an independent literature review may find overlap.

## Mathematical value: PASS

Subexponential coefficient weights define natural regularity scales that can form Banach algebras while losing bounded composition by disk automorphisms. The result quantifies this failure on the canonical monomial tests in two distinct diverging scales. The positive \(n^{3\theta-2}\) term is invisible in a leading stretched-exponential bound and directly reflects the cubic geometry of boundary-angle dilation. The cutoff \(\theta>2/3\) is mathematically motivated because the cubic escape cost then dominates logarithmic finite-size effects; it is not an arbitrary degree or parameter slice. The result is a motivated sharp asymptotic rather than only a qualitative unboundedness example.

## Limits and closest literature

The analysis is restricted to fixed \(0<\lambda<1\), \(2/3<\theta<1\), a single Blaschke automorphism, and a specified coefficient weight. Critical and lower exponents, prefactors and arbitrary finite Blaschke products are not treated. The main residual overlap risk is that 2021 detailed coefficient asymptotics can be integrated after additional saddle analysis, or that specialized weighted norm asymptotics exist outside searched indexes. Supplementary finite rational checks support algebraic identities only; correctness rests on the printed analytic inequalities.

Self-review: passed. Independent audit: not yet performed.
