# Independent audit — 2026-10-01

## Final claim

A post-SDPI family of orthogonal relay-channel counterexamples

## Correctness — PASS

The exact capacity formula follows from independent direct transmission of the noiseless \(B\) bit and decode-forward over \(W_1\) and \(W_2\), matched by the two cutset bounds \(1+C_1\) and \(1+C_2\). Shiu's common relaxation of both proposed compress-forward terms depends only on the orthogonal factorization; conditionally on \((B,X_r)\), the chain \(A\to Y_r\to\widehat Y_r\) uses exactly \(W_1\). Applying the input-free post-processing SDPI gives \(I(A;\widehat Y_r\mid B,X_r)\le\eta I(Y_r;\widehat Y_r\mid B,X_r)\), and feasibility then yields the upper bound \(1+\eta C_2\). The BSC specialization and wedge identity are algebraically correct; the repository checker reproduces the quoted numerical gaps, but the proof does not rely on that finite grid.

## Originality — FAIL

Shiu's published counterexample already performs the decisive argument in a form that is parameter-generic until the last substitution: it relaxes both proposed compress-forward rates to the same factorized optimization, rewrites the objective as \(H(B\mid X_r)+I(A;\widehat Y_r\mid B,X_r)\), reduces feasibility to \(I(\widehat Y_r;Y_r\mid B,X_r)\le I(X_r;B,Z)\), and states the input-free post-SDPI for an arbitrary channel before inserting the BSC\((1/4)\) coefficient. Replacing that specific BSC by an arbitrary binary-input \(W_1\), and bounding the orthogonal \(W_2\) contribution by its capacity \(C_2\), is a mechanical parameter generalization of the published proof. Under the required implication standard, the family criterion is therefore covered even though Shiu does not print the final arbitrary-channel formula.

### Equivalent formulations

Searches/sources: Shiu 2026 relay counterexample equations 7–13 post-SDPI; post-processing contraction relay BSC counterexample.

Evidence: Shiu uses the same relaxed objective, feasibility inequality and conditional Markov chain.

Reasoning: The audited theorem rewrites the same proof with \(W_1,W_2\) symbolic rather than fixed to BSC\((1/4)\).

### Broader coverage

Searches/sources: El Gamal Zahedi orthogonal sender components relay capacity; Shiu counterexample arbitrary post-SDPI theorem.

Evidence: Orthogonal-relay capacity is already known; Shiu supplies the general SDPI step inside the counterexample proof.

Reasoning: Together these cover the two substantive ingredients needed for the claimed family statement.

### Exact database or table

Searches/sources: published SCOPE index: SDPI relay counterexample template; arbitrary BSC relay counterexample family.

Evidence: A later published record states an even broader SDPI template, while the audited record is the earlier exact family record.

Reasoning: The later record is not prior to this record, so it is not the basis of failure; the decisive prior coverage is Shiu’s primary paper.

### Claim versus prior implication

Searches/sources: arXiv:2609.18727 full text Sections 3.3 and Theorem 3.

Evidence: Theorem 3 is stated for a generic conditional distribution; equations 7–13 leave only the BSC coefficient and point-to-point capacity values to substitute.

Reasoning: The audited generalization follows by direct symbolic substitution and the channel-capacity bound, so it is mechanically implied under the audit standard.

## Scientific value — PASS

As a mathematical explanation, the family criterion is useful: it identifies the gap as a mismatch between the relay bottleneck \(\min(C_1,C_2)\) and post-processing contraction \(\eta C_2\), and exposes an open BSC wedge. The rejection is solely originality, not correctness or motivation.

## Sources inspected

- **Chun Hei Michael Shiu, Counterexample to a Proposed Capacity Characterization of the Relay Channel** (https://arxiv.org/abs/2609.18727): DECISIVE_PRIOR_COVERAGE. The paper already carries out the common relaxation and states the channel-generic SDPI; the audited symbolic family follows by replacing the final fixed BSC parameters and using \(C_2\).
- **A. El Gamal and S. Zahedi, Capacity of a Class of Relay Channels With Orthogonal Components** (https://doi.org/10.1109/TIT.2005.846438): CAPACITY_COMPONENT_PRIOR_ART. The exact orthogonal-family capacity is prior knowledge and is expressly not novel.

## Residual risks and limitations

- Scientific rejection is due to prior implication, not a correctness defect.
- The repository finite-grid verifier is only a sanity check and is not evidence for the arbitrary-channel theorem.

## Disposition

**failed**
