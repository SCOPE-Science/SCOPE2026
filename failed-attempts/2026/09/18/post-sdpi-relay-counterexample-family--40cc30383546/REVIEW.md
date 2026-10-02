# Review status

Independent mathematical audit date: 2026-10-01 UTC.

Disposition: **failed**.

Correctness: **PASS**. The exact capacity formula follows from independent direct transmission of the noiseless \(B\) bit and decode-forward over \(W_1\) and \(W_2\), matched by the two cutset bounds \(1+C_1\) and \(1+C_2\). Shiu's common relaxation of both proposed compress-forward terms depends only on the orthogonal factorization; conditionally on \((B,X_r)\), the chain \(A\to Y_r\to\widehat Y_r\) uses exactly \(W_1\). Applying the input-free post-processing SDPI gives \(I(A;\widehat Y_r\mid B,X_r)\le\eta I(Y_r;\widehat Y_r\mid B,X_r)\), and feasibility then yields the upper bound \(1+\eta C_2\). The BSC specialization and wedge identity are algebraically correct; the repository checker reproduces the quoted numerical gaps, but the proof does not rely on that finite grid.

Originality: **FAIL**. Shiu's published counterexample already performs the decisive argument in a form that is parameter-generic until the last substitution: it relaxes both proposed compress-forward rates to the same factorized optimization, rewrites the objective as \(H(B\mid X_r)+I(A;\widehat Y_r\mid B,X_r)\), reduces feasibility to \(I(\widehat Y_r;Y_r\mid B,X_r)\le I(X_r;B,Z)\), and states the input-free post-SDPI for an arbitrary channel before inserting the BSC\((1/4)\) coefficient. Replacing that specific BSC by an arbitrary binary-input \(W_1\), and bounding the orthogonal \(W_2\) contribution by its capacity \(C_2\), is a mechanical parameter generalization of the published proof. Under the required implication standard, the family criterion is therefore covered even though Shiu does not print the final arbitrary-channel formula.

Scientific value: **PASS**. As a mathematical explanation, the family criterion is useful: it identifies the gap as a mismatch between the relay bottleneck \(\min(C_1,C_2)\) and post-processing contraction \(\eta C_2\), and exposes an open BSC wedge. The rejection is solely originality, not correctness or motivation.

Evidence: `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
