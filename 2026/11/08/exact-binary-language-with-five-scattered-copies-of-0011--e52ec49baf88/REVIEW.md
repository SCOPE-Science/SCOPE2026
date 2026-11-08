# Scientific assessment

**Correctness — PASS.** The proof deletes only symbols incapable of joining a \(0011\) embedding, obtains a core with all positions active, excludes the monotone triangular-product case, and then uses the five explicitly counted occurrences of \(001011\) to force equality of the core. Four uniquely placed inactive insertion zones give the regular expression and binomial count. `checker.py` independently verified 32767 complete short words, 4096 parameter tuples, and 50 transfer-recurrence values. The proof, not bounded enumeration, covers all word lengths.

**Originality — PASS (qualified).** The complete exact regular language and count were not found in the relevant inspected sources or indexed comparisons. Bruda's arXiv:2607.02578, Theorem 1.4 and Section 4.2, already establish the eventual degree bound and specifically identify the frequency-five \(0011\) exception; those facts are prior art. Menon–Singh's arXiv:2306.07870 treats counts one through four, and Tian's arXiv:2507.03205 gives a general primitive-word method with an unevaluated sum. This result identifies the unique primitive core and evaluates the corresponding language for all lengths. Its arithmetic specialization may be implicit in Tian's broad algorithm; the lack of a located printed specialization is not proof of universal priority.

**Value — PASS.** The parameter is not chosen arbitrarily: multiplicity five for \(0011\) is the first concrete counterexample singled out by Bruda to the proposed maximal-degree characterization. An exact language, rather than just eventual degree, explains why the degree-three exception occurs and gives a usable test set for subsequence-frequency algorithms. The conclusion is deliberately limited to this natural exceptional boundary case.

**Limits and risks.** The result does not solve the general degree characterization and does not assert an independent review. A previous implicit specialization of general primitive-word enumeration remains possible.

Self-review: passed. Independent audit: not yet performed.
