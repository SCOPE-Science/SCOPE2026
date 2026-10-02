# Independent mathematical audit — SCOPE-20260919-f5661be14848

Final disposition: **FAILED**.

## Correctness
**PASS** — The two-block calculation is correct. Repeated mixed differentiation gives density \(1+	heta(1-2^rU)(1-2^sV)\). The two factors range independently over \([-(2^r-1),1]\) and \([-(2^s-1),1]\), so their product ranges from \(-\max(2^r-1,2^s-1)\) to \((2^r-1)(2^s-1)\), yielding exactly the stated asymmetric interval. The displayed \(r=2,s=1,	heta=1\) point has negative density. For entropy, each block factor is a mean-preserving martingale spread as its arity grows, and strict convexity of \((1+	heta z)\log(1+	heta z)\) makes KL divergence strictly increase whenever a block is enlarged in the interior parameter range.

## Originality
**FAIL** — A published September 18 result, 'Exact FGM thresholds and entropy defects for blockwise copula substitution', was read in full. It already gives the exact one-product-block threshold, the general Euler-operator differentiation criterion, the same \(r=2,s=1\) closure counterexample, and strict entropy nonadditivity in the valid region. Applying its Euler operator independently in the second FGM argument gives the assigned two-block density immediately; the interval is then a two-interval extremum calculation, and applying the same Jensen argument to the second block gives the assigned entropy monotonicity. The source correction and its substantive mechanism are therefore already covered, with the two-sided formula a routine iteration.

### Equivalent formulations
The two-block statement is the coordinatewise iteration of the prior one-block operator identity.

### Broader coverage
The earlier theorem contains the central correction and a more general differential mechanism.

### Exact database or table
The direct published hit is decisive prior coverage.

### Claim versus prior implication
The assigned two-block theorem is a mechanical iteration of the prior theorem, not an independently nontrivial extension.

## Value
**FAIL** — The symmetric two-block formula is neat, but after the September 18 general Euler-operator criterion and entropy-spread theorem it is a straightforward substitution and range calculation. The explicit closure and entropy counterexamples central to the source correction are literally already present in the earlier record. This does not clear the value bar for a separate finding.

## Source inspections
- **Exact FGM thresholds and entropy defects for blockwise copula substitution** (https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-fgm-block-substitution-threshold-entropy-defect--8e6f21783699): complete RESULT.md. Assessment: STRONG_PRIOR_COVERAGE_AND_MECHANICAL_IMPLICATION. Evidence: It proves the exact one-block threshold, general Euler-operator criterion, explicit \(m=2\) closure counterexample, and strict entropy defect.
- **Copula Operad and Copula Entropy** (https://arxiv.org/abs/2609.20512): primary abstract / indexed source record. Assessment: SOURCE_CONTEXT. Evidence: The source proposes unrestricted block substitution and entropy additivity, the claims already countered by the September 18 result.

## Residual risks
- No correctness defect is asserted; rejection is prior coverage plus mechanical implication.
