# Independent mathematical audit — 2026-10-01

## Final claim

Unique BHM maximizers and a quantitative standard-to-lazy gap transfer

## Correctness — PASS

PASS. The equality classification and the quantitative inequality are mathematically correct. In Zhu's single-class tree case, the edge increments are independent and each nonzero-edge probability is at most one half; equality forces every such probability to be one half. Chasing equality through both bipartition classes forces maximum degree at most two, and the remaining even-cycle cases are strict, leaving only a path. For the gap transfer, zero-edge contraction gives a nonnegative defect term for every contraction; retaining only the no-zero-edge event yields exactly the stated lower bound with its probability factor.

## Originality — FAIL

FAIL. Zhu's full 2026 proof already contains the ingredients that mechanically imply both claimed contributions. Proposition 4.4 gives strictness for cyclic auxiliary graphs and, in the tree case, an explicit independent-Bernoulli comparison whose equality condition is immediate. The proof of the BHM theorem then reduces global equality to an equality-case chase. In Section 5, the identity expressing lazy expected range as the expectation of standard expected range over zero-edge quotients is followed by the path comparison; retaining the nonnegative contribution from the no-zero-edge event gives the displayed quantitative gap transfer directly. Under the audit rule that corollaries and mechanically implied refinements count as covered even when not stated verbatim, the final claim is not original.

### equivalent_formulations

Searches: published-record search for BHM equality classification and standard-to-lazy deficit transfer; full-text comparison with Zhu 2026 auxiliary-graph and zero-edge-contraction proofs

Evidence: The exact record appeared in the published-record search, but the decisive evidence was the prior primary proof rather than the absence of an exact title match.

Reasoning: The equality criterion is the equality-case formulation of Zhu's single-class comparisons, and the gap transfer is a one-event lower bound inside Zhu's contraction identity.

### broader_coverage

Searches: Zhu 2026 BHM theorem full proof; Wu-Xu-Zhu 2016 tree equality cases; Bok-Nesetril pseudotree range inequalities

Evidence: Zhu proves the general BHM inequality, strict cyclic auxiliary comparison, and the lazy contraction implication; earlier tree work supplies the path equality background.

Reasoning: The prior primary proof is broader than the audited equality/gap statements and contains enough quantitative structure to derive them without a new independent theorem.

### exact_database_or_table

Searches: published mathematical record semantic search for path uniqueness and gap transfer

Evidence: No earlier record with the exact combined headline was located.

Reasoning: That absence does not establish originality because the stronger implication coverage in Zhu's proof is decisive.

### claim_vs_prior_implication

Searches: Zhu Proposition 4.4 and Theorem 1.1 equality chain; Zhu Proposition 5.5 and zero-edge contraction identity

Evidence: The tree comparison uses independent Bernoulli variables with parameters at most one half, cyclic auxiliary graphs are strict, and the lazy proof writes the target defect as an expectation of nonnegative quotient defects.

Reasoning: These statements mechanically imply the audited equality characterization and the no-zero-event quantitative lower bound.

## Scientific value — PASS

PASS. Equality cases for a newly proved extremal theorem and a quantitative bridge between its standard and lazy models are natural, motivated questions. The rejection is not a value judgment on the mathematical questions; it is caused by prior implication coverage.

## Source inspections

- **Yinfeng Zhu, Paths maximize the expected range of graph-indexed random walks** — https://arxiv.org/abs/2609.19728. Material read: Full text, including the auxiliary-graph comparison, equality-sensitive tree and cycle cases, the proof of Theorem 1.1, and Section 5 through Proposition 5.5. Assessment: COVERING_BY_IMPLICATION. Evidence: The paper does not state the audited headline verbatim, but its proof contains the equality conditions and the nonnegative contraction-defect decomposition from which both audited contributions follow directly.
- **Yaokun Wu, Zeying Xu and Yinfeng Zhu, Average Range of Lipschitz Functions on Trees** — https://zhuyinfeng.org/Data/Preprints/MJCNT16.pdf. Material read: Published theorem/corollary context identifying unique path equality for the tree cases. Assessment: PARTIAL_PRIOR_COVERAGE. Evidence: It covers the tree equality cases but not by itself the all-connected-bipartite extension.

## Limitations and residual risks

The mathematical deductions are correct, but the claimed originality does not survive comparison with the full proof of Zhu's 2026 BHM theorem. The stronger stochastic-domination conjecture is not addressed, and the quantitative factor in the gap transfer can be exponentially small.

- No correctness defect was found; rejection is solely for prior implication coverage.
- The quantitative factor may be very small, but that limitation does not affect correctness.

## Disposition

**failed**
