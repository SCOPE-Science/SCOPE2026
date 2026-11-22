# Review: Complete quartic cyclotomic coefficient-weight spectrum over \(\mathbb F_8\)

## Correctness — PASS

The statement quantifies over all \(18\) quartic cyclotomic orders in \(\mathbb F_8\). Two independent exhaustive enumerations agree on every coefficient-weight bucket; the number of monic irreducible quartics is \(1008\) and the layer totals all equal \(\varphi(n)/4\). A separate trace-one analysis determines the only orders that contain irreducible quartic trinomials, and an exact polynomial remainder certificate verifies root order \(585\). The exhaustive verifier was run from its actual included source; no finite sample is treated as a general-infinite proof.

## Originality — PASS, qualified

Zhu–Wu (arXiv:2611.00647v2) prove the all-trinomial criterion, the non-all-trinomial quartic half-gap bound, and the aggregate number \(56\) of \(\mathbb F_8\) irreducible quartic trinomials, but not the whole \(18\)-row three-weight spectrum or the \(1:4:7\) ratios. Cheng (arXiv:2507.10779v2) covers the all-sparse property of \(X^n-1\). Graner (arXiv:2306.11183v2) gives general explicit factorizations, which make all the needed finite coefficients computable; implicit earlier specialization is a residual risk. Targeted published-record and primary-literature searches found no exactly covering evaluated spectrum; failed search alone is not evidence of priority.

## Mathematical value — PASS

All eighteen natural quartic cyclotomic layers are completely classified by the number of nonzero coefficients of their irreducible factors. The two mixed layers with trinomials have a sharper and exact sparsity fraction \(1/12\), explaining concrete structure beyond a general half-gap upper bound. The result is limited to one finite field and degree; no wider generalization is claimed.

## Evidence and boundaries

The complete reproducible finite verification is `verify.py`, which independently reconstructs the table using a polynomial gcd criterion and Frobenius orbit minimal-polynomial products. Published work remains the source of the broader classification context. A general factorization formula is available and could implicitly determine this specialization. No independent mathematical audit has occurred.

Self-review: passed. Independent audit: not yet performed.
