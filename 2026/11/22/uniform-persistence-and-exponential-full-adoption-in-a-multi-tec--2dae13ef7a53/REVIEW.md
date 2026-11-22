# Scientific review: Uniform persistence and exponential full adoption in a multi-technology opinion network

## Correctness — PASS
The precise claim holds under the positive rates and network assumptions stated in `RESULT.md`. Step 1 gives the uniform opinion floor; step 2 lists four valid length-four local transition paths to every adopter state, including the difficult initially same-technology dissatisfied state; step 3 propagates a non-susceptible seed along a directed spanning reachability tree; step 4 converts the resulting uniform adopter mass to geometric susceptible depletion. Exact matrix products and a full coupled numerical example in `verify_mate_persistence.py` are corroboration, not substitutes for the analytical proof. The constants and time indices were individually reconstructed and checked.

## Originality — PASS (bounded literature comparison)
The 2026 MATE source's Appendix B.6 already contains a related *three-step local mixing lemma*, and Theorem 3.5 already obtains whole-state convergence under small feedback. Neither directly covers **global geometric depletion and simultaneous positive retention of every technology for all admissible feedback**, where full-state convergence or uniqueness can fail. The earlier two-technology paper gives equilibrium results. The Ipsen–Selee work supplies known matrix methodology and is not claimed new. Targeted published-claim searches and prior-research-claim comparisons did not reveal direct coverage; they cannot establish absolute priority. Historical coverage beyond inspected texts is a residual risk.

## Value — PASS
This is a qualitative separation of two issues often conflated in competitive adoption: whether equilibrium shares converge and whether any community/option can remain excluded. The model can admit multiple coexisting adoption-diffused equilibria under strong feedback, yet every seeded trajectory provably eliminates susceptibles at a certified geometric rate and prevents extinction of every alternative at every community. A precise all-parameter structural conclusion and reproducible conservative bounds are directly useful for model interpretation, admissibility of simulated outcomes and future quantitative perturbation analyses, rather than a one-parameter computational slice.

## Boundaries and evidence
The sufficient lower bound can be tiny, and the theorem does not assert convergence of the other state variables or a sharp rate. The all-times statement is only after the explicit transient and requires all strict positivity hypotheses. The complete analytical derivation is in `RESULT.md` and the computational cross-check is in `verify_mate_persistence.py`. Primary sources: https://arxiv.org/abs/2611.04407, https://arxiv.org/abs/2601.16719; general mixing reference https://doi.org/10.1137/090752948. Independent historical priority and mathematical confirmation remain outside the present evidence.

Self-review: passed. Independent audit: not yet performed.
