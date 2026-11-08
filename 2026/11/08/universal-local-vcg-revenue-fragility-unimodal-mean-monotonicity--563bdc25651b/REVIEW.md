# Self-review

## Correctness

**PASS.** The VCG pivot-payment identity reduces the two-by-two market to the signed difference formula \(R(S,T)=S_++T_+-\max(S,T)\). All quadrant boundaries are included. Independence and item exchangeability make the preference gaps iid and symmetric, yielding exact derivative probabilities \(1/8,1/8,3/4\). Pairing positive and negative gaps reduces ex-ante revenue to a shifted absolute-gap integral, and symmetric unimodality proves stochastic monotonicity. The continuous bimodal model is backed by an exact two-sign reference and a uniform Lipschitz bound; finite uniform-shock probability and expectation curves follow by explicit density integration. An executable independent externality calculation and exact symbolic integral checks passed. Finite computations are not used as proofs of continuous statements.

## Originality

**PASS, subject to external priority risk.** The closest primary paper, Hartline (2026), contains the same small matching-market mechanism and explicit dropping-revenue example but no prevalence, distribution-free one-eighth gradient law, unimodality condition or response-curve integrals. Gul and Stacchetti (1999) supply the broader price framework, not a directly observed probability model. Searches of indexed scholarly summaries for the exact incidence, minimum Walrasian prices, preference gaps, unimodality and finite bid shocks returned unrelated assignment/price and stochastic-order records. See `AUDIT.json` for searches, actual retrieved identifiers, inspected materials and implication comparisons. Search nonhits are not novelty proofs. The 1999 and 2007 primary full texts were not read, and unindexed equivalent work remains a risk.

## Mathematical value

**PASS.** The quantitative risk of the canonical two-object VCG revenue anomaly is a motivated mechanism-design comparative static. The exact local incidence holds without item independence; the shape condition yields a new general sufficient criterion for mean revenue monotonicity while an atomless bimodal counterexample rules out a naive unconditional extension. The uniform full-shock laws quantify frequency and expected economic loss, rather than merely restating a deterministic example.

## Limitations

The result concerns exactly two unit-demand bidders and two goods, no reserves, standard pivot payments, independent exchangeable bidder vectors, atomless gaps, and a unimodality condition for general mean monotonicity. Uniform response polynomials require four independent uniform initial values. The theorem is not about strategic truthful-report changes or larger auctions. No independent audit was conducted.

Self-review: passed. Independent audit: not yet performed.
