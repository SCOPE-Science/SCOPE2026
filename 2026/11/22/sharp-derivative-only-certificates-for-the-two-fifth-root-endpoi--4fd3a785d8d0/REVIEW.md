# Scientific review

## Correctness — PASS

The two quadratures are precisely the real fifth-root coefficient classes of Wang's four-term formula. The proof checks six polynomial moments, derives both sixth-order Peano kernels from truncated-power endpoint jets, and factors them into \(z^2(A-z)/720\) and \(-z^2(B+z)/720\) for \(z=t(1-t)\). Since \(A>1/4\) and \(B>0\), their signed difference is strictly positive on the interior. The error-to-rule-gap ratio is a positive weighted mean of a linear decreasing function of \(z\) with exact minimum and maximum. Smooth sixth-derivative bump sequences prove both constants are unimprovable. The stated minimax blend follows from equalizing these endpoint errors. The executable checker verifies the algebra exactly, but the all-function conclusion rests on the analytic proof.

## Originality — PASS, qualified

The motivating 2026 paper explicitly gives the fifth-root rules but does not give any of the signed sixth-order kernels, ratio-interval constants, or minimax a posteriori certificates. Closest shape-certification work establishes Gauss/Lobatto comparisons with different interior-point information. General interpolatory Hermite-error formulas concern a degree-seven rule and do not give the two stated fifth-root rules or their kernel ratios. Searches for equivalent formulas and exact constants disclosed no stronger published theorem in the inspected sources. The coefficients, polynomial exactness, the generic Peano principle, and Gauss/Lobatto comparison theory are **not** separately claimed as new. Historical priority is not independently certified; the relevant interpolatory Hermite paper was accessible at abstract level only.

## Value — PASS

The problem is directly motivated by evaluating the new complex-shift quadratures for a mathematically natural and practically testable shape class. Given the same endpoint derivatives, an otherwise broad raw gap collapses to a sharp certified interval with \(3.7268\%\) of that width, without estimating the magnitude of the sixth derivative. The unique minimax corrected output achieves a sharp gap-relative error constant of about \(1.8634\%\). This supports composite certified quadrature where derivatives are available, although no numerical roundoff study or derivative-evaluation cost model is claimed.

## Closest literature and limitations

Wang, arXiv:2602.01467v1, §3.2 and Table 3.1: source formulas only; directly inspected full text and its displayed page. Wąsowicz, arXiv:2601.16796v1: full available text inspected, Gauss/Lobatto rule and adaptive 5-convex certification. Kania–Wąsowicz, arXiv:2609.34918: abstract and public companion documentation inspected, general Gauss/Lobatto shape bounds. Bui-Thanh–Villatoro–Krishnanunni, arXiv:2602.18634: abstract inspected, interpolatory endpoint Hermite rule; full text not obtained. Historical priority remains provisional. The sign assumption, exact derivative access, absence of floating-point analysis, and no general optimality among all derivative quadratures delimit the theorem.

Self-review: passed. Independent audit: not yet performed.
