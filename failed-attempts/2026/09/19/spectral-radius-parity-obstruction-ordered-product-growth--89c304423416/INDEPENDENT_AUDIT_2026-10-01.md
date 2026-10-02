# Independent mathematical audit — 2026-10-01

## Final claim assessed

Spectral-radius parity obstruction to ordered-product Lyapunov convergence

## Correctness — PASS

PASS. The explicit period-two construction is correct. Direct differentiation gives the stated matrices at the two orbit points and their two-step product is diagonal with multipliers \(e^{2a}\) and \(e^{2b}\), so the per-iterate Lyapunov exponents are \(a\) and \(b\). Exact multiplication gives \(h_{2k}=a\) and \(h_{2k+1}=(a+b)/2\). For the representative parameters \(a=0.2\), \(b=-0.8\), \(s=0.8\), independent recomputation gives one-step spectral radii \(0.8\) and approximately \(0.6860145451\), odd-horizon rate \(-0.3\), even-horizon rate \(0.2\), and singular-value rate \(0.2\) at every tested horizon. The general periodic checkpoint identity and the subadditive singular-value replacement are also mathematically valid.

## Originality — FAIL

FAIL. A published 18 September 2026 record was inspected in full and already proves the same source-specific correction: a smooth deterministic periodic cocycle with a simple top Lyapunov exponent has \(h_{2k}=a\) and \(h_{2k+1}=(a+b)/2\), so the spectral-radius block rate need not converge; it also gives the eigenvector-alignment failure, periodic return-time identity, endpoint-transversality mechanism, frame dependence, and the singular-value repair. The present record supplies a cleaner planar period-two realization in which both one-step spectral radii are below one and the parity branches have opposite signs. Those are stronger witness features, but they are a routine strengthening of the already-published counterexample mechanism rather than a distinct final mathematical claim. Under the required implication/coverage standard, the packaged novelty claim therefore fails.

### equivalent_formulations

Searches: Resultary: ordered product spectral radius parity obstruction Lyapunov exponent smooth period two non-normal Jacobian h_L convergence; Published 2026-09-18 record: Ordered-product spectral growth need not converge to the top Lyapunov exponent

Evidence: The 18 September record states the same parity law for the same \(h_L\) statistic and explicitly identifies failure of the Oseledets-eigenvector justification. It also states the periodic return-time equality and singular-value replacement.

Reasoning: Changing the witness from a period-four cocycle to a planar period-two map and choosing parameters that reverse the odd/even signs strengthens the example but does not change the already-published final conclusion about nonconvergence of the source statistic.

### broader_coverage

Searches: arXiv:2609.18017 full primary text; arXiv:2507.19624 spectral radius cocycle convergence; Aoun Sert spectral radius random matrix products

Evidence: The primary source states on page 2 that \(h_L\) approaches the top Lyapunov exponent and attributes this to eigenvector alignment; the 18 September correction already refutes that statement. General cocycle literature distinguishes norm growth from spectral-radius growth and supplies convergence only under additional structure.

Reasoning: The decisive coverage is the earlier source-specific published correction; broader cocycle theory reinforces that the issue itself is not new.

### exact_database_or_table

Searches: Resultary semantic search for the exact ordered-product statistic and parity law

Evidence: The earlier 18 September published mathematical record is a direct theorem-level match.

Reasoning: A numerical database is inapplicable; exact published-record comparison is decisive.

### claim_vs_prior_implication

Searches: Complete RESULT.md of 2026/9/18/SCOPE-ordered-product-spectral-rate-nonconvergence--4cd423fedf50; Primary arXiv:2609.18017 pages containing Eq. (1) and its convergence claim

Evidence: The earlier result already establishes the same failure of \(h_L\to\lambda_1\), the parity formula, and the standard repair. The current map merely realizes the same mechanism with stronger local spectral stability.

Reasoning: The principal final claim is directly covered; the extra witness properties do not rescue originality of the package.

## Scientific value — PASS

PASS. The strengthened witness is scientifically useful because it shows that every individual step can be spectrally stable while the top Lyapunov exponent is positive and the proposed diagnostic alternates stability sign forever. The source correction itself is important. Rejection is due to prior coverage, not lack of mathematical relevance.

## Source inspections

- **A New Route to Chaos through the Geometric Composition of Non-Normal Amplification** — https://arxiv.org/abs/2609.18017. Material read: Primary full text through the main statement and relevant supplement sections, including Eq. (1), the claimed approach to the Lyapunov exponent, and the exact periodic-return discussion. Assessment: SOURCE_STATEMENT_CONFIRMED. Evidence: The paper explicitly says that as \(L\) increases, \(h_L\) approaches \(\lambda_1\) and attributes this to leading-eigenvector/Oseledets alignment.
- **Ordered-product spectral growth need not converge to the top Lyapunov exponent** — https://github.com/Resultary/2026/blob/main/2026/9/18/SCOPE-ordered-product-spectral-rate-nonconvergence--4cd423fedf50/RESULT.md. Material read: Complete published result. Assessment: DECISIVE_PRIOR_COVERAGE. Evidence: It proves the same parity nonconvergence for the same source statistic, supplies the endpoint-transversality mechanism and frame-dependence explanation, and recommends the singular-value rate.

## Limitations and residual risks

The failed finding remains mathematically correct as a stronger example, but it is not accepted as an original validated finding because the same source-specific convergence obstruction was published one day earlier.

- None affects the originality failure. The current planar one-step-stable witness is stronger than the earlier witness, but the package's principal source-correction theorem is already published.

## Disposition

**failed**
