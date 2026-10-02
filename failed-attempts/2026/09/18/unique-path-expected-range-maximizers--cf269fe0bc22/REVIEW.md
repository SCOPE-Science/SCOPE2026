# Review status

Independent mathematical audit date: 2026-10-01 UTC.

Disposition: **failed**.

Correctness: PASS. The equality classification and the quantitative inequality are mathematically correct. In Zhu's single-class tree case, the edge increments are independent and each nonzero-edge probability is at most one half; equality forces every such probability to be one half. Chasing equality through both bipartition classes forces maximum degree at most two, and the remaining even-cycle cases are strict, leaving only a path. For the gap transfer, zero-edge contraction gives a nonnegative defect term for every contraction; retaining only the no-zero-edge event yields exactly the stated lower bound with its probability factor.

Originality: FAIL. Zhu's full 2026 proof already contains the ingredients that mechanically imply both claimed contributions. Proposition 4.4 gives strictness for cyclic auxiliary graphs and, in the tree case, an explicit independent-Bernoulli comparison whose equality condition is immediate. The proof of the BHM theorem then reduces global equality to an equality-case chase. In Section 5, the identity expressing lazy expected range as the expectation of standard expected range over zero-edge quotients is followed by the path comparison; retaining the nonnegative contribution from the no-zero-edge event gives the displayed quantitative gap transfer directly. Under the audit rule that corollaries and mechanically implied refinements count as covered even when not stated verbatim, the final claim is not original.

Scientific value: PASS. Equality cases for a newly proved extremal theorem and a quantitative bridge between its standard and lazy models are natural, motivated questions. The rejection is not a value judgment on the mathematical questions; it is caused by prior implication coverage.

Evidence: `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.

This record is preserved as failed-audit evidence; see `FAILED_ATTEMPT.md`.
