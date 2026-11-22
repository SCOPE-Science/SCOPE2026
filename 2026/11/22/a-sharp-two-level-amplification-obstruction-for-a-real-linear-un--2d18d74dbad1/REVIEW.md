# Self-review

**Correctness — PASS.** The definition fixes all real-linearity and matrix-amplification conventions. The row compression \(\|[A\ B]\|\le\|X\|\), conjugate-equal row norms, and stacked-row inequality prove the universal \(\sqrt2\) upper bound. The explicit skew-symmetric two-by-two witness gives a unitary input whose image has eigenvalue \(\sqrt2\); padding yields equality at all higher levels. The level-one bound and unitary preservation follow by direct multiplication. Exact symbolic identities and 297 random finite assertions in `CHECK.py` supplement rather than establish the theorem.

**Originality — PASS (qualified).** Cui–Wu–Yuan's arXiv:2611.13822v1, Lemma 2.4 and Corollary 4.5, cover the ordinary norm-one unitary preserver and its structural non-Jordan class. They do not state the \(k\)-amplification formula or the unitary witness at \(k=2\). Searches of published mathematical records for quaternionic first-row completion, real-linear unitary preservers, completely bounded norms, and matrix-level unitary obstructions found no directly covering statement. Closest indexed results concerned either complex-linear Schatten Schur multipliers or unrelated quaternionic moments. Residual priority risk: an older real operator-space treatment of quaternionic row maps might imply the same \(\sqrt2\) law.

**Mathematical value — PASS.** Unitary preservation alone is not stable under a minimal matrix amplification, despite norm-one behavior at the underlying level. The result gives both the smallest failing level and the exact sharp inflation, realized on an actual unitary. That is a motivated structural boundary for newly classified exceptional unitary preservers, rather than an arbitrary matrix example or a restatement of their classification.

The result is specific to this explicit non-Jordan map and does not classify all possible preservers. Its exact matrix norm proof is independent of finite diagnostics. General prior work on operator-space norms may contain an equivalent formulation, not established by the sources inspected.

Self-review: passed. Independent audit: not yet performed.
