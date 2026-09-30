# Independent Audit — 2026/09/11/054

- Audit date: 2026-09-28 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `e1af49188993a6cc817cc8fa16b0896c09044f30`
- Disposition: **FAILED**

## Correctness

**FAIL** — The scalar moment calculation is correct—under the stated truncation, the fourth cumulant of the unnormalized variable grows on the order N^{1/6}, and |m_sc(2+wN^{-2/3})| stays bounded away from zero. But the record then calls L_N=κ_N m_sc^4 a 'fourth-cumulant loop correction' after discarding essential N-dependent normalization. For a Wigner matrix entry h_ij=x_ij/sqrt(N), cum_4(h_ij)=N^{-2}cum_4(x_ij). In the normalized-trace resolvent identity, the index sum and the 1/N trace normalization leave an additional κ_4(x)/N-scale prefactor before the resolvent-derivative structure is estimated. An 'absolute combinatorial prefactor' cannot absorb these powers of N. Consequently divergence of the artificially normalized coefficient κ_N m_sc^4 does not establish divergence of an actual loop-equation term and does not justify the claimed obstruction to edge-comparison arguments. The main research interpretation is therefore incorrect.

## Originality

**FAIL** — After removing the unsupported loop-equation interpretation, the valid calculation is the elementary fact that an alpha=3 tail has a truncated fourth moment growing linearly in the cutoff, evaluated at M_N=N^{1/6}. Heavy-tail breakdown for alpha<4 is already classical, and the submitted scalar lower bound does not supply a correctly normalized new resolvent contribution. There is therefore no original loop-equation result left to validate.

## Scientific value

**FAIL** — A deliberately rescaled cumulant coefficient can be useful as a heuristic diagnostic, but without the Wigner-entry N^{-2} cumulant scaling, trace normalization, and actual resolvent derivative terms it cannot block a comparison method or quantify edge breakdown. Since the claimed scientific consequence depends on that missing normalization, the record does not provide a reliable reusable theorem in its present form.

## Limitations

- This audit does not dispute the exact tail law or the truncated fourth-moment asymptotic; it rejects the identification of the rescaled scalar L_N with an actual loop-equation correction.
- A full edge cumulant expansion would need the precise derivative/index structure and local-law estimates; those are absent from the record.
- The general heavy-tail failure of Tracy–Widom for this alpha=3 ensemble is known independently and does not rescue the submitted quantitative loop claim.

## Sources

- A Necessary and Sufficient Condition for Edge Universality of Wigner Matrices — Ji Oon Lee; Jun Yin: https://arxiv.org/abs/1206.2251 — Established criterion showing this alpha=3 ensemble lies outside the Tracy–Widom regime; does not imply the submitted loop-term normalization.
- Convergence Rate to the Tracy-Widom Laws for the Largest Eigenvalue of Wigner Matrices — Kevin Schnelli; Yuanyuan Xu: https://arxiv.org/abs/2102.04330 — Uses properly normalized iterative cumulant expansions in Wigner comparison; highlights why entry scaling and derivative structure cannot be dropped.
- Poisson convergence for the largest eigenvalues of heavy tailed random matrices — Antonio Auffinger; Gérard Ben Arous; Sandrine Péché: https://arxiv.org/abs/0710.3132 — Classical heavy-tail edge breakdown context; the valid tail conclusion is not new.

GitHub was read only as evidence. The record's pre-existing `AUDIT.json` was inspected only after an independent assessment and was not treated as authority. No repository mutation was performed by this audit chat.
