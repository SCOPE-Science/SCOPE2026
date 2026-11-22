# Review: universal parity for the two-to-one family

## Correctness (PASS)

The theorem is quantified over every odd prime power and all positive \(r,d\) with \(\gcd(d,q+1)=2\), conditional on the polynomial being a bijection. Injectivity forces \(\gcd(r,q-1)=1\). Splitting the nonzero field elements into \(q+1\) cosets of \(\mathbb F_q^*\) gives the exact sign as the quadratic character of the product of fiber multipliers. The two-to-one power map on norm-one roots evaluates that product to a nonzero base-field unit times \((a^{(q+1)/2}-(-1)^{(q+1)/2})^2\). Frobenius invariance forbids nonsquare nonzero coefficients, and the remaining square factor contributes sign \(+1\). The generator factor gives \((-1)^{(r-1)/2}\). Each step is proved in the accompanying result, without extrapolation from finite computations. Exact finite tests of five base fields support the argument.

## Originality (PASS, with unindexed-literature risk)

Tang and Fan (arXiv:2611.14162) classify the permissible coefficients and provide the two-to-one index reduction. Their **Lemma 2.2 already proves that nonzero permissible coefficients are squares**, so the square-class restriction is prior work, not an originality claim. The available full-text PDF rendering was inspected for main results, Lemma 2.2, relevant sections and occurrences of sign/parity and contained no corresponding theorem on the sign of the induced permutation. The earlier index-one classification (arXiv:2609.20354) has a different coefficient structure, and the full-text accessible Ding–Zieve classification focuses on characteristic-two quadrinomials. Published parity results for linearized polynomials concern a different algebraic family. A targeted literature and semantic-record comparison found no statement dominating the claimed uniform parity rule; absence in search results is not proof of novelty. An unindexed more general cyclotomic-permutation parity theorem remains a priority risk.

## Mathematical value (PASS)

Permutation parity is a natural group-theoretic invariant of finite-field bijections. The result determines it **for every admissible coefficient** in the newly classified index-two binomial family, including unusual small-field exceptions, without running the casewise coefficient classification. The previously known square-class restriction makes the new parity rigidity possible and distinguishes this branch from the coprime-index case. It is neither a single computed example nor a small arbitrary parameter slice: the scope is all odd prime powers and all two-to-one exponents. No stronger claim about individual cycles or coefficient counts is made.

## Limitations and closest literature

The primary manuscript's relevant main results, Lemma 2.2, Corollary 1.4 and searched sign/parity passages were directly compared, with no permutation-sign formula identified; the square coefficient obstruction is explicitly acknowledged as their prior result. Unindexed broader signature theorems remain possible. The general cyclotomic coset method is classical, and methodological originality is not asserted. Independent validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
