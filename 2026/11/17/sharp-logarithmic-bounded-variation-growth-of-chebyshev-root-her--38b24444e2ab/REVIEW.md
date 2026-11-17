# Scientific review

## Correctness — PASS

The cardinal polynomial follows from the Chebyshev derivative identities, and positivity plus unitality is exact. The norm is exactly the maximum variation of the \(n-1\) individual step responses: the discrete jump decomposition provides the bound, and each step is realizable by unit-variation input. Counting \(n\) stationary knots and at least one interior stationary point in each of the \(n-2\) same-label gaps exhausts the derivative's degree \(2n-2\), so the interval-by-interval variation formula is exact. The angle-difference squared-cosecant component yields \(\pi^{-2}\log n\) from each half and the reflected component contributes a uniformly bounded sum. Independent central-step midpoint estimates yield the matching coefficient. The numerical checker replays successfully. Risk: the result is only accurate up to \(O(1)\), not an exact finite-degree norm.

## Originality — PASS, qualified

Direct statement/implication comparisons were made with Fejér's classical positivity and uniform convergence, Al-Jarrah–Rababah (1990) full-text pointwise BV approximation estimates, Xiang–He (2020) full-text smooth-function convergence bounds, Gautschi's interpolation survey, Smith's extended-node Lebesgue-function results, and semantically nearest research records. None of the inspected materials asserts the \(BV\to BV\) seminorm asymptotic with coefficient \(4/\pi^2\), nor implies that coefficient from the reported uniform-error or \(L^\infty\) bounds. The Bojanic–Cheng (1983) conference paper and Smith (2002) full text were not accessible for direct inspection, leaving nonzero historical-priority risk. Search absence alone is not proof of novelty.

## Mathematical value — PASS

This determines a sharp asymptotic stability constant for a canonical positive interpolation scheme over all bounded-variation inputs and gives an explicit attaining family at leading order. The unexpected functional-space separation is intrinsic: \(\|H_n\|_{\infty\to\infty}=1\) for every degree while the variation seminorm grows logarithmically. Such stability distinguishes preservation of signal range from control of oscillatory edges and can inform the use of positive high-degree interpolation on discontinuous data. The result does not rely on an arbitrary sample size or a known-table recomputation.

## Literature and limitations

The 1983 paper is a genuine unresolved literature inspection; the scanned 1990 article records its pointwise result but does not substitute for reading the 1983 text. The 2002 Smith result concerns the endpoint-extended Chebyshev system. The theorem does not treat arbitrary Jacobi nodes, endpoint-extended nodes, exact fixed-degree constants, or complex input. It is a self-review, not an independent audit.

Self-review: passed. Independent audit: not yet performed.
