# Independent audit — Weak off-diagonal necessity for monomial-curve commutators in every dimension

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/18/weak-off-diagonal-monomial-curve-commutators--9cc8cf69a607`  
**Audited tree:** `4ed08ceae5897d02854ffb7aaf7cc1102d74e4be`

## Disposition

**FAILED.** Correctness passes, but originality and standalone scientific value fail because an earlier SCOPE record already contains the same substantive finding. The package should be relocated to the designated failed-attempt path without discarding its evidence.

## Correctness

**PASS.** The mathematical argument is sound at the level claimed. The Lorentz associate functional sup_F |F|^{-1/q'} int_F |h| is equivalent to the weak-Lq quasi-norm for 1<q<infinity and is a genuine norm with integral Minkowski. Applied to Li--Zeng's companion-rectangle pointwise decomposition, a test input of Lp size O(|Q|^(1/p)) and a major output subset of size comparable to |Q| give m_Q |Q|^(1/q) <= C ||[b,H_gamma]|| |Q|^(1/p), exactly the anisotropic Campanato normalization. The q=p boundary reduces correctly to BMO.

## Originality

**FAIL.** The repository already contains an earlier 2026-09-17 record, `2026/09/17/weak-off-diagonal-monomial-commutator-necessity--40f2bbfdd125`, with the same title-level claim and essentially the same proof: weak Lp->L^{q,infinity} necessity in every dimension, the same Campanato exponent, the same normable Lorentz functional, the same Li--Zeng companion-cube mechanism, and the same weak/strong equivalence in Oikari's sufficiency region. That prior record predates the assigned 2026-09-18 record, so the assigned finding is not original.

## Scientific Value

**FAIL.** The theorem itself is useful and mathematically correct, but the assigned package adds no materially distinct theorem, mechanism, or regime beyond the already published 2026-09-17 SCOPE record. Retaining both as validated findings would duplicate the same scientific contribution.

## Independent checks

- Verified the weak-Lq associate norm equivalence and its integral Minkowski step used in the proof.
- Checked the scale calculation m_Q |Q|^(1/q) <= C N |Q|^(1/p), giving |Q|^(1/p-1/q) exactly.
- Compared the assigned RESULT.md with the earlier 2026-09-17 SCOPE record; both state the same all-dimensional weak off-diagonal necessity theorem and use the same Li--Zeng/Lorentz proof mechanism.

## Literature and repository prior-art boundary

- https://arxiv.org/abs/2609.18613 — Li and Zeng (2026), higher-dimensional curved-commutator geometry and diagonal necessity used by both SCOPE records.
- https://arxiv.org/abs/2304.00621 — Oikari (2023), all-dimensional off-diagonal sufficiency and plane-only necessity.
- https://github.com/SCOPE-Science/SCOPE2026/tree/main/2026/09/17/weak-off-diagonal-monomial-commutator-necessity--40f2bbfdd125 — Decisive earlier SCOPE record: same weak off-diagonal all-dimensional necessity theorem and proof mechanism, published 2026-09-17T23:14:30Z.

## Limitations

- Failure is based on originality/scientific-value duplication, not a mathematical error in the theorem.
- The theorem remains limited to unweighted 1<p<=q<infinity monomial curves and uses Li--Zeng's higher-dimensional companion geometry.

## Repository identity

The assigned source-tree SHA `4ed08ceae5897d02854ffb7aaf7cc1102d74e4be` exactly matched the current tree at the audited path on `main`; no stale-tree substitution was used. GitHub was read only during this audit.
