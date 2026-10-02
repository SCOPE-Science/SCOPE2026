# Independent audit — 2026-10-01

Final claim assessed: An equal-weight K-component binomial mixture with r known support anchors is globally identifiable exactly when the binomial trial count satisfies N at least K minus r.

## Correctness — PASS

The binomial law determines raw moments through order N by factorial moments. Equal weights and known anchors therefore determine the first M power sums of the M unknown support points. Newton identities recover the support polynomial from the first M power sums. Below M, perturbing only the constant coefficient of a simple-root polynomial preserves the first M minus one power sums while changing the support, giving sharp nonidentifiability.

## Originality — FAIL

After reduction to moments, the claim is a direct classical consequence of Newton–Girard identities: M equal-weight atoms are determined by their first M power sums, while the first M minus one power sums leave the constant coefficient free. The binomial observation model merely supplies those moments. This implication is standard finite-moment/symmetric-polynomial theory even though the exact mixture-model wording was not located.

## Scientific value — FAIL

The result is correct and may be pedagogically useful, but under the required value bar it is a routine textbook deduction once equal weights are imposed: no nonstandard structural lemma, difficult boundary, or independently motivated new invariant remains after the moment reduction.

## Sources and residual risks

- Classical Newton–Girard identities relating the first M power sums to the coefficients of a monic degree-M polynomial.
- Prony/finite-atomic moment literature, including Kunis–Peter–Römer–von der Ohe, Linear Algebra Appl. 490 (2016).
- Classical binomial-mixture identifiability literature cited in the package.
- Published-record semantic search for equal-weight binomial mixture thresholds.
- The failure is not a correctness defect; it is an originality/value determination under the implication-based standard.
- The theorem concerns exact identifiability only and says nothing about conditioning or noisy recovery.
